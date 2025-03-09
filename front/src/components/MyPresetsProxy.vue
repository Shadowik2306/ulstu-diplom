<script>
import ListOfPresets from "./ListOfPresets.vue";
import {defineComponent} from "vue";

export default defineComponent({
  components: {ListOfPresets},
  created() {
    if (!this.storage.token_payload) {
      this.$router.push("/sign_in");
    }
  }
})

</script>

<template>
  <ListOfPresets users_created="users_created"/>
</template>

<style scoped>

</style>