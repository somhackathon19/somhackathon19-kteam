<template>
  <div class="card event-bg">
    <div class="card-image">
      <figure class="image" v-if="event.ambit == 'Esports'">
        <img src="../assets/esports.png">
      </figure>
      <figure class="image" v-if="event.ambit != 'Esports'">
        <img src="../assets/cultura.png" width="">
      </figure>
    </div>
    <div class="card-content card-size has-background-white">
      <p class="title has-text-black">{{ event.titol }}</p>
      <p class="subtitle has-text-black">
        {{ event.descripcio.substring(0, 95) }}<i v-if="event.descripcio.length > 95">...</i>
      </p>
    </div>
    <footer class="card-footer has-background-white">
      <p class="card-footer-item">{{ event.dia.substring(0, 10) }}</p>
      <p class="card-footer-item">{{ event.horaIni.substring(11, 16) }}</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: "EventCard",
  props: ["event"],
  data() {
    return {
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.card-size {
  height: 150px;
}
.navbar {
  display: flex;
  justify-content: center;
}
.event-bg {
  background: url("../assets/mataro.png");
}
</style>
