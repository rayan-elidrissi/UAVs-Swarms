<template>
  <v-app>
    <Sidebar />
    <v-main>
      <Alerts />
      <div class="dashboard">
        <UavMap />
        <VideoFeed />
      </div>
      <Telemetry />
    </v-main>
  </v-app>
</template>

<script>
import Sidebar from "./components/Sidebar.vue";
import UavMap from "./components/UavMap.vue";
import VideoFeed from "./components/VideoFeed.vue";
import Telemetry from "./components/Telemetry.vue";
import Alerts from "./components/Alerts.vue";

export default {
  components: { Sidebar, UavMap, VideoFeed, Telemetry, Alerts }
};
</script>

<style scoped>
.dashboard {
  display: flex;
  height: 500px;
}
</style>
