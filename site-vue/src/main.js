// CSS imports
import './assets/normalize.css'
import './assets/skeleton.css'
import './assets/site.css'

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

const app = createApp(DefaultLayout)
app.use(router)
app.use(auth, { firebaseApp })
app.mount('#app')
