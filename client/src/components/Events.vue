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
        <h1 class="title">Events</h1>
        <h2 class="subtitle">creaa events blablabla..</h2>
        {{ $store.state.count }}
        <div class="columns is-multiline is-mobile">
          <div class="column is-4" v-for="event in events" v-bind:key="event.id">
            <router-link v-bind:to="'/event/'+event.id">
              <event-card
                v-bind:titol="event.titol"
                v-bind:descripcio="event.descripcio"
                v-bind:key="event.id"
              ></event-card>
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
export default {
  name: "Events",
  components: {
    EventCard,
    EventDetail
  },
  data() {
    return {
      events: []
    };
  },
  methods: {
    getEvents: function(callback) {
      const testObj = {
        events: [{ id: 1, titol: "bon dia", descripcio: "hola bon dia" }]
      };
      callback(testObj);
    }
  },
  created() {
    let context = this;
    this.getEvents(function(data) {
      context.events = data.events;
    });
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
