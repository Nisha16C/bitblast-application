<template>
  <!-- Nav and sidenav -->

  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card :title="stats.project.title" :value="stats.project.value" :percentage="stats.project.percentage"
              :iconClass="stats.project.iconClass" :iconBackground="stats.project.iconBackground"
              :detail="stats.project.detail" directionReverse></card>
          </div>

          <div class="col-lg-3 col-md-6 col-12">
            <card :title="stats.cluster.title" :value="stats.cluster.value" :percentage="stats.cluster.percentage"
              :iconClass="stats.cluster.iconClass" :iconBackground="stats.cluster.iconBackground"
              :detail="stats.cluster.detail" directionReverse></card>
          </div>
        </div>

        <div class="row mt-4">
          <div class="col-lg-14 mb-lg-0 mb-4">
            <div class="card">
              <div class="card-header">Welcome {{ username }}!</div>
              <div class="card-body">
                <h5 class="card-title">
                  Empower Your Data Journey with BitBlast!
                </h5>
                <p class="card-text">
                  Experience the transformational power of BitBlast as it
                  propels your data journey forward!
                </p>
                <router-link to="/cluster-create">
                  <argon-button color="success" size="md" variant="gradient">Create New Cluster</argon-button>
                </router-link>
              </div>
            </div>
          </div>
          <div class="col-lg-5">
            <!-- <categories-card /> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Card from "@/examples/Cards/Card.vue";
import argonButton from "@/components/BB_Button.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';
import axios from 'axios';

export default {
  name: "user-dashboard",
  data() {
    return {
      apiUrl: API_ENDPOINT,
      stats: {
        project: {
          title: "Total Projects",
          value: "",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: " ",
          iconBackground: "bg-gradient-primary",
        },
        cluster: {
          title: "Total Clusters",
          value: "",
          percentage: "",
          iconClass: "ni ni-money-coins",
          iconBackground: "bg-gradient-danger",
          detail: " ",
        },
      },
      username: "",
    };
  },
  components: {
    Card,
    argonButton,
  },
  created() {
    this.getUserDetails();
    this.getProject();
    this.getCluster();
  },
  methods: {
    getUserDetails() {
      const authToken = sessionStorage.getItem('token');
      if (!authToken) {
        console.error('User is not authenticated');
        return;
      }
      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json',
      };
      axios.get(`${this.apiUrl}/api/v1/get-user-info/`, { headers })
        .then(response => {
          this.username = response.data.username;
        })
        .catch(error => {
          console.error("Error fetching user details:", error);
        });
    },
    getCluster() {
      const authToken = sessionStorage.getItem('token');
      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json',
      };
      axios.get(`${this.apiUrl}/api/v1/cluster/user/`, { headers })
        .then(response => {
          this.stats.cluster.value = response.data.length.toString();
        })
        .catch(error => {
          console.error("Error fetching cluster count:", error);
        });
    },
    getProject() {
      const authToken = sessionStorage.getItem('token');
      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json',
      };
      axios.get(`${this.apiUrl}/api/v1/project/user/`, { headers })
        .then(response => {
          this.stats.project.value = response.data.length.toString();
        })
        .catch(error => {
          console.error("Error fetching project count:", error);
        });
    }
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
