<template>
  <section class="hero is-success is-fullheight fons-mataro">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-mobile">
          <div class="column is-half is-offset-one-quarter">
            <div class="card">
              <header class="card-header text-center">
                <h1 class="title has-text-black">LOGIN</h1>
              </header>
              <div class="card-content">
                <div v-if="error" class="notification is-danger">
                  {{ error }}
                </div>
                <div class="field">
                  <label class="label">Nom</label>
                  <input class="input" v-model="nom" v-on:keyup.13="doLogin" type="text" placeholder="Introdueix el teu nom">
                </div>
                <div class="field">
                  <button class="button is-primary" id="button" v-on:click="doLogin">Entrar</button>
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
import store from '../store'
import router from '../router'
export default {
  name: "Login",
  data() {
    return {
      nom: '',
      error: ''
    };
  },
  methods: {
    doLogin: function() {
      if (this.nom == '' || this.nom == null) {
        this.error = 'No has introduït cap nom'
      } else {
        store.commit('setNom', this.nom);
        router.push('events')
      }
    }
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
  margin: 10px;
}
.card {
  margin-top: 10px;
  border-radius: 13px 13px 13px 13px;
  -moz-border-radius: 13px 13px 13px 13px;
  -webkit-border-radius: 13px 13px 13px 13px;
  border: 0px solid #000000;
}
</style>
