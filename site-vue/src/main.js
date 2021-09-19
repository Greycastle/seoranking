// CSS imports
import './assets/normalize.css'
import './assets/skeleton.css'
import './assets/site.css'

// Vue setup
import { createApp } from 'vue'
import router from './router';

import DefaultLayout from './layouts/DefaultLayout'

const app = createApp(DefaultLayout)
app.use(router)
app.mount('#app')
