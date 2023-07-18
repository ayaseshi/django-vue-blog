import { createApp } from 'vue'
import App from './App.vue'

import router from './router'
import axios from 'axios'


import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faUser } from '@fortawesome/free-solid-svg-icons'

library.add(faUser)

const app = createApp(App).component('font-awesome-icon', FontAwesomeIcon)

app.use(router)
axios.defaults.baseURL = 'http://127.0.0.1:8000/'
app.mount('#app')