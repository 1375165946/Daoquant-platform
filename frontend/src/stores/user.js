// src/stores/user.js
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    isLoggedIn: false,
    userInfo: null
  }),
  actions: {
    login(user) {
      this.isLoggedIn = true
      this.userInfo = user
    },
    logout() {
      this.isLoggedIn = false
      this.userInfo = null
    }
  },
  persist: true
})
