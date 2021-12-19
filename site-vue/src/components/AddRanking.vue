<template>
  <div>
    <h3>{{ $t('title') }}</h3>
    <p>{{ $t('subtitle') }}</p>
    <form id="add-ranking-form">
      <div class="row">
        <div class="six columns">
            <label for="keyword">{{ $t('keyword') }}</label>
            <input :disabled="isAdding" :placeholder="$t('keyword-placeholder')" v-model="keyword" class="remember-input u-full-width" type="text" id="keyword">

        </div>
        <div class="six columns">
          <label for="site">{{ $t('site') }}</label>
          <input :disabled="isAdding" placeholder="site.xyz" v-model="site" class="remember-input u-full-width" type="text" id="site">
        </div>
      </div>
      <p>
        <button :disabled="isAdding" @click="add()" class="button-primary" type="button">{{ buttonText }}</button>
      </p>
      <PromiseBuilder :promise="addingPromise" v-if="addingPromise">
        <template #fulfilled>
          {{ $t('result-added') }}
        </template>
        <template #rejected>
          {{ $t('result-error') }}
        </template>
      </PromiseBuilder>
    </form>
    <p v-html="$t('keyword-tool')"></p>
  </div>
</template>

<script>
import addRanking from '@/services/addRanking'
import PromiseBuilder from './PromiseBuilder.vue'

export default {
  components: { PromiseBuilder },
  props: {
    defaultSite: String
  },
  data() {
    return {
      site: null,
      keyword: null,
      addingPromise: null,
      isAdding: false
    }
  },
  watch: {
    defaultSite(newSite) {
      if (this.site) return
      this.site = newSite
    }
  },
  computed: {
    buttonText() {
      return this.isAdding ? this.$t('button-saving') : this.$t('button-add')
    }
  },
  methods: {
    async add() {
      this.isAdding = true
      this.addingPromise = addRanking(this.site, this.keyword)
      await this.addingPromise.finally(() => this.isAdding = false)
      this.$emit('added', { site: this.site, keyword: this.keyword })
    }
  }
}
</script>

<i18n>
{
  "en": {
    "title": "Add more rankings",
    "subtitle": "You can add more keywords or sites as well:",
    "keyword": "Keyword",
    "keyword-placeholder": "your keyword",
    "site": "Site",
    "button-saving": "Saving..",
    "button-add": "Add ranking",
    "result-added": "Congrats, new keyword was added!",
    "result-error": "We're sorry, some error occurred. Please try again later.",
    "keyword-tool": "For tips on what keywords your site might rank for, check out <a href=\"https://app.wordstream.com/fkt/app?cid=Web_Any_Products_Keywords_Grader_KWTool&ref=undefined\">wordstream's keyword tool</a>"
  },
  "ja": {
    "title": "ランキングを追加する",
    "subtitle": "上記意外のキーワード・サイトを追跡追加できます:",
    "keyword": "キーワード",
    "keyword-placeholder": "あなたのキーワード",
    "site": "サイト",
    "button-saving": "保存中..",
    "button-add": "ランキングする",
    "result-added": "おめでとう！ キーワードを追加できました!",
    "result-error": "申し訳ございません、エラーが発生しました。少し待ちして、試してください。",
    "keyword-tool": "どのキーワードをランキングするのを<a href=\"https://app.wordstream.com/fkt/app?cid=Web_Any_Products_Keywords_Grader_KWTool&ref=undefined\">wordstreamのキーワードツール</a>をご覧ください"
  }
}
</i18n>