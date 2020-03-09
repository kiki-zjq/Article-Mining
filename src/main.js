import Vue from 'vue'
import App from './App'
import router from './router'
import './plugins/element.js'
// import $ from 'jquery'
import axios from 'axios'
import Vuex from 'vuex'

Vue.use(Vuex)
Vue.prototype.$http=axios
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
