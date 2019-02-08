import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Events from '@/components/Events'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/events',
      name: 'Events',
      component: Events
    }
  ]
})
