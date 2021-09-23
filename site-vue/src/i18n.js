import { createI18n } from 'vue-i18n/index'

// the actual translations are in each vue file
const locales = {
  "en": {},
  "ja": {}
}

const fallbackLocale = 'en'
const localeSettingKey = 'user-locale'
let clientLocale = localStorage.getItem(localeSettingKey) || fallbackLocale

if (!locales[clientLocale]) {
  console.log(`No support for locale device '${clientLocale}', defaulting to '${fallbackLocale}'`)
  clientLocale = fallbackLocale
}

const i18n = createI18n({
  locale: clientLocale,
  fallbackLocale,
  messages: locales
})

const saveClientLocale = (locale) => {
  localStorage.setItem(localeSettingKey, locale)
}

export default i18n

export {
  saveClientLocale
}