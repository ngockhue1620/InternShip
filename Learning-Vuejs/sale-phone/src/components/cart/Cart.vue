<template>
  <div class="cart-component">
    <div class="order-info">
      <Cart-Item-Detail v-if="getCartList().length > 0" :product="product" />
    </div>
    <div >
      <p>Tổng Tiền:{{ count_total_cart }} VNĐ</p>
      <div class="cart-item" >
        <table class="table table-cart-list">
          <thead class="thead-dark">
            <tr>
              <th scope="col">STT</th>
              <th scope="col">Image</th>
              <th scope="col">ProductName</th>
              <th scope="col">Price</th>
              <th scope="col">Số Lượng</th>
              <th scope="col">Thành Tiền</th>
              <th scope="col">Action</th>
            </tr>
          </thead>
          <tbody v-if="getCartList().length > 0"
            
            >
            <CartItem
              v-for="(product, index) in getCartList()"
              :key="index"
              :product="product"
              :index="index"
              :transmit_Product="transmit_Product"
            />

            <tr>
              <td></td>
              <td></td>
              <td>Tổng Tiền</td>
              <td colspan="2">{{ count_total_cart }} VNĐ</td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
          <tbody v-else style="margin:outo">
            <div class="alert alert-warning containner" role="alert">
              
                   <p style="margin:auto">Ban Chưa Có Mặt Hàng Nào</p>
              
             
            </div>
          </tbody>
        </table>
        <button class='btn btn-primary'>Thanh toan</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import CartItemDetail from "./CartItemDetail";
import CartItem from "./CartItem";
export default {
  components: {
    CartItemDetail,
    CartItem,
  },
  data() {
    return {
      product: this.getCartList()[0],
    };
  },
  computed: {
    ...mapGetters(["count_total_cart"]),
  },
  methods: {
    ...mapGetters(["getCartList"]),
    transmit_Product(product) {
      this.product = product;
    },
  },
};
</script>

<style>
.cart-component {
  display: flex;
}

.order-info {
  width: 30%;
  margin: 1%;
}

.cart-item {
  margin: 1%;
  background: lightsteelblue;
  height: 500px;
  overflow: scroll;
}
</style>