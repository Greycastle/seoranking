<template>
  <div>
    <div class="container">
      <section class="header">
        <h2 class="title">{{ $t('title') }}</h2>
        <p> {{ $t('subtitle')}} </p>
        <button @click="share">{{ $t(shared ? 'share-button-done' : 'share-button') }}</button>
      </section>

      <RankingTable :rankings="rankings" :loading="loading" :loaded="loaded" />

      <Footer />
    </div>
  </div>
</template>

<script>
import useClipboard from 'vue-clipboard3'
import { useRoute } from 'vue-router'
import RankingTable from '@/components/RankingTable'
import { getPublicRankings } from '@/services/rankingData'

export default {
  components: {
    RankingTable
  },
  data() {
    return {
      state: 'loading',
      rankings: [],
      account: null,
      defaultSite: '',
      shared: false,
    }
  },
  methods: {
    async share() {
      this.shared = true
      const { toClipboard} = useClipboard()
      const url = window.location.origin
      await toClipboard(url)
      setTimeout(() => this.shared = false, 2500)
    }
  },
  async mounted() {
    const route = useRoute()
    const id = route.params.id
    this.state = 'loading'
    try {
      this.rankings = await getPublicRankings(id)
      this.state = 'loaded'
    } catch (err) {
      this.state = 'error'
      this.message = 'Something went wrong'
    }
  },
  computed: {
    loading() {
      return this.state == 'loading'
    },
    loaded() {
      return this.state == 'loaded'
    }
  }
}
</script>

<i18n>
{
  "en": {
    "title": "Rankings",
    "subtitle": "Below is a list of shared rankings",
    "share-button": "Share this page",
    "share-button-done": "URL copied!"
  },
  "ja": {
    "title": "ランキング",
    "subtitle": "以下は共有されたランキングの一覧です。",
    "share-button": "このページを共有する",
    "share-button-done": "ＵＲＬコピーした!"
  }
}
</i18n>