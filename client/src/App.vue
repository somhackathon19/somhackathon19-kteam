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
  data() {
    return {};
  },
  created() {
    store.state.socket.on('sendEvents', (data) => {
      console.log(data)
      store.commit('setEvents', data)
    });
    store.state.socket.emit('getEvents');
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
