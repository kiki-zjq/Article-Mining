import Vue from 'vue'
import Router from 'vue-router'

import Homepage from '@/views/homepage/index.vue'
import Algorithm from '@/views/algorithm/index.vue'
import Search from '@/views/algorithm/search.vue'
import MeetCount from '@/views/algorithm/meetCount.vue'
import YearCount from '@/views/algorithm/yearCount.vue'
import CompareCount from '@/views/algorithm/compareCount.vue'
import Meet from '@/views/meet/index.vue'
import Meeting from '@/views/meeting/index.vue'
import MeetSearch from '@/views/meeting/search.vue'
import Query from '@/views/query/index.vue'


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
            path:'/algorithm/meetingcount/:search/:meeting',
            component:MeetCount,
        },
        {
            path:'/algorithm/yearcount/:search/:year',
            component:YearCount,
        },
        {
            path:'/algorithm/comparecount/:search/:compare',
            component:CompareCount,
        },
        {
            path:'/meet',
            component:Meet,
        },
        {
            path:'/meeting/:search',
            component:MeetSearch,
        },
        {
            path:'/meeting',
            component:Meeting,
        },
        {
            path:'/query',
            component:Query,
        }
    ]



})