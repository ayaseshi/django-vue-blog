<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <RouterLink to="/" class="navbar-item logo">
          <strong>BLOG</strong>
        </RouterLink>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
          @click="toggleMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" :class="{ 'is-active': isMobileMenuOpen }">
        <div class="navbar-end">
          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link">
              Dishes
            </a>
            <div class="navbar-dropdown is-right">
              <RouterLink v-for="dish in dishes" :key="dish.id" :to="dish.url" class="navbar-item">
                {{ dish.name }}
              </RouterLink>
            </div>
          </div>

          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link">
              <font-awesome-icon :icon="['fa', 'user']" style="color: #28c4a4;" />
            </a>
            <div class="navbar-dropdown is-right">
              <template v-if="isLoggedIn">
                <a class="navbar-item">
                  {{ username }}
                </a>
                <a class="navbar-item">
                  Add your recipe
                </a>
                <a class="navbar-item">
                  Favorites
                </a>
              </template>
              <template v-if="!isLoggedIn">
                <router-link to="/login" class="navbar-item">
                  Sign in
                </router-link>
                <router-link to="/register" class="navbar-item">
                  Sign up
                </router-link>
              </template>
              <a class="navbar-item">
                Download ebook
              </a>
              <template v-if="isLoggedIn">
                <hr class="navbar-divider">
                <a class="navbar-item" @click="logoutUser">
                  Logout
                </a>
              </template>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <RouterView :isLoggedIn="isLoggedIn" @login="updateLoginStatus" />
    </section>

    <footer class="footer">
      <div class="content has-text-centered">
        <p>
          <a href="https://github.com/ayaseshi">
            Created by ayaseshi
          </a>
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      isMobileMenuOpen: false,
      dishes: [],
      isLoggedIn: false,
      username: ''
    };
  },
  async mounted() {
    try {
      const response = await axios.get('/api/v1/tags/');
      const data = response.data;

      this.dishes = data.map(tag => {
        return {
          id: tag.id,
          name: tag.name,
          url: tag.url
        };
      });

      const token = localStorage.getItem('token');
      if (token) {
        this.isLoggedIn = true;
        this.username = localStorage.getItem('login');
      }
    } catch (error) {
      console.error(error);
    }
  },
  methods: {
    toggleMobileMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen;
    },
    logoutUser() {
      localStorage.removeItem('login');
      localStorage.removeItem('token');
      this.isLoggedIn = false;
      this.$router.push({ name: 'home' });
    },
    updateLoginStatus() {
      const token = localStorage.getItem('token');
      if (token) {
        this.isLoggedIn = true;
      } else {
        this.isLoggedIn = false;
      }
    }
  }
};
</script>

<style lang="scss">
@import '../node_modules/bulma/bulma.sass';

.navbar-item {
  padding: 0.5rem 1rem;
}

.navbar-dropdown.is-right {
  right: 0;
}

.footer {
  background-color: #f5f5f5;
  padding: 1rem 0;
}

.logo {
  font-size: 1.5rem;
  text-transform: uppercase;
  letter-spacing: 2px;
}

@media screen and (max-width: 768px) {
  .navbar-menu {
    display: none;
  }

  .navbar-burger {
    display: block;
  }

  .navbar.is-active .navbar-menu {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    background-color: #000000;
    position: absolute;
    top: 100%;
    right: 0;
    left: auto;
    z-index: 1;
    padding: 1rem;
  }

  .navbar.is-active .navbar-item {
    margin: 0;
    width: 100%;
    text-align: right;
  }

  .navbar.is-active .navbar-item:not(:last-child) {
    margin-bottom: 1rem;
  }
}
</style>