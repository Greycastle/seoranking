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
              <td>{{ toOrdinal(ranking.lastRanking) }} place</td>
              <td>{{ getTimeAgo(ranking.lastConfirmed) }} ago</td>
              <td><a href="...">Download past {{ranking.rankingsTotal}} rankings</a></td>
            </tr>
          </tbody>
        </table>
        <Skeletor height="200" v-if="loading" as="div" />
      </div>

      <div class="page-section">
        <h3>Add more rankings</h3>
        <p>
          You can add more keywords or sites as well:
        </p>
        <form id="add-ranking-form">
          <div class="row">
            <div class="six columns">
                <label for="keyword">Keyword</label>
                <input placeholder="yummy greens" class="remember-input u-full-width" type="text" id="keyword">

            </div>
            <div class="six columns">
              <label for="site">Site</label>
              <input placeholder="greens.zed" class="remember-input u-full-width" type="text" id="site">
            </div>
          </div>
          <p>
            <button id="add-ranking" class="button-primary" type="button">Add ranking</button>
          </p>
        </form>
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

export default {
  data() {
    return {
      state: 'loading',
      rankings: [],
      account: null
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
    }
  },
  async created() {
    this.state = 'loading'
    try {
      const data = await getRankingData()
      this.rankings = data.rankings
      this.account = data.account
      this.state = 'loaded'
    } catch (err) {
      this.state = 'error'
      this.message = 'Something went wrong'
    }
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