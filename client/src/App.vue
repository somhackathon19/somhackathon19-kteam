<template>
  <div id="app">
    <transition name="fade" mode="out-in">
        <router-view/>
      </transition>
  </div>
</template>

<script>
import io from 'socket.io-client';
import store from './store'
import axios from 'axios'
export default {
  name: 'App',
  data() {
    return {
      socket : io('localhost:5000')
    };
  },
  created() {
    this.socket.on('sendEvents', (data) => {
      store.commit('setEvents', data)
    });
    this.socket.emit('getEvents');
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
