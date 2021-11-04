<template v-if="is_auth">
  <div class="main-layout">
    <nav class="sidenav">
      <div class="sidenav-content">
        <div>
          <h1>Gestify</h1>
          <details
            v-for="option in options"
            :key="option"
            class="sidenav-options"
          >
            <summary class="sidenav-options__summary">
              <ges-icon icon="chevron-right"></ges-icon>
              <span> {{ option.title }}</span>
            </summary>
            <ul class="sidenav-list">
              <li
                v-for="subitem in option.children"
                :key="subitem"
                class="sidenav-list__subitem"
              >
                <router-link :to="subitem.url" class="sidenav-list__link">
                  {{ subitem.name }}
                </router-link>
              </li>
            </ul>
          </details>
        </div>
        <div class="sidenav-bottom-info">
          <p class="bottom-info__name">{{ name }}</p>
          <div class="bottom-actions-container">
            <router-link to="/user/profile" class="bottom-info__profile"
              >Ver mi perfil</router-link
            >
            <a class="bottom-info__action" v-on:click="logOut">
              <ges-icon icon="sign-out-alt"></ges-icon> Cerrar sesión</a
            >
          </div>
        </div>
      </div>
    </nav>
    <div class="main-content">
      <div class="main-component">
        <router-view> </router-view>
      </div>
    </div>
  </div>
</template>
<script>
import jwt_decode from "jwt-decode";
import axios from "axios";
export default {
  name: "mainLayout",
  data: () => {
    return {
      options: [
        {
          title: "Proveedores",
          children: [
            {
              name: "Registro de proveedores",
              url: "/dashboard/registro-proveedores",
            },
            {
              name: "Consultar proveedores",
              url: "/dashboard/consultar-proveedores",
            },
          ],
        },
        {
          title: "Productos",
          children: [
            {
              name: "Ingreso de producto",
              url: "/dashboard/registro-productos",
            },
            {
              name: "Listado de productos",
              url: "/dashboard/consulta-productos",
            },
          ],
        },
        // {
        //   title: "Usuarios",
        //   children: [
        //     {
        //       name: "Registrar nuevo usuario",
        //       url: "/dashboard/registro-usuarios",
        //     },
        //     {
        //       name: "Usuarios del sistema",
        //       url: "/dashboard/consultar-usuarios",
        //     },
        //   ],
        // },
      ],
      username: localStorage.getItem("username") || "none",
      name: "",
      email: "",
      username: "",
      is_auth: Boolean,
    };
  },
  methods: {
    sendToModule: function (subitem) {
      let urlName = subitem.url;
      this.$router.push({ name: subitem.url });
    },

    logOut: function () {
      localStorage.clear();
      this.$router.push({ name: "logIn" });
    },

    getUserData: async function () {
      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.logOut;
        return;
      }

      await this.verifyToken();

      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();

      axios
        .get(`https://gestify-back-nodb.herokuapp.com/user/${userId}`, {
          headers: { Authorization: `Bearer ${userToken}` },
        })
        .then((result) => {
          this.name = result.data.name;
          this.email = result.data.email;
          this.username = result.data.username;
        })
        .catch(() => this.logOut);
    },

    verifyToken: function () {
      return axios
        .post(
          "https://gestify-back-nodb.herokuapp.com/refresh",
          { refresh: localStorage.getItem("token_refresh") },
          { headers: {} }
        )
        .then((result) => {
          localStorage.setItem("token_access", result.data.access);
        })
        .catch(() => {
          this.logOut;
        });
    },
    created: async function () {
      this.getUserData;
    },

    verifyAuth: function () {
      this.is_auth = localStorage.getItem("isAuth") || false;
      if (this.is_auth == false) this.$router.push({ name: "logIn" });
      else this.$router.push({ name: "mainLayout" });
    },
  },

  beforeMount() {
    this.getUserData();
    this.verifyAuth();
  },
};
</script>
