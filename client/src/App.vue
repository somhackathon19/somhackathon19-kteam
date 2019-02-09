<template>
  <div id="app">
    <transition name="fade" mode="out-in">
        <router-view/>
      </transition>
  </div>
</template>

<script>
import store from './store'
import axios from 'axios'
export default {
  name: 'App',
  created() {
    // axios
    // .get('http://localhost:5000/api/events')
    // .then((response) => {
    //   if (response.status === 200) {
    //     store.commit('setEvents', response.data)  
    //   }
    // })
  }
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.2s;
  transition-property: opacity;
  transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
  opacity: 0
}
</style>
