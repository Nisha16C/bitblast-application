<template>

  <main class="mt-0 main-content">

    <section>
      <div class="page-header min-vh-100">
        <div class="container">
          <div v-if="loading" class="text-center justify-content-center">
            <!-- Show loader while loading -->
            <h4 class="mb-2">
              Loading...
            </h4>
            <div class="spinner-border spinner-border-lg p-3 text-secondary" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
          </div>

          <div v-else>
            <!-- Admin User Creation Section -->
            <div v-if="!adminUserExists && !loading"
              class="mx-auto col-xl-4 col-lg-5 col-md-7 d-flex flex-column mx-lg-0">
              <div class="card card-plain">
                <div class="pb-0 card-header text-start">
                  <h4 class="font-weight-bolder">Create First Admin User
                  </h4>
                  <p class="mb-0">Username (default): {{ defaultUsername }}</p>
                </div>
                <div class="card-body">
                  <form role="form">
                    <div class="mb-3">
                      <argon-input type="email" v-model="email" placeholder="Email" name="Email" size="lg"
                        :isRequired="true" />
                    </div>
                    <div class="mb-3 password-input">
                      <argon-input v-model="adPassword" :type="showPassword ? 'text' : 'password'"
                        placeholder="Password" name="password" size="lg" @keyup.enter="createAdminUser" />
                      <span class="toggle-password" @click="togglePasswordVisibility">
                        <i class="fas fa-eye" v-if="!showPassword"></i>
                        <i class="fas fa-eye-slash" v-else></i>
                      </span>
                    </div>

                    <div class="text-center">
                      <p v-if="errorMessage" class="alert alert-danger alert-dismissible fade show custom-alert mt-3">
                        <span><strong>Error!</strong></span> {{ errorMessage }}
                      </p>
                      <p v-if="successMessage" class="alert alert-success custom-alert1 mt-3"><strong>Success!</strong>
                        {{ successMessage }}</p>
                      <argon-button v-if="showSignInButton" @click.prevent="createAdminUser" class="mt-4"
                        variant="gradient" color="success" fullWidth size="lg">Create Admin User</argon-button>
                    </div>
                  </form>
                </div>
              </div>
            </div>



            <!-- Login Section (Styled similarly as per your original code) -->
            <div class="row">
              <div v-if="adminUserExists" class="mx-auto col-xl-4 col-lg-5 col-md-7 d-flex flex-column mx-lg-0">
                <div class="card card-plain">
                  <div class="pb-0 card-header text-start">
                    <h4 class="font-weight-bolder">
                      Sign In as {{ username }}
                    </h4>
                    <p class="mb-0">Enter your Username and Password to sign in</p>
                  </div>
                  <div class="card-body">
                    <form role="form">
                      <div class="mb-3">
                        <argon-input type="text" v-model="username" placeholder="Username" name="Username" size="lg"
                          :isRequired="true" />
                        <span class="text-danger" v-if="!username && showErrorMessages">Username is required</span>
                      </div>
                      <div class="mb-3 password-input">
                        <argon-input v-model="password" :type="showPassword ? 'text' : 'password'"
                          placeholder="Password" name="password" size="lg" @keyup.enter="login" />
                        <span class="toggle-password" @click="togglePasswordVisibility">
                          <i class="fas fa-eye" v-if="!showPassword"></i>
                          <i class="fas fa-eye-slash" v-else></i>
                        </span>
                        <span class="text-danger" v-if="!password && showErrorMessages">Password is required</span>
                      </div>
                      <div class="text-center" v-if="showLoginWithLDAPButton">
                        <div v-if="error" class="text-danger">{{ error }}</div>
                        <argon-button v-if="showSignInButton" @click.prevent="login" class="mt-4" variant="gradient"
                          color="success" fullWidth size="lg">Sign In</argon-button>
                        <argon-button v-else @click.prevent="loginWithLDAP" class="mt-4" variant="gradient"
                          color="success" fullWidth size="lg">Login with Active Directory</argon-button>
                        <br><br>
                        <a v-if="showSignInButton" @click.prevent="showLDAPLogin" class="mt-2 text-success">Login with
                          Active Directory</a>
                        <a v-else @click.prevent="showSignIn" class="mt-2 text-success">Sign in</a>
                      </div>
                      <div class="text-center" v-else>
                        <div v-if="error" class="text-danger">{{ error }}</div>
                        <argon-button v-if="showSignInButton" @click.prevent="login" class="mt-4" variant="gradient"
                          color="success" fullWidth size="lg">Sign In</argon-button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
              <div
                class="top-0 my-auto text-center col-6 d-lg-flex d-none h-100 pe-0 position-absolute end-0 justify-content-center flex-column">
                <div
                  class="position-relative bg-gradient-primary h-100 m-3 px-7 border-radius-lg d-flex flex-column justify-content-center overflow-hidden"
                  style="background-image: url('@/assets/img/login.svg'); background-size: cover;">
                  <span class="mask bg-gradient-success opacity-6"></span>
                  <h4 class="mt-5 text-white font-weight-bolder position-relative">
                    "Empower Your Data Journey with BitBlast!!"
                  </h4>
                  <p class="text-white position-relative">
                    The most effortless way to manage your database.
                  </p>
                </div>
              </div>
            </div>

          </div>
        </div>

      </div>

    </section>

  </main>

