<script>
import SampleCreator from "./components/SampleCreator.vue";
import VerticalNavbar from "./components/VericalNavbar.vue";

export default {
  components: {
    VerticalNavbar,
    SampleCreator,
  },
  data() {
    return {
      user: null
    }
  },
  computed: {
    user_info() {
      return this.user
    }
  },
  mounted() {
    this.update_user_state()
  },
  methods: {
    update_user_state() {
      const res = localStorage.getItem('token_payload');
      if (res === null) {
        this.user = null;
      }
      else {
        this.user = JSON.parse(res);
      }
    }
  }
}

</script>

<template>
  <div class="app-container">
    <VerticalNavbar class="navbar" ref="nav_bar"
                    :user_info="this.user_info"
    />
    <div class="content">
      <router-view/>
    </div>
  </div>
</template>

<style scoped>

.app-container {
  display: flex;
  width: 100%;
}

.navbar {
  width: 230px;
}

.content {
  width: calc(100% - 230px);
  padding: 20px; /* Adds some padding for content */
  margin-left: 250px;
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
