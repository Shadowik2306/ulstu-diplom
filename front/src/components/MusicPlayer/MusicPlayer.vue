<template>

    <div class="player-container"
         draggable="true"
         @dragstart="startDrag($event, music_data)"
    >
      <div class="music-name">
        <MusicPlayerName :text="this.music_data.name"/>
      </div>
      <div class="music-player">
        <audio ref="audio" :src="this.music_data.music_url" preload="metadata"></audio>
        <div class="player">
          <MusicPlayerPlayButton class="play-button" v-model="is_playing" @toggle="playMusic"/>
          <MusicPlayerScroller class="scroller" v-model="music_place" :duration="duration" :is_playing="is_playing"/>
        </div>
        <div class="delete">
          <MusicPlayerDelete :background_color="this.background_color" @click="this.deleteMusic"/>
        </div>
      </div>
    </div>


</template>

<script>
import MusicPlayerPlayButton from './MusicPlayerPlayButton.vue'
import MusicPlayerScroller from './MusicPlayerScroller.vue'
import MusicPlayerName from "./MusicPlayerName.vue";
import MusicPlayerDelete from "./MusicPlayerDelete.vue";

export default {
  components: {
    MusicPlayerDelete,
    MusicPlayerName,
    MusicPlayerPlayButton,
    MusicPlayerScroller,
  },
  props: {
    background_color: {
      type: String,
      default: '#D9D9D9'
    },
    music_data: {
      type: Object,
      required: true
    }
  },
  emits: ["delete"],
  data() {
    return {
      is_playing: false,
      audio: null,
      duration: 0,
      music_place: 0,
      play_animation: null
    }
  },
  methods: {
    criticalStopMusic() {
      if (this.is_playing) {
        this.audio.pause()
        this.audio.currentTime = 0;
        clearInterval(this.play_animation)
        this.play_animation = null
        this.is_playing = false
      }
    },
    startDrag(event, item) {
      console.log(item);
      event.dataTransfer.dropEffect = "move";
      event.dataTransfer.effectAllowed = "move";
      event.dataTransfer.setData("music_id", item.id)
      this.criticalStopMusic()
    },
    playMusic() {
      if (this.is_playing) {
        this.criticalStopMusic()
        return
      }

      this.is_playing = true;
      this.music_place = 0;
      this.audio.play()

      this.play_animation = setInterval(() => {
        this.music_place += 10
      }, 10)

      setTimeout(() => {
        this.criticalStopMusic()
      }, this.duration)
    },
    deleteMusic() {
      this.criticalStopMusic()
      this.$emit("delete", this.music_data.id)
    },
  },
  mounted() {
    this.audio = this.$refs.audio;
    let await_duration = setInterval(() => {
      if (!this.audio.duration) {
        return
      }
      this.duration = 1000 * this.audio.duration
      clearInterval(await_duration)
    },100)
  }
};
</script>

<style scoped>
  .player-container {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 7.5vh;
  }

  .music-name {
    width: auto;
    align-self: end;
    margin-right: 20%;
    height: 2.5vh;
  }

  .music-player {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 5vh;
    width: 100%;
  }

  .music-player .player {
    width: 85%;
    border: solid 1px black;
    border-radius: 50px;
    display: flex;
    align-items: center;
    height: 5vh;
    background-color: v-bind(background_color)
  }

  .music-player .delete {
    width: 10%;
  }

  .play-button {
    width: 15%;
  }

  .scroller {
    width: 100%;
    padding-right: 3%;
  }

  * {
    color: black;
  }
</style>
