<template>
  <div id="app">
    <div id="mymap"></div>
  </div>
</template>

<script>
  import L from 'leaflet'
  export default {
    data() {
      return {
        zoom:13,
        center: L.latLng(47.413220, -1.219482),
        url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
        attribution:'',
        marker: L.latLng(47.413220, -1.219482),
      }
    },
    mounted() {
        this.initMap();
    },
    methods: {
        initMap() {
            var mymap = L.map('mymap').setView([51.5, -0.09], 14);
            L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(mymap);
            var marker = L.marker([51.5, -0.09]).addTo(mymap);
        }
    },
  }
</script>

<style>
#app,
#mymap {
    position: relative;
    padding: 0;
    width: 600px;
    height: 600px;
}

h1,
h2 {
    font-weight: normal;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: inline-block;
    margin: 0 10px;
}

a {
    color: #42b983;
}
</style>