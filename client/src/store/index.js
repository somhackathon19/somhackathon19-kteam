import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  nom: '',
  events: [
    {
      "id": 1,
      "titol": "bon dia",
      "descripcio": "hola bon dia"
    }
  ]
}

const mutations = {
    setNom (state, data) {
      state.nom = data;
    },
    setEvents (state, data) {
        state.events = data;
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
