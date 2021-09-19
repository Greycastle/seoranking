import { createRouter, createWebHistory } from 'vue-router'

// Public routes
import DefaultLayout from '@/layouts/DefaultLayout'
import Top from '@/components/Top';
import Login from '@/components/Login';
import LoginByUrl from '@/components/LoginByUrl';
import NotFound from '@/components/NotFound';
import SignedOut from '@/components/SignedOut';
import About from '@/components/About';
import Pricing from '@/components/Pricing';
import RankDetails from '@/components/RankDetails';

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
          name: 'Top',
          component: Top,
          meta: {
            redirectIfSignedIn: true
          }
        },
        {
          path: 'login',
          component: Login,
          meta: {
            redirectIfSignedIn: true
          }
        },
        {
          path: 'login-by-url',
          component: LoginByUrl,
          meta: {
            redirectIfSignedIn: true
          }
        },
        {
          path: 'dashboard',
          name: 'Dashboard',
          component: Dashboard,
          meta: {
            requiresAuth: true
          }
        },
        {
          path: 'signed-out',
          component: SignedOut
        },
        {
          path: 'about',
          component: About
        }
        ,
        {
          path: 'pricing',
          component: Pricing
        },
        {
          path: 'details/:id',
          component: RankDetails
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