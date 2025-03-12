<script>
import MusicPlayer from "./MusicPlayer/MusicPlayer.vue";

export default {
  components: {MusicPlayer},
  props: {
    color: {
      type: String,
      required: true,
    },
    note_object: {
      type: Object,
      required: true,
    },
    editable: {
      type: Boolean,
      default: true,
    }
  },
  emits: ["delete"],
  methods: {
    deleteMusic(music_id) {
      this.$emit("delete", music_id);
    }
  }
}
</script>

<template>
  <div class="note-container">
    <div class="note-cloud">
      <p>{{this.note_object.name}}</p>
    </div>

    <div v-if="!this.note_object.music" class="music-container empty"></div>
    <MusicPlayer v-else
                 :music_data="this.note_object.music"
                 :background_color="this.note_object.color"
                 :draggable="this.editable"
                 class="music-container contain"
                 :deletable="this.editable"
                 @delete="this.deleteMusic"
    />
    <div v-if="!this.note_object.music" style="width: 9%"></div>
  </div>
</template>

<style scoped>

.note-container {
  display: flex;
  justify-content: center;
  gap: 1vh;
  height: 7.5vh;
}

.note-cloud {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 10%;
  height: 5vh;
  border-radius: 50px;
  border: solid black 1px;
  text-align: center;
  background-color: v-bind(color); ;
  align-self: flex-end;
}

.note-cloud p {
  color: black;
}

.music-container.empty {
  width: 60%;
  height: 5vh;
  border-radius: 50px;
  border: solid black 1px;
  align-self: flex-end;
}

.music-container.contain {
  width: 70%;
  height: 7.5vh;
  align-self: flex-end;
}


</style>