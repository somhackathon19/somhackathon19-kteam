<template>
  <section class="hero is-fullheight fons-mataro">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-mobile">
          <div class="column is-half is-offset-one-quarter">
            <div class="card">
              <div class="card-content">
                <div class="field">
                  <label class="label">Títol</label>
                  <div class="control">
                    <input class="input" type="text" placeholder="Títol de l'activitat" v-model="event.titol">
                  </div>
                </div>
                <div class="field">
                  <label class="label">Descripció</label>
                  <div class="control">
                    <textarea class="textarea" placeholder="Descripció de l'activitat" v-model="event.descripcio"></textarea>
                  </div>
                </div>
                <div class="field">
                  <label class="label">Observacions</label>
                  <div class="control">
                    <input class="input" type="text" placeholder="Observacions (opcional)" v-model="event.observacions">
                  </div>
                </div>
                <div class="columns is-mobile is-multiline">
                  <div class="column is-4">
                    <div class="field">
                      <label class="label">Número participants</label>
                      <input class="input" type="number" placeholder="Nº Participants" v-model="event.numParticipants">
                    </div>
                  </div>
                  <div class="column is-8">
                    <label class="label">Localització <button class="button is-warning is-small" v-on:click="obrirMapa()"><i class="fa fa-map-marker" aria-hidden="true"></i></button></label>
                    <input class="input" type="text" placeholder="Localització" v-model="event.localitzacio">
                  </div>
                  <div class="column is-4">
                    <b-field label="Escull un dia">
                      <b-datepicker
                        placeholder="Selecciona dia..."
                        icon="calendar-today"
                        position="is-top-right"
                        v-model="event.dia"
                      ></b-datepicker>
                    </b-field>
                  </div>
                  <div class="column is-4">
                    <b-field label="Hora inici">
                      <b-timepicker
                        placeholder="Selecciona hora inici"
                        icon="clock"
                        v-model="event.horaIni"
                        editable
                      ></b-timepicker>
                    </b-field>
                  </div>
                  <div class="column is-4">
                    <b-field label="Hora fi">
                      <b-timepicker
                        placeholder="Selecciona hora fi"
                        icon="clock"
                        v-model="event.horaFi"
                        editable
                      ></b-timepicker>
                    </b-field>
                  </div>
                  <div class="column is-3">
                    <div class="field">
                      <label class="label">Àmbit</label>
                      <div class="control">
                        <div class="select">
                          <select v-model="event.ambit">
                            <option>Esports</option>
                            <option>Cultural</option>
                          </select>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="column is-3">
                    <div class="field" v-if="event.ambit == 'Cultural'">
                      <label class="label">Tipus</label>
                      <div class="control">
                        <div class="select">
                          <select v-model="event.tipus">
                            <option>Teatre</option>
                            <option>Musical</option>
                            <option>Exposició</option>
                            <option>Taller</option>
                            <option>Concurs</option>
                            <option>Altres</option>
                          </select>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="column is-6">
                    <div class="field" v-if="event.tipus == 'Altres' && event.ambit == 'Cultural'">
                      <label class="label">Altres</label>
                      <div class="control">
                        <input class="input" type="text" placeholder="Altres activitats" v-model="event.altres">
                      </div>
                    </div>
                  </div>
                </div>
                <hr>
                <div class="columns is-mobile ">
                  <div class="column is-is-pulled-left">
                    <div class="field">
                      <button class="button is-fullwidth is-success" id="create" v-on:click="crearEvent()">Crear</button>
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
    <div class="container">
      <div class="modal" id="modalApp">
        <div class="modal-background"></div>
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title">Visualitzar espais públics</p>
          </header>
          <section class="modal-card-body">
            <div id="app">
              <div id="mymap"></div>
            </div>
          </section>
          <footer class="modal-card-foot">
            <button class="button" v-on:click="tancarModal()">Tancar</button>
          </footer>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import L from 'leaflet'
import csv from "@/assets/convertcsv.json"
import store from '../store'
import axios from 'axios'
export default {
  name: "NewEvent",
  props: ["id"],
  data() {
    return {
      event: {},
      zoom: 13,
      center: L.latLng(47.413220, -1.219482),
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution: '',
      marker: L.latLng(47.413220, -1.219482),
    };
  },
  mounted() {
    this.initMap();
  },
  methods: {
    obrirMapa: function () {
      document.getElementById("modalApp").classList.add('is-active')
    },
    seleccionar: function(adreca) {
      console.log(adreca)
    },
    tancarModal: function() {
      document.getElementById("modalApp").classList.remove('is-active')
    },
    crearEvent: function() {
      // this.event['participants'] = [store.state.nom];
      // store.state.socket.emit('addEvent', this.event);
    },
    initMap() {
      var mymap = L.map('mymap').setView([41.5395403,2.4346742], 14);
      L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
          attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(mymap);
      for (let i = 0; i < csv.length; ++i) {
        let lat = csv[i]['LAT'];
        let lng = csv[i]['LNG'];
        if (lat != null && lng != null) {
          let coords = [parseFloat(lat.replace(",", ".")), parseFloat(lng.replace(",", "."))];
          let text = '<input class="input is-fullheight" style="" id="'+lat+lng+'" value="'+csv[i]['ADRECA']+'"/><br/><button class="button" onclick="document.getElementById(\''+lat+lng+'\').select().execCommand(\'copy\');">Seleccionar</button><hr>' + csv[i]['NOM'];
          var marker = L.marker(coords).bindPopup(text).addTo(mymap);
        }
      }
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
  margin: 5px;
}

.card {
  margin-top: 10px;
  border-radius: 13px 13px 13px 13px;
  -moz-border-radius: 13px 13px 13px 13px;
  -webkit-border-radius: 13px 13px 13px 13px;
  border: 0px solid #000000;
}
#app,
#mymap {
    position: relative;
    padding: 0;
    width: 600px;
    height: 600px;
}

h1,
h2 {
    font-weight: normal;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: inline-block;
    margin: 0 10px;
}

a {
    color: #42b983;
}
</style>