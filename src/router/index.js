import Vue from 'vue'
import Router from 'vue-router'

import Algorithm from '@/views/algorithm/index.vue'

Vue.use(Router)

export default new Router({
    routes:[
        {
            path: '/',
            name: 'Algorithm',
            component: Algorithm
        }
    ]



})