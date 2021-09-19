<template>
  <div>
    <h3>Add more rankings</h3>
    <p>
      You can add more keywords or sites as well:
    </p>
    <form id="add-ranking-form">
      <div class="row">
        <div class="six columns">
            <label for="keyword">Keyword</label>
            <input :disabled="adding" placeholder="your keyword" v-model="keyword" class="remember-input u-full-width" type="text" id="keyword">

        </div>
        <div class="six columns">
          <label for="site">Site</label>
          <input :disabled="adding" placeholder="site.xyz" v-model="site" class="remember-input u-full-width" type="text" id="site">
        </div>
      </div>
      <p>
        <button :disabled="adding" @click="add()" class="button-primary" type="button">{{ buttonText }}</button>
      </p>
      <transition name="fade">
        <p v-if="isAdded">
          Congrats, new keyword was added!
        </p>
      </transition>
      <transition name="fade">
        <p v-if="hasError">
          We're sorry, some error occurred. Please try again later.
        </p>
      </transition>
    </form>
  </div>
</template>

<script>
import addRanking from '@/services/addRanking'

export default {
  props: {
    defaultSite: String
  },
  data() {
    return {
      site: null,
      adding: false,
      isAdded: false,
      hasError: false,
      keyword: null
    }
  },
  watch: {
    defaultSite(newSite) {
      if (this.site) return
      this.site = newSite
    }
  },
  computed: {
    buttonText() {
      return this.adding ? 'Saving..' : 'Add ranking'
    }
  },
  methods: {
    showError() {
      this.hasError = true
      setTimeout(() => this.hasError = false, 2500)
    },
    showAdded() {
      this.isAdded = true
      setTimeout(() => this.isAdded = false, 2500)
    },
    async add() {
      try {
        this.adding = true
        await addRanking(this.site, this.keyword)
        this.adding = false
        this.$emit('added', { site: this.site, keyword: this.keyword })
        this.showAdded()
      } catch(err) {
        this.adding = false
        this.showError()
      }
    }
  }
}
</script>