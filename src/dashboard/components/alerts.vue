<template>
  <div class="alerts">
    <h3>🚨 Fire Detected! Take Action</h3>
    <v-btn color="primary" @click="rerouteUAV">📡 Re-route UAV</v-btn>
    <v-btn color="red" @click="returnToBase">🏠 Return to Base</v-btn>
  </div>
</template>

<script>
export default {
  methods: {
    rerouteUAV() {
      alert("Re-routing UAV...");
    },
    returnToBase() {
      alert("UAV returning to base...");
    }
  }
};
</script>

<style scoped>
.alerts {
  background: #ff4444;
  color: white;
  padding: 10px;
  text-align: center;
}
</style>
