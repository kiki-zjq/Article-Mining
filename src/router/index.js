import Vue from 'vue'
import Router from 'vue-router'
import Homepage from '@/view/homepage/index.vue'
import Install from '@/view/install/index.vue'
import Document from '@/view/document/index.vue'
import Example from '@/view/example/index.vue'
import Simulator from '@/view/simulator/index.vue'
import Contact from '@/view/contact/index.vue'
<<<<<<< HEAD

import Query from '@/view/query/index.vue'
=======
import Query from '@/view/query/index.vue'

>>>>>>> 1407ff8d6ffabdb6d9f16968993e83a9ff9152e5
import Algorithm from '@/view/algorithm/index.vue'
import Search from '@/view/algorithm/search.vue'
import MeetCount from '@/view/algorithm/meetCount.vue'
import YearCount from '@/view/algorithm/yearCount.vue'
import CompareCount from '@/view/algorithm/compareCount.vue'
<<<<<<< HEAD
import Meeting from '@/view/meeting/index.vue'

=======
>>>>>>> 1407ff8d6ffabdb6d9f16968993e83a9ff9152e5

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Homepage',
      component: Homepage
    },
    {
      path: '/Install',
      name: 'Install',
      component: Install
    },
    {
      path: '/Document',
      name: 'Document',
      component: Document
    },
    {
      path: '/Example',
      name: 'Example',
      component: Example
    },
    {
      path:'/Simulator',
      name:'Simulator',
      component:Simulator
    },
    {
      path:'/Contact',
      name:'Contact',
      component:Contact
    },
    {
      path:'/query',
      name:'query',
      component:Query
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
<<<<<<< HEAD
    {
      path:'/meeting',
      component:Meeting,
    }
  ],


=======
  ],


>>>>>>> 1407ff8d6ffabdb6d9f16968993e83a9ff9152e5
  scrollBehavior (to, from, savedPosition) {
    if (to.hash) {
      //console.log(to.hash)
      return {
        selector: to.hash
      }
    }
  }
})
