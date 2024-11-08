<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.money.title"
              :value="stats.money.value"
              :percentage="stats.money.percentage"
              :iconClass="stats.money.iconClass"
              :iconBackground="stats.money.iconBackground"
              :detail="stats.money.detail"
              directionReverse
            />
          </div>
          <div class="col-lg-8 col-md-12 col-12 w-50">
            <div class="card">
              <div class="p-3 card-body">
                <div>
                  <label for="projectname" class="block custom-text-size text-gray-900 dark:text-black">Project Name</label>
                  <argon-input
                    type="text"
                    placeholder="Project Name"
                    v-model="project.project_name"
                    @input="validateProjectName"
                    :class="{ error: input1Error, shake: shakingInput === 'project.project_name' }"
                  />
                  <div v-if="onTheFlyValidation && project.project_name.trim() !== ''" class="alert alert-danger alert-dismissible fade show custom-alert">
                    <strong>Error!</strong> Project name should be between 5 and 15 characters.
                  </div>
                  <div v-if="existingProjectError" class="alert alert-danger alert-dismissible fade show custom-alert">
                    <strong>Error!</strong> This project name is already exists.
                  </div>
                  <argon-button color="success" size="md" variant="gradient" @click="saveProject">
                    Create Project
                  </argon-button>
                </div>
              </div>
            </div>
          </div>
          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <project-table :projects="projectsData" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Card from "@/examples/Cards/Card.vue";
import ProjectTable from "@/views/components/ProjectUserTable.vue";
import ArgonInput from "@/components/BB_Input.vue";
import ArgonButton from "@/components/BB_Button.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';

export default {
  name: "Projects",
  components: {
    Card,
    ProjectTable,
    ArgonInput,
    ArgonButton,
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      stats: {
        money: {
          title: "Total Projects",
          value: "",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "",
          iconBackground: "bg-gradient-primary",
        },
      },
      project: {
        project_name: '',
        user: '',
      },
      input1Error: false,
      shakingInput: null,
      onTheFlyValidation: false,
      existingProjectError: false,
      projectsData: [],
      error: null,
      isLoading: false,
    };
  },
  created() {
    this.project.user = sessionStorage.getItem('user_id');
    this.fetchProjects();
  },
  methods: {
    fetchProjects() {
      const authToken = sessionStorage.getItem('token');
      if (!authToken) {
        this.error = 'User is not authenticated';
        return;
      }

      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json',
      };

      axios.get(`${this.apiUrl}/api/v1/projects/userlist/`, { headers })
        .then(response => {
          this.projectsData = response.data.results;
          this.stats.money.value = response.data.count.toString();
        })
        .catch(error => {
          this.error = error.response ? error.response.data : 'Error fetching projects';
          setTimeout(() => {
            this.error = '';
          }, 3000);
        });
    },
    validateProjectName() {
      const projectName = this.project.project_name;
      this.onTheFlyValidation = projectName.trim() !== '' && (projectName.length < 5 || projectName.length > 15);
    },
    saveProject() {
      this.input1Error = this.project.project_name === '' || this.onTheFlyValidation;
      if (this.input1Error) {
        this.shakingInput = 'project.project_name';
        setTimeout(() => {
          this.shakingInput = null;
        }, 500);
      } else {
        const authToken = sessionStorage.getItem('token');

        const headers = {
          'Authorization': `Token ${authToken}`,
          'Content-Type': 'application/json'
        };

        this.isLoading = true;

        axios.post(`${this.apiUrl}/api/v1/project/`, this.project, { headers })
          .then(() => {
            this.fetchProjects();
            this.project.project_name = '';
            this.existingProjectError = false;
          })
          .catch(error => {
            if (error.response && error.response.data.error === 'Project already exists') {
              this.existingProjectError = true;
              setTimeout(() => {
                this.existingProjectError = false;
              }, 5000);
            } else {
              this.error = error.response ? error.response.data.error : 'Error saving project';
              setTimeout(() => {
                this.error = '';
              }, 3000);
            }
          })
          .finally(() => {
            this.isLoading = false;
          });
      }
    },
  },
};
</script>

<style scoped>
.error {
  border: 2px solid red;
}

.shake {
  animation: shake 0.5s ease-in-out 8 alternate;
}

@keyframes shake {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(10px, 0);
  }
}

.custom-alert {
  color: white;
  padding: 0.5rem;
}
.custom-text-size {
  font-size: 1rem; /* Adjust this value as needed (1.375rem is between 1.25rem and 1.5rem) */
}
</style>
