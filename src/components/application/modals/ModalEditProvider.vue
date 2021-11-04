<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div
        class="modal-container modal-container--provider"
        role="dialog"
        aria-labelledby="modalTitle"
        aria-describedby="modalDescription"
      >
        <header class="modal-header" id="modalTitle">
          <slot name="header"> Editar proveedor {{ p_name }} </slot>
          <button
            type="button"
            class="close-btn"
            @click="close"
            aria-label="Close modal"
          >
            <ges-icon icon="times-circle" size="lg"></ges-icon>
          </button>
        </header>
        <form class="modal-form-container" v-on:submit.prevent="updateProvider">
          <div class="register-form edit-form">
            <div class="input-container">
              <label for="name" class="input-container__label">Nombre</label>
              <input
                type="text"
                class="input-container__input"
                name="name"
                id="name"
                required
                v-model="p_name"
                disabled
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
                v-model="p_telephone"
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
                v-model="p_email"
              />
            </div>
          </div>
          <div class="buttons-container">
            <button class="primary-btn primary-btn--margin" type="submit">
              Actualizar proveedor
            </button>
            <button class="cancel-btn" v-on:click="close" type="button">
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>
  </transition>
</template>

<script>
import axios from "axios";
import jwt_decode from "jwt-decode";
export default {
  name: "ModalEditProvider",
  data: function () {
    return {
      providerUpdated: {
        p_name: "",
        p_telephone: "",
        p_email: "",
      },
    };
  },
  props: {
    p_name: "",
    p_telephone: "",
    p_email: "",
  },
  methods: {
    close() {
      this.$emit("close");
    },

        getUserProviders: function () {
      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();
      axios
        .get(`https://gestify-back-nodb.herokuapp.com/user/${userId}/providers`, {
          headers: { Authorization: `Bearer ${userToken}` },
        })
        .then((result) => {
          this.userProviders = result.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    setDataProduct: function () {
      this.providerUpdated.p_name = this.p_name;
      this.providerUpdated.p_telephone = this.p_telephone;
      this.providerUpdated.p_email = this.p_email;
    },
    updateProvider: function () {
      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();
      let providerId = this.p_name;
      this.setDataProduct();
      axios
        .put(
          `https://gestify-back-nodb.herokuapp.com/user/${userId}/providers/${providerId}`,
          this.providerUpdated,
          {
            headers: { Authorization: `Bearer ${userToken}` },
          }
        )
        .then((result) => {
          alert("Proveedor editado con éxito");
          this.$emit('close');
        })
        .catch((error) => {
          console.log(error);
          alert("Falló edición de proveedor");
        });
    },
  },
};
</script>