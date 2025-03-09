<script>

import SearchComponent from "./SearchComponent.vue";
import TextCloud from "./TextCloud.vue";
import {myFetch} from "../assets/myFetch.js";

export default {
  components: {TextCloud, SearchComponent},
  props: {
    users_created: {
      type: Boolean,
      default: false
    },
    favorites: {
      type: Boolean,
      default: false
    },
  },
  data() {
    return {
      text_req: "",
      presets: [

      ]
    }
  },
  created() {
    let url = "/presets?"
    if (this.users_created) {
      url = "/presets/users_presets?"
    }

    myFetch(url + new URLSearchParams({
      page: this.$route.query.page ? this.$route.query.page : 0,
      size: 15,
    }),).then(res => {
      return res.json()
    }).then(presets_page => {
      this.presets = presets_page.presets
    })
  }
}
</script>

<template>
<div class="main-container">
  <SearchComponent :model-value="this.text_req"/>
  <div class="preset-container">
    <TextCloud v-for="preset in this.presets" :text="preset.name" :background_color="preset.color" :link="'/preset/' + preset.id"/>
  </div>
</div>
</template>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  gap: 3vh;
}

.preset-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.preset-container div {
  flex: 1 0 calc(25%);
  padding: 10px;
}
</style>