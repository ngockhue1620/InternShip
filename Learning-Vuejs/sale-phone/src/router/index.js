import { createRouter, createWebHistory } from 'vue-router'
import Body from '../components/Body'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Body
  },
  {
    path: '/cart',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../components/cart/Cart')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router