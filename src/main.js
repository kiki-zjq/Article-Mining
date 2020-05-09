// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import $ from 'jquery'
import './plugins/element.js'
import axios from 'axios'
import Vuex from 'vuex'
import "font-awesome/css/font-awesome.css"
// import store from './store/index.js'

Vue.use(Vuex)
Vue.prototype.$http=axios
Vue.config.productionTip = false

const store = new Vuex.Store({
  state:{

    },
  mutations:{

      },
  getters: {},
  actions: {},
});
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
