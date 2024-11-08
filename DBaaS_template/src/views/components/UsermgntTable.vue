<template>
  <div class="card">
    <div class="card-header pb-0">
      <div class="d-flex align-items-center justify-content-between">
        <h6 class="text-2xl">Users Info</h6>
        <div class="d-flex ms-auto">
          <div class="mb-2 me-2">
            <router-link to="/USER">
              <argon-button color="success" size="md" variant="gradient">Create New User</argon-button>
            </router-link>
          </div>
          <div class="mb-2">
            <router-link to="/ADgrouplist">
              <argon-button color="success" size="sm" variant="gradient" style="font-size: 15px;">Active
                Directory Groups</argon-button>
            </router-link>
          </div>
        </div>
      </div>

      <div class="mb-3 d-flex align-items-center">
        <select v-model="selectedFilter" :class="{ 'dark-mode': isDarkMode }" class="form-select mr-3"
          @change="filterUsers">
          <option value="all">All Users</option>
          <option value="local">Local Users</option>
          <option value="ad">AD Users</option>
        </select>
        <div class="mr-3" style="white-space: nowrap;">Search User:</div>
        <input type="text" v-model="searchQuery" class="form-control mr-3 " :class="{ 'dark-mode': isDarkMode }"
          style="width: 300px;" placeholder="Search" @input="searchUser" />
      </div>


    </div>

    <div v-if="loading" class="text-center mt-3">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div v-else class="card-body px-0 pt-0 pb-2">
      <div v-if="users.length === 0" class="text-center">No Users are Available</div>
      <div v-else class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-md font-weight-bolder opacity-7">User Name</th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">Email Address
              </th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">Created On</th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">Last Login</th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">User Status
              </th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">User Password
              </th>

              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">User Role</th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">Change Role
              </th>

            </tr>
          </thead>
          <tbody>
            <tr v-for="user in filteredUsers" :key="user.id">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <img :src="!user.email ? require('@/assets/img/ADuser.png') : (isDarkMode ? logoWhite : logo)"
                      class="avatar avatar-sm me-3" :alt="`user-avatar-${user.id}`" />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <p class="text-md text-secondary mb-0">{{ user.username }}</p>
                  </div>
                </div>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ user.email ? user.email : 'No Email' }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ formatDate(user.date_joined) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ formatDate(user.last_login) }}</span>
              </td>
              <td class="align-middle text-center">
                <div class="d-flex align-items-center justify-content-center">
                  <span :class="user.is_active ? 'text-success' : 'text-danger'" class="me-2">
                    {{ user.is_active ? 'Active' : 'Inactive' }}
                  </span>
                  <div class="dropdown">
                    <button class="btn btn-link p-0 text-large" type="button" id="dropdownMenuButton"
                      data-bs-toggle="dropdown" aria-expanded="false">
                      <i :class="user.is_active ? 'text-success' : 'text-danger'">
                        <i class="fa fa-caret-down"></i>
                      </i>
                    </button>
                    <ul :class="{ 'dropdown-menu-dark': isDarkMode }" class="dropdown-menu"
                      aria-labelledby="dropdownMenuButton">
                      <li>
                        <a class="dropdown-item" href="#" @click.prevent="toggleUserStatus(user)">
                          <span v-if="isLoading">
                            <i class="fas fa-spinner fa-spin"></i> <!-- Loading spinner -->
                          </span>
                          <span v-else>
                            {{ user.is_active ? 'Inactive' : 'Active' }}
                          </span>
                        </a>
                      </li>
                    </ul>

                  </div>
                </div>
              </td>

              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold reset-span"
                  :class="{ 'text-muted': !user.email, 'disabled-reset': !user.email }"
                  @click="user.email ? resetPasswordModal(user) : null"
                  :style="!user.email ? { cursor: 'not-allowed' } : {}">
                  Reset
                  <span v-if="!user.email" class="tooltip-text">
                    You cannot change the password of AD users. Please contact the AD server.
                  </span>
                </span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ user.role ? user.role : 'No Role' }}</span>
              </td>
              <td class="align-middle text-center">
                <argon-button color="success" size="md" variant="gradient" @click="prepareAssignRoles(user)"
                  type="button" class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
                  Changes Roles
                </argon-button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <div class="modal fade" ref="myModal" id="exampleModal" tabindex="-1" role="dialog"
    aria-labelledby="exampleModalLabel" aria-hidden="true" :class="{ 'show': isModalVisible }">
    <div class="modal-dialog" role="document">
      <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
        <div class="modal-header">
          <h2 class="modal-title" id="exampleModalLabel">Select Role</h2>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"
            :class="{ 'close-dark': this.$store.state.darkMode }">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="form-check" v-for="role in roles" :key="role.name">
            <input v-model="selectedRole" :class="{ 'dark-mode': isDarkMode }" class="form-check-input" type="radio"
              :value="role.name" :id="'roleRadio_' + role.name">
            <label class="form-check-label" :for="'roleRadio_' + role.name">{{ role.name }}</label>
          </div>
        </div>
        <div class="modal-footer">
          <argon-button color="secondary" size="md" variant="gradient" @click="isModalVisible = false" type="button"
            class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
            Cancel
          </argon-button>
          <argon-button color="success" size="md" variant="gradient" @click.prevent="assignRoles" type="button"
            class="ml-4 btn btn-success" data-toggle="modal" data-target="#exampleModal">
            Assign Role
          </argon-button>
        </div>
      </div>
    </div>
  </div>

  <!-- reset user password Modal -->
  <div v-if="isResetPasswordModalVisible" class="modal fade show" tabindex="-1" role="dialog"
    aria-labelledby="resetPasswordModalLabel" aria-hidden="true" style="display: block;">
    <div class="modal-dialog" role="document">
      <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
        <div class="modal-header">
          <h5 class="modal-title" id="resetPasswordModalLabel">Reset Password of this user <b>{{ selectedUser.username
              }}</b> ?</h5>
          <button type="button" class="close" @click="closeResetPasswordModal" aria-label="Close"
            :class="{ 'close-dark': this.$store.state.darkMode }">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <h6>New Password</h6>
          <input v-model="newPassword" type="password" class="form-control" placeholder="Enter new password"
            :class="{ 'dark-mode': isDarkMode }">
          <h6>Confirm Password</h6>
          <input v-model="confirmPassword" type="password" class="form-control" placeholder="Confirm new password"
            :class="{ 'dark-mode': isDarkMode }">
          <div v-if="passwordMismatchError" class="alert alert-danger alert-dismissible fade show custom-alert mt-2">
            <strong>Error!</strong> Passwords do not match.
          </div>
          <div v-if="emptyFieldsError" class="alert alert-danger alert-dismissible fade show custom-alert mt-2">
            <strong>Error!</strong> Please fill both password fields.
          </div>

          <div v-if="errorMessage" class="alert alert-danger alert-dismissible fade show custom-alert mt-2">
            <strong>Error!</strong> {{ errorMessage }}
          </div> <!-- Error message from server -->
          <div v-if="successMessage" class="alert alert-success alert-dismissible fade show custom-alert mt-2">
            <strong>Success!</strong> {{ successMessage }}
          </div> <!-- Success message -->
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="closeResetPasswordModal">Close</button>
          <button @click="confirmResetPassword" type="button" class="btn btn-danger">Change</button>
        </div>
      </div>
    </div>
  </div>


