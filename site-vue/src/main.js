// CSS imports
import './assets/normalize.css'
import './assets/skeleton.css'
import './assets/site.css'
import 'vue-skeletor/dist/vue-skeletor.css';

// Firebase
import { initializeApp } from 'firebase/app';
const firebaseConfig = {
  apiKey: "AIzaSyCPVxNQjSUH4lbV4srGxT26YkhYANxj5Fw",
  authDomain: "seoranking-324303.firebaseapp.com",
  projectId: "seoranking-324303",
  storageBucket: "seoranking-324303.appspot.com",
  messagingSenderId: "950631750849",
  appId: "1:950631750849:web:74515513e16bc068560840",
  measurementId: "G-WSP006WNBZ"
};
const firebaseApp = initializeApp(firebaseConfig);

// Vue setup
import { createApp } from 'vue'
import auth from './auth';
import router from './router';
import DefaultLayout from './layouts/DefaultLayout'

// Global components
import { Skeletor } from 'vue-skeletor';
import Footer from '@/components/Footer'
import PromiseBuilder from '@/components/PromiseBuilder'

import i18n from './i18n'


const app = createApp(DefaultLayout)
app.use(i18n)
app.use(router)
app.use(auth, { firebaseApp })
app.component(Skeletor.name, Skeletor);
app.component('Footer', Footer);
app.component('PromiseBuilder', PromiseBuilder);
app.mount('#app')
