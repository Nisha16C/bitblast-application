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

          <div class="col-lg-3 col-md-6 col-12">
            <card :title="stats.user.title" :value="stats.user.value" :percentage="stats.user.percentage"
              :iconClass="stats.user.iconClass" :iconBackground="stats.user.iconBackground" :detail="stats.user.detail"
              directionReverse></card>
          </div>
        </div>
        <div class="row mt-4">
          <div class="col-lg-14 mb-lg-0 mb-4">
            <div class="card">
              <div class="card-header">Welcome Admin!</div>
              <div class="card-body">
                <h5 class="card-title">
                  Empower Your Data Journey with BitBlast!
                </h5>
                <p class="card-text">
                  Experience the transformational power of BitBlast as it
                  propels your data journey forward!
                </p>

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
import axios from "axios";
import { API_ENDPOINT } from '@/../apiconfig.js';


export default {
  name: "user-dashboard",
  data() {
    return {
      apiUrl: API_ENDPOINT,

      stats: {
        cluster: {
          title: "Total Clusters",
          value: " ",
          percentage: "",
          iconClass: "ni ni-money-coins",
          iconBackground: "bg-gradient-danger",
          detail: "",
        },
        user: {
          title: "Total Users",
          value: " ",
          percentage: "",
          iconClass: "ni ni-money-coins",
          iconBackground: "bg-gradient-danger",
          detail: "",
        },
        project: {
          title: "Total Projects",
          value: " ",
          percentage: " ",
          iconClass: "ni ni-money-coins",
          detail: "",
          iconBackground: "bg-gradient-primary",
        },

      },
      sales: {
        us: {
          country: "Projects",
          sales: 12,
          value: "$20",
          bounce: "29.9%",
        },
        germany: {
          country: "Clusters",
          sales: "23",
          value: "$44",
          bounce: "40.22%",
        },
        britain: {
          country: "Users",
          sales: "23",
          value: "$19",
          bounce: "23.44%",
        },
        brasil: {
          country: "Providers",
          sales: "6",
          value: "$14",
          bounce: "32.14%",
        },
      },
    };
  },
  components: {
    Card,
    // GradientLineChart,

    // CategoriesCard,
  },

  methods: {
    // Method to fetch clusters and update stats.cluster.value
    fetchClusters() {
      // Retrieve the token from sessionStorage
      const authToken = sessionStorage.getItem('token');
       // Log the retrieved token

      if (!authToken) {
        console.error('Token not found in session storage');
        return;
      }

      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json'
      };

      axios.get(`${this.apiUrl}/api/v1/cluster/`, { headers })
        .then(response => {
          this.stats.cluster.value = response.data.length.toString();  // Update stats.cluster.value
        })
        .catch(error => {
          console.error('Error fetching clusters:', error);
        });
    },

    fetchUsers(headers) {
      try {
        axios.get(`${this.apiUrl}/api/v1/users/`, { headers })
          .then(response => {
            this.stats.user.value = response.data.length.toString();  // Update total users count
          })
          .catch(error => {
            console.error('Error fetching users:', error);
          });
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },

    async fetchProjectStats(headers) {
      try {
        const response = await axios.get(`${this.apiUrl}/api/v1/project/`, { headers });
        this.stats.project.value = response.data.length.toString();
      } catch (error) {
        console.error("Error fetching project stats:", error);
      }
    },

  },
  created() {
    this.fetchClusters();
    const token = sessionStorage.getItem("token");
    if (token) {
      const headers = {
        Authorization: `Token ${token}`,
        "Content-Type": "application/json",
      };
      this.fetchUsers(headers); // Pass headers to fetchUsers method
      this.fetchProjectStats(headers);
    }
  },


};
</script>
