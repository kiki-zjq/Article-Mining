import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
const store = new Vuex.Store({
    state:{
        language:'Chinese'
    },
    mutations:{
        changeLanguage(state){
            if(state.language == 'Chinese'){
                state.language = 'English'
            }else{
                state.language = 'Chinese'
            }
            alert(state.language)
        }
    }

})