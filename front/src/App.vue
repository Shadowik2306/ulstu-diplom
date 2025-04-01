<script>
import SampleCreator from "./components/SampleCreator.vue";
import VerticalNavbar from "./components/VericalNavbar.vue";
import LikeButton from "./components/LikeButton.vue";
import {myFetch} from "./assets/myFetch.js";

export default {
  components: {
    LikeButton,
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
    this.refresh()
  },
  methods: {
    refresh() {
      if (this.storage.token) {
        myFetch("/auth/refresh")
            .then(res => {
              if (res.ok) {
                return res.json()
              }
              return res.json().then(error => {throw new Error(error.detail)})
            })
            .then(data => {
              const raw_token = data.access_token
              this.storage.token = raw_token;
              this.storage.token_header = window.atob(raw_token.split('.')[0]);
              this.storage.token_payload = window.atob(raw_token.split('.')[1]);
            })
            .catch(err => {
              console.log(err)
              delete this.storage.token_payload
              delete this.storage.token_header
              delete this.storage.token
              window.location.href = "/"
            })
      }
    }
  }
}

</script>

<template>
  <div class="app-container">
    <VerticalNavbar class="navbar" ref="nav_bar"
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
