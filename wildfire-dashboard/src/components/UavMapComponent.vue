<template>
  <v-container>
    <v-card class="map-card" outlined>
      <v-card-title>
        🌍 UAV Live Map
      </v-card-title>
      <v-card-subtitle>
        Real-time tracking of UAVs in wildfire monitoring
      </v-card-subtitle>
      <v-card-text>
        <div id="map" class="map"></div>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import L from "leaflet";
import "leaflet/dist/leaflet.css";

export default {
  data() {
    return {
      map: null,
      uavMarker: null,
      uavPath: [],
    };
  },
  mounted() {
    this.initMap();
    this.simulateUAVMovement();
  },
  methods: {
    initMap() {
      this.map = L.map("map").setView([37.7749, -122.4194], 7);

      // Dark-themed map tiles for better contrast
      L.tileLayer("https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png", {
        attribution: "© OpenStreetMap & CartoDB",
      }).addTo(this.map);

      // Custom UAV Icon
      const uavIcon = L.icon({
        iconUrl: "https://upload.wikimedia.org/wikipedia/commons/6/6e/Drone_icon.png",
        iconSize: [40, 40],
      });

      // UAV Marker with popup
      this.uavMarker = L.marker([37.7749, -122.4194], { icon: uavIcon })
        .addTo(this.map)
        .bindPopup("🚁 UAV-1 <br> Status: Active");

      // UAV Path Layer
      this.uavPath = L.polyline([], { color: "red", weight: 3 }).addTo(this.map);
    },

    simulateUAVMovement() {
      const route = [
        [37.7749, -122.4194],
        [37.8049, -122.2711],
        [37.8715, -122.2730],
        [38.1041, -122.2566],
      ];
      let index = 0;

      setInterval(() => {
        if (index < route.length) {
          const [lat, lng] = route[index];
          this.uavMarker.setLatLng([lat, lng]).bindPopup(`🚁 UAV-1 <br> Position: (${lat.toFixed(4)}, ${lng.toFixed(4)})`).openPopup();
          
          // Update the UAV path
          this.uavPath.addLatLng([lat, lng]);

          // Pan map to the new location
          this.map.panTo([lat, lng]);
          
          index++;
        }
      }, 3000);
    }
  }
};
</script>

<style scoped>
.map-card {
  background: #1E1E2F;
  color: white;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.map {
  width: 100%;
  height: 500px;
  border-radius: 10px;
}
</style>
