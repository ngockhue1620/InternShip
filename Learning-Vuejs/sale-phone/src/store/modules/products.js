import axios from 'axios'

const state ={
    listProduct:[],
    query_search:""

}

const getters={
    getProduct:state=>{
        if(state.query_search=="")
        {   
           
            return state.listProduct
        }

        else
        {       
            let products=[]
            state.listProduct.map(product=>{
                // let productName =
                let index=product.productName.toUpperCase().search(!isNaN(state.query_search)?state.query_search:state.query_search.toUpperCase())
                if(index>=0|product.id==1)
                {
                    products.push(product)
                }
            })
           
            
            return products;
        }
        
    }
}

const actions ={
    async getListProduct({commit})
    {
        try {
            await axios.get('http://laravel-react-sell-web.herokuapp.com/api/product').
            then(response=>{
                commit('GET_PRODUCTS', response.data)
                
            })
           
          } catch (error) {
              console.log(error)
          } 
    },
    search({commit},keyWord)
    {
        commit('SEARCH',keyWord)

    },
    delete_search({commit})
    {
        commit('DELETE_SEARCH')
    }

}

const mutations ={
    GET_PRODUCTS(state,products)
    {
        state.listProduct=products
        console.log("list",state.listProduct)
    },
    SEARCH(state,keyWord)
    {
        state.query_search=keyWord
    },
    DELETE_SEARCH(state)
    {
        state.query_search=""
    }

}

export default {
    state,
    getters,
    mutations,
    actions
}