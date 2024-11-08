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
                <authors-table />
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
import AuthorsTable from "./components/ProjectTable.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';

import axios from "axios"

export default {
  name: "Project",
  components: {
    Card,
    AuthorsTable,
    // ArgonInput,
    // argonButton,
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
        project_name: "", // Make sure project_name is defined
        // ... other project properties
      },
      input1Error: false,
      shakingInput: null,
      error: "",
    };
  },

  methods: {
    async fetchProjectCount(headers) {
      try {
        const response = await axios.get(`${this.apiUrl}/api/v1/project/`, {
          headers: headers,
        });
        this.stats.money.value = response.data.length.toString();
      } catch (error) {
        console.error("Error fetching project count:", error);
      }
    },
  },
  created() {
    const token = sessionStorage.getItem("token");
    if (token) {
      const headers = {
        Authorization: `Token ${token}`,
        "Content-Type": "application/json",
      };
      this.fetchProjectCount(headers);
    }
  },
};
</script>
