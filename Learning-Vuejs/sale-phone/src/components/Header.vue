<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <router-link  class="btn btn-outline-info" to='/'>SHOP</router-link>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          
          <router-link  class="nav-link" to="/">HOME</router-link>
        </li>
        
      </ul>
      <div class="cart">
        
        <router-link  class="btn btn-outline-info" to="/cart">
       
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-cart-dash"
          viewBox="0 0 16 16"
        >
          <path d="M6.5 7a.5.5 0 0 0 0 1h4a.5.5 0 0 0 0-1h-4z" />
          <path
            d="M.5 1a.5.5 0 0 0 0 1h1.11l.401 1.607 1.498 7.985A.5.5 0 0 0 4 12h1a2 2 0 1 0 0 4 2 2 0 0 0 0-4h7a2 2 0 1 0 0 4 2 2 0 0 0 0-4h1a.5.5 0 0 0 .491-.408l1.5-8A.5.5 0 0 0 14.5 3H2.89l-.405-1.621A.5.5 0 0 0 2 1H.5zm3.915 10L3.102 4h10.796l-1.313 7h-8.17zM6 14a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm7 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"
          />
          
        </svg>
        {{count_amount_cart}}
        </router-link>

      </div>
      <div class="form-inline my-2 my-lg-0" method="get">
        <input
          class="form-control mr-sm-2"
          type="text"
          placeholder="Search"
          aria-label="Search"
          v-model="keyWord"
        />
        <button class="btn btn-outline-success my-2 my-sm-0" 
        @click="search(keyWord)">
          Search
        </button>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapActions,mapGetters} from 'vuex'
export default {
  name: "HelloWorld",
  data() {
    return {
      keyWord:""
    }
  },
  computed:{
    ...mapGetters(['count_amount_cart'])
  },
  methods: {
    ...mapActions(['search']),
   
  },
};
</script>

