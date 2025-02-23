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
}
</style>