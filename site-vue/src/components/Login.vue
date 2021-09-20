<template>
  <div class="container">
    <section class="header">
      <h2 class="title">{{ $t('title') }}</h2>
      <p>{{ $t('subtitle') }}</p>
    </section>

    <div class="page-section">
      <h3>{{ $t('title') }}</h3>
      <div v-if="state == 'input'">
        <div class="row">
            <p>
                <label for="email">{{ $t('email') }}</label>
                <input v-model="email" placeholder="user@email.com" class="remember-input u-full-width" type="email" id="email">
            </p>
        </div>
        <p>
          <button @click="login" class="button-primary">{{ $t('button-send') }}</button>
        </p>
      </div>
      <div v-if="state == 'sent'">
        <p>{{ $t('message-sent') }}</p>
        <p>
          <button @click="retry" class="button-primary">{{ $t('button-retry') }}</button>
        </p>
      </div>
    </div>

    <Footer />
  </div>
</template>

<script>

export default {
  data() {
    return {
      state: 'input',
      email: ''
    }
  },
  methods: {
    async login() {
      await this.$auth.sendEmailLink(this.email)
      this.state = 'sent'
    },
    retry() {
      this.state = 'input'
    }
  }
}
</script>

<i18n>
{
  "en": {
    "title": "Login",
    "subtitle": "Login to check your ranking history.",
    "email": "Email",
    "button-send": "Send login code",
    "message-sent": "A code has been sent to your email. Please open the link provided inside to continue.",
    "button-retry": "Retry"
  },
  "ja": {
    "title": "ログイン",
    "subtitle": "ランキング履歴を見るために、ログインしてください。",
    "email": "メールアドレス",
    "button-send": "ログインコード送る",
    "message-sent": "ログインリンクは上記のメールに送りました。進むためにメールのリンク開いてください。",
    "button-retry": "再試行"
  }
}
</i18n>