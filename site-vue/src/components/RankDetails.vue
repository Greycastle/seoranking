<template>
  <div class="container">
    <section class="header">
      <h2 class="title">Rank details</h2>
    </section>

    <div class="page-section">
      <h3>Ranking statistics</h3>
      <RankChart :dataPoints="statistics" />
    </div>

    <div class="page-section">
      <h3>Current competitor placement</h3>
      <div>
        <div v-for="(competitor, index) in competitors" :key="index" class="competitor-card">
          <span>Rank {{ index + 1 }}</span>
          <span>{{ competitor.domain }}</span>
          <span>{{ competitor.url }}</span>
        </div>
      </div>
    </div>

    <Footer />
  </div>
</template>

<script>
import { useRoute } from 'vue-router'
import RankChart from '@/components/RankChart'

export default {
  components: {
    RankChart
  },
  data() {
    return {
      id: 'pending..',
      competitors: [
        { domain: 'greycastle.se', url: 'https://greycastle.se' }
      ],
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
  mounted() {
    const route = useRoute()
    this.id = route.params.id
  }
}
</script>

<style scoped>

.competitor-card span {
  display: block;
}

</style>