<script>
export default {
  props: {
    text: {
      type: String,
      default: '',
    }
  }
}
</script>

<template>
  <div class="musicPlayerName">
    {{this.text}}
  </div>

</template>

<style scoped>
.musicPlayerName {
  width: 100%;
  background-color: transparent;
  border: solid 1px black;
  border-radius: 10px 10px 0 0;
  border-bottom-color: transparent;
  color: black;
  padding: 0 5px;

  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 1; /* number of lines to show */
  line-clamp: 2;
  -webkit-box-orient: vertical;
}

</style>