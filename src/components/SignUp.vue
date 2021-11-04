<template>
  <div>
    <!-- <div class="bg-img"></div> -->
    <div class="center-content-column">
      <div class="register-form-container">
        <div class="bg-register">
          <img
            class="register-img"
            src="../assets/img/register.svg"
            alt="user-inventory"
          />
        </div>
        <div class="white-container">
          <div class="header-back-button">
            <router-link to="/" class="header-back-button__link">
              <ges-icon icon="chevron-left" />
              VOLVER
            </router-link>
            <h1 class="form-title form-title--login">Regístrate</h1>
          </div>
          <form class="login-form" v-on:submit.prevent="sendToLogIn">
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
            <div class="input-container">
              <label for="username" class="input-container__label"
                >Nombre de usuario</label
              >
              <input
                type="text"
                class="input-container__input"
                name="username"
                id="username"
                v-model="user.username"
                required
              />
            </div>
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
            <div class="input-container">
              <label for="password" class="input-container__label"
                >Contraseña</label
              >
              <input
                type="password"
                class="input-container__input"
                name="password"
                id="pass"
                v-model="user.password"
                required
              />
            </div>
            <button
              type="submit"
              class="primary-btn"
            >
              Registrarme
            </button>
          </form>
          <div class="bottom-actions">
            <p>
              ¿Ya tienes cuenta?
              <router-link to="/user/login" class="bottom-actions__link">Inicia sesión</router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "signUp",
  data: function () {
    return {
      user: {
        name: "",
        username: "",
        email: "",
        password: "",
      },
    };
  },
  methods: {
    sendToLogIn: function () {
      axios
        .post("https://gestify-back-nodb.herokuapp.com/user", this.user, {
          headers: {},
        })
        .then((result) => {
          let dataSignUp = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };
          this.$emit("completedSignUp", dataSignUp);
        })
        .catch((error) => {
          console.error(error);
          alert("Falló el registro");
        });
    },
  },
};
</script>