<template>
  <nav class="navbar navbar-main navbar-expand-lg px-0 mx-4 shadow-none border-radius-xl" :class="this.$store.state.isRTL ? 'top-0 position-sticky z-index-sticky' : ''
    " v-bind="$attrs" id="navbarBlur" data-scroll="true">
    <div class="px-3 py-1 container-fluid">
      <breadcrumbs :currentPage="currentRouteName" textWhite="text-white" />
      <div class="mt-2 collapse navbar-collapse mt-sm-0 me-md-0 me-sm-4"
        :class="this.$store.state.isRTL ? 'px-0' : 'me-sm-4'" id="navbar">
        <div class="pe-md-3 d-flex align-items-center" :class="'ms-md-auto'">
        </div>
        <ul class="navbar-nav justify-content-end">
          <li class="nav-item d-flex align-items-center">
            <a @click="logout" class="px-0 nav-link font-weight-bold text-white cursor-pointer" target="_blank">
              <i class="fa fa-user" :class="'me-sm-2'"></i>
              <span class="d-sm-inline d-none">Logout</span>
            </a>
          </li>
          <li class="nav-item  ps-3 d-flex align-items-center">
            <a href="#" @click="toggleSidebar" class="p-0 nav-link text-white" id="iconNavbarSidenav">
              <div class="sidenav-toggler-inner">
                <i class="sidenav-toggler-line bg-white"></i>
                <i class="sidenav-toggler-line bg-white"></i>
                <i class="sidenav-toggler-line bg-white"></i>
              </div>
            </a>
          </li>
          <li class="px-3 nav-item d-flex align-items-center">
            <!-- <a class="p-0 nav-link text-white" @click="toggleConfigurator"> -->
              <!-- <i class="cursor-pointer fa fa-cog fixed-plugin-button-nav"></i> -->
            <!-- </a> -->
          </li>

        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
import Breadcrumbs from "../Breadcrumbs.vue";
import { mapMutations, mapActions } from "vuex";
import { API_ENDPOINT } from '@/../apiconfig.js';
import axios from "axios";
// import router from "@/router";

export default {
  name: "navbar",
  data() {
    return {
      showMenu: false,
      apiUrl: API_ENDPOINT,
    };
  },
  props: ["minNav", "textWhite"],
  created() {
    this.minNav;
  },
  methods: {
    ...mapMutations(["navbarMinimize", "toggleConfigurator", "toggleObservabilityBackupVisibility", "toggleDatabaseBackupVisibility"]),
    ...mapActions(["toggleSidebarColor", "toggleProjectSelect"]),

    // toggleSidebar() {
    //   this.toggleSidebarColor("bg-white");
    //   this.navbarMinimize();
    //   this.$store.dispatch('toggleLogo');
    //   this.toggleObservabilityBackupVisibility(); // Dispatch the mutation
    //   this.toggleDatabaseBackupVisibility(); // Dispatch the mutation
    //   this.toggleProjectSelect(); // Dispatch the toggleProjectSelect action
    //   this.$store.dispatch('toggleshowdocx');


    // },
    toggleSidebar() {
      // If dark mode is active, set the sidebar background to #111c44
      if (this.$store.state.darkMode) {
        this.toggleSidebarColor("#111c44");
      } else {
        // Otherwise, use white for the sidebar background
        this.toggleSidebarColor("bg-white");
      }
      this.navbarMinimize();
      this.$store.dispatch("toggleLogo");
      this.toggleObservabilityBackupVisibility(); // Mutation dispatch
      this.toggleDatabaseBackupVisibility(); // Mutation dispatch
      this.toggleProjectSelect(); // Dispatch the action
      this.$store.dispatch("toggleshowdocx");
    },
    logout() {
      const logoutUrl = `${this.apiUrl}/api/v1/logout/`;
      const authToken = sessionStorage.getItem('token')
      // Make an HTTP POST request to the logout endpoint
      axios
        .post(
          logoutUrl, {},
          {
            headers: {
              Authorization: `Token ${authToken}`, // Include the authentication token
            },
          }
        )
        .then(() => {
          sessionStorage.removeItem('token')
          sessionStorage.removeItem('role')
          this.$router.push('/signin');
        })
        .catch((error) => {
          // Handle logout error
          console.error("Logout error:", error.response.data);
        });
      // router.push({ name: "/" });
    },
  },
  components: {
    Breadcrumbs
  },
  computed: {
    currentRouteName() {
      return this.$route.name;
    }
  }
};
</script>