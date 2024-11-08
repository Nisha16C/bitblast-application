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
import { mapState } from 'vuex';
import axios from 'axios';
import Card from "@/examples/Cards/Card.vue";
import ProjectTable from "@/views/components/ProjectselectTable.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';

export default {
  name: "Cluster",
  components: {
    Card,
    ProjectTable,
  },
  computed: {
    ...mapState(['project_name', 'project_id']),
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
          iconBackground: "bg-gradient-primary",
          detail: "" // Ensure detail is always defined
        },
      },
      projectsData: [],
      error: null,
    };
  },
  created() {
    this.fetchProjects();
  },
  methods: {
    fetchProjects() {
      const authToken = sessionStorage.getItem('token');
      if (!authToken) {
        console.error('User is not authenticated');
        return;
      }

      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json',
      };

      axios.get(`${this.apiUrl}/api/v1/project/user/`, { headers })
        .then(response => {
          this.projectsData = response.data;
          this.stats.money.value = response.data.length.toString();
        })
        .catch(error => {
          console.error("Error fetching projects:", error);
          this.error = error.response ? error.response.data : 'Error fetching projects';
          setTimeout(() => {
            this.error = null;
          }, 3000);
        });
    },
  }
};
</script>

<style scoped>
.error {
  border: 2px solid red;
}

.main_content {
  background: linear-gradient(90deg, #25316D 0%, #8b7c59 100%);
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
</style>
