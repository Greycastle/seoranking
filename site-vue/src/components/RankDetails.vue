<template>
  <div class="container">
    <section class="header">
      <h2 class="title">{{ $t('title') }}</h2>
      <router-link v-if="$auth.user" to="/dashboard">{{ $t('dashboard-link') }}</router-link>
    </section>

    <PromiseBuilder :promise="loadPromise" v-if="loadPromise">
      <template #pending>
        <div class="page-section">
          <Skeletor height="120" />
        </div>
      </template>
      <template #rejected>
        <div class="page-section">
          <p>Something went wrong..</p>
        </div>
      </template>
      <template #fulfilled>
        <div class="page-section">
          <h3>Ranking</h3>
          <p v-html="$t('overview.subtitle', { site, keyword })"></p>
          <button @click="share">{{ copied ? $t('overview.button-copied') : $t('overview.button-share') }}</button>
        </div>
        <div class="page-section">
          <h3>{{ $t('stats.title') }}</h3>
          <RankChart :dataPoints="statistics" v-if="hasRanks" />
          <p v-else>{{ $t('stats.none') }}</p>
        </div>

        <div class="page-section">
          <h3>{{ $t('competition.title') }}</h3>
          <div>
            <div :class="competitor.matchClass" v-for="(competitor, index) in competitors" :key="index" class="competitor-card">
              <div class="rank">{{ index + 1 }}</div>
                <div class="competitor">
                  <span class="title">{{ competitor.title }}</span>
                  <a class="url" :href="competitor.link" target="_blank"><span>{{ competitor.link }}</span></a>
                </div>
            </div>
          </div>
        </div>
      </template>
    </PromiseBuilder>

    <Footer />
  </div>
</template>

<script>
import { useRoute } from 'vue-router'
import RankChart from '@/components/RankChart'
import getDetails from '@/services/details'
import useClipboard from 'vue-clipboard3'

export default {
  components: {
    RankChart
  },
  data() {
    return {
      loadPromise: null,
      id: 'pending..',
      competitors: [],
      keyword: null,
      site: null,
      copied: false,
      statistics: [
        { date: new Date(2021, 9, 14), rank: 1 },
        { date: new Date(2021, 9, 15), rank: 2 },
        { date: new Date(2021, 9, 16), rank: 1 },
        { date: new Date(2021, 9, 17), rank: 5 },
        { date: new Date(2021, 9, 18), rank: 3 },
        { date: new Date(2021, 9, 19), rank: 15 },
        { date: new Date(2021, 9, 20), rank: 3 },
      ]
    }
  },
  methods: {
    async share() {
      const { toClipboard} = useClipboard()
      await toClipboard(window.location.href)
      this.copied = true
      setTimeout(() => this.copied = false, 2500)
    }
  },
  async mounted() {
    const route = useRoute()
    this.id = route.params.id
    this.loadPromise = getDetails(this.id)
    const data = await this.loadPromise
    this.competitors = data.competitors

    this.site = data.ranking.site
    this.keyword = data.ranking.keyword
    this.statistics = data.stats.map((stat) => {
      return {
        date: Date.parse(stat.date),
        rank: stat.rank
      }
    }).filter((item) => item.rank !== null).reverse()

    const siteRegex = new RegExp('(http|https)://(.+\\.)?' + 'greycastle.se')
    for (let competitor of this.competitors) {
      competitor.matchClass = competitor.link.match(siteRegex) ? 'match' : ''
    }
  },
  computed: {
    isLoggedIn() {
      return this.$auth.user != null
    },
    hasRanks() {
      return this.statistics.length > 0
    }
  },
}
</script>

<i18n>
{
  "en": {
    "title": "Rank details",
    "dashboard-link": "Back to dashboard",
    "overview": {
      "title": "Ranking",
      "subtitle": "Tracking <b>{site}</b> for <b>{keyword}</b>",
      "button-share": "Share this page",
      "button-copied": "Copied to clipboard!"
    },
    "stats": {
      "title": "Ranking statistics",
      "none": "This keyword has not ranked since it started being tracked."
    },
    "competition": {
      "title": "CURRENT COMPETITOR PLACEMENT"
    }
  },
  "ja": {
    "title": "ランキング詳細",
    "dashboard-link": "ダッシュボードへ戻る",
    "overview": {
      "title": "ランキング",
      "subtitle": "「<b>{site}</b>」サイトを「<b>{keyword}</b>」キーワードでランキングしています",
      "button-share": "このページを共有する",
      "button-copied": "コピーされました!"
    },
    "stats": {
      "title": "ランキングスタティスティックス",
      "none": "サイトはこのキーワードでまだ検索に上の50件の中には表示されていません"
    },
    "competition": {
      "title": "現在の競合状態"
    }
  },
}
</i18n>

<style scoped>

.competitor-card {
  display: block;
  display: flex;
  flex-direction: row;
  margin: 12px 0px;
  border: 1px solid gray;
  border-radius: 8px;
  align-items: stretch;
  width: 100%;
}

.competitor-card .rank {
  border-radius: 8px 0 0 8px;
  min-width: 48px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 2em;
  font-weight: bold;
}

.competitor-card .competitor {
  display: flex;
  flex-direction: column;
  padding: 4px 8px;
  min-width: 0;
}

.competitor-card .title {
  font-size: 1.2em;
}

.competitor-card .url {
  font-size: 0.8em;
  opacity: 0.6;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}

.competitor-card.match {
  background: #33F09E;
}

.competitor-card:hover {
  background: #eee;
  border-color: #222;
}

</style>