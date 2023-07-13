<template>
    <div v-if="notification" class="notification" :class="notificationType" @animationend="clearNotification">
      {{ notification }}
    </div>
  </template>
  
  <script>
  export default {
    props: {
      notification: {
        type: String,
        required: true
      },
      notificationType: {
        type: String,
        required: true
      }
    },
    methods: {
      clearNotification() {
        this.$emit('clear');
      }
    }
  };
  </script>
  
  <style lang="scss">
  .notification {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #fff;
    padding: 10px 20px;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    animation: fadeOut 5s forwards;
    z-index: 9999;
    color: #ff3860;
  }
  
  @keyframes fadeOut {
    0% {
      opacity: 1;
    }
    100% {
      opacity: 0;
    }
  }
  </style>