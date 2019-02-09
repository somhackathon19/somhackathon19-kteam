<template>
  <section class="hero is-success is-fullheight">
    <div class="hero-head1">
      <header class="navbar bg-nav is-transparent">
        <a class="navbar-item">
          <img src="https://bulma.io/images/bulma-type-white.png" alt="Logo">
        </a>
      </header>
    </div>
    <div class="hero-body">
      <div class="container has-text-centered">
        <h1 class="title">Events
          <router-link to="newEvent">
            <a class="button is-rounded is-primary">
              <span class="icon is-small">
                <i class="fas fa-plus"></i>
              </span>
            </a>
          </router-link>
        </h1>
        <h2 class="subtitle">crear events</h2>
        {{ $store.state.count }}
        <div class="columns is-multiline is-mobile">
          <div class="column is-4" v-for="event in events" v-bind:key="event['_id']['$oid']">
            <router-link v-bind:to="'/event/'+event['_id']['$oid']">
              <event-card v-bind:event="event"></event-card>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <pre>{{events}}</pre>
  </section>
</template>

<script>
import EventCard from "@/components/EventCard";
import EventDetail from "@/components/EventDetail";
import { mapGetters, mapActions } from 'vuex'
import store from '../store'
export default {
  name: "Events",
  components: {
    EventCard,
    EventDetail
  },
  data() {
    return {
    };
  },
  computed: {
    events () {
      return store.state.events
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar {
  display: flex;
  justify-content: center;
}
.bg-nav {
  background-color: cadetblue;
}
</style>
