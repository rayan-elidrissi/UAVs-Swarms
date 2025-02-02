<template>
  <div class="video-container">
    <h3>🎥 UAV Live Feed</h3>
    <video src="rtsp://your-drone-ip" controls autoplay class="video-feed"></video>
  </div>
</template>

<style scoped>
.video-container {
  background: black;
  color: white;
  text-align: center;
  padding: 10px;
}
.video-feed {
  width: 100%;
  height: 100%;
}
</style>
