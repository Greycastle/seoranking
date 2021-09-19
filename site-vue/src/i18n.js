import { createI18n } from 'vue-i18n/index'

const messages = {
  en: {
    test: 'test'
  },
  ja: {
    test: 'test'
  }
}

const i18n = createI18n({
  locale: 'ja',
  fallbackLocale: 'en',
  messages
})

export default i18n