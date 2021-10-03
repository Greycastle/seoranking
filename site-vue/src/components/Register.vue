<template>
  <div>
    <div v-if="!registerPromise">
      <h2>{{ $t('title') }}</h2>
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
        <p>
          <button @click="register()" class="button-primary" type="button">{{ $t('button-check') }}</button>
          <span class="login">{{ $t('or-login') }} <router-link to="/login">{{ $t('login') }}</router-link></span>
        </p>
      </form>
    </div>
    <PromiseBuilder :promise="registerPromise" v-if="registerPromise">
      <template #pending>
        <div>
          <h3>{{ $t('registering.title') }}</h3>
          <p>{{ $t('registering.message') }}</p>
        </div>
      </template>
      <template #fulfilled>
        <div>
          <h3>{{ $t('done.title') }}</h3>
          <p>{{ $t('done.message') }}</p>
          <p>
            <router-link class="button button-primary" to="/login">{{ $t('done.button-login') }}</router-link>
          </p>
        </div>
      </template>
      <template #rejected="{ error }">
        <div>
          <h3>{{ $t('error.title') }}</h3>
          <p>{{ $t('error.message') }}</p>
          <p>
            {{ error }}
          </p>
          <p>
            <button @click="reset()">{{ $t('try-again') }}</button>
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
    },
    reset() {
      this.registerPromise = null
    }
  }
}
</script>

<style scoped>
.login {
  opacity: 0.7;
  margin-left: 20px;
}
</style>

<i18n>
{
  "en": {
    "title": "Track your rank",
    "subtitle": "Enter your email to get reports to here and then your keyword and your site:",
    "keyword": "Keyword",
    "keyword-placeholder": "your keyword",
    "site": "Site",
    "email": "Email",
    "or-login": "or",
    "login": "login",
    "button-check": "Start tracking!",
    "try-again": "Try again",
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
    "title": "トラッキングを始まる",
    "subtitle": "ランキングを確認開始ために、以下にキーワード・サイトとどのメールアドレスにランキングアップデートを送って欲しいを入力してください：",
    "keyword": "キーワード",
    "keyword-placeholder": "あなたのキーワード",
    "site": "サイト",
    "email": "メールアドレス",
    "button-check": "ランキングを確認する",
    "or-login": "または",
    "login": "ログイン",
    "try-again": "戻る",
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
      "button-login": "トラッキングを始まる"
    }
  },
}

</i18n>