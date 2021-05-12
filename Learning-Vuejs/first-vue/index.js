const root ={
    data(){
        return{
            obj:{}
        }
    },
    mounted() {
        this.obj.name = "SamSumg GALAXY"
        this.obj.url  ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaxSZoaIzx1dKEIb8XNygT9ikE-iS4HV3teihEfouxfjL73WNmrrqdgklcSg&usqp=CAc"
        this.obj.price =8600000
        this.obj.quantity=1
    },
}

Vue.createApp(root).mount('#root')