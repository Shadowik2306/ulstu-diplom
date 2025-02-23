<template>
  <div class="input-container">
    <input type="text"
           placeholder="Enter request..."
           :value="modelValue"
           @input="$emit('update:modelValue', $event.target.value)"
    />

  </div>
</template>

<script>
export default {
  props: {
    modelValue: {
      type: String,
      required: true
    }
  },
  emits: ['update:modelValue'],
  data() {
    return {
      inputValue: this.value,
    };
  },
  methods: {
    emitValue() {
      this.$emit('input', this.inputValue);
    },
  },
  watch: {
    value(newValue) {
      this.inputValue = newValue;
    },
  },
};
</script>

<style scoped>
.input-container {
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid black;
  border-radius: 5px;
  padding: 10px; /* Adjust inner spacing */
}

input {
  border: none;
  outline: none;
  width: 100%; /* Take full width */
  font-size: 16px; /* Adjust font size */
  padding: 5px; /* Inner padding */
  background-color: transparent;
  color: black;
  text-align: center;
}

input::placeholder {
  color: #1E1E1E; /* Placeholder color */
  opacity: 1; /* Fully opaque placeholder */
}
</style>