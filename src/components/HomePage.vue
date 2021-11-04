<template>
  <div>
    <div class="bg-img"></div>
    <div class="container">
      <nav class="nav">
        <img src="../assets/img/g-icon.svg" alt="Gestify" class="gestify-icon" />
        <button class="primary-btn custom-home-btn" v-on:click="sendToLogIn">
          <ges-icon icon="sign-in-alt" size="lg" />
          Iniciar sesión
        </button>
      </nav>
      <div class="content">
        <section class="welcome">
          <article class="welcome-text">
            <h1 class="welcome-text__title">Bienvenidos a Gestify,</h1>
            <p class="welcome-text__description">
              Consulta, Edita y añade todo lo relacionado al inventario de tu
              negocio. A través de un único sistema, Gestify.
            </p>
            <button class="primary-btn custom-home-btn" v-on:click="sendToSignUp">
              Registrarme
            </button>
          </article>
          <img
            class="welcome-img"
            src="../assets/img/img-home.svg"
            alt="user-inventory"
          />
        </section>
        <section class="modules">
          <h1 class="modules-title">Algunos de nuestros módulos</h1>
          <div class="cards-modules-container">
            <div
              v-for="module in modules"
              :key="module"
              class="ges-card ges-card--home"
            >
              <h2 class="ges-card__title">{{ module.title }}</h2>
              <p class="ges-card__text">{{ module.description }}</p>
            </div>
          </div>
        </section>
      </div>
    </div>
    <div class="footer-container">
      <footer class="footer">
        <div class="footer-content">
          <p>Todos los derechos reservados</p>
          <p>Gestify | 2021</p>
        </div>
      </footer>
    </div>
  </div>
</template>
<script>
export default {
  name: "homePage",
  data: () => {
    return {
      modules: [
        {
          title: "Proveedores",
          description:
            "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et",
        },
        {
          title: "Usuarios",
          description:
            "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et",
        },
        {
          title: "Productos",
          description:
            "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et",
        },
      ],
    };
  },
  methods: {
    sendToLogIn: function () {
      this.$router.push({ name: "logIn" });
    },
      sendToSignUp: function () {
      this.$router.push({ name: "signUp" });
    },
  },
};
</script>