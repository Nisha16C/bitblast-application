<template>
  <div class="card">
    <div class="card-header pb-0 d-flex">
      <div class="col-lg-5">

        <div class="d-flex align-items-center">
          <div class="me-0" @click="goBack">
            <i class="fas fa-arrow-left"></i>
          </div>
          <label class="text-sm  col-sm-3">Backup Method :</label>
          <select :class="{ 'BGdark': isDarkMode }" @click="fetchServers()" class="form-select col-sm-5 mb-2"
            aria-label="Default select example" v-model="backup_method">
            <option value="nfs">NFS</option>
            <option value="s3">S3</option>
          </select>
        </div>
      </div>

    </div>

    <div class="card-body px-0 pt-0 pb-2">
      <div v-if="servers.length === 0" class="text-center">No Servers are found</div>
      <div v-else class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary  font-weight-bolder opacity-7">Database Name</th>
              <th class="text-uppercase text-secondary  font-weight-bolder opacity-7">View Backups</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(description, serverName) in servers" :key="serverName">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <img src="../../assets/img/db-png.png" class="avatar avatar-sm me-3" alt="user1" />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm">{{ serverName }}</h6>
                    <p class="text-xs text-secondary mb-0"></p>
                  </div>
                </div>
              </td>
              <td class="align-middle ">
                <argon-button color="success" size="md" variant="gradient" @click="viewServer(serverName)" type="button"
                  class="btn btn-danger" data-toggle="modal" data-target="#viewModal">
                  View
                </argon-button>
                <!-- <a href="javascript:;" class="text-secondary font-weight-bold text-xs" data-toggle="tooltip"
                  data-original-title="View server" @click="viewServer(serverName)">View</a> -->
              </td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { API_ENDPOINT } from '@/../apiconfig.js';
import argonButton from '@/components/BB_Button.vue';
export default {
  name: "server-table",
  components: {
    argonButton

  },
  data() {
    return {
      servers: [],
      serverName: '', // Initialize clusters as an empty array
      backup_method: 'nfs',
      apiUrl: API_ENDPOINT,
      username: '',
    };
  },
  mounted() {
    // Fetch data when the component is mounted
    this.fetchServers();
  },

  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    }
  },

  created() {
    this.username = sessionStorage.getItem('username');
  },
  methods: {
    goBack() {
      window.history.back();
    },
    async fetchServers() {
      const authToken = sessionStorage.getItem('token');

      // Check if the token exists
      if (!authToken) {
        console.error('Token not found in session storage');
        return;
      }

      // Set up the headers with the token
      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json'
      };
      try {
        // Make a GET request to the endpoint
        const response = await axios.get(`${this.apiUrl}/api/v1/barman/list-servers?storage_method=${this.backup_method}`, { headers });

        // Update the clusters data with the fetched data
        this.servers = response.data.message;

      } catch (error) {
        console.error('Error fetching servers:', error);
      }
    },
    viewServer(serverName) {
      this.$router.push({
        name: 'BackupDetails',
        params: {
          serverName,
          backupMethod: this.backup_method
        }
      });
    }
  },
};
</script>

<style scoped>
.BGdark {
  background-color: #111c44;
  color: #fff;

}
</style>