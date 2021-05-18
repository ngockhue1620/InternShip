<template>
  <div class="card-item-in-cart">
    <img
      class="product-Image-content-cart"
      :src="product.imageAddress"
      alt="Card image cap"
    />
    <div class="card-body">
      <p class="card-text">
        {{ product.productName }}
      </p>
      <p class="product-price">{{ product.price }} VNĐ</p>
      <p>{{product.description}}</p>
    </div>
    
  </div>
  <!-- Button trigger modal -->
</template>

<script>
export default {
  props: {
    product: Object,
  },
};
</script>

<style>
img.product-Image-content-cart {
  width: 70%;

  height: 381px;
}
.card-item-in-cart {
  margin: auto;
}
</style>