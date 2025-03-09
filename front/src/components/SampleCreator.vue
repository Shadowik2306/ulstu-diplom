<script>
import MusicPlayer from "./MusicPlayer/MusicPlayer.vue";
import NoteContainer from "./NoteContainer.vue";
import SearchComponent from "./SearchComponent.vue";
import ButtonComponent from "./ButtonComponent.vue";
import {myFetch, serverUrl} from "../assets/myFetch.js";

export default {
  components: {ButtonComponent, SearchComponent, MusicPlayer, NoteContainer},
  data(){
    return {
      notes_data: [
        {id: 1, name: "C", color: "#B4FFAE"},
        {id: 2, name: "C#", color: "#FFBBDF"},
        {id: 3, name: "D", color: "#86E3EF"},
        {id: 4, name: "D#", color: "#FF8D8A"},
        {id: 5, name: "E", color: "#FFCC73"},
        {id: 6, name: "F", color: "#D797FF"},
        {id: 7, name: "F#", color: "#D797FF"},
        {id: 8, name: "G", color: "#F8FFAE"},
        {id: 9, name: "G#", color: "#9BFFF0"},
        {id: 10, name: "A", color: "#9BFFF0"},
        {id: 11, name: "A#", color: "#9BFFF0"},
        {id: 12, name: "B", color: "#9BFFF0"},
      ],
      music: [
        {id: 1, name: "Text Size", note_id: null, music_url: "https://assets.codepen.io/4358584/Anitek_-_Komorebi.mp3"},
        {id: 3, name: "Hello", note_id: null, music_url: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 4, name: "Hello World", note_id: null, music_url: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 5, name: "Hello World", note_id: null, music_url: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 2, name: "Hello World Hello World", note_id: null, music_url: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
      ],
      request_text: "",
      is_loaded: false,
    }
  },
  computed: {
    unused_music() {
      return this.music.filter(it => it.note_id === null)
    },
    notes_info() {
      return this.notes_data.map(it => {
        const music = this.music.find(note => note.note_id === it.id);
        return {
          ...it,
          music: music || null
        };
      })
    }
  },
  methods: {
    onDrop(event, note_id) {
      const music_id = parseInt(event.dataTransfer.getData("music_id"));
      const id_in_list = this.music.findIndex(it => it.id === music_id)

      this.music.forEach(it => {
        if (it.note_id === note_id) {
          it.note_id = null;
        }
      })

      if (note_id !== -1) {
        this.music[id_in_list].note_id = note_id;
      }
      else {
        this.music[id_in_list].note_id = null;
      }

      this.update_sample(this.music[id_in_list].id, this.music[id_in_list].note_id)
    },
    get_preset() {
      if (this.$route.params.id === 0) {
        this.is_loaded = true
        return
      }

      myFetch(`/preset/${this.$route.params.id}`
      ).then(response => {
        return response.json();
      }).then(preset => {
        console.log(preset)
        this.music = []
        for (let sample of preset.samples) {
          this.music.push({
            id: sample.id,
            name: sample.name,
            music_url: serverUrl + "/files/" + sample.music_url,
            note_id: sample.note_id,
          })
        }
        this.is_loaded = true
      })
    },
    create_samples() {
      if (this.$route.params.id === 0) {
        return
      }
      myFetch(`/preset/${this.$route.params.id}/samples`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          'text_request': this.request_text,
          'count': 1
        })
      }).then(response => {
        return response.json();
      }).then(data => {
        console.log(data)
        this.get_preset()
      }).catch(error => {
        console.warn(error)
      })
    },
    update_sample(sample_id, note_id) {
      myFetch(`/preset/${this.$route.params.id}/samples/${sample_id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          'note_id': note_id
        })
      }).then(response => {
        return response.json();
      }).then(data => {
        console.log(data)
      }).catch(error => {
        console.warn(error)
      })
    },
    delete_sample(sample_id) {
      console.info("Deleting music ", sample_id);
      const index = this.music.findIndex(item => item.id === sample_id);
      if (index !== -1) {
        this.music.splice(index, 1);
      } else {
        console.warn('Item not found');
      }

      myFetch(`/preset/${this.$route.params.id}/samples/${sample_id}`, {
        method: 'DELETE',
      }).then(response => {
        return response.text();
      }).then(data => {
        console.log(data)
      }).catch(error => {
        console.warn(error)
      })
    },
  },
  created() {
    this.get_preset()
  }
}
</script>
<template>
  <div class="constructor" v-if="is_loaded">
    <div class="request-area">
      <SearchComponent v-model="request_text"/>
      <ButtonComponent label="Generate" class="button" @click="this.create_samples"/>
    </div>
    <div class="constructor-area">
      <div class="notes-part">
        <NoteContainer v-for="note in this.notes_info" :note_object="note" :color="note.color"
                       @drop="onDrop($event, note.id)"
                       @dragenter.prevent
                       @dragover.prevent
                       @delete="this.delete_sample"
        />
      </div>
      <div class="music-list-group"
           @drop="onDrop($event, -1)"
           @dragenter.prevent
           @dragover.prevent
      >
        <MusicPlayer v-for="music in this.unused_music" :music_data="music" draggable="true" @delete="this.delete_sample"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
.constructor {
  display: flex;
  flex-direction: column;
  gap: 1vh;
  height: 100vh;
}

.request-area {
  display: flex;
  flex-direction: column;
  gap: 2vh;
}

.request-area .button {
  width: 30%;
  align-self: center;
}

.constructor-area {
  display: flex;
  justify-content: space-between;
}

.notes-part {
  display: flex;
  flex-direction: column;
  width: 40%;
  gap: 2vh;
}


.music-list-group {
  width: 40%;
  height: 100%;
  overflow-y: scroll;   /* Enable vertical scroll */
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2vh;
}
</style>