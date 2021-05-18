const state={
    carts:[]
}

const getters={
    count_amount_cart:state=>{
       
        let amount=0;
        state.carts.map(product=>{
            amount+=product.quantity
            console.log("run")
        })
        return amount
    },
    getCartList:state=>{
        console.log(state.carts)
        return state.carts
    },
    count_total_cart:state=>{
       
        let total=0;
        state.carts.map(product=>{
            total+=parseInt(product.price)*product.quantity
            
        })
        return total
    },
    
}

const actions={
    // binary_seach(state,product)
    // {   
    //     left=0
    //     right =state.cart.lenght
    //     for(i=left;i<right;i++)
    //     {   


    //     }
    // }
    addProductTocart({commit},obj)
    {
        commit('ADD_TO_CART',obj)
    },
    updateCartQuantity({commit},obj)
    {
        commit('UPDATE_CART_QUANTITY',obj)
    },
    remove_cart_item({commit},index)
    {
        commit('REMOVE_CART_ITEM',index)
    }


}

const mutations={

    ADD_TO_CART(state,obj)
    {   
        let check=true
        state.carts.map(product=>{
            if(product.id==obj.id)
            {   
                console.log("update gio hang")
                product.quantity+=1
                check=false
                return;
            }
            
        })
        console.log("them gio hang")
        if(check==true)
        {
            obj.quantity=1
            state.carts.push(obj)
        }
        
        console.log(state.carts)
        
        
    },
    UPDATE_CART_QUANTITY(state,obj)
    {
        state.carts[obj.index].quantity=parseInt(obj.quantity)
    },
    REMOVE_CART_ITEM(state,index)
    {
        state.carts.splice(index,1)
    }
    

}
export default {
    state,
    getters,
    actions,
    mutations
}