<template>
  <div class="container">
    <section class="header">
      <h2 class="title">SEO Ranking</h2>
      <p>{{ $t('subtitle') }}</p>
    </section>

    <div>
      <Register @registered="onRegistered" />

      <div v-if="showLogin" class="page-section">
        <h3>{{ $t('registered.title') }}</h3>
        <p>{{ $t('registered.subtitle') }}</p>
        <p>
          <router-link class="button button-primary" to="'/login">{{ $t('start.button-check') }}</router-link>
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

<i18n>
{
  "en": {
    "subtitle": "This tool allows you to sign up for continous search ranking checks for your site.",
    "registered": {
      "title": "Already started?",
      "subtitle": "If you've already registered, log in to see your recent ranking history.",
      "button-check": "Check your ranking history"
    }
  },
  "ja": {
    "subtitle": "このツールでは、定期的なGoogleランキングを確認できます。",
    "registered": {
      "title": "もう登録しました?",
      "subtitle": "以前登録したかたはこちらでランキングを見るためにログインできます。",
      "button-check": "ランキングを確認する"
    }
  },
}
</i18n>