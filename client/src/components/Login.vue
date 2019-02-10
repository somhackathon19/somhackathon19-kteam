<template>
  <section class="hero is-fullheight fons-mataro">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-mobile">
          <div class="column is-half is-offset-one-quarter has-text-centered">
            <img src="../assets/logo_nostre.png" class="logo_nostre">
            <div class="card">
              <header class="card-header text-center">
                <h1 class="title has-text-black">MataroViva</h1>
              </header>
              <div class="card-content">
                <div v-if="error" class="notification is-danger">
                  {{ error }}
                </div>
                <div class="field">
                  <label class="label has-text-left">Nom</label>
                  <input class="input" v-model="nom" v-on:keyup.13="doLogin" type="text" placeholder="Introdueix el teu nom">
                </div>
                <div class="field">
                  <label class="label has-text-left">DNI</label>
                  <input class="input" v-model="dni" v-on:keyup.13="doLogin" type="text" placeholder="Introdueix el teu DNI">
                </div>
                <div class="field">
                  <label class="label has-text-left">Email</label>
                  <input class="input" v-model="email" v-on:keyup.13="doLogin" type="text" placeholder="Introdueix el teu Email">
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
      dni: '',
      emails: '',
      error: ''
    };
  },
  methods: {
    doLogin: function() {
      if (this.nom == '' || this.nom == null) {
        this.error = 'No has introduït cap nom'
      } else {
        if (this.dni == '' || this.dni == null) {
          this.error = 'No has introduït cap dni'
        } else {
          if (this.email == '' || this.email == null) {
            this.error = 'No has introduït cap email'
          } else {
            store.commit('setNom', this.nom);
            store.commit('setDni', this.dni);
            store.commit('setEmail', this.email);
            router.push('events')
          }
        }
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#button{
  background-color:#002f6c; 
}

.logo_nostre{
  width: 300px;
  height: 200px;
}
.fons-mataro {
  background: url("../assets/foto_portada.png");
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
