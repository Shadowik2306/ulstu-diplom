<script>

import SearchComponent from "./InputComponent.vue";
import TextCloud from "./TextCloud.vue";
import PaginationComponent from "./PaginationComponent.vue";
import {myFetch} from "../assets/myFetch.js";

export default {
  components: {PaginationComponent, TextCloud, SearchComponent},
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
      presets: [],
      totalPages: 0,
      page: 0
    }
  },
  created() {
    if (this.users_created || this.favorites) {
      if (!this.storage.token_payload) {
        this.$router.push("/sign_in");
      }
    }

    let url = "/presets?"
    if (this.users_created) {
      url = "/presets/users_presets?"
    }

    this.page = this.$route.query.page ? parseInt(this.$route.query.page) : 1

    myFetch(url +  new URLSearchParams({
      page: this.page,
      size: 15,
    }),).then(res => {
      return res.json()
    }).then(presets_page => {
      this.presets = presets_page.presets
      this.totalPages = presets_page.total_pages
    })
  }
}
</script>

<template>
<div class="main-container">
  <SearchComponent :model-value="this.text_req" placeholder="Search" />
  <div class="preset-container">
    <TextCloud v-for="preset in this.presets" :text="preset.name === '' ? 'Untitled' : preset.name"
               :background_color="preset.color" :link="'/preset/' + preset.id"/>
  </div>
  <PaginationComponent
      class="pagination"
      :current-page="this.page"
      :total-pages="this.totalPages"
      :url="$route.path"
  />
</div>
</template>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  gap: 3vh;
  height: 95vh;
}

.pagination {
  margin-top: auto;
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