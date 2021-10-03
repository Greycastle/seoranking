<template>
  <div class="container">
    <section class="header">
      <h1 class="title">SEO Ranking</h1>
      <p>{{ $t('subtitle') }}</p>
    </section>

    <section class="row page-section">
      <div class="six columns">
        <h2>The cheap rank tracker</h2>
        <p>
          Just launched your website ✓ <br />
          But no visitors?
        </p>
        <p>
          You need to rank on top 1-5 results on Google to get visitors. <br />
          And you need to know for what keywords.
        </p>
        <p>
          SEORanking is the affordable starter-kit to track any number of keywords for any of your pages.
        </p>
        <p>
          This is how SEORanking is different:
        </p>
        <ul>
          <li>Completely free to get started</li>
          <li>No monthly fee. Pay per use</li>
          <li>Cheap! Paying only for what you need means $1/month or less</li>
          <li>Beginner friendly. SEORanking is built as a first-time-tool</li>
        </ul>
        <p>
          <router-link to="/about">Read more here ></router-link>
        </p>
      </div>
      <Register class="six columns" @registered="onRegistered" />
    </section>

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
    "subtitle": "Automatically keep track of your google ranking in just one click.",
  },
  "ja": {
    "subtitle": "このツールでは、定期的なGoogleランキングを確認できます。",
  },
}
</i18n>