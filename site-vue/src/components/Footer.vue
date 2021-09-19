<template>
  <div class="page-section">
    <h3>About</h3>
    <p>
      This app is built by <a target="_blank" href="https://twitter.com/almundgrey">David</a> @ <a target="_blank" href="https://greycastle.se">Greycastle</a>, visuals based on the <a target="_blank" href="http://getskeleton.com/">Skeleton</a> css framework.
      <router-link :to="{ name: isLoggedIn ? 'Dashboard' : 'Top' }">Top</router-link> | <router-link to="/about">About</router-link><span v-if="!isLoggedIn"> | <router-link to="/pricing">Pricing</router-link></span><span v-else> | <a href="/logout" @click="logout()">Logout</a></span>
    </p>
  </div>
</template>

<script>
export default {
  computed: {
    isLoggedIn() {
      return this.$auth.user != null
    }
  },
  methods: {
    async logout() {
      this.$auth.logout()
      this.$router.replace('signed-out')
    }
  }
}
</script>
