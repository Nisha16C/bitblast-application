export default {
    data() {
      return {
        inactivityTimeout: null,
        logoutAfter: 30 * 60 * 1000, // 1 hr in milliseconds
      };
    },  
    created() {
      this.resetInactivityTimeout();
      this.setupEventListeners();
    },
    beforeDestroy() {
      this.removeEventListeners();
      this.clearInactivityTimeout();
    },
    methods: {
      resetInactivityTimeout() {
        this.clearInactivityTimeout();
        this.inactivityTimeout = setTimeout(() => {
          this.logoutUser();
        }, this.logoutAfter);
      },
      clearInactivityTimeout() {
        if (this.inactivityTimeout) {
          clearTimeout(this.inactivityTimeout);
        }
      },
      setupEventListeners() {
        window.addEventListener("mousemove", this.resetInactivityTimeout);
        window.addEventListener("keypress", this.resetInactivityTimeout);
        window.addEventListener("click", this.resetInactivityTimeout);
      },
      removeEventListeners() {
        window.removeEventListener("mousemove", this.resetInactivityTimeout);
        window.removeEventListener("keypress", this.resetInactivityTimeout);
        window.removeEventListener("click", this.resetInactivityTimeout);
      },
      logoutUser() {
        // Clear the user session and redirect to the login page
        sessionStorage.removeItem("token");
        sessionStorage.removeItem("role");
        this.$router.push({ name: "Signin" });
      },
    },
  };
  