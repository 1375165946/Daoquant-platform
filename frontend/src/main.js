import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import 'vue3-carousel/dist/carousel.css'


// 设置 axios 默认配置
axios.defaults.baseURL = 'http://127.0.0.1:8000' // 后端地址（可修改）
axios.defaults.withCredentials = true           // 允许发送 Cookie（关键）
axios.defaults.headers.post['Content-Type'] = 'application/json'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const app = createApp(App)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

app.use(pinia)
app.use(router)
app.use(ElementPlus) // 启用 Element Plus

app.mount('#app')
