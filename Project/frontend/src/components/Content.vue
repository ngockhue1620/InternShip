<template>
  <div class="container">
    <div class="row">
    <div class="card col-sm" style="width: 18rem"
    v-for="product in getProduct" :key = product.id
    >
      <img :src="product.image" class="card-img-top"  />
      <div class="card-body">
        <h5 class="card-title">{{product.productName}}</h5>
        <p class="card-text">
         {{product.description}}
        </p>
        <button @click="addTocart(product)" class="btn btn-primary">Add to cart</button>
      </div>
    </div>
     </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  data() {
    return {
      listProduct: [],
    };
  },
  created() {
    this.fetchProduct();
  },
  computed: {
      ...mapGetters(['getProduct'])
  },
  methods: {
    ...mapActions(["fetchProduct",'addTocart']),
  },
};
</script>

<style>
img.card-img-top {
    width: 100%;
    height: 67%;
}
</style>