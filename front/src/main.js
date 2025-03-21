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
import MainPage from "./components/MainPage.vue";



const routes = [
    { path: '/', component: MainPage, name: "MainPage" },
    { path: '/preset/:id', component: SampleCreator, name: 'sample_creator' },
    { path: '/presets', component: ListOfPresets, name: 'presets'},
    { path: '/my_presets', component: ListOfPresets, props: {users_created: true}, name: 'my_presets'},
    { path: '/favorites', component: ListOfPresets, props: {favorites: true}, name: 'favorites'},
    { path: '/sign_in', component: SignInComponent, name: 'sign_in' },
    { path: '/sign_up', component: SignUpComponent, name: 'sign_up' },
]

const router = createRouter({
    history: createWebHistory(),
    linkActiveClass: 'active',
    routes
})


createApp(App).use(router).use(ReactiveStorage, {}).mount('#app')
