<template>
  <main>
    <div class="container-fluid py-8">
      <div class="page-header min-height-100" style="
          margin-right: -24px;
          margin-left: -54%;
        ">
 
      </div>
      <div class="card shadow-lg mt-n6  w-full">
        <div class="card-header pb-0 ">
          <h3 class="mb-3 ml-2 mr-5">Monitoring</h3>
          <div class="button-container px-4 mt-0 mb-3 mx-3 d-flex">
            <select :class="{ 'BGdark': isDarkMode }" class="form-select mr-3 col-7" v-model="username"
              @change="fetchProjects()">
              <option value="" selected>Select User</option>
              <option v-for="user in users" :key="user.username" :value="user.username">{{ user.username }}
              </option>
            </select>
 
            <select :class="{ 'BGdark': isDarkMode }" class="form-select mr-3 col-7" v-model="selectedProject"
              @change="fetchClustersByProject">
              <option value="" selected>Select Project</option>
              <option v-for="project in projects" :key="project.id" :value="project.id">{{ project.project_name }}
              </option>
            </select>
 
            <select :class="{ 'BGdark': isDarkMode }" class="form-select mr-3 col-7" v-model="selectedCluster"
              @change="setEmbedUrl()">
              <option value="" selected>Select Cluster</option>
              <option v-for="cluster in localClusters" :key="cluster.cluster_name" :value="cluster.cluster_name">{{
                cluster.cluster_name }}
              </option>
            </select>
          </div>
        </div>
        <div class="card-body p-0">
          
          <div class="row gx-4">
            <iframe class="min-vh-100" width="100%" height="100%" :src="embedUrl" frameborder="0"></iframe>
          </div>
        </div>
      </div>
    </div>
 
  </main>
</template>
 
<script>
import setNavPills from "@/assets/js/nav-pills.js";
import setTooltip from "@/assets/js/tooltip.js";
import { API_ENDPOINT } from '@/../apiconfig.js';
import axios from "axios";
 
export default {
  name: "profile",
  data() {
    return {
      username: '',
      selectedCluster: '',
      selectedProject: '',
      user_id: '',
      apiUrl: API_ENDPOINT,
      users: [],
      projects: [],
      localClusters: [],
      embedUrl: "",
    };
  },
  created() {
    this.setEmbedUrl();
    this.fetchUsers();
  },
  methods: {           
    setEmbedUrl() {
      const baseEmbedUrl = `http://172.16.1.190:3000/d/07/postgresql-for-admins?orgId=1&refresh=10s&&var-DS_PROMETHEUS=ankithumai&var-interval=$__auto_interval_interval&var-user=${this.username}&var-project=${this.selectedProject}&var-datversion=16&var-clustertype=${this.clusterType}&var-cluster=${this.selectedCluster}&var-datname=All&var-mode=All&kiosk=1`;
      // http://172.16.1.190:3000/d/07/postgresql-for-admins?orgId=1&refresh=10s&from=1728644475338&to=1728644775338&theme=light
      // Check if dark mode is active and append the theme parameter
      const themeParam = this.isDarkMode ? '&theme=dark' : '&theme=light';
 
      this.embedUrl = baseEmbedUrl + themeParam;
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
        console.log("users : ", localUsers);
 
 
        // Assign the filtered users to the component data
        this.users = localUsers;
 
        this.loading = false;
      } catch (error) {
        console.error('Error fetching users:', error);
        this.loading = false;
      }
    },
 
    fetchProjects() {
      console.log(this.username);
      const authToken = sessionStorage.getItem('token');
      // Log the retrieved token
 
      if (!authToken) {
        console.error('Token not found in session storage');
        // Handle the absence of token as needed
        return;
      }
 
      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json'
      };
 
      axios
        .get(`${this.apiUrl}/api/v1/projects/username?username=${this.username}`, {}, { headers })
        .then(response => {
 
          this.projects = response.data;
          console.log(this.projects);
        })
        .catch(error => {
          console.error('Error fetching projects:', error); // Log any errors
        });
    },
    fetchClustersByProject() {
      const token = sessionStorage.getItem('token'); // Retrieve the token from session storage
 
      if (!token) {
        console.error('Token not found in session storage');
        this.loading = false;
        return;
      }
 
      const headers = {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json'
      };
 
      if (this.selectedProject === "") {
        // If "All Projects" is selected, fetch all clusters
        this.fetchClusters();
      } else {
        // Fetch clusters for the selected project
        axios.get(`${this.apiUrl}/api/v1/cluster/project/${this.selectedProject}/`, { headers })
          .then(response => {
            this.localClusters = response.data;
            this.stats.money.value = this.localClusters.length;
            this.loading = false;
          })
          .catch(error => {
            console.error('Error fetching clusters by project:', error);
            this.loading = false;
          });
      }
    },
 
    fetchClusters() {
 
      const token = sessionStorage.getItem('token');
      if (!token) {
        console.error('Token not found');
        return;
      }
 
      const headers = {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json'
      };
 
      axios.get(`${this.apiUrl}/api/v1/clusters/userlist/`, { headers })
        .then(response => {
          if (response.data && Array.isArray(response.data.results)) {
            this.localClusters = response.data.results;
            console.log(this.localClusters);
          } else {
            console.error('Invalid clusters response format:', response.data);
          }
        })
        .catch(error => {
          console.error('Error fetching clusters:', error);
        });
    },
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
    document.body.classList.add("profile-overview");
  },
  beforeUnmount() {
    this.$store.state.isAbsolute = false;
    this.$store.state.imageLayout = "default";
    this.$store.state.showNavbar = true;
    this.$store.state.showFooter = true;
    this.$store.state.hideConfigButton = false;
    document.body.classList.remove("profile-overview");
  },
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  }
};
</script>
 
<style scoped>
.overlay-text {
  position: absolute;
  top: 0;
  left: 0;
  width: 99.5%;
  height: 80px;
  text-align: center;
  background-color: white;
  z-index: 2;
  padding: 10px;
 
}
 
.dark-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 99.5%;
  height: 80px;
  text-align: center;
  color: white;
  background-color: black;
  padding: 10px;
  border-radius: 8px;
  z-index: 2;
}
 
.card-header {
  display: flex;
  align-items: center;
}
 
.card-header .button-container {
  margin-left: auto;
}
.BGdark {
  background-color: #111c44;
  color: #fff;
}
</style>
 