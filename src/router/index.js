import Vue from 'vue'
import VueRouter from 'vue-router'

import Magnet from '../views/Magnet.vue'
import Torrent from '../views/Torrent.vue'

Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    { path: '/', redirect: '/magnet' },
    { path: '/magnet', component: Magnet },
    { path: '/torrent', component: Torrent }
  ]
})

export default router
