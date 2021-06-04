import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import Content from '../components/Content.vue'
import Cart from '../components/cart/Cart.vue'

const routes = [
    { path: '/',name:'Home', component: Content },
    { path: '/cart', component: Cart }
    
  ]
  
  
  const router = new VueRouter({
    routes // short for `routes: routes`
  })

  export default router