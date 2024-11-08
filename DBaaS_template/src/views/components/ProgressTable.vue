<template>
  <div class="container mt-2">
    <div class="alert text-center" v-show="!isCompleted && !isFailed">
      <h4 class="font-weight-bold px-2 text-danger">
        Please do not refresh or close this page until the progress is
        completed!
      </h4>
    </div>
    <div class="card shadow-sm">
      <div v-if="popupMessage" class="alert alert-success mb-3">
        <div class="text-center"> <strong>Success!</strong> {{ popupMessage }}</div>
      </div>
      <div v-if="errorMessage" class="alert alert-danger mb-3">
        <div class="text-center"> <strong>Error!</strong> {{ errorMessage }}</div>
      </div>
 
      <div class="card-header text-center justify-content-between">
        <h5 class="mb-0">Database Installation Result</h5>
        <div class="spinner-border mt-3 p-4 spinner-border-md text-primary" v-show="!isCompleted" role="status"
          aria-hidden="true"></div>
      </div>
      <div class="card-body">
        <h2 class="card-title">Installation Status...</h2>
        <div style="height: 30px; width: 100%; position: relative;">
          <progress class="progress bg-primary"
            style="height: 100%; width: 100%; border-radius: 50px 20px; color: #5e72e4" :value="averageProgress"
            max="100"></progress>
          <span style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #ffff;">{{
            averageProgress }}%</span>
        </div>
        <div class="mt-3">
          Database Installation Status: {{ latestPipelineStatus }}
        </div>
 
        <!-- Terminal-like log container -->
        <div class="log-container mt-3"
          style="height: 200px; overflow-y: auto; border: 1px solid #ccc; background-color: #ffffff; color: #282c34; padding: 10px; border-radius: 5px;">
          <div v-for="entry in pipelineLogs" :key="entry.job_id" class="log-entry">
            <!-- <strong>{{ entry.job_name }}</strong>: -->
            <div v-for="(log, index) in entry.logs" :key="index" class="log-message">
              {{ log }}
            </div>
          </div>
        </div>
      </div>
    </div>
 
    <div class="card shadow-sm" v-show="isCompleted">
      <div class="card-body">
        <div class="text-center mt-3">
          <h4 class="text-primary cursor">
            We are redirecting you to the cluster list page. If you are not
            redirected,
            <a @click.prevent="RedirectclusterPage" class="text-dark">click here</a>
          </h4>
        </div>
      </div>
    </div>
  </div>
</template>
 
 
<script>
import axios from "axios";
import { API_ENDPOINT } from "@/../apiconfig.js";
import { mapState } from "vuex";
 
