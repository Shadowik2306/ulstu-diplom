import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import {createRouter, createWebHistory} from 'vue-router'
import SampleCreator from "./components/SampleCreator.vue";
import ListOfPresets from "./components/ListOfPresets.vue";
import SignInComponent from "./components/SignInComponent.vue";
import SignUpComponent from "./components/SignUpComponent.vue";
import ReactiveStorage from "vue-reactive-localstorage";
import "@fortawesome/fontawesome-free/css/all.css";



const routes = [
    { path: '/'},
    { path: '/preset/:id', component: SampleCreator},
    { path: '/presets', component: ListOfPresets},
    { path: '/my_presets', component: ListOfPresets, props: {users_created: true}},
    { path: '/favorites', component: ListOfPresets, props: {favorites: true}},
    { path: '/sign_in', component: SignInComponent},
    { path: '/sign_up', component: SignUpComponent},
]

const router = createRouter({
    history: createWebHistory(),
    linkActiveClass: 'active',
    routes
})


createApp(App).use(router).use(ReactiveStorage, {}).mount('#app')
