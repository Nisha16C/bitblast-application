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
      <div v-if="projects.length === 0" class="text-center">No Projects are Available</div>
      <div v-else class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-md font-weight-bolder opacity-7"> PROJECT ID & NAME </th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7"> CREATE ON
              </th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7"> UPDATED ON
              </th>
              <th class="text-secondary opacity-7"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(project, index) in projects" :key="index">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <img :src="this.$store.state.darkMode ||
      this.$store.state.sidebarType === 'bg-default'
      ? logoWhite
      : logo" class="avatar avatar-sm me-3" alt="logo" />
                  </div>
                  <div class="d-flex flex-column">
                    <h6 class="mb-0 text-md">{{ project.id }}</h6>
                    <p class="text-md font-weight-bold mb-0">{{ project.project_name }}</p>
                  </div>
                </div>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ formatDate(project.created_date) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ formatDate(project.updated_date) }}</span>
              </td>
              <td class="align-middle">
                <argon-button color="success" size="md" variant="gradient" @click="prepareRename(project)" type="button"
                  class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
                  Edit
                </argon-button>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="pagination-container">
          <button @click="fetchPage(page - 1)" :disabled="page === 1" class="pagination-button">Previous</button>
          <span class="pagination-info">Page {{ page }} of {{ totalPages }}</span>
          <button @click="fetchPage(page + 1)" :disabled="page === totalPages" class="pagination-button">Next</button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" ref="myModal" id="exampleModal" tabindex="-1" role="dialog"
    aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Rename Your Project: {{ newProjectName }} </h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"
          :class="{ 'close-dark': this.$store.state.darkMode }">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          New Project Name:
          <argon-input type="text" placeholder="New Project Name" v-model="newProjectName" class=" " />
        </div>
        <div class="modal-footer">
          <argon-button color="secondary" size="md" variant="gradient" type="button" class="ml-4 btn btn-danger"
            data-toggle="modal" data-target="#exampleModal">
            Close
          </argon-button>
          <argon-button color="success" size="md" variant="gradient" @click.prevent="renameProject" type="button"
            class="ml-4 btn btn-success" data-toggle="modal" data-target="#exampleModal">
            Rename
          </argon-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ArgonButton from "@/components/BB_Button.vue";
import ArgonInput from "@/components/BB_Input.vue";
import axios from "axios";
import { API_ENDPOINT } from '@/../apiconfig.js';
import logo from "@/assets/img/projectTable.png";
import logoWhite from "@/assets/img/project.png";


export default {
  name: "projects-table",
  components: {
    // Card,
    // projectsTable,
    ArgonButton,
    ArgonInput
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      projects: [], // Initialize projects as an empty array
      renamingProjectId: null,
      newProjectName: "",
      loading: true,
      logo,
      logoWhite,
      page: 1,
      pageSize: 5,
      totalPages: 1,
      localProjects: [],
    };
  },
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    }
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
    prepareRename(project) {
      // Emit an event to notify the parent component about the rename action
      this.renamingProjectId = project.id;
      this.newProjectName = project.project_name;
      this.$emit("rename-project", project);
    },

    renameProject() {
      const token = sessionStorage.getItem("token");

      if (!token) {
        console.error("Token not found in session storage");
        return;
      }

      const headers = {
        Authorization: `Token ${token}`,
        "Content-Type": "application/json",
      };

      const payload = { new_project_name: this.newProjectName };

      axios
        .put(
          `${this.apiUrl}/api/v1/project/${this.renamingProjectId}/rename/`,
          payload,
          { headers }
        )
        .then(() => {
          this.fetchPage(this.page); // Refresh the projects list
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },


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

      axios.get(`${this.apiUrl}/api/v1/projects/`, {
        headers,
        params: {
          page: this.page,
          page_size: this.pageSize
        }
      })
        .then(response => {
          this.projects = response.data.results; // Update projects directly
          this.totalPages = Math.ceil(response.data.count / this.pageSize);
        })
        .catch(error => {
          console.error("There was an error fetching the projects!", error);
        })
        .finally(() => {
          this.loading = false;
        });
    },


    formatDate(dateString) {
      // Format the date as per your requirement using a library like moment.js
      // Example using JavaScript built-in methods (customize as needed):
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('en-US', options);
    },

  },
};
</script>

<style scoped>
.dark-mode {
  /* Define dark mode styles */
  background-color: #111c44;
  color: #ffffff;
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