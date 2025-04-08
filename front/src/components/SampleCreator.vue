<script>
import MusicPlayer from "./MusicPlayer/MusicPlayer.vue";
import NoteContainer from "./NoteContainer.vue";
import SearchComponent from "./InputComponent.vue";
import ButtonComponent from "./ButtonComponent.vue";
import {myFetch, serverUrl} from "../assets/myFetch.js";
import TextCloud from "./TextCloud.vue";
import LikeButton from "./LikeButton.vue";
import AddButton from "./AddButton.vue";
import LoadingSpinner from "./SpinnerComponent.vue";

export default {
  components: {
    LoadingSpinner,
    AddButton,
    LikeButton, TextCloud, ButtonComponent, InputComponent: SearchComponent, MusicPlayer, NoteContainer},
  data(){
    return {
      notes_data: [
        {id: 1, name: "C", color: "#B4FFAE"},
        {id: 2, name: "C#", color: "#FFBBDF"},
        {id: 3, name: "D", color: "#86E3EF"},
        {id: 4, name: "D#", color: "#FF8D8A"},
        {id: 5, name: "E", color: "#FFCC73"},
        {id: 6, name: "F", color: "#D797FF"},
        {id: 7, name: "F#", color: "#F8FFAE"},
        {id: 8, name: "G", color: "#DADE55"},
        {id: 9, name: "G#", color: "#F1DCC9"},
        {id: 10, name: "A", color: "#448158"},
        {id: 11, name: "A#", color: "#53A6FF"},
        {id: 12, name: "B", color: "#CF7BA1"},
      ],
      music: [],
      request_text: "",
      preset_name: "",
      preset_creator: 0,
      is_inited: false,
      editable: false,
      is_liked: false,
      is_user_connected: false,
      isWaiting: null
    }
  },
  validations: {
    raw_preset_name: {
      minLength: 1,
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
    },
  },
  watch: {
    preset_name(newVal, oldVal) {
      if (!this.is_inited) return;
      if (newVal === "") {
        if (window.confirm("If you delete full name, you will delete preset. Are you sure?")) {
          console.log("Just joking");

          myFetch(`/preset/${this.$route.params.id}`, {
            method: "DELETE",
          }).then(response => {
            return response.json();
          }).then((data) => {
            console.log(data);
          })

          window.location.href = '/my_presets';
          return;
        }
        else {
          this.$nextTick(() => {
            this.preset_name = oldVal;
          })
          return
        }
      }

      myFetch(`/preset/${this.$route.params.id}`, {
        method: "PATCH",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          'name': newVal
        })
      })
      console.log(newVal)
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
        this.is_inited = true
        return
      }
      myFetch(`/preset/${this.$route.params.id}`
      ).then(response => {
        return response.json();
      }).then(preset => {
        console.log(preset)
        this.music = []
        this.preset_name = preset.name
        if (this.storage.token_payload) {
          const cur_user = JSON.parse(this.storage.token_payload).sub
          this.is_user_connected = true
          this.editable = cur_user === preset.user_id

          myFetch(`/preset/${this.$route.params.id}/like`, {}
          ).then(response => response.json()
          ).then(data => {
            console.log(data)
            this.is_liked = data
          })

        }

        for (let sample of preset.samples) {
          this.music.push({
            id: sample.id,
            name: sample.name,
            music_url: serverUrl + "/files/" + sample.music_url,
            note_id: sample.note_id,
          })
        }
      }).then(() => {
        this.is_inited = true
      })
    },
    async abort_sample(job_id) {
      myFetch(`/preset/${this.$route.params.id}/samples/status/${job_id}`, {method: "DELETE"}
      ).then(response => {
        if (response.ok) {
          return response.json()
        }
        return response.json().then(error => {throw new Error(error.detail)})
      }).then(data => {
        console.log("ITS ME JOHNY")
        console.log(data)
      }).catch(error => {
        console.warn(error)
        window.alert(error)
      })
    },
    async beforeUnloadAction(ev) {
      await this.abort_sample(this.isWaiting)
    },
    wait_for_response(Job_id) {
      this.isWaiting = Job_id
      let vr = this;

      window.addEventListener('beforeunload', this.beforeUnloadAction)


      const interval = setInterval(() => {
        myFetch(`/preset/${this.$route.params.id}/samples/status/${Job_id}`)
            .then(response => {
              if (response.ok) {
                return response.json();
              }
              return response.json().then(error => {throw new Error(error.detail)})
            }).then(data => {
              if (data.status === "complete") {
                this.get_preset();
                this.isWaiting = null;
                clearInterval(interval)
                window.removeEventListener("beforeunload", this.beforeUnloadAction);
              }
            }).catch(error => {
              console.warn(error)
              window.alert(error)
            })
      }, 10000)
    },
    create_samples() {
      if (this.isWaiting !== null) return;
      if (this.$route.params.id === 0) {
        return
      }
      if (this.request_text === "") {
        return;
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
        if (response.ok) {
          return response.json();
        }
        else {
          return response.json().then(error => {throw new Error(error.detail)})
        }
      }).then(data => {
        this.wait_for_response(data)
      }).catch(error => {
        console.warn(error)
        window.alert(error)
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
    like_preset() {
      this.is_liked = !this.is_liked
      myFetch(`/preset/${this.$route.params.id}/like`, {
        method: 'PATCH',
      }).then(response => response.json()
      ).then(data => {})
    },
    clone_preset() {
      myFetch(`/preset/${this.$route.params.id}`, {
        method: 'POST',
      }).then(response => {
        if (response.ok) {
          return response.json()
        }
        return response.json().then(error => {throw new Error(error.detail)})
      }).then(data => {
        window.location.href = `/preset/${data.id}`
      }).catch(error => {
        window.alert(error)
      })
    }
  },
  created() {
    this.get_preset()
  },
}
</script>
<template>
  <loading-spinner :visible="isWaiting !== null" />
  <div class="constructor" v-if="is_inited">
    <div class="request-area">
      <div class="name-and-search" v-if="editable">
        <InputComponent class="name"
                        placeholder="UNSAVED"
                        v-model="preset_name"
                        :nullable="false"
        />
        <InputComponent class="search"
                        placeholder="Enter request..."
                        v-model="request_text"
                        @keyup.enter="this.create_samples"
        />
        <LikeButton
            :initial_liked="this.is_liked"
            @like="like_preset"
        />

      </div>
      <div v-else class="preset-name">
        <TextCloud :text="this.preset_name"></TextCloud>
        <LikeButton
            :initial_liked="this.is_liked"
            @like="like_preset"
        />
        <AddButton v-if="is_user_connected" @click="this.clone_preset"/>
      </div>
      <div class="generate-button-container" v-if="editable">
        <ButtonComponent label="Generate" class="button" @click="this.create_samples"/>
      </div>
      <div>

      </div>
    </div>
    <div v-if="editable" class="constructor-area">
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
        <MusicPlayer v-for="music in this.unused_music"
                     :music_data="music"
                     draggable="true"
                     @delete="this.delete_sample"
        />
        <TextCloud
            v-if="this.unused_music.length === 0"
            text="Any free tinkling."
            border="dashed 1px black"
            style="margin-top: 30px "
        />
      </div>
    </div>
    <div v-else class="notes-container">
      <NoteContainer v-for="note in this.notes_info" :note_object="note" :color="note.color" :editable="false"/>
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

.generate-button-container {
  display: flex;
  justify-content: center;
}

.name-and-search {
  display: flex;
  width: 100%;
  justify-content: space-between;
  gap: 1vh;
}

.name-and-search .search {
  width: 70%;
}

.name-and-search .name {
  width: 25%;
}

.request-area {
  display: flex;
  flex-direction: column;
  gap: 2vh;
}

.preset-name {
  display: flex;
  gap: 1vh;
}

.request-area .button {
  width: 30%;
  align-self: center;
}

.constructor-area {
  display: flex;
  justify-content: space-between;
}

.notes-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 1vh;
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
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2vh;
}
</style>