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
          <!-- Overlay Text "Activity Logs" -->
          <!-- <div class="overlay-text bg-white text-center p-3" :class="{ 'dark-overlay': isDarkMode }">
  <h2 class="mb-0">Monitoring</h2>
  </div> -->
          <div class="row gx-4">
            <iframe class="min-vh-100" width="100%" height="100%" :src="embedUrl" frameborder="0"
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
import axios from "axios";
import { API_ENDPOINT } from '@/../apiconfig.js';
export default {
  name: "profile",
  data() {
    return {
      user_id: '',
      apiUrl: API_ENDPOINT,
      project: 'default-happy-rainbow',
      clusterType: 'Multiple',
      clusterName: 'test-123',
      projects: [],
      localClusters: [],
      selectedProject: '',
      selectedCluster: '',
      database_version: '',
      cluster_type: '',
      embedUrl: '',
    };
  },
  created() {
    this.username = sessionStorage.getItem('username');
    this.user_id = sessionStorage.getItem('user_id');
    this.fetchProjects();
    this.setEmbedUrl();
  },
  methods: {
    setEmbedUrl() {
      const baseEmbedUrl = `http://172.16.1.190:3000/d/07/postgresql-for-admins?orgId=1&refresh=10s&&var-DS_PROMETHEUS=ankithumai&var-interval=$__auto_interval_interval&var-user=${this.username}&var-project=${this.selectedProject}&var-datversion=16&var-clustertype=${this.clusterType}&var-cluster=${this.selectedCluster}&var-datname=All&var-mode=All&kiosk=1`;
      // Check if dark mode is active and append the theme parameter
      const themeParam = this.isDarkMode ? '&theme=dark' : '&theme=light';
      this.embedUrl = baseEmbedUrl + themeParam;
    },
    fetchProjects() {
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
        .get(`${this.apiUrl}/api/v1/project/user/`, { headers })
        .then(response => {
          this.projects = response.data;
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
            this.stats.money.value = response.data.count;
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
  width: 100%;
  text-align: center;
  background-color: white;
  z-index: 2;
}
.dark-overlay {
  position: absolute;
  top: 0%;
  left: 0%;
  width: 99.5%;
  height: 9.5%;
  text-align: center;
  color: white;
  background-color: rgb(15, 15, 15);
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