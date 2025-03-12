<script>
export default {
  username: 'TextCloud',
  props: {
    text: {
      type: String,
      required: true,
    },
    background_color: {
      type: String,
      default: '#FFF',
    },
    link: {
      type: String,
      required: false,
    },
    border: {
      type: String,
      default: 'solid 1px black',
    }
  },
  methods: {
    navigate(path) {
      this.$router.push(path);
    }
  }
}
</script>

<template>
  <div class="cloud" :class="{link_block: this.link}" @click="(this.link) ? navigate(this.link) : null">
    <p>{{this.text}}</p>
  </div>
</template>

<style scoped>
.cloud {
  width: 100%;
  border: v-bind(border);
  border-radius: 50px;
  display: flex;
  justify-content: center;
  color: black;
  background-color: v-bind(background_color)
}

.link_block:hover {
  filter: brightness(85%);
  cursor: pointer;
}
</style>