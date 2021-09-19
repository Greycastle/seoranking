<template>
  <div class="container">
    <section class="header">
      <h2 class="title">Dashboard</h2>
      <p>You're in, welcome!</p>
      <p>
        <button @click="logout" class="button-primary">Logout</button>
      </p>
    </section>
  </div>
</template>

<script>
import { getAuth, signOut } from "firebase/auth";

export default {
  methods: {
    logout() {
      signOut(getAuth())
      this.$router.push('signed-out')
    }
  }
}
</script>

<style scoped>
</style>