export default [
  { path: '/strategy-dev', component: () => import('@/views/strategy/strategy-develop.vue') },
  { path: '/strategy-new', component: () => import('@/views/strategy/strategy-new.vue') },
  { path: '/strategy-ai', component: () => import('@/views/strategy/strategy-ai.vue') },
  { path: '/strategy-famous', component: () => import('@/views/strategy/strategy-famous.vue') },
  { path: '/strategy-forum', component: () => import('@/views/strategy/strategy-forum.vue') },
  { path: '/strategy-mall', component: () => import('@/views/strategy/strategy-mall.vue') },
  { path: '/strategy-simulation', component: () => import('@/views/strategy/strategy-simulation.vue') },
]