<template>
  <div class="page-section">
    <h3>Rank history</h3>
    <table v-if="loaded" style="width: 100%">
      <thead>
        <tr>
          <th>Site</th>
          <th>Keyword</th>
          <th>Last ranking</th>
          <th>Last confirmed</th>
          <th>Ranking statistics</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="ranking in rankings" :key="ranking.keyword">
          <td>{{ ranking.site }}</td>
          <td>{{ ranking.keyword }}</td>
          <td>{{ getRanking(ranking.lastRanking) }}</td>
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
    getRanking(rank) {
      if (rank) {
        return `${ordinal(rank)} place`
      }

      return 'Pending..'
    },
  }
}
</script>