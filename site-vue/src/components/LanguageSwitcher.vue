<template>
  <span class="languages">
    <span v-for="(locale, index) in locales" :key="index">
      <span v-if="isSelected(locale)">{{ locale.toUpperCase() }}</span>
      <a @click="setLocale(locale)" v-else>{{ locale.toUpperCase() }}</a>
      <span v-if="index < locales.length - 1">&nbsp;|&nbsp;</span>
    </span>
  </span>
</template>

<script>
import { saveClientLocale } from '../i18n'

export default {
  data() {
    return {
      locales: this.$i18n.availableLocales
    }
  },
  methods: {
    isSelected(locale) {
      return locale == this.$i18n.locale
    },
    setLocale(locale) {
      saveClientLocale(locale)
      this.$i18n.locale = locale
    }
  }
}
</script>

<style scoped>
.languages {
  margin-left: 12px;
}

.languages a {
  cursor: pointer;
}
</style>