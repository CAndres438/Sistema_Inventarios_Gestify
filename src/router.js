import { createRouter, createWebHashHistory } from 'vue-router'
import App from "./App.vue"
import LogIn from "./components/LogIn.vue"
import HomePage from "./components/HomePage.vue"
import SignUp from "./components/SignUp.vue"
import MainLayout from "./components/application/MainLayout.vue"
import RegistroProveedores from "./components/application/modules/RegistroProveedores.vue"
import ConsultaProveedores from "./components/application/modules/ConsultaProveedores.vue"
import RegistroInventario from "./components/application/modules/RegistroInventario.vue"
import ConsultaProductos from "./components/application/modules/ConsultaProductos.vue"
import Profile from "./components/application/modules/Profile.vue"

const routes = [{
        path: '/',
        name: 'homePage',
        component: HomePage
    },
    {
        path: '/user/login',
        name: 'logIn',
        component: LogIn
    },
    {
        path: '/user/signup',
        name: 'signUp',
        component: SignUp
    },
    {
        path: '/dashboard',
        name: 'mainLayout',
        component: MainLayout,
        children: [{
                path: 'registro-productos',
                component: RegistroInventario,
            },
            {
                path: 'consulta-productos',
                component: ConsultaProductos,
            },
            {
                path: 'registro-proveedores',
                component: RegistroProveedores,
            },
            {
                path: 'consultar-proveedores',
                component: ConsultaProveedores,
            },
            {
                path: '/user/profile',
                component: Profile
            }
        ],
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router