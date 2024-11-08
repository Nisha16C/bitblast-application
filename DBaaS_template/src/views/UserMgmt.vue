
<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card :title="stats.money.title" :value="stats.money.value" :percentage="stats.money.percentage"
              :iconClass="stats.money.iconClass" :iconBackground="stats.money.iconBackground"
              :detail="stats.money.detail" directionReverse>
            </card>
          </div>
          <!-- <div class="col-lg-5 col-md-12 col-12">
            <div class="mb-4 card">
              <div class="p-3 card-body">
                <div class="px-6 d-flex justify-content-between align-items-center">
                  <div class="mb-2 mt-3">
                    <router-link to="/USER">
                      <argon-button color="success" size="md" variant="gradient">Create New User</argon-button>
                    </router-link>
                  </div>
                  <div class="mb-2 mt-3">
                    <router-link to="/ADgrouplist">
                      <argon-button color="success" size="sm" variant="gradient" style="font-size: 15px;">Active
                        Directory Groups</argon-button>
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </div> -->

          <!--
          <div class="col-lg-3 col-md-12 col-12">
    <div class="mb-4 card">
        <div class="p-3 card-body">
            <div class="px-4">
                <select :class="{ 'BGdark': isDarkMode }" class="form-select" v-model="selectedProject" @change="fetchUsersByProject">
                    <option value="">All Projects</option>
                    <option v-for="project in projects" :key="project.id" :value="project.id">{{ project.project_name }}</option>
                </select>
            </div>
        </div>
    </div>
</div> -->
          <!-- <div class="col-lg-3 col-md-12 col-12">
            <div class="mb-4 card">
              <div class="p-3 card-body">
                <div class="px-7">
                  <div class="mb-2 mt-3">
                    <router-link to="/ADauthprovider">
                      <argon-button color="success" size="md" variant="gradient">Auth Provider</argon-button>
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </div> -->
          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <UsermgnTable />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Card from "@/examples/Cards/Card.vue";
//   import AuthorsTable from "./components/ProjectTable.vue";
import UsermgnTable from "./components/UsermgntTable.vue";
// import argonButton from "@/components/BB_Button.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';

import axios from "axios";

export default {
  name: "User",
  components: {
    Card,
    UsermgnTable,

    // argonButton,
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      stats: {
        money: {
          title: "Total Users",
          value: " ",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "",
          iconBackground: "bg-gradient-primary",
        },
      },
    };
  },
  created() {
    // Fetch clusters when the component is created
    this.fetchUsers();
  },

  methods: {
    // Method to fetch clusters and update totalClusters
    fetchUsers() {
      try {
        // Get token from session storage
        const token = sessionStorage.getItem('token');

        // Check if token exists
        if (!token) {
          throw new Error('Token not found in session storage');
        }

        // Define headers
        const headers = {
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json' // Assuming JSON content type
        };

        // Make a GET request to the endpoint with headers
        axios.get(`${this.apiUrl}/api/v1/users/`, {
          headers: headers
        })
          .then(response => {
            this.stats.money.value = response.data.length.toString();  // Update totalClusters
          })
          .catch(error => {
            console.error('Error fetching users:', error);
          });
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },

    // ... (rest of your methods)
  },
};
</script>
<style scoped></style>