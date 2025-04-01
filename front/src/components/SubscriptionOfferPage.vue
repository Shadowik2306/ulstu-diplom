<template>
  <div class="subscription">
    <h1>Subscription Offer</h1>
    <div class="comparison">
      <div class="option not-subscribed">
        <h2>Without Subscription</h2>
        <ul>
          <li>Limited content access</li>
          <li>Advertisements</li>
          <li>No exclusive features</li>
        </ul>
      </div>
      <div class="option subscribed">
        <h2>With Subscription</h2>
        <ul>
          <li>Unlimited content access</li>
          <li>Ad-free experience</li>
          <li>Access to premium features</li>
          <li>Priority customer support</li>
        </ul>
      </div>
    </div>
    <ButtonComponent label="Subscribe" @click="this.subscribe"/>
  </div>
</template>

<script>
import ButtonComponent from "./ButtonComponent.vue";
import {myFetch} from "../assets/myFetch.js";

export default {
  name: "SubscriptionOfferPage",
  components: {ButtonComponent},
  methods: {
    subscribe() {
      myFetch("/auth/subscribe", {method: "POST"})
          .then(res => {
            if (res.ok) {
              return res.json()
            }
            return res.json().then(error => {throw new Error(error.detail)})
          })
          .then(data => {
            window.location.href = "/"
          })
          .catch(error => {
            window.alert(error);
          })
    }
  }
};
</script>

<style scoped>
.subscription-offer {
  font-family: Arial, sans-serif;
  padding: 20px;
  text-align: center;
}

.comparison {
  display: flex;
  justify-content: space-around;
  margin: 20px 0;
  gap: 1vh;
  height: 70vh;
}

.option {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 20px;
  width: 45%;
}

.not-subscribed {
  background-color: #F8FFAE;
}

.subscribed {
  background-color: #FFCC73;
  border: 2px #FF7C7C solid;
}

h1, h2 {
  color: #333;
}

li {
  color: black;
  font-size: 2vh;
}

li:not(:last-child) {
  margin-bottom: 1vh;
}


button {
  background-color: #00acc1;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
}

button:hover {
  background-color: #007c91;
}
</style>
