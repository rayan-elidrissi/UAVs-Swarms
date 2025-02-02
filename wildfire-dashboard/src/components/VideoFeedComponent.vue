<template>
  <v-container>
    <v-card class="video-card" outlined>
      <v-card-title>
        🎥 UAV Live Feed
        <v-spacer></v-spacer>
        <v-btn icon @click="toggleFullscreen">
          <v-icon>mdi-fullscreen</v-icon>
        </v-btn>
      </v-card-title>

      <v-card-text>
        <div ref="videoWrapper" class="video-wrapper">
          <video ref="video" class="video-feed" src="rtsp://your-drone-ip" controls autoplay></video>
        </div>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  methods: {
    toggleFullscreen() {
      const videoElement = this.$refs.videoWrapper;
      if (videoElement.requestFullscreen) {
        videoElement.requestFullscreen();
      } else if (videoElement.mozRequestFullScreen) {
        videoElement.mozRequestFullScreen();
      } else if (videoElement.webkitRequestFullscreen) {
        videoElement.webkitRequestFullscreen();
      } else if (videoElement.msRequestFullscreen) {
        videoElement.msRequestFullscreen();
      }
    }
  }
};
</script>

<style scoped>
.video-card {
  background: #1E1E2F;
  color: white;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  text-align: center;
}

.video-wrapper {
  position: relative;
  width: 100%;
  max-height: 500px;
  overflow: hidden;
  border-radius: 10px;
  background: black;
}

.video-feed {
  width: 100%;
  height: auto;
  display: block;
}
</style>
