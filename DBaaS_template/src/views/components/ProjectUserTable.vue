<template>
  <div class="card">
    <div class="card-header pb-0">
      <h6 class="text-2xl"> Projects Info </h6>
    </div>
    <div v-if="loading" class="text-center mt-3">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div v-else class="card-body px-0 pt-0 pb-2">
      <div v-if="localProjects.length === 0" class="text-center">No Projects are Available</div>
      <div v-else class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-md font-weight-bolder opacity-7"> PROJECT ID & NAME</th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7"> CREATED ON </th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7"> UPDATED ON </th>
              <th class="text-secondary opacity-7"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(project, index) in localProjects" :key="index">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <!-- You can customize the image source or remove it based on your needs -->
                    <img :src="
            this.$store.state.darkMode ||
            this.$store.state.sidebarType === 'bg-default'
              ? logoWhite
              : logo"
              class="avatar avatar-sm me-3 w-3 h-3" alt="projectImage" />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-md">{{ project.id }}</h6>
                    <p class="text-md text-secondary mb-0">{{ project.project_name }}</p>
                  </div>
                </div>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ formatDate(project.created_date) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ formatDate(project.updated_date) }}</span>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="pagination-container">
          <button class="pagination-button" @click="fetchPage(page - 1)" :disabled="page === 1">Previous</button>
          <span class="pagination-info">Page {{ page }} of {{ totalPages }}</span>
          <button class="pagination-button" @click="fetchPage(page + 1)" :disabled="page === totalPages">Next</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { API_ENDPOINT } from '@/../apiconfig.js';
import logo from "@/assets/img/projectTable.png";
import logoWhite from "@/assets/img/project.png";

export default {
  name: "projects-table",
  props: {
    projects: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      loading: true,
      logo,
      logoWhite,
      page: 1,
      pageSize: 5,
      totalPages: 1,
      localProjects: [],
    };
  },
  watch: {
    projects: {
      immediate: true,
      handler(newVal) {
        this.localProjects = newVal;
      },
    },
  },
  created() {
    this.fetchPage(this.page);
  },
  methods: {
    fetchPage(page) {
      if (page < 1 || page > this.totalPages) return;

      this.loading = true;
      this.page = page;

      const authToken = sessionStorage.getItem('token');

      if (!authToken) {
        console.error('Token not found in session storage');
        this.loading = false;
        return;
      }

      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json'
      };

      axios.get(`${this.apiUrl}/api/v1/projects/userlist/?page=${page}&page_size=${this.pageSize}`, { headers })
        .then(response => {
          this.localProjects = response.data.results;
          this.totalPages = Math.ceil(response.data.count / this.pageSize);  // Correctly calculate total pages
        })
        .catch(error => {
          console.error("There was an error fetching the projects!", error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('en-US', options);
    },
  },
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
  margin-left: 0px; /* Move the pagination container to the left */
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
  margin-right: 10px ;
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
</style>





