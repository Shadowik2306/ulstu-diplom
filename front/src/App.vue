<script>
import SampleCreator from "./components/SampleCreator.vue";
import VerticalNavbar from "./components/VericalNavbar.vue";

export default {
  components: {
    VerticalNavbar,
    SampleCreator,
  }
}

</script>

<template>
  <div class="app-container">
    <VerticalNavbar />
    <div class="content">
      <router-view/>
    </div>
  </div>
</template>

<style scoped>
.app-container {
  display: flex;
}

.content {
  margin-left: 200px; /* Matches the width of the vertical navbar */
  padding: 20px; /* Adds some padding for content */
  width: calc(100% - 200px); /* Prevents overlap, calculates full width minus navbar */
}

@font-face {
  font-family: "golos-text";
  src: url("./assets/GolosText-VariableFont_wght.ttf");
}

* {
  font-family: "golos-text", serif;
  color: #fff
}
</style>
