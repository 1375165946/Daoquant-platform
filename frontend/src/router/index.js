import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import stockRoutes from './stock'
import strategyRoutes from './strategy'
import userRoutes from './user'

const routes = [
  { path: '/',
    component: Home,
    Children:[]},
  ...stockRoutes,
  ...strategyRoutes,
  ...userRoutes,
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
