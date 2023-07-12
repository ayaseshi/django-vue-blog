<template>
    <div class="register-container">
      <h1 class="title">Sing up</h1>
      <form class="register-form">
        <div class="field">
          <label class="label">Username</label>
          <div class="control">
            <input class="input" type="text" placeholder="Enter username" />
          </div>
        </div>
        <div class="field">
          <label class="label">Email</label>
          <div class="control">
            <input class="input" type="email" placeholder="Enter email address" />
          </div>
        </div>
        <div class="field">
          <label class="label">Password</label>
          <div class="control">
            <input class="input" type="password" placeholder="Enter your password" />
          </div>
        </div>
        <div class="field">
          <label class="label">Repeat Password</label>
          <div class="control">
            <input class="input" type="password" placeholder="Repeat your password" />
          </div>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-primary">Sing up</button>
          </div>
        </div>
      </form>
    </div>
  </template>
  
  <style lang="scss">
    @import "@/assets/LoginRegister.css";
  </style>