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
  methods: {
    redirect() {
      window.location.href = this.$route.path + "?" + new URLSearchParams({
        text: this.text_req,
        page: this.page
      })
    },
    prevPage() {
      this.page = Math.max(this.page - 1, 1);
      this.redirect()
    },
    nextPage() {
      this.page = Math.min(this.page + 1, this.totalPages);
      this.redirect()
    },
    goToPage(page) {
      this.page = page;
      this.redirect()
    },
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
    if (this.favorites) {
      url = "/presets/favorites?"
    }

    this.page = this.$route.query.page ? parseInt(this.$route.query.page) : 1
    this.text_req = this.$route.query.text ? this.$route.query.text : ""

    let params = {
      page: this.page,
      size: 15,
    }

    if (this.text_req !== "") {
      params.text = this.text_req
    }

    myFetch(url +  new URLSearchParams(params)).then(res => {
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
  <SearchComponent v-model="this.text_req" placeholder="Search" @keydown.enter="redirect" />
  <div class="preset-container">
    <TextCloud v-for="preset in this.presets"
               :text="preset.name === '' ? 'UNSAVED' : preset.name"
               :background_color="preset.color" :link="'/preset/' + preset.id"
               :border="preset.name === '' ? 'dashed 1px black' : 'solid 1px black'"/>
  </div>
  <PaginationComponent
      class="pagination"
      :current-page="this.page"
      :total-pages="this.totalPages"
      :url="$route.path"
      @next-page="nextPage"
      @prev-page="prevPage"
      @change-page="goToPage"
  />
</div>
</template>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
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