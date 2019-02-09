<template>
  <section class="hero is-fullheight">
    <div class="hero-head1">
      <header class="navbar bg-nav is-transparent">
        <a class="navbar-item">
          <img src="../assets/logo_nostre.png" class="logo_nostre">
        </a>
      </header>
    </div>
    <div class="hero-body fons-mataro">
      <div class="container has-text-centered">
        <h1 class="title has-text-white">Esdeveniments
          <router-link to="newEvent">
            <a class="button is-rounded crear-event">
              <span class="icon is-small">
                <i class="fas fa-plus"></i>
              </span>
            </a>
          </router-link>
        </h1>
        <h2 class="subtitle has-text-white">crear esdeveniment</h2>
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
.crear-event{
  color: white;
  background-color:#002f6c;
}
.logo_nostre{
  width: 85px;
  height: 100%;
}
.fons-mataro {
  background: url("../assets/mataro_transparent.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
.navbar {
  display: flex;
  justify-content: center;
}
.bg-nav {
  background-color: cadetblue;
}
</style>
