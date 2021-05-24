<template>
  <div class="Menu-component">
   
    <!-- Example single danger button -->
    <div class="btn-group">
      <button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        Category
      </button>
      <div class="dropdown-menu">
        <ul>
        <li class="dropdown-item"
          v-for="(item, index) in categoryList"
        :key="index"
        @click="search(item.id)"
        >  {{ item.categoryName }}</li>       
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
// import axios from "axios";

import axiosinstance from "../sevice/axiosinstance";
export default {
  data() {
    return {
      categoryList: [],
    };
  },
  created() {
    this.getCategory();
  },
  methods: {
    ...mapActions(['search']),
    getCategory() {
      axiosinstance.get(`api/category`).then((response) => {        
        this.categoryList=response.data        
      });
    },
  },
};
</script>

<style>
.Menu-component {
  position: fixed;
  right: 5%;
  bottom: 20%;
  z-index: 1;
  opacity: 0.3;
}
.Menu-component:hover{
  opacity: 1;
}
.dropdown-item:hover{
 
  background: lightgreen;
}
</style>