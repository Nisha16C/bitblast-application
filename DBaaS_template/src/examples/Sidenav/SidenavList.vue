<template>
  <div class="collapse navbar-collapse w-auto h-auto h-100" id="sidenav-collapse-main " style="margin-top:49px;">
    <hr style="margin: 0; padding: 0; border: none;">
    <ul class="navbar-nav">
      <li class="text-green" v-if="!isAdmin && !$store.state.hideProjectSelect"
        :style="{ backgroundColor: isDarkMode ? '#111c44' : '#e0f7fa' }">
        <router-link to="/Project-Select" class="nav-link ">
          <span class="nav-link-text text-center" :class="'ms-1'">
            {{ project_name ? project_name : ' SELECT PROJECT' }}
          </span>
        </router-link>
        <hr style="margin: 0; padding: 0; border: none;">
      </li>
      <li class="nav-item mt-3" v-if="isAdmin">
        <sidenav-item url="/admin-dashboard" :class="getRoute() === 'admin-dashboard' ? 'active' : ''"
          :navText="'Admin Dashboard'">
          <template v-slot:icon>
            <i class="ni ni-tv-2 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item mt-3" v-else>
        <sidenav-item url="/User-dashboard" :class="getRoute() === 'User-dashboard' ? 'active' : ''"
          :navText="'Overview'">
          <template v-slot:icon>
            <i class="ni ni-tv-2 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-if="isAdmin">
        <sidenav-item url="/Clusters-Management" :class="getRoute() === 'Clusters' ? 'active' : ''"
          :navText="'Cluster Management'">
          <template v-slot:icon>
            <!-- <i class="ni ni-umbrella-13 text-info text-sm opacity-10"></i> -->
            <i class="fa fa-database text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item url="/Clusters" :class="getRoute() === 'Clusters' ? 'active' : ''" :navText="'Clusters '">
          <template v-slot:icon>
            <i class="fa fa-database text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-if="isAdmin">
        <sidenav-item url="/Project-Management" :class="getRoute() === 'Projects' ? 'active' : ''"
          :navText="'Project Management'">
          <template v-slot:icon>
            <i class="far fa-folder text-info text-sm opacity-10"></i> </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item url="/Projects" :class="getRoute() === 'Projects' ? 'active' : ''" :navText="'Projects '">
          <template v-slot:icon>
            <i class="far fa-folder text-info text-sm opacity-10"></i> </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-if="isAdmin">
        <sidenav-item url="/manage-provider" :class="getRoute() === 'Provider Management' ? 'active' : ''"
          :navText="'Provider Management'">
          <template v-slot:icon>
            <i class="fa fa-cogs text-info text-sm opacity-10"></i> </template>
        </sidenav-item>
      </li>
      <li class="nav-item shift-right" v-if="isAdmin">
        <a href="#" @click="toggleDropdown('user-management')" class="nav-link">
          <i class="fa fa-users text-info text-sm opacity-10"></i>
          <span class="nav-link-text text-center fs-6" style="margin-right: 10px;">User Management</span>
          <i class="fa fa-angle-down"></i>
        </a>
        <ul v-show="isOpen('user-management')" class="sub-nav">
          <li>
            <router-link to="/User-Management" class="nav-link">
              <i class="fa fa-user-plus" style="color: #3f775e; font-size: 13px"></i>
              <!-- SVG icon for User Creation -->
              <span class="nav-link-text text-center">User Creation</span>
            </router-link>
          </li>
          <li>
            <router-link to="/ADauthprovider" @click="redirectToADSave" class="nav-link">
              <!-- <router-link to="/ADauthprovider" class="nav-link"> -->
              <!-- <i class="fa fa-lock"></i>  -->
              <i> <!-- Start of SVG icon -->
                <svg height="15px" width="15px" viewBox="0 0 502.664 502.664" fill="#3f775e">
                  <path style="fill:#3f775e;"
                    d="M132.099,230.872c55.394,0,100.088-44.759,100.088-99.937c0-55.243-44.673-99.981-100.088-99.981c-55.135,0-99.808,44.738-99.808,99.981C32.291,186.091,76.965,230.872,132.099,230.872z">
                  </path>
                  <path style="fill:#3f775e;"
                    d="M212.3,247.136H52.072C23.469,247.136,0,273.431,0,305.636v160.896c0,1.769,0.841,3.387,1.014,5.177h262.387c0.108-1.79,0.949-3.408,0.949-5.177V305.636C264.35,273.431,240.967,247.136,212.3,247.136z">
                  </path>
                  <path style="fill:#3f775e;"
                    d="M502.664,137.751c-0.108-58.673-53.711-105.934-119.33-105.783c-65.92,0.108-119.092,47.758-119.006,106.279c0.108,46.226,33.478,85.334,79.812,99.722l0.626,202.55l38.676,27.826l40.208-28.064l-0.065-26.877h-18.572l-0.086-26.338h18.616l-0.173-29.121h-18.486l-0.086-26.295h18.572l-0.086-26.316h-18.551l-0.065-26.316l18.637-0.022l-0.302-41.157C469.402,223.279,502.664,184.02,502.664,137.751z M383.399,77.612c14.776,0,26.899,12.101,26.899,26.856c0.108,14.949-12.015,27.007-26.834,27.007c-14.905,0-26.942-11.886-26.942-26.877C356.436,89.778,368.494,77.655,383.399,77.612z">
                  </path>
                </svg> <!-- End of SVG icon -->
              </i>
              <span class="nav-link-text text-center">Auth Providers</span>
            </router-link>
          </li>
        </ul>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item url="/Provider" :class="getRoute() === 'Provider' ? 'active' : ''" :navText="'Provider'">
          <template v-slot:icon>
            <i class="fa fa-cogs text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="mt-3 nav-item" v-if="isAdmin" v-show="observabilityBackupVisible">
        <h6 class="text-xl ps-1  text-uppercase font-weight-bolder opacity-6 "
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'">
          Observability & Backup
        </h6>
      </li>
      <li class="mt-3 nav-item" v-else v-show="databaseBackupVisible">
        <h6 class="text-xl ps-3 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'">
          Database Backup
        </h6>
      </li>
      <li class="nav-item" v-if="isAdmin">
        <sidenav-item url="/admin-monitoring" :class="getRoute() === 'admin-monitoring' ? 'active' : ''"
          :navText="'Monitoring'">
          <template v-slot:icon>
            <i class="ni ni-single-02 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item url="/user-monitoring" :class="getRoute() === 'admin-monitoring' ? 'active' : ''"
          :navText="'Monitoring'">
          <template v-slot:icon>
            <i class="ni ni-single-02 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-if="isAdmin">
        <!-- <sidenav-item url="/mount-backup-method" :class="getRoute() === 'mount-backup-method' ? 'active' : ''"
          :navText="'Backup & Restore'">
          <template v-slot:icon>
            <i class="ni ni-money-coins text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item> -->
      </li>
      <li class="nav-item" v-else>
        <sidenav-item url="/mount-backup-method" :class="getRoute() === 'mount-backup-method' ? 'active' : ''"
          :navText="'Backup & Restore'">
          <template v-slot:icon>
            <i class="ni ni-money-coins text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-if="isAdmin">
        <sidenav-item url="/ActivityLog" :class="getRoute() === ' ' ? 'active' : ''" :navText="'Activity Log'">
          <template v-slot:icon>
            <i class="ni ni-ui-04 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <!-- <li class="nav-item" v-if="showdocx">
        <sidenav-item url="/ActivityLog">
          <template v-slot:icon>
            <i class="ni ni-book-bookmark text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li> -->
    </ul>
  </div>
  <div class="pt-2 mx-3 mt-3 sidenav-footer">
    <sidenav-card :class="cardBg" textPrimary="Need Help?" />
  </div>
