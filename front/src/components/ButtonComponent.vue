<template>
  <button class="generate-button" @click="handleClick">
    {{ label }}
  </button>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
    },
    backgroundColor: {
      type: String,
      default: '#f4a7a4',
    }
  },
  emits: ["click"],
  methods: {
    handleClick() {
      this.$emit('click');
    }
  }
};
</script>

<style scoped>
.generate-button {
  background-color: v-bind(backgroundColor); /* Light pink background */
  border: 1px solid black;
  border-radius: 10px;
  font-size: 20px;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  color: black;
}

.generate-button:hover {
  filter: brightness(85%);
}
</style>
