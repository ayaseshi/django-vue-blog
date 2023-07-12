<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <RouterLink to="/" class="navbar-item logo">
          <strong>BLOG</strong>
        </RouterLink>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="toggleMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" :class="{'is-active': isMobileMenuOpen}">
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
              Opcje
            </a>
            <div class="navbar-dropdown is-right">
              <router-link to="/login" class="navbar-item">
                Sign in
              </router-link>
              <router-link to="/register" class="navbar-item">
                Sign up
              </router-link>
              <a class="navbar-item">
                Download ebook
              </a>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <RouterView />
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
      dishes: []
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
    } catch (error) {
      console.error(error);
    }
  },
  methods: {
    toggleMobileMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen;
    },
  },
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

/* Dodatkowe style dla napisu "BLOG" */
.logo {
  font-size: 1.5rem;
  text-transform: uppercase;
  letter-spacing: 2px;
}

/* Responsywność dla aplikacji na telefonach */
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