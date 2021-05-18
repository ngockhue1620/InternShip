<template>
  <div class="Menu-component">
    <ul class="list-group">
      <li
        class="list-group-item"
        v-for="(item, index) in categoryList"
        :key="index"
        @click="search(item.id)"
      >
        {{ item.categoryName }}
      </li>
      
    </ul>
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
  width: 20%;
  background: cadetblue;
}
</style>