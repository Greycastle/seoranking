<template>
  <div class="container">
    <section class="header">
      <h2 class="title">Signed out</h2>
      <p>
          Thank you for using SEORank this time around. See you again!
      </p>
      <p>
        <router-link class="button" to='/'>Back to top</router-link>
      </p>
    </section>
  </div>
</template>

<script>
export default {
  created() {
    setTimeout(() => {
      this.$router.replace('/')
    }, 5000)
  }
}
</script>

<style scoped>
</style>