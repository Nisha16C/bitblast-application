<template>
  <main>
    <div class="container-fluid py-8">
      <div class="page-header min-height-100 " style="
            margin-right: -54%;
            margin-left: -34%;
          ">
        <!-- <span class="mask bg-gradient-success opacity-6"></span> -->
      </div>
      <div class="card shadow-lg mt-n6  w-full">
        <div class="card-body p-0 ">
          <!-- Overlay Text "Activity Logs" -->
          <!-- <div class=" bg-white text-center p-3" :class="{ 'dark-overlay': isDarkMode }">
            <h2 class="mb-0">Activity Logs</h2>
          </div> -->
          <div class="card-header pb-0 ">
          <h3 class="mb-3 ml-2 ">Activity Logs</h3></div>
          <div class="row gx-4">
            <iframe class="min-vh-100" width="46%" height="20%" :src="embedUrl2" frameborder="0"
              allowfullscreen></iframe>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
import setNavPills from "@/assets/js/nav-pills.js";
import setTooltip from "@/assets/js/tooltip.js";
const body = document.getElementsByTagName("body")[0];
export default {
  name: "profile",
  data() {
    return {
      showMenu: false,
      embedUrl: {
        light: 'http://172.16.1.190:3000/d/a13b79ff-237d-4f2c-897b-60e721e7b2b7/login-activities?orgId=1&from=now-2d&to=now&theme=light&kiosk=1',
        dark: 'http://172.16.1.190:3000/d/a13b79ff-237d-4f2c-897b-60e721e7b2b7/login-activities?orgId=1&from=now-2d&to=now&theme=dark&kiosk=1'
      }
    };
  },
  components: {
  },
  mounted() {
    this.$store.state.isAbsolute = true;
    setNavPills();
    setTooltip();
  },
  beforeMount() {
    this.$store.state.imageLayout = "profile-overview";
    this.$store.state.showNavbar = true;
    this.$store.state.showFooter = true;
    // this.$store.state.hideConfigButton = true;
    body.classList.add("profile-overview");
  },
  beforeUnmount() {
    this.$store.state.isAbsolute = false;
    this.$store.state.imageLayout = "default";
    this.$store.state.showNavbar = true;
    this.$store.state.showFooter = true;
    this.$store.state.hideConfigButton = false;
    body.classList.remove("profile-overview");
  },
  computed: {
    // Compute dark mode state
    isDarkMode() {
      return this.$store.state.darkMode;
    },
    embedUrl2() {
      return this.isDarkMode ? this.embedUrl.dark : this.embedUrl.light;
    },
  }
};
</script>
<style scoped>
.overlay-text {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  text-align: center;
  background-color: white;
  z-index: 2;
}


/* Conditional styling for dark mode */
.dark-overlay {
  position: absolute;
  top: 0%;
  left: 0%;
  /* right: 0%; */
  width: 100%;
  height: 12%;
  /* transform: translateX(-50%); */
  text-align: center;
  color: white;
  /* Change the text color if needed */
  background-color: rgb(15, 15, 15);
  /* Set white background color */
  padding: 10px;
  /* Optional: Add padding for better visual appearance */
  border-radius: 8px;
  /* Optional: Add rounded corners for a softer look */
  z-index: 2;
  /* Ensures the text appears on top of other elements */
}
.card-header {

display: flex;

align-items: center;

}

/* .card-header .button-container {

margin-left: auto;

} */
</style>
