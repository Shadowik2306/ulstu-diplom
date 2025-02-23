<template>
  <div class="slider-container">
    <div class="marker"></div>
    <input
        type="range"
        min="0"
        :max="duration"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        class="slider"
        disabled
    />
    <div class="marker"></div>
  </div>
</template>

<script>
export default {
  props: {
    modelValue: {
      type: Number,
      required: true
    },
    duration: {
      type: Number,
      default: 0
    },
    is_playing: {
      type: Boolean,
      required: true
    }
  },
  computed: {
    thumb_color() {
      if (this.is_playing) {
        return "#000"
      }
      else {
        return "transparent"
      }
    }
  },
  emits: ['update:modelValue'],
  data() {
    return {

    };
  },
  methods: {

  },
};
</script>

<style scoped>
.slider-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.slider {
  -webkit-appearance: none; /* Removes default styling in webkit browsers */
  appearance: none; /* Removes default styling */
  width: 100%; /* Full-width */
  height: 2px; /* Thickness */
  background: #000000; /* Background color */
  border-radius: 5px; /* Rounded edges */
  outline: none; /* Removes outline on focus */
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 1.5vh; /* Width of the thumb */
  height: 1.5vh; /* Height of the thumb */
  border-radius: 50%; /* Circular thumb */
  background: v-bind(thumb_color); /* Thumb color */
}

.slider::-moz-range-thumb {
  width: 20px; /* Width of the thumb */
  height: 20px; /* Height of the thumb */
  border-radius: 50%; /* Circular thumb */
  background: v-bind(thumb_color); /* Thumb color */
}

/* Optional: style for Firefox */
.slider::-ms-thumb {
  width: 20px; /* Width of the thumb */
  height: 20px; /* Height of the thumb */
  border-radius: 50%; /* Circular thumb */
  background: v-bind(thumb_color); /* Thumb color */
}

.marker {
  width: 2px; /* Толщина засечек */
  height: 10px; /* Высота засечек */
  background-color: #000000; /* Цвет засечек */
}
</style>
