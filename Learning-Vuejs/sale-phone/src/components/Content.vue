<template >
<Suspense>
  <template #default>
  <div class="Content-component ">   

    <div class="card " 
    
         v-for="product in getProduct" :key="product.id"
    >
      <img class="productImage-content" :src="product.imageAddress" alt="Card image cap" />
      <div class="card-body">
        <p class="card-text">
            {{product.productName}}
        </p>
      </div>
      <div class="component-price-Add-button">
             <p class="product-price">{{product.price}} VNĐ</p>
             <button class="btn btn-primary"
            @click="addProductTocart(product)"
             >Add To Cart</button>
        </div>
    </div>

  </div>
  </template>
  <template #fallback>

      <div  class="Content-component ">Đang tải dữ liệu</div>
  </template>
</Suspense>
</template>

<script>
// import axios from 'axios';

import { mapActions, mapGetters } from "vuex";
export default {
  data() {
    return {
      listProduct: [],
    };
  },
  created() {
    this.getListProduct();
    this.delete_search();
    //  this.testApi();
    
     
  },
  computed:{
    ...mapGetters(["getProduct"]),
  },
  methods: {
    ...mapActions(["getListProduct","addProductTocart","delete_search"]),
  //  async testApi(){

  //    await axios.get("http://127.0.0.1:90/api/category/").
  //     then(response=>{
  //       console.log(response)

        
        
  //     }).catch(e=>{
  //       console.log(e)
  //     })
  //   }

    
  },
};
</script>

<style>
.Content-component {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
}
img.productImage-content {
    height: 75%;
}
p.card-text {text-align: center;}
.card {
    width: 20rem;
    height: 40rem;
    margin-top: 1rem;
}

.component-price-Add-button {
    position: absolute;
    bottom: 0px;
    text-align: center;
    /* justify-content: center; */
    left: 30%;
}

</style>







