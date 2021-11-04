<template>
  <div>
    <h1>Consulta de Productos</h1>
    <!-- <form action="" class="search-form">
      <div class="flex">
        <div class="input-container input-container--search">
          <label for="search" class="input-container__label">Buscar</label>
          <input
            type="text"
            class="input-container__input"
            name="search"
            id="search"
            required
            v-model="filterProductsInput"
          />
          <small>Puedes buscar por código o nombre del producto</small>
        </div>
        <button v-on:click="filterProducts" class="primary-btn primary-btn--search">Filtrar</button>
      </div>
    </form> -->
    <div class="scroll-table">
      <table class="table">
        <thead>
          <tr class="table__header">
            <th class="table__header-item">Código</th>
            <th class="table__header-item">Nombre</th>
            <th class="table__header-item">Stock</th>
            <th class="table__header-item">Proveedor</th>
            <th class="table__header-item">Categoría</th>
            <th class="table__header-item">Costo unitario</th>
            <th class="table__header-item">Acciones</th>
          </tr>
        </thead>
        <tbody class="table__body">
          <tr v-for="(product, index) in userProducts" :key="index">
            <td class="table__body-item">{{ product.code }}</td>
            <td class="table__body-item">{{ product.p_name }}</td>
            <td class="table__body-item">{{ product.quantity }}</td>
            <td class="table__body-item">{{ product.prov_name }}</td>
            <td class="table__body-item">{{ product.category }}</td>
            <td class="table__body-item">$ {{ product.price }}</td>
            <td class="table__body-item">
              <button class="edit-btn" @click="openEditModal(index)">
                <ges-icon icon="edit" size="lg"></ges-icon>
              </button>
              <button
                type="button"
                class="close-btn"
                @click="openConfirmationModal(index)"
              >
                <ges-icon size="lg" icon="trash-alt"></ges-icon>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <ModalEditProduct
      v-show="isModalVisible"
      @close="closeModal"
      v-bind="editProduct"
    >
    </ModalEditProduct>
    <ConfirmationModal
      v-show="isConfirmationModalVisible"
      @close="closeConfirmationModal"
      @delete-item="deleteProduct"
      :idItem="deleteProductId"
    ></ConfirmationModal>
  </div>
</template>
<script>
import axios from "axios";
import jwt_decode from "jwt-decode";
import ModalEditProduct from "../modals/ModalEditProduct.vue";
import ConfirmationModal from "../modals/ConfirmationModal.vue";

export default {
  name: "consultaProductos",
  components: {
    ModalEditProduct,
    ConfirmationModal,
  },
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
      userProducts: [],
      editProduct: {},
      isModalVisible: false,
      filterProductsInput: "",
      isConfirmationModalVisible: false,
      deleteProductId: {},
    };
  },
  methods: {
    getUserProducts: function () {
      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();
      axios
        .get(`https:///user/${userId}/products`, {
          headers: { Authorization: `Bearer ${userToken}` },
        })
        .then((result) => {
          this.userProducts = result.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    openEditModal(productId) {
      this.isModalVisible = true;
      this.editProduct = this.userProducts[productId];
    },
    closeModal() {
      this.isModalVisible = false;
      this.getUserProducts()
    },

    closeConfirmationModal() {
      this.isConfirmationModalVisible = false;
    },

    openConfirmationModal(productId) {
      this.isConfirmationModalVisible = true;
      this.deleteProductId = productId;
    },

    deleteProduct(productCodeDelete) {
      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();
      let productId = this.userProducts[productCodeDelete].code;
      axios
        .delete(
          `https:///user/${userId}/products/${productId}`,
          {
            headers: { Authorization: `Bearer ${userToken}` },
          }
        )
        .then((result) => {
          alert("Producto eliminado con éxito");
          this.getUserProducts();
          this.closeModal();
        })
        .catch((error) => {
          console.log(error);
          alert("Falló eliminación de producto");
        });
    },
  },
  beforeMount() {
    this.getUserProducts();
  },
};
</script>
