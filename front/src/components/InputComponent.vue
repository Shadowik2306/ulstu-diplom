<template>
  <div class="input-container">
    <input type="text"
           :placeholder="this.placeholder"
           :value="modelValue"
           @input="input($event)"
    />

  </div>
</template>

<script>
export default {
  props: {
    modelValue: {
      type: String,
      required: true
    },
    placeholder: {
      type: String,
      default: ""
    },
    nullable: {
      type: Boolean,
      default: true
    }
  },
  emits: ['update:modelValue'],
  data() {
    return {

    };
  },
  methods: {
    input(event) {
      this.$emit('update:modelValue', event.target.value)
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