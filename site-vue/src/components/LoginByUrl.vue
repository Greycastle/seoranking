<template>
  <div class="container">
    <section class="header">
      <h2 class="title">Login</h2>
      <p v-if="state == 'checking'">
          Processing your login credentials..
      </p>
      <p v-if="state == 'no-url'">
        This ain't no login url. Please try to login first:
        <router-link to='login'>Login</router-link>
      </p>
      <div v-if="state == 'enter-email'">
        <p>
          We're ready to log you in but first we need to confirm your email:
        </p>
        <input v-model="email" type="email" />
        <a @click="login" class="button">Login</a>
      </div>
      <p v-if="state == 'error'">
        That didn't work out... Try again
      </p>
    </section>
  </div>
</template>

<script>
import { getAuth, setPersistence, browserLocalPersistence, isSignInWithEmailLink, signInWithEmailLink } from 'firebase/auth';

export default {
  data() {
    return {
      state: 'checking',
    }
  },
  methods: {
    async login() {
      try {
        await setPersistence(this.auth, browserLocalPersistence);
        await signInWithEmailLink(this.auth, this.email, window.location.href)
        this.$router.push('/dashboard')
      } catch(err) {
        console.error(err)
        this.state = 'error'
      }
    }
  },
  created() {
    this.auth = getAuth();

    if (!isSignInWithEmailLink(this.auth, window.location.href)) {
      this.state = 'no-url'
      return
    }

    this.email = window.localStorage.getItem('email')
    if (this.email) {
      this.login()
    } else {
      this.state = 'enter-email'
    }
  },
}
</script>

<style scoped>
</style>