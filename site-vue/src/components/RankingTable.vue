<template>
  <div class="page-section">
    <h3>{{ $t('title') }}</h3>
    <table v-if="loaded" style="width: 100%">
      <thead>
        <tr>
          <th><Sorting sortKey="site" :selectedKey="sortBy" @sorted="sort">{{ $t('header.site') }}</Sorting></th>
          <th><Sorting sortKey="keyword" :selectedKey="sortBy" @sorted="sort">{{ $t('header.keyword') }}</Sorting></th>
          <th><Sorting sortKey="lastRanking" :selectedKey="sortBy" @sorted="sort">{{ $t('header.lastRanking') }}</Sorting></th>
          <th><Sorting sortKey="lastConfirmed" :selectedKey="sortBy" @sorted="sort">{{ $t('header.lastConfirmed') }}</Sorting></th>
          <th>{{ $t('header.rankingStatistics') }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="ranking in sortedRankings" :key="ranking.keyword">
          <td>{{ ranking.site }}</td>
          <td>{{ ranking.keyword }}</td>
          <td>
            <span v-if="ranking.lastRanking" :class="rankClass(ranking.lastRanking)">{{ getRanking(ranking.lastRanking) }}</span>
            <span class="error" v-else>Below top 5 pages</span>
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
import Sorting from './Sorting.vue'

export default {
  components: {
    Sorting
  },
  data() {
    return {
      sortBy: 'site',
      direction: 'down',
      sortedRankings: []
    }
  },
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
  watch: {
    loaded(value) {
      const clientSetting = localStorage.getItem('sort-order')
      let sortOrder = {key: 'lastRanking', direction: 'down'}
      if (clientSetting) {
        sortOrder = JSON.parse(clientSetting)
      }
      if (value) {
        this.sort(sortOrder)
      }
    }
  },
  methods: {
    sort({key, direction}) {
      this.sortDirection = direction
      this.sortBy = key
      localStorage.setItem('sort-order', JSON.stringify({ key, direction }))

      this.sortedRankings = [...this.rankings]
      this.sortedRankings.sort((e1, e2) => this.compareRankings(e1, e2))
    },
    compareRankings(e1, e2) {
      const defaultRank = 99
      const val1 = e1[this.sortBy] || defaultRank
      const val2 = e2[this.sortBy] || defaultRank

      const modifier = this.sortDirection == 'down' ? 1 : -1;
      if (val1.localeCompare)
        return e1[this.sortBy].localeCompare(e2[this.sortBy]) * modifier

      return (val1 - val2) * modifier
    },
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