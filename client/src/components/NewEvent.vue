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
                    <label class="label">Localització</label>
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
                  <div class="column is-pulled-left">
                    <div class="field">
                      <button class="button is-fullwidth is-success" id="save" v-on:click="editarEvent()">Editar</button>
                    </div>
                  </div>
                  <div class="column is-pulled-right">
                    <div class="field">
                      <button class="button is-fullwidth is-danger " id="delete" v-on:click="borrarEvent()">Borrar</button>
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
import io from 'socket.io-client';
import store from '../store'
import axios from 'axios'
export default {
  name: "NewEvent",
  props: ["id"],
  data() {
    return {
      event: {},
      socket : io('localhost:5000')
    };
  },
  methods: {
    crearEvent: function() {
      this.event['participants'] = [store.state.nom];
      this.socket.emit('addEvent', this.event);
    },
    editarEvent: function() {
      this.socket.emit('editEvent', { 'id': id, 'event': this.event });
    },
    borrarEvent: function() {
      this.socket.emit('deleteEvent', { 'id': id });
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
</style>