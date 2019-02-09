<template>
  <section class="hero is-fullheight fons-mataro">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-mobile">
          <div class="column is-half is-offset-one-quarter">
            <div class="card">
              <header class="card-header text-center">
                <h1 class="title has-text-black">Partit de fútbol {{ event }}</h1>
              </header>
              <div class="card-content">
                <div>
                  <img src="../assets/esports.png">
                </div>
                <div class="field">
                  <label class="label">Descripció</label>
                  <div class="control">
                    <textarea class="textarea" readonly> Hola amics, m'agradaria montar un partidet de fútbol en el camp municipal de mataró, però ens falten alguns jugados. Us agradaria apuntar-vos?{{ event }} </textarea>
                  </div>
                </div>
                <div class="field">
                  <label class="label">Observacions</label>
                  <div class="control">
                    <input class="input" type="text" v-bind:value="event" readonly>
                  </div>
                </div>
                <div class="columns is-mobile is-multiline">
                  <div class="column is-4">
                    <div class="field">
                      <label class="label">Número participants</label>
                      <input class="input" type="text" v-bind:value="event+'/'+event" readonly>
                    </div>
                  </div>
                  <div class="column is-8">
                    <label class="label">Localització</label>
                    <input class="input" type="text" placeholder="Localització">
                  </div>
                  <div class="column is-4">
                    <b-field label="Escull un dia">
                      <b-datepicker
                        placeholder="Selecciona dia..."
                        icon="calendar-today"
                        position="is-top-right"
                      ></b-datepicker>
                    </b-field>
                  </div>
                  <div class="column is-4">
                    <b-field label="Hora inici">
                      <b-timepicker placeholder="Selecciona hora inici" icon="clock" editable></b-timepicker>
                    </b-field>
                  </div>
                  <div class="column is-4">
                    <b-field label="Hora fi">
                      <b-timepicker placeholder="Selecciona hora fi" icon="clock" editable></b-timepicker>
                    </b-field>
                  </div>
                  <div class="column is-3">
                    <div class="field">
                      <label class="label">Àmbit</label>
                      <div class="control">
                        <div class="select">
                          <select>
                            <option>Esports</option>
                            <option>Cultural</option>
                          </select>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="column is-3">
                    <div class="field">
                      <label class="label">Tipus</label>
                      <div class="control">
                        <div class="select">
                          <select>
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
                    <div class="field">
                      <label class="label">Altres</label>
                      <div class="control">
                        <input class="input" type="text" placeholder="Altres activitats">
                      </div>
                    </div>
                  </div>
                </div>
                <div class="columns is-mobile level-right">
                  <div class="column is-2">
                    <div class="field">
                      <button class="button is-success" id="create" v-on:click>Inscriure'm</button>
                    </div>
                  </div>
                  <div class="column is-3">
                    <div class="field">
                      <button class="button is-danger" id="delete" v-on:click>Desinscriure'm</button>
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
export default {
  name: "Event",
  props: ["event"],
  data() {
    return {};
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.fons-mataro {
  background: url("../assets/mataro.png");
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
