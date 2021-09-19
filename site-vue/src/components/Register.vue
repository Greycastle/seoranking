<template>
  <div>
    <div v-if="!registered && !registering" class="page-section">
      <h3>Get started</h3>
      <p>
          Enter your email to get reports to here and then your keyword and your site:
      </p>
      <form class="form">
        <div class="row">
            <p>
                <label for="keyword">Keyword</label>
                <input v-model="keyword" placeholder="yummy greens" class="remember-input u-full-width" type="text" id="keyword">

            </p>
            <p>
              <label for="site">Site</label>
              <input v-model="site" placeholder="greens.zed" class="remember-input u-full-width" type="text" id="site">
            </p>
            <p>
              <label for="api-key">Email</label>
              <input v-model="email" placeholder="sales@greens.zed" class="remember-input u-full-width" type="email" id="email">
            </p>
        </div>
        <p><button @click="register()" class="button-primary" type="button">Check ranking!</button></p>
      </form>
    </div>

    <div v-if="registering" class="page-section">
      <h3>Registering..</h3>
      <p>
        Give us a sec..
      </p>
    </div>

    <div v-if="registered" class="page-section">
      <h3>All done!</h3>
      <p>
          You should very soon get a first email with your new rank. You can also head straight in to check it.
      </p>
      <p>
        <router-link class="button button-primary" to="/login">Login to check your rank</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import register from '@/services/register'

export default {
  data() {
    return {
      registered: false,
      registering: false,
      site: null,
      keyword: null,
      email: null
    }
  },
  methods: {
    async register() {
      this.registering = true
      await register(this.email, this.keyword, this.site)
      this.registering = false
      this.registered = true
      this.$emit('registered')
    }
  }
}
</script>
