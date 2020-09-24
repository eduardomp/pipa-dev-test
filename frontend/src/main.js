import Vue from 'vue'
import VueRouter from 'vue-router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import App from './App.vue'
import Info from './components/pages/Info'
import Bandas from './components/pages/Bandas'
import Generos from './components/pages/Generos'
import axios from 'axios';

Vue.use(VueRouter)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.config.productionTip = false

axios.defaults.headers.common['Content-Type'] = 'application/x-www-form-urlencoded'
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

const routes = [
  { path: '/', component: Info },
  { path: '/bandas', component: Bandas },
  { path: '/generos', component: Generos },
]

const router = new VueRouter({
  routes
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
