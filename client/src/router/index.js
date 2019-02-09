import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Events from '@/components/Events'
import EventDetail from '@/components/EventDetail'

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
    },
    {
      path: '/event/:id',
      name: 'Event Detail',
      component: EventDetail
    }
  ]
})
