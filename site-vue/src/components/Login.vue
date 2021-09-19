<template>
  <div class="container">
    <section class="header">
      <h2 class="title">Login</h2>
      <p>
          Login to check your ranking history.
      </p>
    </section>

    <div class="page-section">
      <h3>Login</h3>
      <div v-if="state == 'input'">
        <div class="row">
            <p>
                <label for="email">Email</label>
                <input v-model="email" placeholder="your@email.com" class="remember-input u-full-width" type="email" id="email">
            </p>
        </div>
        <p>
          <button @click="login" class="button-primary">Send login code</button>
        </p>
      </div>
      <div v-if="state == 'sent'">
        <p>
          A code has been sent to your email. Please open the link provided inside to continue.
        </p>
        <p>
          <button @click="retry" class="button-primary">Retry</button>
        </p>
      </div>
    </div>

    <div class="page-section">
      <h3>About</h3>
      <p>
          This app is built by <a target="_blank" href="https://twitter.com/almundgrey">David</a> @ <a target="_blank" href="https://greycastle.se">Greycastle</a>, visuals based on the <a target="_blank" href="http://getskeleton.com/">Skeleton</a> css framework. <a href="about.html">About</a> | <a href="pricing.html">Pricing</a>.
      </p>
    </div>
  </div>
</template>

<script>
import { getAuth, setPersistence, browserLocalPersistence, sendSignInLinkToEmail } from 'firebase/auth';

export default {
  data() {
    return {
      state: 'input',
      email: window.localStorage.getItem('email')
    }
  },
  methods: {
    async login() {
      let host = `${window.location.protocol}//${window.location.hostname}`
      if (host.endsWith('localhost')) host = `${host}:${window.location.port}`
      const actionCodeSettings = {
        url: `${host}/login-by-url`,
        handleCodeInApp: true
      }
      const auth = getAuth();
      setPersistence(auth, browserLocalPersistence);

      window.localStorage.setItem('email', this.email)
      await sendSignInLinkToEmail(auth, this.email, actionCodeSettings)
      this.state = 'sent'
    },
    retry() {
      this.state = 'input'
    }
  }
}
</script>

<style scoped>
</style>