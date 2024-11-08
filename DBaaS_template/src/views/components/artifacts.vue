<template>
  <div class="card">
    <div class="card-header pb-0">
      <h6 class="text-2xl">Cluster Member</h6>
    </div>
    <div v-if="loading" class="text-center mt-3">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    <div v-else class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0 table-bordered">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-md font-weight-bolder opacity-7 text-center">Member</th>
              <th class="text-uppercase text-secondary text-md font-weight-bolder opacity-7 text-center">State</th>
              <th class="text-uppercase text-secondary text-md font-weight-bolder opacity-7 text-center">Role</th>
              <th class="text-uppercase text-secondary text-md font-weight-bolder opacity-7 text-center">Host</th>
              <th class="text-uppercase text-secondary text-md font-weight-bolder opacity-7 text-center">Port</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(member, index) in members" :key="index" :class="roleClass(member.role)">
              <td>
                <!-- <div class="d-flex px-2 py-1"> -->
                <!-- <div class="d-flex flex-column text-center"> -->
                <p class="mb-0 text-md font-weight-bold text-center">{{ member.name }}</p>
                <!-- <p class="text-md text-secondary mb- text-center">{{ member.cluster_name }}</p> -->
                <!-- </div> -->
                <!-- </div> -->
              </td>
              <td>
                <p class="text-md font-weight-bold mb-0 text-center">{{ member.state }}</p>
              </td>
              <td class="align-middle text-md">
                <p class=" text-md font-weight-bold mb-0 text-center">{{ member.role }}</p>
              </td>
              <td class="align-middle">
                <p class=" text-md font-weight-bold mb-0 text-center">{{ member.host }}</p>
              </td>
              <td class="align-middle">
                <p class="text-md font-weight-bold mb-0 text-center">{{ member.port }}</p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script>
import { API_ENDPOINT } from '@/../apiconfig.js';
export default {
  name: "PostgreSQLClusterVisualization",
  data() {
    return {
      members: [],
      loading: true,
      page: 1,
      pageSize: 10, // Adjust page size as needed
      totalPages: 1,
      apiUrl: API_ENDPOINT,
    };
  },
  props: {
    clusterName: {
      type: String,
      required: true
    }
  },
  methods: {
    fetchData(page) {
      this.loading = true;
      this.page = page;
 
      // Encode the clusterName and page in the URL
      const url = new URL(`${this.apiUrl}/api/v1/get-data/`);
      url.searchParams.append('clusterName', this.clusterName);
      // url.searchParams.append('page', this.page); // If you want to include page as well
 
      fetch(url)
        .then(response => response.json())
        .then(data => {
          this.members = data.members;
          this.totalPages = Math.ceil(this.members.length / this.pageSize);
        })
        .catch(error => {
          console.error("Error fetching data:", error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    roleClass(role) {
      switch (role) {
        case 'leader':
          return 'leader';
        default:
          return 'other-role';
      }
    },
  },
  mounted() {
    this.fetchData(this.page);
    // Refresh data every 5 seconds
    // setInterval(() => {
    //   this.fetchData(this.page);
    // }, 5000);
  }
};
</script>
<style scoped>
/* Scoped CSS */
.card {
  background-color: #ffffff;
  /* Adjust background color as per your design */
  border-radius: 6px;
  border: 1px solid #e9ecef;
  margin-bottom: 30px;
  /* Adjust margin as needed */
  margin: 10px;
  margin-top: 20px;
}
 
.card-header {
  background-color: #f8f9fe;
  /* Adjust header background color */
  border-bottom: 1px solid #e9ecef;
}
 
.card-body {
  position: relative;
}
 
.leader {
  background-color: #dff0d8;
  /* Green color for leader role */
  /* color: rgb(61, 56, 56);  */
}
 
.other-role {
  background-color: #f2dede;
  /* Grey color for other roles */
  /* color: black; */
}
</style>
 
 