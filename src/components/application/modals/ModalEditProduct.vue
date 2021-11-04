<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div
        class="modal-container"
        role="dialog"
        aria-labelledby="modalTitle"
        aria-describedby="modalDescription"
      >
        <header class="modal-header" id="modalTitle">
          <slot name="header"> Editar producto No. {{ code }} </slot>
          <button
            type="button"
            class="close-btn"
            @click="close"
            aria-label="Close modal"
          >
            <ges-icon icon="times-circle" size="lg"></ges-icon>
          </button>
        </header>
        <form class="modal-form-container" v-on:submit.prevent="updateProduct">
          <div class="register-form">
            <div class="input-container">
              <label for="code" class="input-container__label">Código</label>
              <input
                type="text"
                class="input-container__input"
                name="code"
                id="code"
                required
                v-model="code"
                disabled
              />
            </div>
            <div class="input-container">
              <label for="p_name" class="input-container__label"
                >Nombre del producto</label
              >
              <input
                type="text"
                class="input-container__input"
                name="p_name"
                id="p_name"
                required
                v-model="p_name"
                maxlength="40"
              />
            </div>
            <div class="input-container">
              <label for="provider" class="input-container__label"
                >Proveedor</label
              >
              <select
                class="input-container__input"
                name="provider"
                id="provider"
                required
                v-model="prov_name"
              >
                <option disabled>Seleccione</option>
                <option v-for="prov in providers" :key="prov">
                  {{ prov.p_name }}
                </option>
              </select>
            </div>
            <div class="input-container">
              <label for="quantity" class="input-container__label"
                >Cantidad</label
              >
              <input
                type="number"
                class="input-container__input"
                name="quantity"
                id="quantity"
                required
                v-model="quantity"
              />
            </div>
            <div class="input-container">
              <label for="price" class="input-container__label"
                >Costo unitario</label
              >
              <input
                type="number"
                class="input-container__input"
                name="price"
                id="price"
                required
                v-model="price"
              />
            </div>
            <div class="input-container">
              <label for="category" class="input-contailer__label"
                >Categoría del producto</label
              >
              <select
                class="input-container__input"
                name="unit"
                id="unit"
                required
                v-model="category"
              >
                <option disabled>Seleccione</option>
                <option
                  v-for="cat in categories"
                  :key="cat"
                  v-bind:value="cat.cod"
                >
                  {{ cat.name }}
                </option>
              </select>
            </div>
            <div class="input-container">
              <label for="movement" class="input-contailer__label"
                >Movimiento</label
              >
              <select
                class="input-container__input"
                name="movementt"
                id="movement"
                required
                v-model="movement"
              >
                <option value="Entrada">Entrada</option>
                <option value="Salida">Salida</option>
              </select>
            </div>
            <div class="input-container">
              <label for="description" class="input-container__label"
                >Descripción</label
              >
              <input
                type="text"
                class="input-container__input"
                name="description"
                id="description"
                required
                v-model="description"
              />
            </div>
          </div>
          <button
            type="submit"
            class="primary-btn primary-btn--margin"
          >
            Actualizar producto
          </button>
          <button class="cancel-btn" @click="close" type="button">Cancelar</button>
        </form>
      </div>
    </div>
  </transition>
</template>

<script>
import axios from "axios";
import jwt_decode from "jwt-decode";
export default {
  name: "ModalEditProduct",
  data: function () {
    return {
      productUpdated: {
        code: "",
        p_name: "",
        prov_name: "",
        quantity: 0,
        movement: "",
        price: 0,
        category: "",
        description: "",
      },
      categories: [],
      providers: [],
    };
  },
  props: {
    code: "",
    prov_name: "",
    p_name: "",
    quantity: "",
    price: "",
    category: "",
    description: "",
  },
  methods: {
    close() {
      this.$emit("close");
    },
    getRemoteCategories: function () {
      axios
        .get("https:///categories", {})
        .then((categories) => {
          this.categories = categories.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getUserProviders: function () {
      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();
      axios
        .get(`https:///providers`, {
          headers: { Authorization: `Bearer ${userToken}` },
        })
        .then((result) => {
          this.providers = result.data;
        });
    },

    setDataProduct: function () {
      this.productUpdated.code = this.code;
      this.productUpdated.p_name = this.p_name;
      this.productUpdated.prov_name = this.prov_name;
      this.productUpdated.quantity = this.quantity;
      this.productUpdated.price = this.price;
      this.productUpdated.category = this.category;
      this.productUpdated.description = this.description;
      this.productUpdated.movement = this.movement;
    },
    updateProduct: function () {
      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();
      let productId = this.code.toString();
      this.setDataProduct();

      axios
        .put(
          `https:///user/${userId}/products/${productId}`,
          this.productUpdated,
          {
            headers: { Authorization: `Bearer ${userToken}` },
          }
        )
        .then((result) => {
          console.log(result)
          alert("Producto actualizado con éxito");
          this.$emit('close')
        })
        .catch((error) => {
          console.log(error)
          alert("Falló actualización de producto");
        });
    },
  },
  beforeMount() {
    this.getRemoteCategories();
    this.getUserProviders();
  },
};
</script>
