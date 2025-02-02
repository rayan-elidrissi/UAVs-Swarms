<template>
  <v-navigation-drawer app permanent color="indigo darken-3" dark>
    <v-list>
      <!-- Dashboard Title -->
      <v-list-item>
        <v-list-item-avatar class="dashboard-logo">
          <v-icon size="36">mdi-fire</v-icon>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title class="headline">
            UAV Wildfire Dashboard
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <!-- Menu Items -->
      <v-list-item-group>
        <v-list-item v-for="(item, index) in menuItems" :key="index" link>
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
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
        { text: "Live UAV Tracking", icon: "mdi-drone" },
        { text: "Toggle Map Layers", icon: "mdi-map" },
        { text: "Fire Reports", icon: "mdi-fire-alert" },
        { text: "UAV Missions", icon: "mdi-airplane" },
        { text: "Settings", icon: "mdi-cog" }
      ]
    };
  }
};
</script>

<style scoped>
.headline {
  font-size: 1.2rem;
  font-weight: bold;
}

.dashboard-logo {
  background-color: rgba(255, 69, 0, 0.7); /* Slight fire-themed highlight */
}

.v-list-item {
  transition: background 0.3s ease-in-out;
}

.v-list-item:hover {
  background: rgba(255, 255, 255, 0.1);
}
</style>
