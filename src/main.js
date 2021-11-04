import { createApp } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'

import App from './App.vue'
import router from './router'

library.add(fas)

// Aquí se importa la hoja de estilos global del proyecto
import "@/assets/css/main.css"

createApp(App).component('ges-icon', FontAwesomeIcon)
    .use(router).mount('#app')