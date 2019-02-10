<template>
  <section class="hero is-fullheight fons-mataro">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-mobile">
          <div class="column is-half is-offset-one-quarter">
            <div class="card">
              <header class="card-header text-center">
                <h1 class="title has-text-black">{{ event.titol }}</h1>
              </header>
              <div class="card-content">
                <figure class="image " v-if="event.ambit == 'Esports'">
                  <img src="../assets/esports.png">
                </figure>
                <figure class="image" v-if="event.ambit != 'Esports'">
                  <img src="../assets/cultura.png" >
                </figure>
                <div class="field">
                  <label class="label" style="font-size:25px">Descripció</label>
                  <p>{{ event.descripcio }}</p>
                </div>
                <div class="field" v-if="event.observacions != ''">
                  <label class="label" style="font-size:20px">Observacions</label>
                  <p>{{ event.observacions }}</p>
                </div>
                <div class="field">
                  <label class="label" style="font-size:25px">Informació sobre l'esdeveniment</label>
                </div>
                <div class="columns is-mobile is-multiline">
                  <div class="column is-6">
                    <p>
                      <b>Dia:</b>
                      {{ event.dia.substring(0, 10) }}
                    </p>
                  </div>
                  <div class="column is-6">
                    <p>
                      <b>Durada:</b>
                      {{ event.horaIni.substring(11, 16) }} fins {{ event.horaFi.substring(11, 16) }}
                    </p>
                  </div>
                </div>
                <div class="columns">
                  <div class="column">
                    <p>
                      <b>Localització:</b>
                      {{ event.localitzacio }}
                    </p>
                  </div>
                </div>
                <div class="columns">
                  <div class="column">
                    <p>
                      <b>Àmbits:</b>
                      {{ event.ambit }}
                    </p>
                  </div>
                </div>
                <div class="columns">
                  <div class="column">
                    <p>
                      <b>Participants ({{ event.participants.length }} / {{ event.numParticipants }}):</b>
                      {{ event.participants.join(', ') }}
                    </p>
                  </div>
                </div>
                <hr>
                <div v-if="error" class="notification is-danger">
                  {{ error }}
                </div>
                <div class="columns">
                  <div class="column is-mobile is-pulled-left" v-if="!estaDins">
                    <div class="field">
                      <button class="button is-fullwidth is-success" id="create" v-on:click="unirse()">Inscriure'm</button>
                    </div>
                  </div>
                  <div class="column is-mobile is-pulled-left" v-if="estaDins">
                    <div class="field">
                      <button class="button is-fullwidth is-danger" id="delete" v-on:click="sortir()">Desinscriure'm</button>
                    </div>
                  </div>
                  <div class="column is-pulled-right">
                    <div class="field">
                      <router-link to="/events">
                        <button class="button is-fullwidth is-primary" id="delete">Sortir</button>
                      </router-link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import store from '../store';
export default {
  name: "Event",
  data() {
    return {
      event: {},
      error: ''
    };
  },
  methods: {
    unirse: function() {
      if (this.event.participants.indexOf(store.state.nom) >= 0) {
        this.error = 'Ja estàs inscrit a aquest esdeveniment';
      } else if (this.event.participants.length >= this.event.numParticipants) {
        this.error = 'Aquest esdeveniment ja està ple';
      } else {
        store.state.socket.emit('unirse', { 'name': store.state.nom, 'id': this.event['_id']['$oid'] });
      }
    },
    sortir: function() {
      if (this.event.participants.indexOf(store.state.nom) >= 0) {
        store.state.socket.emit('sortir', { 'name': store.state.nom, 'id': this.event['_id']['$oid'] });
      } else {
        this.error = 'No estàs en aquest esdeveniment';
      }
    }
  },
  created() {
    store.state.socket.on('sendEvent', (data) => {
      this.event = JSON.parse(data.data)[0];
    });
    store.state.socket.emit('getEvent', { 'id': this.$route.params.id });
  },
  computed: {
    estaDins: function () {
      return this.event.participants.indexOf(store.state.nom) >= 0;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.fons-mataro {
  background: url("../assets/mataro_transparent.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
.card-header {
  justify-content: center;
}
.title {
  margin: 10px;
}
p {
  font-size: 20px;
}
.card {
  margin-top: 10px;
  border-radius: 13px 13px 13px 13px;
  -moz-border-radius: 13px 13px 13px 13px;
  -webkit-border-radius: 13px 13px 13px 13px;
  border: 0px solid #000000;
}
</style>
