import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Dialog from 'vue-dialog-loading'
import 'bootstrap/dist/css/bootstrap.css' 


Vue.config.productionTip = false

//axios.defaults.baseURL = 'http://127.0.0.1:3250'
axios.defaults.headers.post['Content-Type'] = 'application/json'

Vue.use(VueAxios, axios)

Vue.use(Dialog)

Vue.directive('ctitle', {
  inserted: function(el, binding){
    document.title = binding.value
  }
})



new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
