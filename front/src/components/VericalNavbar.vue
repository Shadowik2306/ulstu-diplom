<template>
  <nav class="vertical-navbar">
    <div class="logo" @click="navigate('/')">
      <span v-for="(letter, index) in this.logo_text"
      :style="{color: colors[index % colors.length]}">
        {{letter}}
      </span>
    </div>
    <ul>
      <li v-for="item in navItems" :key="item.name" @click="item.action(item.params)"
          :class="{active: item.url_name === currentRouteName}">
        {{ item.name }}
      </li>
    </ul>
    <div v-if="!this.user_info" class="button-container">
      <button class="btn sign-in" @click="navigate('/sign_in')">Sign In</button>
      <button class="btn sign-up" @click="navigate('/sign_up')">Sign Up</button>
    </div>
    <div class="user-info" v-else @click="sign_out">
      {{ this.user_info.username }} {{ this.user_info.is_subscribed ? 'SUBSCRIBED' : 'UNSUBSCRIBED' }}
    </div>
  </nav>
</template>

<script>
import {myFetch} from "../assets/myFetch.js";

export default {
  username: 'VerticalNavbar',
  props: {
    logo_text: {
      type: String,
      default: 'Tinkling',
    },
    colors: {
      type: Array,
      default: [
        "#B4FFAE",
        "#FFBBDF",
        "#86E3EF",
        "#FF8D8A",
        "#FFCC73",
        "#D797FF",
        "#F8FFAE",
        "#9BFFF0",
      ]
    },
  },
  computed: {
    currentRouteName() {
      return this.$route.name;
    },
    user_info() {
      if (!this.storage.token_payload) {
        return null
      }
      return JSON.parse(this.storage.token_payload);
    },
    navItems() {
      let lst = this.public_nav_items;
      if (this.user_info) {
        lst = lst.concat(this.private_nav_items)
      }
      return lst;
    }
  },
  data() {
    return {
      public_nav_items: [
        { name: 'All Presets', action: this.navigate, params: ('/presets'), url_name: "presets" },
      ],
      private_nav_items: [
        {name: "New Preset", action: this.create_new_preset, url_name: "preset"},
        {name: "My Presets", action: this.navigate, params: ('/my_presets'), url_name: "my_presets"},
        {name: "Favorites", action: this.navigate, params: ("/favorites"), url_name: "favorites" },
        {name: "Subscription", action: this.navigate, params: ('/subscription'), url_name: "subscription"},
      ]
    };
  },
  methods: {
    navigate(path) {
      window.location.href = path;
    },
    sign_out() {
      myFetch("/auth/sing_out", {method: "POST"})
          .then(res => {
            if (res.ok) {
              return res.json()
            }
            return res.json().then(error => {throw new Error(error.detail)})
          })
          .then(data => {
            delete this.storage.token_payload
            delete this.storage.token_header
            delete this.storage.token
            this.navigate("/")
          })
          .catch(err => {
            console.log(err)
          })
    },
    create_new_preset() {
      myFetch(
          "/presets",
          {
            method: "POST",
          }
      ).then(res => {
        if (res.ok) {
          return res.json();
        }
        else {
          return res.json().then(error => {throw new Error(error.detail)})
        }
      }).then( data => {
        this.navigate(`/preset/${data.id}`);
      }).catch(error => {
        window.alert(error);
        console.error(error)
      })
    }
  },
  mounted() {
    // console.log(this.user_info);
  }
}
</script>

<style scoped>
.vertical-navbar {
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: #D9D9D9;
  color: black;
  border-right: 1px solid #ddd;
  padding: 10px;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
}

.logo {
  font-size: 50px;
  font-weight: bold;
  padding: 20px 10px;
  text-align: center;
  -webkit-text-stroke: 1px #000;
}

.logo:hover {
  filter: brightness(90%);
  cursor: pointer;
}

.vertical-navbar ul {
  list-style: none;
  padding: 0;
  margin: 0;
  flex-grow: 1; /* Allows the list to grow and fill available space */
}

.vertical-navbar li {
  font-size: 20px;
  padding: 10px;
  cursor: pointer;
  text-align: center;
}

.vertical-navbar li:hover {
  background-color: #e2e6ea;
}

.vertical-navbar li.active {
  background-color: #e2e6ea;
}


.button-container {
  width: 100%;
  display: flex;
  justify-content: space-around;
  wrap-option: wrap;
  gap: 10px;
  margin-bottom: 20px;

}

.btn {
  font-size: 20px;
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
}

.sign-in {
  background-color: gray;
  color: white;
  border: none;
}

.sign-up {
  background-color: transparent;
  color: gray;
  border: 2px solid gray;
}

.btn:hover {
  filter: brightness(80%);
}

.user-info {
  margin-bottom: 20px;
}

</style>
