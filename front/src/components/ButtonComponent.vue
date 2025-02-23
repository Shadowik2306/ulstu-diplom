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
      default: '',
    }
  },
  methods: {
    handleClick() {
      this.$emit('click');
    }
  }
};
</script>

<style scoped>
.generate-button {
  background-color: #f4a7a4; /* Light pink background */
  border: 1px solid black;
  border-radius: 10px;
  font-size: 20px;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  color: black;
}

.generate-button:hover {
  background-color: #e49491; /* Slightly darker on hover */
}
</style>
