<template>
  <v-navigation-drawer app permanent color="indigo darken-3" dark>
    <v-list dense>
      <v-list-item-group>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="headline">🔥 UAV Wildfire Dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item v-for="(item, index) in menuItems" :key="index" link>
          <v-list-item-content>
            <v-list-item-title>{{ item.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data() {
    return {
      menuItems: [
        { text: "📍 Live UAV Tracking" },
        { text: "🗺 Toggle Map Layers" },
        { text: "🔥 Fire Reports" },
        { text: "🚁 UAV Missions" },
        { text: "⚙ Settings" }
      ]
    };
  }
};
</script>

<style scoped>
.headline {
  padding: 20px;
}
</style>
