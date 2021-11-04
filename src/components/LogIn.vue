<template>
  <div class="center-content-column">
    <div class="login-form-container">
      <div class="bg-login"></div>
      <div class="white-container">
        <div class="header-back-button">
          <router-link to="/" class="header-back-button__link">
            <ges-icon icon="chevron-left" />
            VOLVER
          </router-link>
          <h1 class="form-title form-title--login">Inicio de sesión</h1>
        </div>
        <form class="login-form" v-on:submit.prevent="sendToDashboard">
          <div class="input-container">
            <label for="username" class="input-container__label"
              >Nombre de usuario</label
            >
            <input
              type="username"
              class="input-container__input"
              name="username"
              id="username"
              v-model="user.username"
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
            />
          </div>
          <button type="submit" class="primary-btn">Iniciar sesión</button>
        </form>
        <div class="bottom-actions">
          <p>
          ¿Aún no eres usuario?
          <router-link to="/user/signup" class="bottom-actions__link">Regístrate</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "logIn",
  data: function () {
    return {
      user: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    sendToDashboard: function () {
      axios
        .post("https://gestify-back-nodb.herokuapp.com/login", this.user, {
          headers: {},
        })
        .then((result) => {
          let dataLogIn = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };
          this.$emit("logInSuccess", dataLogIn);
          this.$router.push({ name: "mainLayout", });
        })
        .catch((error) => {
          if (error.response.status == "401")
            alert("Verifica tus credenciales para continuar");
        });
    },
  },
};
</script>
