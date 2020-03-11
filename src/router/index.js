import Vue from 'vue'
import Router from 'vue-router'

import Homepage from '@/views/homepage/index.vue'
import Algorithm from '@/views/algorithm/index.vue'
import Search from '@/views/algorithm/search.vue'
import Meet from '@/views/meet/index.vue'
Vue.use(Router)

export default new Router({
    routes:[
        {
            path:'/',
            name:'Homepage',
            component:Homepage,
        },
        {
            path: '/algorithm',
            component: Algorithm,
            name:'Algorithm'
            
        },
        {
            path:'/algorithm/:search',
            component:Search,
        },
        {
            path:'/meet',
            component:Meet,
        }
    ]



})