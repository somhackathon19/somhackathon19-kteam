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
                  <label class="label" style="font-size:25px">Descripció</label>
                  <p>
                    Hola amics, m'agradaria montar un partidet de fútbol en el camp municipal de
                    mataró, però ens falten alguns jugados. Us agradaria apuntar-vos? {{ event }}
                  </p>
                </div>
                <!-- <div class="field">
                  <label class="label" style="font-size:20px">Observacions</label>
                  <p>{{ event }}</p>
                </div>-->
                <div class="field">
                  <label class="label" style="font-size:25px">Informació sobre l'esdeveniment</label>
                </div>
                <div class="columns is-mobile is-multiline">
                  <div class="column is-6">
                    <p>
                      <b>Dia:</b>
                      {{ event }}
                    </p>
                  </div>
                  <div class="column is-6">
                    <p>
                      <b>Durada:</b>
                      {{ event }} - {{ event }}
                    </p>
                  </div>
                </div>
                <div class="columns">
                  <div class="column">
                    <p>
                      <b>Localització:</b>
                      {{ event }}
                    </p>
                  </div>
                </div>
                <div class="columns">
                  <div class="column">
                    <p>
                      <b>Número de participants:</b>
                      {{ event }} / {{ event }}
                    </p>
                  </div>
                </div>
                <div class="columns">
                  <div class="column">
                    <p>
                      <b>Àmbits:</b>
                      {{ event }} ({{ event }},{{ event }})
                    </p>
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
