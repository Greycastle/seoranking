import { createRouter, createWebHistory } from 'vue-router'

// Public routes
import DefaultLayout from '@/layouts/DefaultLayout'
import Top from '@/components/Top';
import Login from '@/components/Login';
import LoginByUrl from '@/components/LoginByUrl';
import NotFound from '@/components/NotFound';

// Secure routes
import Dashboard from '@/components/Dashboard'

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
        },
        {
          path: 'login-by-url',
          component: LoginByUrl
        },
        {
          path: 'dashboard',
          component: Dashboard
        }
      ]
    },
    {
      path: '/:pathMatch(.*)*',
      component: NotFound
    }
  ],
});

export default router