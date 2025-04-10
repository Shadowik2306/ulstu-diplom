<template>
    <button type="button" class="open-modal-button" @click="showModal">
      <i class="fas fa-cog"></i>
    </button>

    <div v-if="isModalVisible" class="modal-backdrop" @click="hideModal"></div>

    <div v-if="isModalVisible" class="modal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3 class="modal-title">Settings</h3>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitForm">
            <div class="form-group">
              <label for="negative-prompt">Negative Prompt</label>
              <input
                  type="text"
                  class="form-control"
                  id="negative-prompt"
                  v-model="negative_prompt"
                  placeholder="Enter negative prompt"
              />
            </div>

            <div class="form-group">
              <label for="audio-length">Audio Length (seconds)</label>
              <input
                  type="range"
                  class="form-range"
                  id="audio-length"
                  v-model="audio_length_in_s"
                  min="2"
                  max="10"
              />
              <small>{{ audio_length_in_s }} seconds</small>
            </div>

            <div class="form-group">
              <label for="num-inference-steps">Number of Inference Steps</label>
              <input
                  type="range"
                  class="form-range"
                  id="num-inference-steps"
                  v-model="num_inference_steps"
                  min="10"
                  max="500"
                  @input="this.reset_count"
              />
              <small>{{ num_inference_steps }} steps</small>
            </div>

            <div class="form-group">
              <label for="num-waveforms-per-prompt">Number of Waveforms per Prompt</label>
              <input
                  type="range"
                  class="form-range"
                  id="num-waveforms-per-prompt"
                  v-model="num_waveforms_per_prompt"
                  min="1"
                  max="5"
              />
              <small>{{ num_waveforms_per_prompt }} waveform(s)</small>
            </div>

            <div class="form-group">
              <label for="count">Count</label>
              <select class="form-control" id="count" v-model="count">
                <option
                    v-for="option in validCounts"
                    :key="option"
                    :value="option"
                >
                  {{ option }}
                </option>
              </select>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button class="save-button" @click="submitForm">Save changes</button>
        </div>
      </div>
    </div>

    <div v-if="isModalVisible" class="modal-backdrop" @click="hideModal"></div>
</template>

<script>
export default {
  data() {
    return {
      isModalVisible: false,
      negative_prompt: "Low quality.",
      audio_length_in_s: 5,
      num_inference_steps: 200,
      num_waveforms_per_prompt: 3,
      count: 1,
    };
  },
  computed: {
    validCounts() {
      if (this.num_inference_steps > 400) {
        return [1]; // Only 1 is valid
      } else if (this.num_inference_steps > 200) {
        return [1, 2]; // Valid count is 1 or 2
      } else {
        return [1, 2, 3]; // Valid count is 1, 2, or 3
      }
    }
  },
  methods: {
    showModal() {
      this.isModalVisible = true;
    },
    hideModal() {
      this.isModalVisible = false;
    },
    submitForm() {
      const settingsData = {
        negative_prompt: this.negative_prompt,
        audio_length_in_s: this.audio_length_in_s,
        num_inference_steps: this.num_inference_steps,
        num_waveforms_per_prompt: this.num_waveforms_per_prompt,
        count: this.count,
      };

      this.$emit('submit', settingsData);
      this.hideModal();
    },
    reset_count() {
      this.count = 1
    }
  }
};
</script>

<style scoped>
.open-modal-button {
  background: none;
  border: solid 1px black;
  font-size: 24px;
  cursor: pointer;
}

.modal {
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  justify-content: center;
  align-items: center;
  display: flex;
  z-index: 2000; /* Ensure modal is on top of other elements */
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  max-width: 500px;
  width: 100%;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: relative;
  z-index: 2001; /* Ensure modal content is above the backdrop */
}

.modal-header {
  display: flex;
  justify-content: center; /* Center header title */
  align-items: center;
  margin-bottom: 20px; /* Space below the header */
}

.modal-title {
  color: black; /* Set title color to black */
}

.modal-body {
  margin-top: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
  color: black; /* Set text color to black */
}

.save-button {
  background: #007bff;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1999;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  max-width: 500px;
  width: 100%;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: relative;
  z-index: 2001;
}


.form-control {
  text-align: center;
}
</style>