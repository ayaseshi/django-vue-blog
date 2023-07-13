<template>
    <div class="login-container">
      <h1 class="title">Sign in</h1>
      <form class="login-form" @submit.prevent="loginUser">
        <div class="field">
          <label class="label">Username</label>
          <div class="control">
            <input class="input" type="text" v-model="username" placeholder="Enter your username" />
          </div>
        </div>
        <div class="field">
          <label class="label">Password</label>
          <div class="control">
            <input class="input" type="password" v-model="password" placeholder="Enter your password" />
          </div>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-primary">Sign in</button>
          </div>
        </div>
      </form>
      <Notification v-for="(notification, index) in notifications" :key="index" :notification="notification.message" :notificationType="notification.type" @clear="clearNotification(index)" />
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Notification from '@/components/Notification.vue';
  
  export default {
    components: {
      Notification
    },
    data() {
      return {
        username: '',
        password: '',
        notifications: []
      };
    },
    methods: {
      async loginUser() {
        if (!this.username || !this.password) {
          this.showNotification('All fields must be filled.');
          return;
        }
  
        const userData = {
          username: this.username,
          password: this.password
        };
  
        try {
          const response = await axios.post('/api/v1/login/', userData);
          const data = response.data;
  
          if (data.token) {
            localStorage.setItem('login', this.username);
            localStorage.setItem('token', data.token);
  
            this.$router.push({ name: 'home' });
          } else if (data.error) {
            this.showNotification(data.error);
          } else {
            this.showNotification('An error occurred during login.');
          }
        } catch (error) {
          if (error.response) {
            this.showNotification(error.response.data.error);
          } else {
            this.showNotification('An error occurred while communicating with the server.');
          }
        }
      },
  
      showNotification(message) {
        this.notifications.push({ message });
      },
  
      clearNotification(index) {
        this.notifications.splice(index, 1);
      }
    }
  };
  </script>
  
  <style lang="scss">
  @import "@/assets/LoginRegister.css";
  </style>