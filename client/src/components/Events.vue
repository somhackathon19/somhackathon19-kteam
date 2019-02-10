<template>
  <section class="hero is-fullheight">
    <div class="hero-head1">
      <header class="navbar bg-nav is-transparent">
        <img src="../assets/logo_nostre.png" class="logo_nostre">
      </header>
    </div>
    <div class="hero-body fons-mataro">
      <div class="container has-text-centered">
        <div class="columns is-mobile">
          <div class="column column is-half is-offset-one-quarter has-text-centered">
            <h1 class="title has-text-white">Esdeveniments
              <router-link to="/event/new">
                <a class="button is-rounded crear-event">
                  <span class="icon is-small">
                    <i class="fas fa-plus"></i>
                  </span>
                </a>
              </router-link>
            </h1>
            <h2 class="subtitle has-text-white">crear esdeveniment</h2>
          </div>
          <div class="column is-4 is offset-8">
            <div class="control has-text-white">
              <p style="font-size: 20px">Filtrar per:</p>
              <div class="select">
                <select v-model="seleccio">
                  <option value="tot">Tot</option>
                  <option value="esports">Esports</option>
                  <option value="cultural">Cultural</option>
                </select>
              </div>
            </div>
          </div>
        </div>
        {{ $store.state.count }}
        <div class="columns is-multiline is-mobile">
          <div class="column is-4" v-for="event in filterEvents()" v-bind:key="event['_id']['$oid']">
            <router-link v-bind:to="'/event/'+event['_id']['$oid']">
              <event-card v-bind:event="event"></event-card>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import EventCard from "@/components/EventCard";
import EventDetail from "@/components/EventDetail";
import { mapGetters, mapActions } from "vuex";
import store from "../store";
export default {
  name: "Events",
  components: {
    EventCard,
    EventDetail
  },
  data() {
    return {
      seleccio: "tot"
    };
  },
  methods: {
    filterEvents: function() {
      let newEvents = []
      for (let i = 0; i < this.events.length; ++i) {
        if ((this.seleccio == 'esports' && this.events[i].ambit == 'Esports') ||
          (this.seleccio == 'cultural' && this.events[i].ambit =='Cultural') || this.seleccio == 'tot') {
          newEvents.push(this.events[i]);
        }
      }
      return newEvents;
    }
  },
  computed: {
    events() {
      return store.state.events;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.crear-event {
  color: white;
  background-color: #002f6c;
}
.logo_nostre {
  width: 90px;
  height: 60px;
  margin-top: 2px;
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
  background-color: #ff8c00;
  /* background-color: #FFC107; */
  height: 65px;
}
</style>