</template>

<script>
import axios from "axios";
import ArgonButton from "@/components/BB_Button.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';
import logo from "@/assets/img/userTable.png";
import logoWhite from "@/assets/img/user.png";

export default {
  name: "users-table",
  components: {
    ArgonButton,
  },
  data() {
    return {
      searchQuery: "",
      selectedFilter: "all",
      apiUrl: API_ENDPOINT,
      users: [],
      isModalVisible: false,
      roles: [
        { id: 1, name: 'Admin' },
        { id: 2, name: 'Standard' },
        // Add more roles as needed
      ],
      selectedRole: '',
      selectedUser: null,
      loading: true,
      logo,
      logoWhite,
      isResetPasswordModalVisible: false,
      newPassword: '',
      errorMessage: '',  // Add this to store error messages
      confirmPassword: '',
      passwordMismatchError: false, // For real-time password mismatch error
      emptyFieldsError: false,// For real-time empty fields error
      successMessage: '', // For success message
      isLoading: false,



    };
  },
  mounted() {
    this.fetchUsers();
  },
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
    filteredUsers() {
      let filtered = [];

      // Filter users based on the selected filter
      if (this.selectedFilter === "local") {
        // Show users with an email address
        filtered = this.users.filter(user => user.email);
      } else if (this.selectedFilter === "ad") {
        // Show users without an email address
        filtered = this.users.filter(user => !user.email);
      } else {
        // Show all users
        filtered = this.users;
      }

      // Apply search query if provided
      if (this.searchQuery) {
        filtered = filtered.filter(user =>
          user.username.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }

      return filtered;
    }
  },
  watch: {
    newPassword() {
      this.validatePasswords();
    },
    confirmPassword() {
      this.validatePasswords();
    }
  },
  methods: {
    async toggleUserStatus(user) {
      const authToken = sessionStorage.getItem('token');

      if (!authToken) {
        throw new Error('Token not found in session storage');
      }

      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json'
      };

      this.isLoading = true; // Start loader

      try {
        // Toggle status for the application's user
        const appResponse = await axios.patch(`${this.apiUrl}/api/v1/users/${user.username}/toggle-status/`, {}, { headers });
        console.log('App User Status Toggled:', appResponse.data);

        // Fetch the updated list of users
        this.fetchUsers();

        // Handle pgAdmin user status based on the app's status
        let pgAdminIsActive = user.is_active ? false : true; // Logic for pgAdmin user status

        // Make the API call to update pgAdmin user status
        const pgAdminResponse = await axios.post(
          `${this.apiUrl}/api/v1/update-user-status/`,
          {
            email: user.email,
            is_active: pgAdminIsActive
          },
          { headers }
        );
        console.log('PgAdmin User Status Updated:', pgAdminResponse.data);

      } catch (error) {
        console.error('Error toggling user status:', error);
        // Handle error case
      } finally {
        this.isLoading = false; // Stop loader
      }
    },

    async fetchUsers() {
      try {
        const authToken = sessionStorage.getItem('token');

        if (!authToken) {
          throw new Error('Token not found in session storage');
        }

        const headers = {
          'Authorization': `Token ${authToken}`,
          'Content-Type': 'application/json'
        };

        // Fetch AD users data
        const adUsersResponse = await axios.get(`${this.apiUrl}/api/v1/save-ad-users/`, { headers });
        const adUsers = adUsersResponse.data.users;

        // Fetch all users data
        const usersResponse = await axios.get(`${this.apiUrl}/api/v1/users/`, { headers });
        const allUsers = usersResponse.data;

        // Subtract AD users from all users
        const localUsers = allUsers.filter(user => !adUsers.some(adUser => adUser.username === user.username));


        // Assign the filtered users to the component data
        this.users = localUsers;

        this.loading = false;
      } catch (error) {
        console.error('Error fetching users:', error);
        this.loading = false;
      }
    },


    searchUser() {
      this.filterUsers();
    },

    filterUsers() {
      // Simply call the filteredUsers computed property to update the list
      this.filteredUsers;
    },

    formatDate(dateString) {
      if (!dateString) {
        return '---'; // Return placeholder if dateString is null or empty
      }

      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('en-US', options);
    },


    async prepareAssignRoles(user) {
      this.selectedUser = user;
      await this.fetchUserRoles(user.username);  // Pass the username here
      this.isModalVisible = true;
    },

    async fetchUserRoles(username) {
      try {
        const authToken = sessionStorage.getItem('token');

        if (!authToken) {
          throw new Error('Token not found in session storage');
        }

        const headers = {
          'Authorization': `Token ${authToken}`,
          'Content-Type': 'application/json'
        };

        const response = await axios.get(`${this.apiUrl}/api/v1/users/${username}/user-role/`, { headers });
        if (response.data && response.data.role) {
          this.selectedRole = response.data.role;
        } else {
          console.error('Failed to fetch user roles:', response.data.error);
        }
      } catch (error) {
        console.error('Error fetching user roles:', error);
      }
    },

    async assignRoles() {
      try {
        if (!this.selectedUser || !this.selectedRole) {
          console.error('No user or role selected.');
          return;
        }

        const authToken = sessionStorage.getItem('token');
        if (!authToken) {
          console.error('Token not found in session storage');
          return;
        }

        const headers = {
          'Authorization': `Token ${authToken}`,
          'Content-Type': 'application/json'
        };

        const data = {
          role: this.selectedRole
        };

        const response = await axios.post(`${this.apiUrl}/api/v1/users/${this.selectedUser.username}/assign-role/`, data, { headers });

        if (response.data.message) {
          // console.log(response.data.message);
        }

        this.isModalVisible = false;
        await this.fetchUsers(); // Refresh the users list after assigning roles
      } catch (error) {
        console.error('Error assigning roles:', error);
      }
    },

    resetPasswordModal(user) {
      this.selectedUser = user;
      this.isResetPasswordModalVisible = true;
    },

    closeResetPasswordModal() {
      this.isResetPasswordModalVisible = false;
      this.selectedUser = null;
      this.newPassword = '';
      this.errorMessage = ''; // Clear error message when closing the modal
      this.confirmPassword = '';  // Reset confirmPassword when opening the modal
      this.passwordMismatchError = false; // Reset real-time password mismatch error
      this.emptyFieldsError = false; // Reset real-time empty fields error
      this.successMessage = '';

    },

    async confirmResetPassword() {
      // Reset error and success messages
      this.errorMessage = '';
      this.successMessage = '';
      this.emptyFieldsError = false; // Reset empty fields error
      this.passwordMismatchError = false; // Reset password mismatch error

      // Validate passwords
      this.validatePasswords();

      // Check if fields are empty
      if (!this.newPassword || !this.confirmPassword) {
        this.emptyFieldsError = true;
        return; // Do not proceed if there are validation errors
      }
      // Validate password length
      if (this.newPassword.length < 6 || this.confirmPassword.length < 6) {
        this.errorMessage = 'Password must be at least 6 characters long.';

        // Automatically hide the error message after 5 seconds
        setTimeout(() => {
          this.errorMessage = '';
        }, 5000); // 5000 milliseconds = 5 seconds

        return; // Do not proceed if the password is too short
      }

      if (this.emptyFieldsError || this.passwordMismatchError) {
        return; // Do not proceed if there are validation errors
      }

      try {
        const authToken = sessionStorage.getItem('token');
        if (!authToken) {
          throw new Error('Token not found in session storage');
        }

        const headers = {
          'Authorization': `Token ${authToken}`,
          'Content-Type': 'application/json'
        };

        // Check if the user is an AD user
        const adUsersResponse = await axios.get(`${this.apiUrl}/api/v1/save-ad-users/`, { headers });
        const adUsers = adUsersResponse.data.users; // Access the users array

        if (Array.isArray(adUsers)) {
          const isADUser = adUsers.some(user => user.sAMAccountName === this.selectedUser.username);

          if (isADUser) {
            this.errorMessage = `You cannot change the password for AD user ${this.selectedUser.username}.`;
            return;
          }
        } else {
          console.error('Unexpected format for AD users:', adUsers);
          return;
        }

        // Proceed with password reset if not an AD user
        const data = { new_password: this.newPassword };
        const response = await axios.post(`${this.apiUrl}/api/v1/reset-password/${this.selectedUser.username}/`, data, { headers });

        if (response.data && response.data.message) {
          // Show success message
          this.successMessage = 'Password has been successfully changed.';

          // Ensure modal closes after showing the success message
          setTimeout(() => {
            this.closeResetPasswordModal();
            this.fetchUsers(); // Refresh the users list after password reset
          }, 3000); // Show success message for 3 seconds

          // Trigger pgAdmin user password update in the background
          this.updatePgAdminPassword(this.selectedUser.email, this.newPassword);

        } else {
          console.error('Error resetting password: No success message found');
        }
      } catch (error) {
        console.error('Error resetting password:', error.response ? error.response.data : error.message);
        this.errorMessage = 'An error occurred while resetting the password.';
      }
    },

    // Method to update pgAdmin user password in the background
    async updatePgAdminPassword(email, newPassword) {
      try {
        const authToken = sessionStorage.getItem('token');
        if (!authToken) {
          throw new Error('Token not found in session storage');
        }

        const headers = {
          'Authorization': `Token ${authToken}`,
          'Content-Type': 'application/json'
        };

        // Send a request to the update-user-status API for pgAdmin
        await axios.post(
          `${this.apiUrl}/api/v1/update-user-status/`,
          {
            email: email,
            password: newPassword // Pass the new password for pgAdmin user
          },
          { headers }
        );
        // This is in the background, so no UI message is required
      } catch (error) {
        console.error('Error updating pgAdmin password:', error.response ? error.response.data : error.message);
        // No need to display this error to the user, just log it
      }
    },




    validatePasswords() {
      this.passwordMismatchError = false;
      this.emptyFieldsError = false;

      if (!this.newPassword || !this.confirmPassword) {
        this.emptyFieldsError = true;
      } else if (this.newPassword !== this.confirmPassword) {
        this.passwordMismatchError = true;
      }
    },
  }
};
</script>


