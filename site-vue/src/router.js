import { createRouter, createWebHistory } from 'vue-router'

// Public routes
import DefaultLayout from '@/layouts/DefaultLayout'
import Top from '@/components/Top';
import Login from '@/components/Login';

// Secure routes
// ...

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: DefaultLayout,
      children: [
        {
          path: '',
          component: Top
        },
        {
          path: 'login',
          component: Login
        }
      ]
    },
  ],
});

export default router