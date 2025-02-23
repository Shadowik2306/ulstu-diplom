<script>
import MusicPlayer from "./MusicPlayer/MusicPlayer.vue";
import NoteContainer from "./NoteContainer.vue";
import SearchComponent from "./SearchComponent.vue";
import ButtonComponent from "./ButtonComponent.vue";

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
        {id: 7, name: "G", color: "#F8FFAE"},
        {id: 8, name: "D#", color: "#9BFFF0"},
      ],
      music: [
        {id: 1, name: "Text Size", note_id: null, link_to_song: "https://assets.codepen.io/4358584/Anitek_-_Komorebi.mp3"},

        {id: 3, name: "Hello", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 4, name: "Hello World", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 5, name: "Hello World", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 7, name: "Hello World", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 8, name: "Hello World", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 9, name: "Hello World", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 10, name: "Hello World", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 11, name: "Hello World", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 12, name: "Hello World", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 13, name: "Hello World", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 14, name: "Hello World", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 15, name: "Hello World", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
        {id: 2, name: "Hello World Hello World", note_id: null, link_to_song: "https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/Poc47WdXrlsjaFHln2AaK9tSHg92VWlNbkTnjy7r.mp3"},
      ],
      request_text: ""
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
    },
    delete_music(music_id) {
      console.info("Deleting music ", music_id);
      const index = this.music.findIndex(item => item.id === music_id);
      if (index !== -1) {
        this.music.splice(index, 1);
      } else {
        console.warn('Item not found');
      }
    }
  }
}
</script>
<template>
  <div class="constructor">
    <div class="request-area">
      <SearchComponent v-model="request_text"/>
      <ButtonComponent label="Generate" class="button"/>
    </div>
    <div class="constructor-area">
      <div class="notes-part">
        <NoteContainer v-for="note in this.notes_info" :note_object="note" :color="note.color"
                       @drop="onDrop($event, note.id)"
                       @dragenter.prevent
                       @dragover.prevent
                       @delete="this.delete_music"
        />
      </div>
      <div class="music-list-group"
           @drop="onDrop($event, -1)"
           @dragenter.prevent
           @dragover.prevent
      >
        <MusicPlayer v-for="music in this.unused_music" :music_data="music" draggable="true" @delete="this.delete_music"/>
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