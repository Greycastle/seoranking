<template>
  <div>
    <div class="container">
      <section class="header">
        <h2 class="title">{{ $t('title') }}</h2>
        <p> {{ $t('subtitle')}} </p>
      </section>

      <RankingTable :rankings="rankings" :loading="loading" :loaded="loaded" />

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

      <Footer />
    </div>
  </div>
</template>

<script>
import { pluralize } from 'humanize-plus'

import getRankingData from '@/services/rankingData'
import AddRanking from '@/components/AddRanking'
import RankingTable from '@/components/RankingTable'

export default {
  components: {
    AddRanking,
    RankingTable
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

<i18n>
{
  "en": {
    "title": "Dashboard",
    "subtitle": "Welcome in! Here's your recent history and remaining credits."
  },
  "ja": {
    "title": "ダッシュボード",
    "subtitle": "ようこそう！このページにはランキング追跡と残っているランキングポイントが見えています。"
  }
}
</i18n>