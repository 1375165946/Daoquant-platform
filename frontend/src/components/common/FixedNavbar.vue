<template>
  <header class="c-header">
    <div class="c-header-wrapper">

      <!-- 左侧部分：Logo + 专业版按钮 -->
      <div class="c-header-left">
        <div class="header-logo">DaoQuant</div>
        <a class="c-header-button" href="https://www.baidu.com" target="_blank">了解专业版</a>
      </div>

      <!-- 中间部分：导航菜单 -->
      <div class="c-header-center">
        <nav class="c-header-nav">
          <ul class="c-header-nav-ul">
            <li><router-link to="/">首页</router-link></li>
            <li><a @click="checkAuthAndGo('/strategy-dev')" class="nav-link">策略研发</a></li>
            <!-- 编写策略带下拉 -->
            <li class="dropdown">
              <a @click="checkAuthAndGo('/strategy-new')" class="dropdown-trigger">
                编写策略
                <svg class="arrow" viewBox="0 0 1024 1024" width="10" height="10" xmlns="http://www.w3.org/2000/svg">
                  <path d="M512 640L192 320h640z" fill="currentColor"/>
                </svg>
              </a>
              <ul class="dropdown-menu">
                <li><a @click="checkAuthAndGo('/strategy-new')"class="nav-link">新建策略</a></li>
                <li><a @click="checkAuthAndGo('/strategy-ai')"class="nav-link">AI策略助手</a></li>
              </ul>
            </li>

            <!-- 策略社区下拉 -->
            <li class="dropdown">
              <a @click="checkAuthAndGo('/strategy-forum')" class="dropdown-trigger">
                策略社区
                <svg class="arrow" viewBox="0 0 1024 1024" width="10" height="10">
                  <path d="M512 640L192 320h640z" fill="currentColor"/>
                </svg>
              </a>
              <ul class="dropdown-menu">
               <li><a @click="checkAuthAndGo('/strategy-mall')"class="nav-link">策略商城</a></li>
              <li><a @click="checkAuthAndGo('/strategy-famous')"class="nav-link">名人堂</a></li>
              <li><a @click="checkAuthAndGo('/strategy-forum')"class="nav-link">策略论坛</a></li>
              </ul>
            </li>

            <li v-if="userStore.isLoggedIn">
              <router-link to="/user-strategy">我的策略</router-link>
            </li>
            <li><a @click="checkAuthAndGo('/stock-diagnosis')" class="nav-link">个股诊断</a></li>
            <li><router-link to="/stock-calendar">股票日历</router-link></li>
            <li><a @click="checkAuthAndGo('/strategy-simulation')" class="nav-link">策略模拟</a></li>
          </ul>
        </nav>
      </div>

      <!-- 右侧按钮 -->
            <!-- 已登录 -->
      <div class="c-header-right" v-if="userStore.isLoggedIn">
        <div class="user-dropdown">
          <span class="user-name">
            {{ userStore.userInfo.name }}
            <svg class="arrow" viewBox="0 0 1024 1024" width="10" height="10">
              <path d="M512 640L192 320h640z" fill="currentColor"/>
            </svg>
          </span>
          <ul class="dropdown-menu">
            <li><router-link to="/my-subscription">我的订阅</router-link></li>
            <li><router-link to="/my-following">我的关注</router-link></li>
            <li><router-link to="/profile">个人信息</router-link></li>
            <li><a @click.prevent="handleLogout">退出登录</a></li>
          </ul>
        </div>
      </div>

      <!-- 未登录 -->
      <div class="c-header-right" v-else>
        <router-link to="/register" class="btn-primary">免费注册</router-link>
        <router-link to="/login" class="btn-outline">登录</router-link>
      </div>
    </div>
  </header>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
import { ElMessageBox } from 'element-plus'

const userStore = useUserStore()
const router = useRouter()

const checkAuthAndGo = async (path) => {
  if (userStore.isLoggedIn) {
    router.push(path)
  } else {
    await ElMessageBox.confirm(
      '您尚未登录，是否前往登录页面？',
      '请先登录',
      {
        confirmButtonText: '去登录',
        cancelButtonText: '取消',
        type: 'warning',
      }
    ).then(() => {
      router.push('/login')
    }).catch(() => {
      // 用户点了“取消”，什么也不做
    })
  }
}

const handleLogout = () => {
  userStore.logout()
  router.push('/')  // 可跳转登录页或首页
}
</script>
  
<style scoped>
 @import '@/assets/css/common/FixedNavbar.css';
</style>