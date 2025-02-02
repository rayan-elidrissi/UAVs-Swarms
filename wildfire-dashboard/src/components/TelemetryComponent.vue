<template>
  <v-container fluid>
    <v-row>
      <!-- Left Side: UAV Fleet Statistics -->
      <v-col cols="12" md="6">
        <v-card class="telemetry-card" outlined>
          <v-card-title>📊 UAV Fleet Statistics</v-card-title>
          <v-card-subtitle>Overview of all UAVs</v-card-subtitle>

          <v-card-text>
            <v-list dense>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title><strong>Total UAVs:</strong> 3</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>

              <v-list-item v-for="(uav, index) in uavs" :key="index">
                <v-list-item-content>
                  <v-list-item-title class="uav-title">🚁 <strong>{{ uav.name }}</strong></v-list-item-title>
                  <v-list-item-subtitle class="uav-data">
                    <span><strong>Battery:</strong> {{ uav.battery }}%</span><br>
                    <span><strong>Altitude:</strong> {{ uav.altitude }}m</span><br>
                    <span><strong>Speed:</strong> {{ uav.speed }} km/h</span>
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>

      <!-- Right Side: UAV Selection & Detailed Telemetry -->
      <v-col cols="12" md="6">
        <v-card class="telemetry-card" outlined>
          <v-card-title>🔍 Select UAV</v-card-title>
          <v-card-subtitle>View telemetry data for a specific UAV</v-card-subtitle>

          <v-card-text>
            <v-radio-group v-model="selectedUAV">
              <v-radio v-for="(uav, index) in uavs" :key="index" :label="uav.name" :value="index"></v-radio>
            </v-radio-group>

            <v-divider></v-divider>

            <v-list dense v-if="selectedUAV !== null">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="uav-title">🚁 <strong>{{ uavs[selectedUAV].name }}</strong></v-list-item-title>
                  <v-list-item-subtitle class="uav-data">
                    <span><strong>Battery:</strong> {{ uavs[selectedUAV].battery }}%</span><br>
                    <span><strong>Altitude:</strong> {{ uavs[selectedUAV].altitude }}m</span><br>
                    <span><strong>Speed:</strong> {{ uavs[selectedUAV].speed }} km/h</span><br>
                    <span><strong>Temperature:</strong> {{ uavs[selectedUAV].temperature }}°C</span><br>
                    <span><strong>Wind Speed:</strong> {{ uavs[selectedUAV].windSpeed }} km/h</span>
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      selectedUAV: null,
      uavs: [
        { name: "UAV1", battery: 85, altitude: 120, speed: 45, temperature: 30, windSpeed: 10 },
        { name: "UAV2", battery: 70, altitude: 100, speed: 50, temperature: 28, windSpeed: 12 },
        { name: "UAV3", battery: 90, altitude: 140, speed: 55, temperature: 32, windSpeed: 8 }
      ]
    };
  }
};
</script>

<style scoped>
.telemetry-card {
  background: #1E1E2F;
  color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  min-height: 280px;
}

/* Proper spacing for text */
.uav-title {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 5px;
}

.uav-data {
  font-size: 14px;
  line-height: 1.6;
  padding-left: 10px;
}

.v-list-item-content {
  white-space: pre-line;
}

/* Ensure proper column sizing */
@media (max-width: 960px) {
  .v-col {
    max-width: 100%;
  }
}
</style>
