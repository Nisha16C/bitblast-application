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
                <div class="mb-4 card">
                  <div class="card-body px-0 pt-0 pb-2">
                    

                    <div  class="table-responsive p-0">
                      <clusters-table />
                    </div>
                  </div>
                </div>
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
import ClustersTable from "@/views/components/ClusteruserTable.vue";
// import argonButton from "@/components/BB_Button.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';



import axios from "axios";
export default {
  name: "Cluster",
  components: {
    Card,
    ClustersTable,
    // argonButton,
  },
  created() {
    this.user_id = sessionStorage.getItem("user_id");
    this.fetchProjects();
    this.fetchClusters();

  },
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    }
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      stats: {
        money: {
          title: "Total Clusters",
          value: '',
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "",
          iconBackground: "bg-gradient-primary",
        },
      },
      clusterData: [],
      user_id: '',
      selectedProject: "", // New property to store the selected project ID
      projects: [],
      contentList: [],
      deleteClusterName: '',
      clusterName: '',
      selectedCluster: '',




      // clusters: {
      //   type: Array,
      //   required: true,
      // },
      deleteModal: false,
      viewModal: false
    };
  },
  methods: {
    prepareDelete(clusterName) {
      this.deleteModal = true
      this.deleteClusterName = clusterName;

    },
    deleteCluster() {

      const formData = {
        cluster_name: this.deleteClusterName
      };

      this.$router.push('/delete');
      axios.post(`${this.apiUrl}/api/v1/deletecluster/`, formData)
        .then(() => {
          this.deleteModal = false
        })
        .catch(error => {
          console.error('Error deleting cluster:', error);
          this.toggleModal1();
        });
    },

    viewCluster(clusterName) {
      this.clusterName = clusterName;
      axios.get(`${this.apiUrl}/api/v1/result/content/${clusterName}/`)
        .then(response => {
          this.contentList = response.data;

        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    addLineBreaks(text) {
      const formattedContent = text.replace(/([^:\n]+):/g, '<h class="text-sm fw-bolder">$1</h>:');
      return formattedContent.replace(/\n/g, '<br>');

    },



    fetchProjects() {
      const authToken = sessionStorage.getItem('token');
       // Log the retrieved token

      if (!authToken) {
        console.error('Token not found in session storage');
        // Handle the absence of token as needed
        return;
      }

      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json'
      };

      axios
        .get(`${this.apiUrl}/api/v1/project/user/`, { headers })
        .then(response => {
         
          this.projects = response.data;
        })
        .catch(error => {
          console.error('Error fetching projects:', error); // Log any errors
        });
    },

    fetchClusters() {

      const token = sessionStorage.getItem('token');
      if (!token) {
        console.error('Token not found');
        return;
      }

      const headers = {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json'
      };

      axios.get(`${this.apiUrl}/api/v1/clusters/userlist/`, { headers })
        .then(response => {
          if (response.data && Array.isArray(response.data.results)) {
            this.clusterData = response.data.results;
            this.stats.money.value = response.data.count;
          } else {
            console.error('Invalid clusters response format:', response.data);
          }
        })
        .catch(error => {
          console.error('Error fetching clusters:', error);
        });
    },

    fetchClustersByProject() {
      const token = sessionStorage.getItem('token'); // Retrieve the token from session storage

      if (!token) {
        console.error('Token not found in session storage');
        this.loading = false;
        return;
      }

      const headers = {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json'
      };

      if (this.selectedProject === "") {
        // If "All Projects" is selected, fetch all clusters
        this.fetchClusters();
      } else {
        // Fetch clusters for the selected project
        axios.get(`${this.apiUrl}/api/v1/cluster/project/${this.selectedProject}/`, { headers })
          .then(response => {
            this.clusterData = response.data;
            this.stats.money.value = this.clusterData.length;
            this.loading = false;
          })
          .catch(error => {
            console.error('Error fetching clusters by project:', error);
            this.loading = false;
          });
      }
    },


    toggleModal1: function () {
      this.showModal = !this.showModal;
    },
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('en-US', options);
    },
  }
};
</script>

<style scoped>
.custom-right-align {
  direction: rtl;
  text-align: right;
}

.BGdark {
  background-color: #111c44;
  ;
  /* Choose your dark mode background color */
  color: #fff;
  /* Choose your dark mode text color */
}
</style>