<template>
  <button :class="{ liked: initial_liked }" @click="toggleLike">
    <i :class="initial_liked ? 'fas fa-heart' : 'far fa-heart'"></i>
  </button>
</template>

<script>
export default {
  name: "LikeButton",
  props: {
    initial_liked: {
      type: Boolean,
      default: false
    },
  },
  emits: ["like"],
  data() {

  },
  methods: {
    toggleLike() {
      // this.isLiked = !this.isLiked;
      this.$emit("like")
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

button.liked {
  color: red;
}

</style>