<template>
  <button @click="toggle" class="svg-button">
    <img v-if="modelValue" :src="iconOn" class="Play" alt="Play" @focus="disableDrag(this)"/>
    <img v-else :src="iconOff" class="Stop" alt="Stop" @focus="disableDrag(this)"/>
  </button>
</template>

<script>
import iconOn from '../../assets/pause_icon.svg'; // Adjust the path as needed
import iconOff from '../../assets/play_icon.svg'; // Adjust the path as needed

export default {
  props: {
    modelValue: {
      type: Boolean,
      required: true
    }
  },
  emits: ['update:modelValue', 'toggle'],
  data() {
    return {
      iconOn,
      iconOff,
    };
  },
  methods: {
    toggle() {
      this.$emit('toggle', this.isToggled);
    },
    disableDrag(e) {
      e.closest("div").setAttribute("draggable", false)
    }
  },
  computed: {
    buttonStyle() {
      return {
        border: 'none',

        cursor: 'pointer',
      };
    },
  },
};
</script>

<style scoped>
.svg-button {
  width: 100%; /* Set a width for the button */
  height: 100%; /* Set a height for the button */
  background: none;
  border: none;
}

img {
  max-width: 70%;
  max-height: 70%;
  -webkit-user-drag: none;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
}


button:focus {
  outline: none;
}

button:hover {
  cursor: pointer;
}
</style>
