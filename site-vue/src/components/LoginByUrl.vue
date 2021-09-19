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
        <a @click="login()" class="button">Login</a>
      </div>
      <div v-if="state == 'error'">
        That didn't work out... Try sending a new link:
        <router-link to="login">Login</router-link>
      </div>
    </section>
  </div>
</template>

<script>

export default {
  data() {
    return {
      state: 'checking',
      email: ''
    }
  },
  methods: {
    async login() {
      try {
        console.log(`Trying login with email = ${this.email}`)
        await this.$auth.trySignInEmail(this.email)
        this.$router.push('/dashboard')
      } catch (err) {
        if (err.message == 'Wrong url') {
          this.state = 'no-url'
        } else if(err.message == 'No email') {
          this.state = 'enter-email'
        } else {
          console.error(err)
          this.state = 'error'
        }
      }
    }
  },
  async created() {
    await this.login()
  },
}
</script>

<style scoped>
</style>