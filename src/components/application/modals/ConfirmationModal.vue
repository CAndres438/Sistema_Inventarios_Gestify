<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div
        class="modal-container modal-container--delete"
        role="dialog"
        aria-labelledby="modalTitle"
        aria-describedby="modalDescription"
      >
        <header class="modal-header modal-header--delete" id="modalTitle">
          <slot name="header">Eliminar elemento</slot>
          <button
            type="button"
            class="close-btn"
            @click="close"
            aria-label="Close modal"
          >
            <ges-icon icon="times-circle" size="lg"></ges-icon>
          </button>
        </header>
        <section class="modal-body" id="modalDescription">
          <slot name="body"
            >¿Estás seguro de que deseas continuar? <br />Esta acción no se
            puede deshacer</slot
          >
          <div class="buttons-container">
            <button
              type="submit"
              class="primary-btn primary-btn--margin"
              @click="deleteItem(idItem)"
            >
              Sí, eliminar
            </button>
            <button class="cancel-btn" @click="close" type="button">
              Cancelar
            </button>
          </div>
        </section>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "ConfirmationModal",
  data: function () {
    return {
      idDeleteItem: "",
    };
  },
  props: ["idItem"],
  methods: {
    close() {
      this.$emit("close");
    },
    deleteItem() {
      this.idDeleteItem = this.idItem;
      this.$emit("delete-item", this.idDeleteItem);
      this.close()
    },
  },
};
</script>