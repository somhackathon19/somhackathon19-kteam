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
                    <input class="input" type="text" placeholder="Títol de l'activitat">
                  </div>
                </div>
                <div class="field">
                  <label class="label">Descripció</label>
                  <div class="control">
                    <textarea class="textarea" placeholder="Descripció de l'activitat"></textarea>
                  </div>
                </div>
                <div class="field">
                  <label class="label">Observacions</label>
                  <div class="control">
                    <input class="input" type="text" placeholder="Observacions (opcional)">
                  </div>
                </div>
                <div class="columns is-mobile">
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
                  <div class="column is-5">
                    <label class="label">Altres</label>
                    <div class="control">
                      <input class="input" type="text" placeholder="Altres activitats">
                    </div>
                  </div>
                </div>
                <div class="columns is-mobile level-right" >
                  <div class="column is-2">
                    <div class="field">
                      <button class="button is-success" id="create" v-on:click="doLogin">Create</button>
                    </div>
                  </div>
                  <div class="column is-2">
                    <div class="field">
                      <button class="button is-success" id="save" v-on:click="doLogin">Save</button>
                    </div>
                  </div>
                  <div class="column is-2">
                    <div class="field">
                      <button class="button is-danger" id="delete" v-on:click="doLogin">Edit</button>
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
  name: "NewEvent",
  props: ["titol", "descripcio"],
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
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