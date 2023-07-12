<template>
    <div class="login-container">
      <h1 class="title">Sign in</h1>
      <form class="login-form">
        <div>
          <label class="label">Email</label>
          <div class="control">
            <input class="input" type="email" placeholder="Enter email address" />
          </div>
        </div>
        <div class="field">
          <label class="label">Password</label>
          <div class="control">
            <input class="input" type="password" placeholder="Enter your password"/>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-primary">Sign in</button>
          </div>
        </div>
      </form>
    </div>
  </template>
  
  <style lang="scss">
    @import "@/assets/LoginRegister.css";
  </style>