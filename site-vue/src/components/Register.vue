<template>
  <div>
    <div v-if="!registerPromise" class="page-section">
      <h3>{{ $t('title') }}</h3>
      <p>{{ $t('subtitle') }}</p>
      <form class="form">
        <div class="row">
            <p>
                <label for="keyword">{{ $t('keyword') }}</label>
                <input v-model="keyword" :placeholder="$t('keyword-placeholder')" class="remember-input u-full-width" type="text" id="keyword">

            </p>
            <p>
              <label for="site">{{ $t('site') }}</label>
              <input v-model="site" placeholder="greens.zed" class="remember-input u-full-width" type="text" id="site">
            </p>
            <p>
              <label for="api-key">{{ $t('email') }}</label>
              <input v-model="email" placeholder="sales@greens.zed" class="remember-input u-full-width" type="email" id="email">
            </p>
        </div>
        <p><button @click="register()" class="button-primary" type="button">{{ $t('button-check') }}</button></p>
      </form>
    </div>
    <PromiseBuilder :promise="registerPromise" v-if="registerPromise">
      <template #pending>
        <div class="page-section">
          <h3>{{ $t('registering.title') }}</h3>
          <p>{{ $t('registering.message') }}</p>
        </div>
      </template>
      <template #fulfilled>
        <div class="page-section">
          <h3>{{ $t('done.title') }}</h3>
          <p>{{ $t('done.message') }}</p>
          <p>
            <router-link class="button button-primary" to="/login">{{ $t('done.button-login') }}</router-link>
          </p>
        </div>
      </template>
      <template #rejected="{ error }">
        <div class="page-section">
          <h3>{{ $t('error.title') }}</h3>
          <p>{{ $t('error.message') }}</p>
          <p>
            {{ error }}
          </p>
        </div>
      </template>
    </PromiseBuilder>
  </div>
</template>

<script>
import register from '@/services/register'

export default {
  data() {
    return {
      registerPromise: null,
      site: null,
      keyword: null,
      email: null
    }
  },
  emits: [ 'registered' ],
  methods: {
    async register() {
      this.registerPromise = register(this.email, this.keyword, this.site)
      await this.registerPromise
      this.$emit('registered')
    }
  }
}
</script>

<i18n>
{
  "en": {
    "title": "Get started",
    "subtitle": "Enter your email to get reports to here and then your keyword and your site:",
    "keyword": "Keyword",
    "keyword-placeholder": "your keyword",
    "site": "Site",
    "email": "Email",
    "button-check": "Check ranking!",
    "registering": {
      "title": "Registering..",
      "message": "Give us a sec.."
    },
    "error": {
      "title": "Error!",
      "message": "Something went wrong. Please try again later."
    },
    "done": {
      "title": "All done!",
      "message": "You should very soon get a first email with your new rank. You can also head straight in to check it.",
      "button-login": "Login to check your rank"
    }
  },
  "ja": {
    "title": "はじまる",
    "subtitle": "ランキングを確認開始ために、以下にキーワード・サイトとどのメールアドレスにランキングアップデートを送って欲しいを入力してください：",
    "keyword": "キーワード",
    "keyword-placeholder": "あなたのキーワード",
    "site": "サイト",
    "email": "メールアドレス",
    "button-check": "ランキングを確認する",
    "registering": {
      "title": "登録中..",
      "message": "ちょっと待ってね.."
    },
    "error": {
      "title": "エラー!",
      "message": "申し訳ございません、エラーが発生しました。少し待ちして試してください。"
    },
    "done": {
      "title": "できました!",
      "message": "もう少しと最初のランキングメールが届けます。今でもすぐにログイン、チェックできます。",
      "button-login": "ランクを確認する"
    }
  },
}

</i18n>