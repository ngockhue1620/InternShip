

import products from './modules/products'
import cart from './modules/cart'


import { createStore } from 'vuex'
import VuexPersistence from 'vuex-persist'
const vuexLocal = new VuexPersistence({
  storage: window.localStorage
})
const store =createStore({
    modules :
    {
        products,
        cart
    },
    plugins: [vuexLocal.plugin]
})

export default store

