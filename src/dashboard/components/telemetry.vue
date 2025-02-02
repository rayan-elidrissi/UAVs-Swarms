<template>
  <div class="telemetry-container">
    <h3>📊 UAV Telemetry</h3>
    <canvas id="telemetryChart"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";

export default {
  mounted() {
    this.renderChart();
  },
  methods: {
    renderChart() {
      const ctx = document.getElementById("telemetryChart").getContext("2d");
      new Chart(ctx, {
        type: "line",
        data: {
          labels: ["10s", "20s", "30s", "40s", "50s"],
          datasets: [
            {
              label: "Temperature (°C)",
              data: [28, 29, 30, 32, 35],
              borderColor: "red",
              fill: false
            },
            {
              label: "Wind Speed (km/h)",
              data: [5, 6, 8, 10, 12],
              borderColor: "blue",
              fill: false
            }
          ]
        },
        options: {
          responsive: true
        }
      });
    }
  }
};
</script>

<style scoped>
.telemetry-container {
  width: 100%;
  height: 250px;
  background: #282c34;
  padding: 20px;
  color: white;
}
</style>