</template>
<script>
import { mapState } from 'vuex';
import SidenavItem from "./SidenavItem.vue";
import SidenavCard from "./SidenavCard.vue";
import axios from "axios";
import { API_ENDPOINT } from '@/../apiconfig.js';
export default {
  name: "SidenavList",
  props: {
    cardBg: String,
  },
  computed: {
    ...mapState(['project_name', 'project_id', 'observabilityBackupVisible', 'databaseBackupVisible'
    ]),
    showdocx() {
      return this.$store.state.showdocx;
    },
    isAdmin() {
      const role = sessionStorage.getItem('role');
      return role === 'Admin';
    },
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      title: "BitBlast",
      controls: "dashboardsExamples",
      username: "",
      user_id: '',
      userRoles: {}, // Initialize userRoles as an empty object
      openDropdown: null, // Track which dropdown is open
    };
  },
  created() {
    this.username = sessionStorage.getItem('username');
    this.user_id = sessionStorage.getItem('user_id');
  },
  components: {
    SidenavItem,
    SidenavCard,
  },
  mounted() {
    this.fetchProject();
    //this.fetchUserRoles(); // Fetch user roles when the component is mounted
    //this.fetchConnectedStatus();
  },
  methods: {
    getRoute() {
      const routeArr = this.$route.path.split("/");
      return routeArr[1];
    },
    // fetchProject() {
    //   this.$store.dispatch('fetchFirstProject', this.user_id);
    // },
    fetchProject() {
      const authToken = sessionStorage.getItem('token');
      if (!authToken) {
        this.error = 'User is not authenticated';
        return;
      }
      this.$store.dispatch('fetchFirstProject', authToken);
    },
    fetchUserRoles() {
      const authToken = sessionStorage.getItem('token');
      if (!authToken) {
        console.error('User is not authenticated');
        return;
      }
      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json'
      };
      // Make the API request to fetch the user's role
      axios
        .get(`${this.apiUrl}/api/v1/role/`, { headers })
        .then(response => {
          if (response.data) {
            // Handle the user's role data here as needed
          } else {
            console.error('Error fetching user role: No data in response');
          }
        })
        .catch(error => {
          if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.error('Error fetching user role:', error.response.data);
          } else if (error.request) {
            // The request was made but no response was received
            console.error('Error fetching user role: No response received', error.request);
          } else {
            // Something happened in setting up the request that triggered an Error
            console.error('Error fetching user role:', error.message);
          }
        });
    },
    toggleDropdown(section) {
      if (this.openDropdown === section) {
        this.openDropdown = null; // Close the dropdown if already open
      } else {
        this.openDropdown = section; // Open the specified dropdown
      }
    },
    isOpen(section) {
      return this.openDropdown === section;
    },
    async fetchConnectedStatus() {
      try {
        const token = sessionStorage.getItem('token'); // Or however you store your token
        if (!token) {
          console.error('No token found');
          return; // Return undefined if no token is found
        }
        const response = await axios.get(`${this.apiUrl}/api/v1/is-connected/`, {
          headers: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'application/json'
          }
        });
        if (response.status === 200 && response.data && response.data.is_connected) {
          return response.data.is_connected === 'True' ? 'Active' : 'Inactive';
        } else {
          console.error('Unexpected response format:', response);
          return; // Return undefined if response format is unexpected
        }
      } catch (error) {
        console.error('Error fetching status:', error);
        return; // Return undefined if an error occurs
      }
    },
    async redirectToADSave() {
      try {
        const isConnected = await this.fetchConnectedStatus();
        if (isConnected === 'Active') {
          this.$router.push('/ADsave'); // Redirect to ADsave when isConnected is 'Active'
        } else if (isConnected === 'Inactive') {
          this.$router.push('/ADauthprovider'); // Redirect to ADauthprovider when isConnected is 'Inactive'
        } else {
          console.error('Unexpected value for isConnected:', isConnected);
          // Handle unexpected value here
        }
      } catch (error) {
        console.error('Error redirecting:', error);
        // Handle error or fallback redirection here if necessary
      }
    }
  },
};
</script>
<style scoped>
.sub-nav {
  list-style: none;
  /* Hide default bullet points */
  padding: 0;
  /* Remove default padding */
  margin: 0;
  /* Remove default margin */
  color: #3f775e;
}

.navbar-collapse {
  overflow-y: hidden;
  /* Hide vertical scrollbar */
}

/* Forcefully hide the scrollbar */
.navbar-collapse::-webkit-scrollbar {
  display: none;
}

.shift-right {
  margin-left: 7px;
  /* margin-right: 1; */
  /* display: 5px; */
  /* justify-content: flex-end; */
}

.text-green {
  background-color: #e0f7fa;
  /* Soft cyan background */
  color: #00695c;
  /* Dark teal text color */
  /* padding: 15px 20px; */
  /* Increase padding for better spacing */
  border-radius: 8px;
  /* More rounded corners */
  box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.15);
  /* Enhanced shadow for raised effect */
  font-weight: bold;
  /* Make the text bold */
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
  /* Stronger shadow for more prominence */
  display: inline-block;
  /* Ensure proper alignment */
  font-size: 1.2em;
  /* Slightly larger text */
  transition: transform 0.2s, box-shadow 0.2s;
  /* Smooth transition for interactive effect */
}

.text-green:hover {
  transform: translateY(-3px);
  /* Slight upward movement on hover */
  box-shadow: 6px 6px 15px rgba(0, 0, 0, 0.2);
  /* Stronger shadow on hover */
}
</style>