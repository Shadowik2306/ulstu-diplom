import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import {createRouter, createWebHistory} from 'vue-router'
import SampleCreator from "./components/SampleCreator.vue";
import AllPresets from "./components/AllPresets.vue";




const routes = [
    { path: '/'},
    { path: '/preset/:id', component: SampleCreator},
    { path: '/presets', component: AllPresets},
]

const router = createRouter({
    history: createWebHistory(),
    linkActiveClass: 'active',
    routes
})

createApp(App).use(router).mount('#app')
