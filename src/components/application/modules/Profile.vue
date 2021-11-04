<template>
  <div>
    <h1>Bienvenido a tu perfil,</h1>
    <div class="profile-information-container" v-if="profileInfo">
      <div>
        <h2>Información personal</h2>
        <p class="profile-information__title">Nombre</p>
        <p class="profile-information__data">{{ user.name }}</p>
      </div>
      <div>
        <h2>Información de contacto</h2>
        <p class="profile-information__title">Email</p>
        <p class="profile-information__data">{{ user.email }}</p>
      </div>
      <div>
        <h2>Información de Acceso al portal</h2>
        <p class="profile-information__title">Nombre de usuario</p>
        <p class="profile-information__data">{{ user.username }}</p>
      </div>
      <button class="primary-btn" v-on:click="showForm">
        Quiero actualizar mi información
      </button>
    </div>
    <div
      class="global-form-container global-form-container--profile"
      v-if="updateInfo"
    >
      <form v-on:submit.prevent="updateUser">
        <div class="user-profile-form">
          <h2>Información personal</h2>
          <div>
            <div class="input-container">
              <label for="name" class="input-container__label"
                >Nombre completo</label
              >
              <input
                type="text"
                class="input-container__input"
                name="name"
                id="name"
                v-model="user.name"
                required
              />
            </div>
          </div>
          <div>
            <h2>Información de acceso al sistema</h2>
            <div class="input-container input-container-no-margin">
              <label for="username" class="input-container__label"
                >Nombre de usuario</label
              >
              <input
                type="text"
                class="input-container__input input-no-margin"
                name="username"
                id="username"
                v-model="user.username"
                required
              />
            </div>
            <a
              v-on:click="updatePassword"
              class="bottom-info__action password-action"
              >Actualizar contraseña</a
            >
          </div>
          <div>
            <h2>Información de contacto</h2>
            <div class="input-container">
              <label for="email" class="input-container__label"
                >Correo electrónico</label
              >
              <input
                type="email"
                class="input-container__input"
                name="email"
                id="email"
                v-model="user.email"
                required
              />
            </div>
          </div>
        </div>
        <button type="submit" class="primary-btn">Actualizar información</button>
        <button type="button" class="cancel-btn" v-on:click="showForm">
          Cancelar
        </button>
      </form>
    </div>
    <div
      v-if="showPasswordUpdate"
      class="global-form-container global-form-container--profile"
    >
      <h2>Actualizar contraseña</h2>
      <form action="">
        <div class="input-container">
          <label for="password" class="input-container__label"
            >Contraseña</label
          >
          <input
            type="password"
            class="input-container__input"
            name="password"
            id="password"
            v-model="newPassword"
            required
          />
        </div>
        <div class="input-container">
          <label for="passwordConfirmation" class="input-container__label"
            >Contraseña</label
          >
          <input
            type="password"
            class="input-container__input"
            name="passwordConfirmation"
            id="passwordConfirmation"
            v-model="confirmPassword"
            required
          />
        </div>
        <button class="primary-btn" v-on:click="setNewPassword">
          Actualizar contraseña
        </button>
        <button type="button" class="cancel-btn" v-on:click="updatePassword">
          Regresar
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import jwt_decode from "jwt-decode";
import axios from "axios";
export default {
  name: "profile",

  data: () => {
    return {
      username: localStorage.getItem("username") || "none",
      name: "",
      email: "",
      username: "",
      password: "",
      user: {
        name: "",
        username: "",
        email: "",
        password: "",
      },
      newPassword: "",
      confirmPassword: "",
      is_auth: true,
      profileInfo: true,
      updateInfo: false,
      showPasswordUpdate: false,
    };
  },

  methods: {
    getUserDataProfile: async function () {
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
          this.user.name = result.data.name;
          this.user.email = result.data.email;
          this.user.username = result.data.username;
          this.user.password = result.data.password;
        })
        .catch(() => this.logOut);
    },

    logOut: function () {
      localStorage.clear();
      this.$router.push({ name: "logIn" });
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
      this.is_auth = localStorage.getItem("isAuth");
      if (this.is_auth == false) this.$router.push({ name: "logIn" });
      else this.$router.push("/user/profile");
    },

    updateUser: function () {
      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();
      axios
        .put(`https://gestify-back-nodb.herokuapp.com/user/${userId}`, this.user, {
          headers: { Authorization: `Bearer ${userToken}` },
        })
        .then((result) => {
          alert("Información actualizada con éxito");
          this.getUserDataProfile()
          this.updateInfo = false,
          this.profileInfo = true
        })
        .catch((error) => {
          console.error(error);
          alert("Falló el registro");
        });
    },

    updatePassword: function () {
      if (this.showPasswordUpdate == false) {
        this.showPasswordUpdate = true;
        this.updateInfo = false;
        this.profileInfo = false;
      } else {
        (this.showPasswordUpdate = false), (this.updateInfo = true);
        this.profileInfo = false;
      }
    },

    setNewPassword: function () {
      if (this.newPassword != this.confirmPassword) {
        alert(
          "Las contraseña y su confirmación deben coincidir. Verifica e intenta nuevamente"
        );
      } else if (this.newPassword === this.confirmPassword) {
        alert("Contraseña actualizada con éxito");
        this.user.password = this.confirmPassword;
        console.log(this.user);
        this.updateUser();
        this.$router.push("logIn");
      }
    },

    showForm: function () {
      if (this.updateInfo == false) {
        this.updateInfo = true;
        this.profileInfo = false;
      } else {
        this.updateInfo = false;
        this.profileInfo = true;
      }
    },
  },
  beforeMount() {
    this.getUserDataProfile();
    this.verifyAuth();
  },
};
</script>