<template>
  <div class="page-section">
    <h3>{{ $t('title') }}</h3>
    <table v-if="loaded" style="width: 100%">
      <thead>
        <tr>
          <th>{{ $t('header.site') }}</th>
          <th>{{ $t('header.keyword') }}</th>
          <th>{{ $t('header.lastRanking') }}</th>
          <th>{{ $t('header.lastConfirmed') }}</th>
          <th>{{ $t('header.rankingStatistics') }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="ranking in rankings" :key="ranking.keyword">
          <td>{{ ranking.site }}</td>
          <td>{{ ranking.keyword }}</td>
          <td>
            <span v-if="ranking.lastRanking" :class="rankClass(ranking.lastRanking)">{{ getRanking(ranking.lastRanking) }}</span>
            <span class="error" v-else>Below top 50</span>
          </td>
          <td>{{ getTimeAgo(ranking.lastConfirmed) }} ago</td>
          <td><router-link :to="'/details/' + ranking.downloadId">Check past {{ranking.rankingsTotal}} rankings</router-link></td>
        </tr>
      </tbody>
    </table>
    <Skeletor height="200" v-if="loading" as="div" />
  </div>
</template>

<script>
import humanizeDuration from 'humanize-duration'
import { ordinal } from 'humanize-plus'

export default {
  props: {
    rankings: {
      type: Array,
      required: true
    },
    loaded: {
      type: Boolean,
      required: true
    },
    loading: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    getTimeAgo(date) {
      return humanizeDuration(new Date() - date, { round: true, largest: 1 })
    },
    getRanking(rank) { return `${ordinal(rank)} place` },
    rankClass(rank) {
      return rank <= 3 ? 'good' : 'warn';
    }
  }
}
</script>

<i18n>
{
  "en": {
    "title": "Rank history",
    "header": {
      "site": "Site",
      "keyword": "Keyword",
      "lastRanking": "Last ranking",
      "lastConfirmed": "Last confirmed",
      "rankingStatistics": "Ranking statistics",
    }
  },
  "ja": {
    "title": "ランキング履歴",
    "header": {
      "site": "サイト",
      "keyword": "キーワード",
      "lastRanking": "最新ランク",
      "lastConfirmed": "最新確認日時",
      "rankingStatistics": "詳細",
    }
  },
}
</i18n>

<style scoped>
.error {
  color: #F03346
}

.warn {
  color: #F09E33;
}

.good {
  color: #33F09E;
}
</style>