export default {
  data() {
    return {
      apiUrl: API_ENDPOINT,
      isDropdownOpen: false,
      ProjectToggle: false,
      UserToggle: false,
      Username: "",
      user_id: null,
      projects: [],
      selectedProject: "",
      clusters: [],
      isCompleted: false,
      isFailed: false,
      completionText: "Loading...",
      completionColor: "",
      averageProgress: 0,
      latestPipelineStatus: "",
      extractedArtifacts: [], // Initialize as an array
      stopFetching: false,
      isPopupVisible: false,
      popupMessage: "",
      errorMessage: "",
      pipelineLogs: [],
      showcred: false,
      // selectedHour: '12',
      // selectedMin: "30",
      // selectedDate: '10',
      // selectedDay: 'Sunday',
      // backup_method: 'nfs',
      // retentionPeriod: '6',
      // selected_value: 'd',
      date_time: '',
      // backupType: 'weekly',
      // serverName: 'pr-demo-2',
      days: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      daysOfMonth: Array.from({ length: 31 }, (_, i) => i + 1),
 
    };
  },
  props: {
    height: {
      type: Number,
      default: 100,
    },
  },
  methods: {
    RedirectclusterPage() {
      this.$router.push("/Clusters");
    },
    logout() {
      sessionStorage.removeItem("user_id");
      sessionStorage.removeItem("username");
      sessionStorage.removeItem("project_id");
      sessionStorage.removeItem("project_name");
      window.location.reload();
    },
    getFirstLetter(username) {
      return username.charAt(0, 1).toUpperCase();
    },
    toggleDarkMode() {
      this.toggleDark();
    },
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    userToggle() {
      this.UserToggle = !this.UserToggle;
    },
    async updateLatestPipelineStatusAndArtifacts() {
      if (this.stopFetching) {
        return;
      }
 
      try {
        const url = `${this.apiUrl}/api/v1/get_pipeline_status/`;
        const formdata = {
          project_id: this.project_id,
          cluster_name: this.clusterName,
          cluster_type: this.clusterType,
          postgres_version: this.postgres_version,
          provider_name: this.providerName,
        };
 
        // Retrieve the token from session storage
        const authToken = sessionStorage.getItem('token');
 
        if (!authToken) {
          console.error('Token not found in session storage');
          return;
        }
 
        const headers = {
          'Authorization': `Token ${authToken}`,
          'Content-Type': 'application/json'
        };
 
        const response = await axios.post(url, formdata, { headers });
        const data = response.data;
        this.latestPipelineStatus = data.status;
        this.pipelineLogs = data.logs;
        console.log(this.pipelineLogs);
 
        // Update the component's data properties based on the received data
        this.averageProgress = this.calculateAverageProgress(this.latestPipelineStatus);
 
        this.isCompleted = this.averageProgress === 100;
        this.isFailed = this.averageProgress === 99;
        this.completionText = this.isCompleted
          ? "Completed"
          : this.isFailed
            ? "Failed"
            : "Loading...";
        this.completionColor = this.isCompleted
          ? "green"
          : this.isFailed
            ? "red"
            : "";
 
        // this.extractedArtifacts = this.extractArtifacts(data.artifacts);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
 
      if (this.isCompleted) {
        this.stopFetching = true;
        this.showSuccessPopup();
      } else if (this.isFailed) {
        this.stopFetching = true;
        this.showFailedPopup();
      }
 
      setTimeout(this.updateLatestPipelineStatusAndArtifacts, 1000);
    },
    calculateAverageProgress(pipeline) {
      let totalProgress = 0;
      switch (pipeline) {
        case "created":
          totalProgress += 20;
          break;
        case "pending":
          totalProgress += 40;
          break;
        case "running":
          totalProgress += 70;
          break;
        case "success":
          totalProgress += 100;
          break;
        case "failed":
          // Handle 'failed' status separately (you can adjust the value as needed)
          totalProgress += 99.9;
          break;
        default:
          // Handle other statuses if needed
          break;
      }
      return Math.floor(totalProgress);
    },
    extractArtifacts(pipelines_artifact) {
      if (pipelines_artifact && pipelines_artifact.length > 0) {
        const extractedArtifacts = pipelines_artifact[0].content;
        return this.formatArtifactContent(extractedArtifacts);
      }
      return [];
    },
    formatArtifactContent(content) {
      if (typeof content === 'string') {
        return content.split('\n');
      }
      return [];
    },
    scheduleBackup() {
      this.loading = true;
      if (this.backup_type == 'weekly') {
        this.date_time = this.selected_day
      } else if (this.backup_type == 'monthly') {
        this.date_time = this.selected_date
      } else {
        this.date_time = ''
      }
      const authToken = sessionStorage.getItem('token');
 
      // Check if the token exists
      if (!authToken) {
        console.error('Token not found in session storage');
        return;
      }
 
      // Set up the headers with the token
      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json'
      };
 
 
      axios
        .post(
          `${this.apiUrl}/api/v1/barman/schedule-backup?server_name=${this.clusterName}&retention=${this.retention}${this.selectedValue}&storage_method=${this.backupMethod}&schedule_hour=${this.selected_hour}&schedule_minute=${this.selected_min}${this.date_time !== '' ? '&schedule_day=' + this.date_time : ''}`, {}, { headers }
        )
        .then(() => {
          this.successMessage = "Backup scheduled successfully";
          setTimeout(() => {
            this.$router.push("/clusters");
          }, 5000);
        })
        .catch((error) => {
          this.errorMessage = error;
          setTimeout(() => {
            this.$router.push("/clusters");
          }, 5000);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    showSuccessPopup() {
 
      this.popupMessage = "Installation successful!";
      this.showcred = true;
      setTimeout(() => {
        if (this.clusterType == 'Standalone' && this.providerName == 'CloudStack' && this.schedule_backup == true) {
          // Redirect to the overview page here
          this.popupMessage = "Schedulling automatic backup"
          this.scheduleBackup()
        }
        else {
          this.$router.push("/Clusters");
        }
      }, 5000);
    },
    showFailedPopup() {
      this.errorMessage = "Installation failed. Please try again.";
      this.showcred = true;
      setTimeout(() => {
        // Redirect to the overview page here
        this.$router.push("/Clusters");
      }, 5000);
    },
  },
  created() {
    this.Username = sessionStorage.getItem("username");
    this.user_id = sessionStorage.getItem("user_id");
  },
  computed: {
    formattedArtifacts() {
      return this.extractedArtifacts.join("<br>");
    },
    ...mapState([
      "clusterType",
      "providerName",
      "postgres_version",
      "dbUsername",
      "dbPassword",
      "clusterName",
      "project_id",
      "computeOfferings",
      "selectedStorageOffering",
      "flavors",
      "retention",
      "selectedValue",
      "selected_min",
      "selected_hour",
      "selected_day",
      "selected_date",
      "backup_type",
      "backupMethod",
      "schedule_backup"
    ]),
  },
  mounted() {
    setTimeout(() => {
      this.updateLatestPipelineStatusAndArtifacts();
    }, 4000);
  },
  unmounted() {
    this.stopFetching = true;
  },
  beforeUnmount() {
    this.stopFetching = true;
    this.popupMessage = "";
  },
};
</script>
 
<style scoped>
.cursor {
  cursor: pointer;
}
 
.blink {
  animation: blinker 1.5s linear infinite;
  color: red;
  font-family: sans-serif;
}
 
@keyframes blinker {
  50% {
    opacity: 0;
  }
}
 
.terminal {
  background-color: black;
  color: green;
  padding: 10px;
  font-family: monospace;
  overflow-y: auto;
  height: 300px;
  /* Adjust height as needed */
}
 
.log-entry {
  margin: 10px 0;
  /* Adds spacing between job entries */
}
 
.log-message {
  margin-left: 20px;
  /* Indent log messages */
}
</style>
 