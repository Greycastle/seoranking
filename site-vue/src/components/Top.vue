<template>
  <div class="container">
    <section class="header">
      <h2 class="title">SEO Ranking</h2>
      <p>
          This tool allows you to sign up for continous search ranking checks for your site.
      </p>
    </section>

    <div>
      <Register @registered="onRegistered" />

      <div v-if="showLogin" class="page-section">
        <h3>Already started?</h3>
        <p>
            If you've already registered, log in to see your recent ranking history.
        </p>
        <p>
          <router-link class="button button-primary" to="'/login">Check your ranking history</router-link>
        </p>
      </div>
    </div>

    <Footer/>
  </div>
</template>

<script>
import Register from '@/components/Register'

export default {
  components: {
    Register
  },
  data() {
    return {
      showLogin: true
    }
  },
  methods: {
    onRegistered() {
      this.showLogin = false
    }
  }
}
</script>