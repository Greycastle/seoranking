<template>
  <div class="container">
    <section class="header">
      <h2 class="title">Rank details</h2>
    </section>

    <PromiseBuilder :promise="loadPromise" v-if="loadPromise">
      <template #pending>
        <div class="page-section">
          <p>Loading..</p>
        </div>
      </template>
      <template #rejected>
        <div class="page-section">
          <p>Something went wrong..</p>
        </div>
      </template>
      <template #fulfilled>
        <div class="page-section">
          <h3>Ranking statistics</h3>
          <RankChart :dataPoints="statistics" />
        </div>

        <div class="page-section">
          <h3>Current competitor placement</h3>
          <div>
            <div :class="competitor.matchClass" v-for="(competitor, index) in competitors" :key="index" class="competitor-card">
              <div class="rank">{{ index + 1 }}</div>
              <div class="competitor">
                <span class="title">{{ competitor.title }}</span>
                <span class="url">{{ competitor.link }}</span>
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

export default {
  components: {
    RankChart
  },
  data() {
    return {
      loadPromise: null,
      id: 'pending..',
      competitors: [],
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
  async mounted() {
    const route = useRoute()
    this.id = route.params.id
    this.loadPromise = getDetails(this.id)
    const data = await this.loadPromise
    this.competitors = data.competitors

    this.statistics = data.stats.map((stat) => ({date: Date.parse(stat.date), rank: stat.rank}))

    const siteRegex = new RegExp('(http|https)://(.+\\.)?' + 'greycastle.se')
    for (let competitor of this.competitors) {
      competitor.matchClass = competitor.link.match(siteRegex) ? 'match' : ''
    }
  }
}
</script>

<style scoped>

.competitor-card {
  display: block;
  display: flex;
  flex-direction: row;
  margin: 12px 0px;
  border: 1px solid gray;
  border-radius: 8px;
  align-items: stretch;
}

.competitor-card .rank {
  border-radius: 8px 0 0 8px;
  width: 48px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 2em;
  font-weight: bold
}

.competitor-card .competitor {
  display: flex;
  flex-direction: column;
  padding: 4px 8px;
}

.competitor-card .title {
  font-size: 1.2em;
}

.competitor-card .url {
  font-size: 0.8em;
  opacity: 0.6;
}

.competitor-card.match {
  background: rgb(75, 192, 192);
}

.competitor-card:hover {
  background: #eee;
  border-color: #222;
}

</style>