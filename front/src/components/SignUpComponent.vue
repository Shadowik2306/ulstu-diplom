<template>
  <div class="form-container">
    <h2>Sign Up</h2>
    <form @submit.prevent="signUp">
      <input type="text" v-model="username" placeholder="Nickname" required />
      <input type="email" v-model="email" placeholder="Email" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
import {myFetch} from "../assets/myFetch.js";

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
    };
  },
  methods: {
    signUp() {
      myFetch(
          "/auth/sign_up",
          {
            method: "POST",
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              'username': this.username,
              'email': this.email,
              'password': this.password
            })
          }
      ).then(response => {
        return response.json();
      }).then(data => {
        console.log(data)
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
  color: black;
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
  background-color: transparent;
  color: #00103D;
  cursor: pointer;
  border: 2px solid #00103D;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #00103D;
  color: white;
}
</style>
