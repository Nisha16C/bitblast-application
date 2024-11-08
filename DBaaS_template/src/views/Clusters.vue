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


          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <authors-table :selectedProject="selectedProject" />
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
import AuthorsTable from "./components/AuthorsTable.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';

// import argonButton from "@/components/BB_Button.vue";
import axios from "axios";

export default {
  name: "Cluster",
  components: {
    Card, AuthorsTable,
    // argonButton
  },
  
  data() {
    return {
      apiUrl: API_ENDPOINT,
      selectedProject: '',
      stats: {
        money: {
          title: "Total Clusters ",
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
    this.fetchClusters();
  },

  methods: {
    // Method to fetch clusters and update totalClusters
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
          this.stats.money.value = response.data.length.toString();  // Update totalClusters
        })
        .catch(error => {
          console.error('Error fetching clusters:', error);
        });
    }


    // ... (rest of your methods)
  },
};

</script>