<style scoped>
.dark-mode {
  background-color: #111c44;
  color: #ffffff;
}

select.form-select {
  width: 150px;
  font-size: 14px;
  padding: 8px;
  border-radius: 9px;
}

.text-large {
  font-size: 1rem;

  /* Adjust this value as needed */
}

.reset-span {
  cursor: pointer;
  /* Changes cursor to pointer on hover */
  transition: color 0.3s ease;
  /* Smooth color transition */
}

.reset-span {
  cursor: pointer;
  /* Changes cursor to pointer on hover */
  transition: color 0.3s ease;
  /* Smooth color transition */
  color: #6c757d;
  /* Default color */
}

.reset-span:hover {
  color: #00ff88 !important;
  /* Change to your preferred hover color */
  text-decoration: underline;
  /* Optional: underline text on hover */
}

.custom-alert {
  color: white;
  padding: 0.5rem;
  /* Reduce padding */

}

.disabled-reset {
  position: relative;
  color: red;
  /* Ensure the disabled "Reset" button text is red */
}

.disabled-reset .tooltip-text {
  visibility: hidden;
  width: 350px;
  /* Adjust the width for better display */
  background-color: #333;
  /* Darker background for better readability */
  color: #fff;
  text-align: center;
  border-radius: 4px;
  padding: 5px;
  position: absolute;
  z-index: 1;
  bottom: 100%;
  /* Position the tooltip above the button */
  left: 50%;
  transform: translateX(-50%);
  /* Center the tooltip */
  opacity: 0;
  transition: opacity 0.3s;
  white-space: normal;
  /* Ensure the tooltip text wraps properly */
}

.disabled-reset .tooltip-text::after {
  content: '';
  position: absolute;
  top: 100%;
  /* Arrow pointing downwards */
  left: 50%;
  transform: translateX(-50%);
  border-width: 5px;
  border-style: solid;
  border-color: #333 transparent transparent transparent;
  /* Match tooltip background */
}

.disabled-reset:hover .tooltip-text {
  visibility: visible;
  opacity: 1;
}

.close-dark {
  color: white !important;
}
</style>