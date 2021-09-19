import { createRouter, createWebHistory } from 'vue-router'

// Public routes
import DefaultLayout from '@/layouts/DefaultLayout'
import Top from '@/components/Top';
import Login from '@/components/Login';
import LoginByUrl from '@/components/LoginByUrl';
import NotFound from '@/components/NotFound';
import SignedOut from '@/components/SignedOut';

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
          component: Dashboard,
          meta: {
            requiresAuth: true
          }
        },
        {
          path: 'signed-out',
          component: SignedOut
        }
      ]
    },
    {
      path: '/:pathMatch(.*)*',
      component: NotFound
    }
  ],
});

// Add security
import { onAuthStateChanged, getAuth } from 'firebase/auth';
const getCurrentUser = () => {
  return new Promise((resolve, reject) => {
      const unsubscribe = onAuthStateChanged(getAuth(), user => {
          unsubscribe();
          resolve(user);
      }, reject);
  })
};

router.beforeEach(async (to, _, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const redirectIfSignedIn = to.matched.some(record => record.meta.redirectIfSignedIn);
  if (requiresAuth || redirectIfSignedIn){
    const user = await getCurrentUser();
    if (requiresAuth && !user) {
      next('login');
    } else if(redirectIfSignedIn && user) {
      next('dashboard')
    } else {
      next()
    }
  }else{
    next();
  }
})

export default router