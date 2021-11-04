<template>
  <div>
    <h1 class="form-title">Registro Proveedores</h1>
    <form class="global-form-container" v-on:submit.prevent="createProvider">
      <div class="register-form">
        <div class="input-container">
          <label for="name" class="input-container__label">Nombre</label>
          <input
            type="text"
            class="input-container__input"
            name="name"
            id="name"
            required
            v-model="provider.p_name"
          />
        </div>
        <div class="input-container">
          <label for="contactNumber" class="input-container__label"
            >Número de contacto</label
          >
          <input
            type="text"
            class="input-container__input"
            name="contactNumber"
            id="contactNumber"
            required
            v-model="provider.p_telephone"
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
            required
            v-model="provider.p_email"
          />
        </div>
      </div>
      <button class="primary-btn primary-btn--margin" type="submit">
        Registrar proveedor
      </button>
    </form>
  </div>
</template>
<script>
import axios from "axios";
import jwt_decode from "jwt-decode";
export default {
  name: "registroProveedores",
  data: function () {
    return {
      provider: {
        p_name: "",
        p_telephone: "",
        p_email: "",
      },
    };
  },
  methods: {
    createProvider: function () {
      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();

      axios.post(`https:///user/${userId}/providers`, this.provider, {
        headers: { Authorization: `Bearer ${userToken}` },
      }).then((result) => {
        alert("Proveedor creado con éxito")
        this.clearData()
      }).catch((error) => {
        console.log(error);
        alert("Falló creación de proveedor")
      });
    },

    clearData: function () {
      this.provider.p_name = "";
      this.provider.p_telephone = "";
      this.provider.p_email = "";
    }

  },
};
</script>
