<template>
  <div>
    <div class="container">
      <section class="header">
        <h2 class="title">History</h2>
        <p>
            Welcome in! Here's your recent history and remaining credits.
        </p>
      </section>

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
              <td><a href="...">Download past {{ranking.rankingsTotal}} rankings</a></td>
            </tr>
          </tbody>
        </table>
        <Skeletor height="200" v-if="loading" as="div" />
      </div>

      <div class="page-section">
        <AddRanking @added="onAdded" :defaultSite="defaultSite" />
      </div>

      <div class="page-section">
        <h3>Credit status</h3>
        <Skeletor v-if="loading" />
        <Skeletor v-if="loading" />
        <div v-if="loaded">
          <p>
            You have done <b>{{ account.ranksTotal }}</b> rank checks this far and have another <b>{{ account.ranksRemaining }}</b> remaining. As you are running a rank check <b>{{ schedule }}</b> on <b>1 keyword</b> it will last for another <b>{{ daysLeft }}</b>.
          </p>
          <h3>Running out?</h3>
          <p>
            No worries! Right now, this service is completely new and still in BETA so if you need more funds, send me an email at <a href="mailto:david@greycastle.se?subject=I%20need%20more%20credits!">david@greycastle.se</a> and I'll sort it out for free!
          </p>
        </div>
      </div>

      <div class="page-section">
        <h3>About</h3>
        <p>
            This app is built by <a target="_blank" href="https://twitter.com/almundgrey">David</a> @ <a target="_blank" href="https://greycastle.se">Greycastle</a>, visuals based on the <a target="_blank" href="http://getskeleton.com/">Skeleton</a> css framework. <a href="about.html">About</a> | <a href="pricing.html">Pricing</a> | <a @click="logout">Logout</a>.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { pluralize, ordinal } from 'humanize-plus'
import humanizeDuration from 'humanize-duration'
import getRankingData from '@/services/rankingData'
import AddRanking from '@/components/AddRanking'

export default {
  components: {
    AddRanking
  },
  data() {
    return {
      state: 'loading',
      rankings: [],
      account: null,
      defaultSite: ''
    }
  },
  methods: {
    async logout() {
      await this.$auth.logout()
      this.$router.push('signed-out')
    },
    toOrdinal(val) {
      return ordinal(val)
    },
    getTimeAgo(date) {
      return humanizeDuration(new Date() - date, { round: true, largest: 1 })
    },
    getRanking(rank) {
      if (rank) {
        return `${this.toOrdinal(rank)} place`
      }

      return 'Pending..'
    },
    async load() {
      this.state = 'loading'
      try {
        const data = await getRankingData()
        this.rankings = data.rankings
        this.account = data.account
        if (this.rankings.length > 0) {
          this.defaultSite = this.rankings[0].site
        }
        this.state = 'loaded'
      } catch (err) {
        this.state = 'error'
        this.message = 'Something went wrong'
      }
    },
    onAdded() {
      this.load()
    }
  },
  async created() {
    this.load()
  },
  computed: {
    schedule() {
      return this.account.rankSchedule == 1 ? 'every day' : `every ${this.account.rankSchedule} days`
    },
    daysLeft() {
      const remainingEstimate = Math.floor(this.account.ranksRemaining / ((1 / this.account.rankSchedule) * this.rankings.length))
      return `${remainingEstimate} ${pluralize(remainingEstimate, 'day')}`
    },
    loading() {
      return this.state == 'loading'
    },
    loaded() {
      return this.state == 'loaded'
    }
  }
}
</script>

<style scoped>
</style>