</template>


<script>

import axios from 'axios';

import ArgonInput from "@/components/BB_Input.vue";

import argonButton from "@/components/BB_Button.vue";

import { API_ENDPOINT } from '@/../apiconfig.js';

const body = document.getElementsByTagName("body")[0];


export default {

  name: "signin",

  components: {

    ArgonInput,

    argonButton,

  },

  data() {

    return {
      adPassword: '',
      defaultUsername: 'admin', // default username
      defaultRole: 'Admin',
      email: '',
      errorMessage: '',
      successMessage: '',

      username: '',

      password: '',

      error: null,

      showErrorMessages: false,
      loading: false,
      apiUrl: API_ENDPOINT,
      showSignInButton: true, // Initially show the Sign in button
      showLoginWithLDAPButton: false,
      showPassword: false, // Add this property
      adminUserExists: false,


    };

  },

  created() {

    this.$store.state.hideConfigButton = true;

    this.$store.state.showNavbar = false;

    this.$store.state.showSidenav = false;

    this.$store.state.showFooter = false;

    body.classList.remove("bg-gray-100");
    this.fetchIsConnected();
    this.checkAdminUserExists();


  },

  beforeUnmount() {

    this.$store.state.hideConfigButton = false;

    this.$store.state.showNavbar = true;

    this.$store.state.showSidenav = true;

    this.$store.state.showFooter = true;

    body.classList.add("bg-gray-100");

  },

  methods: {
    createAdminUser() {
      // Reset messages
      this.errorMessage = '';
      this.successMessage = '';

      // Check password length
      if (this.adPassword.length < 6) {
        this.errorMessage = 'Password must be at least 6 characters long.';

        // Set a timeout to clear the error message after 3 seconds
        setTimeout(() => {
          this.errorMessage = '';
        }, 3000); // 3000 milliseconds = 3 seconds

        return; // Stop execution if the password is too short
      }

      // Call the first API to create admin user in your system
      fetch(`${this.apiUrl}/api/v1/create_first_admin/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: this.defaultUsername,
          password: this.adPassword,
          email: this.email,
          role: this.defaultRole
        })
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Failed to create admin user.');
          }
          return response.json();
        })
        .then(data => {
          this.successMessage = data.success;
          this.errorMessage = '';
          window.location.reload();

          // Immediately after the first API call, call the second API to create the pgAdmin user
          return fetch(`${this.apiUrl}/api/v1/create-pgadmin-user/`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              email: this.email, // Use the same email
              password: this.adPassword, // Use the same password
              is_admin: true // Set is_admin to true to create an admin user in pgAdmin
            })
          });
        })
        .then(pgAdminResponse => {
          // Check if pgAdmin response is OK but don't show any messages
          if (!pgAdminResponse.ok) {
            console.error('Failed to create pgAdmin user.');
          } else {
            console.log('pgAdmin user created successfully!');
          }
        })
        .catch(error => {
          // Show error messages for the first API only, and silence pgAdmin errors
          this.errorMessage = error.message || 'Failed to create admin user.';
          this.successMessage = '';

          // Optionally set a timeout to clear the error message after 3 seconds
          setTimeout(() => {
            this.errorMessage = '';
          }, 5000);
        });
    },

    
    checkAdminUserExists() {
      this.loading = true;
      axios.get(`${this.apiUrl}/api/v1/check-admin-user-exists/`)
        .then(response => {
          if (response && response.data) {
            this.adminUserExists = response.data.exists;
          } else {
            console.error('Invalid response:', response);
          }
        })
        .catch(error => {
          console.error('Error checking admin user:', error);
        })
        .finally(() => {
          this.loading = false;
        });
    },

    fetchIsConnected() {
      axios.get(`${this.apiUrl}/api/v1/is-connected/`)
        .then(response => {
          if (response && response.data) {
            const isConnectedValue = response.data.is_connected;
            if (isConnectedValue === "True") {
              this.showLoginWithLDAPButton = true;
            } else if (isConnectedValue === "None") {
              this.showLoginWithLDAPButton = false;
            } else {
              console.error('Unexpected value for is_connected:', isConnectedValue);
            }
          } else {
            console.error('Invalid response:', response);
          }
        })
        .catch(error => {
          console.error('Error fetching is_connected:', error);
          this.showLoginWithLDAPButton = false;
        });
    },
    // fetchUserRole() {
    //   const authToken = sessionStorage.getItem('token');
    //   if (!authToken) {
    //     console.error('User is not authenticated');
    //     return;
    //   }

    //   const headers = {
    //     'Authorization': `Token ${authToken}`,
    //     'Content-Type': 'application/json'
    //   };

    //   // Make the API request to fetch the user's role
    //   axios
    //     .get(`${this.apiUrl}/api/v1/role/`, { headers })
    //     .then(response => {
    //       if (response.data.success) {

    //         // You can handle the user's role data here as needed
    //       } else {
    //         console.error('Error fetching user role:');
    //       }
    //     })
    //     .catch(error => {
    //       console.error('Error fetching user role:', error);
    //     });
    // },

    loginWithLDAP() {
      if (!this.username || !this.password) {
        this.showErrorMessages = true;
        setTimeout(() => {
          this.showErrorMessages = false;
        }, 5000);
        return; // Do not proceed with login if fields are empty
      }

      const formData = {
        username: this.username,
        password: this.password
      };

      axios.post(`${this.apiUrl}/api/v1/ldap-login/`, formData)
        .then(response => {
          if (response && response.data) {
            // Store token, role, and username in session storage
            sessionStorage.setItem('token', response.data.token);
            sessionStorage.setItem('role', response.data.role);
            sessionStorage.setItem('username', response.data.username);

            // Redirect based on user role
            if (response.data.role === 'Admin') {
              this.$router.push('/admin-dashboard');
            } else if (response.data.role === 'Standard') {
              this.$router.push('/user-dashboard');
            }
          } else {
            console.error('Invalid response:', response);
            this.error = 'Invalid response from server';
          }
        })
        .catch(error => {
          this.error = error.response?.data?.error || 'Invalid credentials. Please check again';
          this.password = null;
          this.username = null;
          setTimeout(() => {
            this.error = null;
          }, 3000);
        });
    },

    login() {
      if (!this.username || !this.password) {
        this.showErrorMessages = true;
        setTimeout(() => {
          this.showErrorMessages = false;
        }, 5000);
        return; // Do not proceed with login if fields are empty
      }

      const formData = {
        username: this.username,
        password: this.password
      };

      axios
        .post(`${this.apiUrl}/api/v1/login/`, formData)
        .then((response) => {
          sessionStorage.setItem('token', response.data.token);
          sessionStorage.setItem('role', response.data.role);
          sessionStorage.setItem('username', response.data.user_data.username);


          // Redirect based on user role
          if (response.data.role === 'Admin') {
            this.$router.push('/admin-dashboard');
          } else if (response.data.role === 'Standard') {
            this.$router.push('/user-dashboard');
          }
        })
        .catch((error) => {
          this.error = error.response.data.error;
          this.error = "Invalid credentials. Please check again";
          this.password = null;
          this.username = null;
          setTimeout(() => {
            this.error = null;
          }, 3000);
        });
    },

    showSignIn() {
      this.showSignInButton = true; // Show the Sign in button
    },
    showLDAPLogin() {
      this.showSignInButton = false; // Hide the Sign in button
    },
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },

  },

};

</script>
<style scoped>
.password-input {
  position: relative;
}

.toggle-password {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  cursor: pointer;
}

.custom-alert {
  color: white;
  padding: 0.5rem;
  /* Reduce padding */

}

.custom-alert1 {
  color: white;
  padding: 0.5rem;
  margin-top: 5px;
  /* Reduce padding */

}
</style>