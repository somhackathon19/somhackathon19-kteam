<template>
  <div class="card event-bg">
    <div class="card-content">
      <p class="title has-text-black">{{ titol }}</p>
      <p class="subtitle has-text-black">{{ descripcio }}</p>
    </div>
    <footer class="card-footer">
      <p class="card-footer-item">
        <span>View on
          <a href="https://twitter.com/codinghorror/status/506010907021828096">Twitter</a>
        </span>
      </p>
      <p class="card-footer-item">
        <span>Share on
          <a href="#">Facebook</a>
        </span>
      </p>
    </footer>
  </div>
</template>

<script>
export default {
  name: "EventCard",
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
.navbar {
  display: flex;
  justify-content: center;
}
.event-bg {
  background: url("../assets/mataro.png");
}
</style>
