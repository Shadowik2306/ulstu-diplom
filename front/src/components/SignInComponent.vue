<template>
  <div class="form-container">
    <h2>Sign In</h2>
    <form @submit.prevent="signIn">
      <input type="email" v-model="email" placeholder="Email" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Sign In</button>
    </form>
  </div>
</template>

<script>
import {myFetch} from "../assets/myFetch.js";

export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    signIn() {
      myFetch(
          "/auth/sing_in",
          {
            method: "POST",
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              'email': this.email,
              'password': this.password
            })
          }
      ).then(response => {
        return response.json();
      }).then(data => {
        const raw_token = data.access_token
        this.storage.token = raw_token;
        this.storage.token_header = window.atob(raw_token.split('.')[0]);
        this.storage.token_payload = window.atob(raw_token.split('.')[1]);
      })
    },
  },
};
</script>

<style scoped>
.form-container {
  width: 300px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 5px;
  background-color: #D9D9D9;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  color:black;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

input {
  display: block;
  width: 100%;
  padding: 10px 0;
  margin: 10px 0;
  border-radius: 5px;
  border: 1px solid #ccc;
  text-align: center;
}

button {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: none;
  background-color: #00103D;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #000080;
}
</style>
