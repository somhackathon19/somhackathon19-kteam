<template>
  <div id="app">
    <div id="mymap"></div>
  </div>
</template>

<script>
  import axios from 'axios'
  import L from 'leaflet'
  import csv from "@/assets/convertcsv.json"
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
          var mymap = L.map('mymap').setView([41.5395403,2.4346742], 14);
          L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
              attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          }).addTo(mymap);
          for (let i = 0; i < csv.length; ++i) {
            let lat = csv[i]['LAT'];
            let lng = csv[i]['LNG'];
            if (lat != null && lng != null) {
              let coords = [parseFloat(lat.replace(",", ".")), parseFloat(lng.replace(",", "."))];
              var marker = L.marker(coords).bindPopup(csv[i]['ADRECA']).addTo(mymap);
            }
          }
      }
    }
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