import Vue from 'vue'
import Vuex from 'vuex'
import io from 'socket.io-client';
import FullCalendar from 'vue-full-calendar'
import "fullcalendar/dist/fullcalendar.min.css";

Vue.use(FullCalendar);
Vue.use(Vuex)

const state = {
  nom: '',
  dni: '',
  email: '',
  socket : io('192.168.45.127:5000'),
  events: [
    // {
    //   "id": 1,
    //   "titol": "bon dia",
    //   "descripcio": "hola bon dia"
    // },
    // {
    //   "id": 2,
    //   "titol": "Partit de futbol",
    //   "descripcio": "Partit de futbol 11, al camp municipal de mataro. I després birrilles",
    //   "observacions":"",
    //   "numParticipants": "15",
    //   "maxParticipants": "20",
    //   "localitzacio": "Camp municipal de fútbol de Mataró",
    //   "dia":"28/02/2019",
    //   "horaIni":"15:00",
    //   "horaFi":"16:00",
    //   "ambit":"Esportiu",
    //   "tipus":"",
    //   "altres":""
    // }
  ]
}

const mutations = {
  setNom (state, data) {
    state.nom = data;
  },
  setDni (state, data) {
    state.dni = data;
  },
  setEmail (state, data) {
    state.email = data;
  },
  setEvents (state, data) {
    state.events = JSON.parse(data.data);
  }
}

const actions = {}
const getters = {}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
