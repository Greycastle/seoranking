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
            <input :disabled="isAdding" placeholder="your keyword" v-model="keyword" class="remember-input u-full-width" type="text" id="keyword">

        </div>
        <div class="six columns">
          <label for="site">Site</label>
          <input :disabled="isAdding" placeholder="site.xyz" v-model="site" class="remember-input u-full-width" type="text" id="site">
        </div>
      </div>
      <p>
        <button :disabled="isAdding" @click="add()" class="button-primary" type="button">{{ buttonText }}</button>
      </p>
      <PromiseBuilder :promise="addingPromise" v-if="addingPromise">
        <template #fulfilled>
          Congrats, new keyword was added!
        </template>
        <template #rejected>
          We're sorry, some error occurred. Please try again later.
        </template>
      </PromiseBuilder>
    </form>
  </div>
</template>

<script>
import addRanking from '@/services/addRanking'
import PromiseBuilder from './PromiseBuilder.vue'

export default {
  components: { PromiseBuilder },
  props: {
    defaultSite: String
  },
  data() {
    return {
      site: null,
      keyword: null,
      addingPromise: null,
      isAdding: false
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
      return this.isAdding ? 'Saving..' : 'Add ranking'
    }
  },
  methods: {
    async add() {
      this.isAdding = true
      this.addingPromise = addRanking(this.site, this.keyword)
      await this.addingPromise.finally(() => this.isAdding = false)
      this.$emit('added', { site: this.site, keyword: this.keyword })
    }
  }
}
</script>