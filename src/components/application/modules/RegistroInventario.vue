<template>
  <div>
    <h1 class="form-title">Registro de productos</h1>
    <form class="global-form-container" v-on:submit.prevent="createProduct">
      <div class="register-form">
        <div class="input-container">
          <label for="code" class="input-container__label">Código</label>
          <input
            type="text"
            class="input-container__input"
            name="code"
            id="code"
            required
            v-model="product.code"
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
            v-model="product.p_name"
            maxlength="40"
          />
        </div>
        <div class="input-container">
          <label for="provider" class="input-container__label">Proveedor</label>
          <select
            class="input-container__input"
            name="provider"
            id="provider"
            required
            v-model="product.prov_name"
          >
            <option disabled>Seleccione</option>
            <option v-for="prov in providers" :key="prov">
              {{ prov.p_name }}
            </option>
          </select>
        </div>
        <div class="input-container">
          <label for="quantity" class="input-container__label">Cantidad</label>
          <input
            type="number"
            class="input-container__input"
            name="quantity"
            id="quantity"
            required
            v-model="product.quantity"
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
            v-model="product.price"
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
            v-model="product.category"
          >
            <option disabled>Seleccione</option>
            <option v-for="cat in categories" :key="cat" v-bind:value="cat.cod">
              {{ cat.name }}
            </option>
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
            v-model="product.description"
          />
        </div>
      </div>
      <button type="submit" class="primary-btn primary-btn--margin">
        Ingresar producto a inventario
      </button>
    </form>
  </div>
</template>
<script>
import axios from "axios";
import jwt_decode from "jwt-decode";

export default {
  name: "registroProducto",
  data: function () {
    return {
      product: {
        code: "",
        prov_name: "",
        p_name: "",
        quantity: "",
        movement: "Entrada",
        price: "",
        category: "",
        description: "",
      },
      categories: [],
      providers: [],
    };
  },
  methods: {
    getRemoteCategories: function () {
      axios
        .get("https://gestify-back-nodb.herokuapp.com/categories", {})
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
        .get(`https://gestify-back-nodb.herokuapp.com/user/${userId}/providers`, {
          headers: { Authorization: `Bearer ${userToken}` },
        })
        .then((result) => {
          this.providers = result.data;
        });
    },
    createProduct: function () {
      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();
      axios
        .post(
          `https://gestify-back-nodb.herokuapp.com/user/${userId}/products`,
          this.product,
          {
            headers: { Authorization: `Bearer ${userToken}` },
          }
        )
        .then((result) => {
          alert("Producto creado con éxito");
          this.clearData()
        })
        .catch((error) => {
          console.log(error);
          alert("Falló registro de producto");
        });
    },
    clearData: function () {
      this.product.code = "";
      this.product.prov_name = "";
      this.product.p_name = "";
      this.product.quantity = "";
      this.product.movement = "";
      this.product.price = "";
      this.product.category = "";
      this.product.description = "";
    },
  },
  beforeMount() {
    this.getRemoteCategories();
    this.getUserProviders();
  },
};
</script>