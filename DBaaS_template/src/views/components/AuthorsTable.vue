<template>
  <div class="card">
    <div class="card-header pb-0">
      <h6 class="text-2xl">Database Info</h6>
    </div>
    <div v-if="loading" class="text-center mt-3">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div v-else class="card-body px-0 pt-0 pb-2">
      <div v-if="clusters.length === 0" class="text-center text-gray-400 text-2xl mt-5">No Clusters are Available</div>
      <div v-else class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary  text-md font-weight-bolder opacity-7">Database ID & Name</th>
              <th class="text-uppercase text-secondary  text-center text-md font-weight-bolder opacity-7 ">Database Type &
                Version</th>
              <th class="text-uppercase text-secondary  text-center text-md font-weight-bolder opacity-7">Storage
                Provider</th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">Provider Name
              </th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">Created On</th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">Updated On</th>
              <th class="text-secondary opacity-7"></th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="(cluster, index) in clusters" :key="index">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <img :src="cluster.cluster_type === 'Multiple'
                      ? (this.$store.state.darkMode || this.$store.state.sidebarType === 'bg-default'
                        ? require('@/assets/img/ha2.png')
                        : require('@/assets/img/ha.webp'))
                      : (this.$store.state.darkMode || this.$store.state.sidebarType === 'bg-default'
                        ? logoWhite
                        : logo)" class="avatar avatar-sm me-3" alt="clusterImage" />

                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-md">{{ cluster.id }}</h6>
                    <p class="text-md text-secondary mb-0">{{ cluster.cluster_name }}</p>
                  </div>
                </div>
              </td>
              <td class="align-middle text-center">
                <p class="text-md font-weight-bold mb-0">{{ cluster.cluster_type }}</p>
                <p class="text-md text-secondary mb-0">{{ cluster.database_version }}</p>
              </td>
              <td class="align-middle text-center text-md">
                <span class="text-secondary text-md font-weight-bold">
                  {{ cluster.backup_method ? cluster.backup_method : '---' }}
                </span>
              </td>
              <td class="align-middle text-center text-md">
                <span class="text-secondary text-md font-weight-bold">{{ cluster.provider }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ formatDate(cluster.created_date) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ formatDate(cluster.updated_date) }}</span>
              </td>
              <td class="align-middle">
                <argon-button color="success" size="md" variant="gradient" @click="viewCluster(cluster.cluster_name)"
                  type="button" class="btn btn-danger" data-toggle="modal" data-target="#viewModal">
                  View
                </argon-button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Pagination container conditionally rendered -->
      <div v-if="clusters.length > 0" class="pagination-container">
        <button @click="fetchPage(page - 1)" :disabled="page === 1" class="pagination-button">Previous</button>
        <span class="pagination-info">Page {{ page }} of {{ totalPages }}</span>
        <button @click="fetchPage(page + 1)" :disabled="page === totalPages" class="pagination-button">Next</button>
      </div>
    </div>
  </div>

  <!-- View Modal -->
  <div class="modal fade" id="viewModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
    aria-hidden="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Cluster Details</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"
            :class="{ 'close-dark': this.$store.state.darkMode }">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <h3>{{ clusterName }}</h3>
          <div v-if="contentList.length > 0">
            <p v-html="addLineBreaks(contentList[0].content)"></p>
          </div>
          <div v-else>No data available</div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ArgonButton from "@/components/BB_Button.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';
import logo from "@/assets/img/db-png.png";
import logoWhite from "@/assets/img/logo3.png";
import axios from 'axios';

export default {
  name: "AuthorTable",
  components: {
    ArgonButton,
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      logo,
      logoWhite,
      clusterName: '',
      deleteClusterName: '',
      user_id: '',
      clusters: [],
      contentList: [],
      loading: true,
      page: 1,
      pageSize: 5,
      totalPages: 1,
    };
  },
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    }
  },
  created() {
    this.user_id = sessionStorage.getItem("user_id");
    this.fetchPage(this.page);
  },
  methods: {
    fetchPage(page) {
      if (page < 1 || page > this.totalPages) return;

      this.loading = true;
      this.page = page;

      // Retrieve the token from sessionStorage
      const authToken = sessionStorage.getItem('token');

      if (!authToken) {
        console.error('Token not found in session storage');
        this.loading = false;
        return;
      }

      // Set up the headers with the token
      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json'
      };

      axios.get(`${this.apiUrl}/api/v1/clusters/`, {
        headers,
        params: {
          page: this.page,
          page_size: this.pageSize
        }
      })
        .then(response => {
          this.clusters = response.data.results;
          this.totalPages = Math.ceil(response.data.count / this.pageSize);
        })
        .catch(error => {
          console.error("There was an error fetching the clusters!", error);
        })
        .finally(() => {
          this.loading = false;
        });
    },


    viewCluster(clusterName) {
      this.clusterName = clusterName;

      // Get the token from sessionStorage
      const authToken = sessionStorage.getItem('token');

      if (!authToken) {
        console.error('Token not found in session storage');
        return;
      }

      // Set up the headers with the token
      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json'
      };

      axios.get(`${this.apiUrl}/api/v1/result/content/${clusterName}/`, { headers })
        .then(response => {
          this.contentList = response.data;
          console.log(this.contentList);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },

    addLineBreaks(text) {
      const formattedContent = text.replace(/([^:\n]+):/g, '<h class="text-md fw-bolder">$1</h>:');
      return formattedContent.replace(/\n/g, '<br>');
    },

    formatDate(dateString) {
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('en-US', options);
    },
  }
};
</script>

<style scoped>
.dark-mode {
  background-color: #111c44;
  color: #ffffff;
}

.card-body {
  position: relative;
}

.pagination-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  margin-left: 0px;
  /* Move the pagination container to the left */
}

.pagination-button {
  background-color: #3ba73e;
  border: none;
  color: white;
  padding: 5px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  margin-right: 10px;
  cursor: pointer;
  border-radius: 4px;
}

.pagination-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.pagination-info {
  margin: 0 10px;
  font-size: 14px;
}

.close-dark {
  color: white !important;
}
</style>
