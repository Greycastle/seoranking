import {
  initializeAuth,
  browserLocalPersistence,
  onAuthStateChanged,
  signInWithEmailLink,
  isSignInWithEmailLink,
  sendSignInLinkToEmail
 } from 'firebase/auth';

class Auth {
  constructor(firebaseApp, router) {
    this.auth = initializeAuth(firebaseApp, {
      persistence: browserLocalPersistence
    })

    this.loaded = false
    this.user = null
    this.error = null

    const authState = new Promise((resolve, reject) => {
      onAuthStateChanged(this.auth, user => {
        this.user = user
        this.error = null
        this.loaded = true
        resolve(user)
      }, (error) => {
        this.error = error
        this.loaded = true
        reject(error)
      })
    })

    router.beforeEach(async (to, _, next) => {
      const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
      const redirectIfSignedIn = to.matched.some(record => record.meta.redirectIfSignedIn);
      const user = await authState

      if (requiresAuth && !user) {
        next('login')
      } else if (redirectIfSignedIn && user) {
        next('dashboard')
      } else {
        next()
      }
    })
  }

  async sendEmailLink(email) {
    let host = `${window.location.protocol}//${window.location.hostname}`
      if (host.endsWith('localhost')) host = `${host}:${window.location.port}`
      const actionCodeSettings = {
        url: `${host}/login-by-url`,
        handleCodeInApp: true
      }

      window.localStorage.setItem('authEmail', email)
      await sendSignInLinkToEmail(this.auth, email, actionCodeSettings)
  }

  async trySignInEmail(fallbackEmail) {
    if (!isSignInWithEmailLink(this.auth, window.location.href)) {
      throw Error('Wrong url')
    }
    const email = window.localStorage.getItem('authEmail') || fallbackEmail
    if (!email) {
      throw Error('No email')
    }
    console.log(`Attempting login by email: ${email}`)
    await signInWithEmailLink(this.auth, email, window.location.href)
    console.log("Successfully logged in!")
  }
}

export default {
  install: (app, options) => {
    const router  = app.config.globalProperties.$router
    if (!router) {
      throw new Error("Please register router before the auth module")
    }

    const auth = new Auth(options.firebaseApp, router)
    app.config.globalProperties.$auth = auth
  }
};