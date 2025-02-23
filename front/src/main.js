import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import {createRouter, createWebHashHistory} from 'vue-router'


const routes = [
    { path: '/'},
]

const router = createRouter({
    history: createWebHashHistory(),
    linkActiveClass: 'active',
    routes
})

createApp(App).use(router).mount('#app')
