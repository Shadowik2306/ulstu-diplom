import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import {createRouter, createWebHashHistory} from 'vue-router'
import SampleCreator from "./components/SampleCreator.vue";




const routes = [
    { path: '/'},
    { path: '/preset/:id', component: SampleCreator}
]

const router = createRouter({
    history: createWebHashHistory(),
    linkActiveClass: 'active',
    routes
})

createApp(App).use(router).mount('#app')
