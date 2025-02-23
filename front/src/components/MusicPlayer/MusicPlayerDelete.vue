<template>
  <button class="close-button" @click="handleClick">
    &times;
  </button>
</template>

<script>
export default {
  props: {
    background_color: {
      type: String,
      default: '#D9D9D9',
    }
  },
  emits: ['click'],
  methods: {
    handleClick() {
      this.$emit('click');
    }
  }
}
</script>

<style scoped>
.close-button {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid #999;
  background-color: v-bind(background_color);
  font-size: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  padding: 0;
}

</style>
