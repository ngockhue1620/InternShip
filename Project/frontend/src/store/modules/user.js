import axios from "axios"

const user ={
    state={
        isAuthentication:false,
        token:''
    },
    getters={

    },
    actions={
        async login({commit},user){
            await axios.post('')
        }
        
    },
    mutations={

    }
}

export default user