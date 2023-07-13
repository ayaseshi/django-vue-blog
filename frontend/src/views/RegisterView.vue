<template>
  <div class="register-container">
    <h1 class="title">Sign up</h1>
    <form class="register-form" @submit.prevent="registerUser">
      <div class="field">
        <label class="label">Username</label>
        <div class="control">
          <input class="input" type="text" v-model="username" placeholder="Enter username" />
        </div>
      </div>
      <div class="field">
        <label class="label">Password</label>
        <div class="control">
          <input class="input" type="password" v-model="password" placeholder="Enter your password" />
        </div>
      </div>
      <div class="field">
        <label class="label">Repeat Password</label>
        <div class="control">
          <input class="input" type="password" v-model="repeatPassword" placeholder="Repeat your password" />
        </div>
      </div>
      <div class="field">
        <div class="control">
          <button class="button is-primary">Sign up</button>
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
      repeatPassword: '',
      notifications: []
    };
  },
  methods: {
    async registerUser() {
      if (!this.username || !this.password || !this.repeatPassword) {
        this.showNotification('All fields must be filled.');
        return;
      }

      if (this.password !== this.repeatPassword) {
        this.showNotification('Passwords do not match.');
        return;
      }

      if (this.username.length <= 4) {
        this.showNotification('Username must be longer than 4 characters.');
        return;
      }

      if (this.password.length <= 6 || !/[A-Z]/.test(this.password)) {
        this.showNotification('Password must be longer than 6 characters and contain at least one uppercase letter.');
        return;
      }

      const userData = {
        username: this.username,
        password: this.password
      };

      try {
        const response = await axios.post('/api/v1/register/', userData);
        const data = response.data;

        if (data.token) {
          localStorage.setItem('login', this.username);
          localStorage.setItem('token', data.token);

          this.$router.push({ name: 'home' });
        } else if (data.error) {
          this.showNotification(data.error);
        } else {
          this.showNotification('An error occurred during registration.');
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