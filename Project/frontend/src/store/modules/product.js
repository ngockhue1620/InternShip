import axios from 'axios'
const product ={
    state:{
        listProduct:[]
    },
    getters:{
        getProduct:state=>{
            return state.listProduct;
        }
    },
    mutations:{
        GET_PRODUCT(state,products){
            state.listProduct = products
        }

    },
    actions:{
       async fetchProduct({commit}){
            await axios.get('http://127.0.0.1:8000/api/product/')
                        .then(response=>{
                            console.log(response.data)
                            commit('GET_PRODUCT',response.data)
                        })
        }
    }
}
export default product