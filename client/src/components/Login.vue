<template>
  <section class="hero is-success is-fullheight fons-mataro">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-mobile">
          <div class="column is-half is-offset-one-quarter">
            <div class="card">
              <header class="card-header text-center">
                <h1 class="title" style="color:black">LOGIN</h1>
              </header>
              <div class="card-content">
                <div class="field">
                  <label class="label">Username</label>
                  <input class="input" v-model="name" type="text" placeholder="Introdueix el teu nom">
                </div>
                <div class="field">
                <button class="button is-primary" id="button" v-on:click="doLogin">Submit</button>
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
  name: "Login",
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      name: ""
    };
  },
  methods: {
    doLogin: function() {
      console.log(this.name);
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
.title{
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
