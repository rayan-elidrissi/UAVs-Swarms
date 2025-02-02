<template>
  <v-app>
    <!-- Top Navigation Bar -->
    <v-app-bar app color="indigo darken-4" dark>
      <v-toolbar-title class="nav-title">
        <v-icon left>mdi-fire</v-icon> UAV Wildfire Monitoring
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <!-- Navigation Links -->
      <v-btn text>
        <v-icon left>mdi-map</v-icon> Map
      </v-btn>

      <v-btn text>
        <v-icon left>mdi-video</v-icon> Live Feed
      </v-btn>

      <v-btn text>
        <v-icon left>mdi-chart-line</v-icon> Telemetry
      </v-btn>

      <!-- Settings Dropdown -->
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon v-bind="attrs" v-on="on">
            <v-icon>mdi-cog</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item>
            <v-list-item-title>Preferences</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>About</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <!-- Sidebar -->
    <SidebarComponent />

    <!-- Main Content -->
    <v-main class="main-content">
      <!-- Dashboard Grid (Map & Video) -->
      <div class="dashboard">
        <div class="dashboard-left">
          <UavMapComponent />
        </div>
        <div class="dashboard-right">
          <VideoFeedComponent />
        </div>
      </div>

      <!-- Telemetry Section -->
      <div class="telemetry-container">
        <TelemetryComponent />
      </div>
    </v-main>
  </v-app>
</template>

<script>
const components = [
  "SidebarComponent",
  "UavMapComponent",
  "VideoFeedComponent",
  "TelemetryComponent"
];

export default {
  components: Object.fromEntries(
    components.map(name => [name, require(`@/components/${name}.vue`).default])
  )
};
</script>

<style scoped>
/* 🏗 Fix Sidebar Overlap */
.main-content {
  padding-left: 260px; /* Sidebar width */
  padding-top: 70px; /* Adjusted for Navbar */
  padding-right: 20px;
  background: #121212;
  color: white;
}

/* 🖥 Fix Dashboard Layout (Map & Video Feed) */
.dashboard {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 20px;
  margin-top: 20px;
  height: 500px;
}

.dashboard-left {
  flex: 2; /* Map takes more space */
  min-height: 500px;
}

.dashboard-right {
  flex: 1.5; /* Video smaller */
  min-height: 500px;
}

/* 📊 Fix Telemetry Section */
.telemetry-container {
  margin-top: 40px;
  padding: 25px;
  background: #1e1e2f;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
}

/* 🏠 Navbar Styling */
.nav-title {
  font-weight: bold;
}

/* 🔄 Ensure Responsive Design */
@media (max-width: 1200px) {
  .dashboard {
    flex-direction: column;
    height: auto;
  }
  .dashboard-left, .dashboard-right {
    width: 100%;
    min-height: auto;
  }
}
</style>
