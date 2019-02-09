import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Events from '@/components/Events'
import EventDetail from '@/components/EventDetail'
import NewEvent from '@/components/NewEvent'
import Calendari from '@/components/Calendari'

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
      path: '/event/new',
      name: 'New Event',
      component: NewEvent
    },
    {
      path: '/event/:id',
      name: 'Event Detail',
      component: EventDetail
    },
    {
      path: '/calendari',
      name: 'Calendari',
      component: Calendari
    }
  ]
})
