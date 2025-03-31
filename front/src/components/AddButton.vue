<template>
  <button @click="toggleLike">
    <i class="fas fa-plus"></i>
  </button>
</template>

<script>
export default {
  name: "AddButton",
  emits: ["click"],
  data() {

  },
  methods: {
    toggleLike() {
      this.$emit("click")
    }
  }
};
</script>

<style scoped>


button {
  cursor: pointer;
  background: none;
  border: solid 1px black;
  font-size: 1.5em;
  display: flex;
  align-items: center;
  color: black;
}


</style>