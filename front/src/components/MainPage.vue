<script>

import {defineComponent} from "vue";
import TextCloud from "./TextCloud.vue";
import {myFetch} from "../assets/myFetch.js";

export default defineComponent({
  components: {TextCloud},
  data() {
    return {
      last_created: [],
      most_liked: []
    }
  },
  created() {
    this.page = 1

    myFetch('/presets/last').then(res => {
      return res.json()
    }).then(presets_page => {
      this.last_created = presets_page.slice(0, 10)
    })

    myFetch('/presets/most_liked').then(res => {
      return res.json()
    }).then(presets_page => {
      this.most_liked = presets_page.slice(0, 10)
    })
  }
})
</script>

<template>
  <div class="main-container">
    <div class="topic-container">
      <h1>Most liked</h1>
      <div class="presets-container">
        <TextCloud v-for="preset in this.most_liked"
                   :text="preset.name === '' ? 'UNSAVED' : preset.name"
                   :background_color="preset.color" :link="'/preset/' + preset.id"
                   :border="preset.name === '' ? 'dashed 1px black' : 'solid 1px black'"/>
      </div>
    </div>


    <div class="topic-container">
      <h1>Last Ones</h1>
      <div class="presets-container">
        <TextCloud v-for="preset in this.last_created"
                   :text="preset.name === '' ? 'UNSAVED' : preset.name"
                   :background_color="preset.color" :link="'/preset/' + preset.id"
                   :border="preset.name === '' ? 'dashed 1px black' : 'solid 1px black'"/>
      </div>
    </div>
  </div>

</template>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  gap: 3vh;
  height: 80vh;
}

.presets-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.presets-container div{
  flex: 1 0 calc(25%);
  padding: 10px;
}

h1 {
  color: black;
  text-align: left;
}
</style>