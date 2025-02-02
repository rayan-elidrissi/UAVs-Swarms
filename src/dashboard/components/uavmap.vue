<template>
  <div id="map" class="map"></div>
</template>

<script>
import L from "leaflet";
import "leaflet/dist/leaflet.css";

export default {
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      const map = L.map("map").setView([37.7749, -122.4194], 7);

      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "© OpenStreetMap contributors"
      }).addTo(map);

      // Example UAV Marker
      L.marker([37.7749, -122.4194], { title: "UAV-1" })
        .addTo(map)
        .bindPopup("🚁 UAV-1 <br> Status: Active");
    }
  }
};
</script>

<style scoped>
.map {
  width: 100%;
  height: 500px;
}
</style>
