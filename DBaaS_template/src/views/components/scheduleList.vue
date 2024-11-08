<template>
  <div class="card">
    <div class="card-header pb-0">
      <div class="col-lg-5">
        <div class="d-flex align-items-center">
          <div class="me-0" @click="goBack">
            <i class="fas fa-arrow-left"></i>
          </div>
          <label class="text-sm col-sm-3">Backup Method :</label>
          <select :class="{ BGdark: isDarkMode }" @click="fetchBackups()" class="form-select col-sm-5 mb-2"
            aria-label="Default select example" v-model="storage_method">
            <option value="nfs">NFS</option>
            <option value="s3">S3</option>
          </select>
        </div>
      </div>
    </div>
    <div v-if="successMessage" class="alert alert-success mb-3">
      <!-- Show success message when backup is completed -->
      <div class="text-center">
        {{ successMessage }}
      </div>
    </div>
    <div class="card-body px-0 pt-0 pb-2">
      <div v-if="backups.length === 0" class="text-center mt-3">
        No Backups are found
      </div>
      <div v-else class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-secondary opacity-7 align-middle">
                Database Name
              </th>
              <th class="text-secondary opacity-7">Retention Period</th>
              <th class="text-secondary opacity-7">Scheduled Time</th>
              <th class="text-secondary opacity-7">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="backup in backups" :key="backup.id">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <img src="../../assets/img/db-png.png" class="avatar avatar-sm me-3" alt="user1" />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm">{{ backup.server_name }}</h6>
                  </div>
                </div>
              </td>
              <td class="align-middle">
                <div class="">
                  <h6 class="mb-0 text-sm">{{ backup.retention_period }}</h6>
                </div>
              </td>
              <td class="align-middle">
                <div class="">
                  <h6 class="mb-0 text-sm">
                    {{ formateDate(backup.scheduled_time) }}
                  </h6>
                </div>
              </td>
              <td class="align-middle">
                <argon-button color="success" size="md" variant="gradient"
                  @click="fetchBackupMethod(backup.server_name)" type="button" class="ml-4 mt-2 btn btn-success"
                  data-toggle="modal" data-target="#exampleModal">
                  Change
                </argon-button>
                <argon-button color="danger" size="md" variant="gradient" @click="fetchBackupMethod(backup.server_name)"
                  type="button" class="ml-4 mt-2 btn btn-danger" data-toggle="modal" data-target="#unschedule">
                  Unschedule
                </argon-button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="modal fade" id="unschedule" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
      aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">
              Unschedule backup
            </h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            Are You Sure Want to unschedule backup !!
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">
              Close
            </button>
            <button type="button" class="btn btn-danger" data-dismiss="modal" @click="Unschedule(server_name)">
              Unschedule
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" :class="{ show: isOpen }" id="exampleModal" tabindex="-1" role="dialog"
      aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">
              Edit Scheduled Backup
            </h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <h3 class="ml-4">{{ server_name }}</h3>
          <div class="form-group ml-3 mt-2 row">
            <label class="text-sm col-lg-5" for="retentionPeriod">Retention Period :</label>
            <div class="input-group d-flex">
              <input type="email" class="form-control col-5" id="retentionPeriod" v-model="newRetentionPeriod" />
              <select class="form-select bg-light col-3" aria-label="Default select example" v-model="selected_value">
                <option value="d" selected>days</option>
                <option value="m">months</option>
                <option value="y">years</option>
              </select>
            </div>
            <div class="mx-3 mt-5">
              <h6>Scheduled Backup Settings</h6>

              <div>
                <label>
                  <input type="radio" v-model="backupType" value="daily" />
                  Daily Backups
                </label>
                <div v-if="backupType === 'daily'" class="form-group mt-3 d-flex align-items-center">
                  <label class="text-sm col-md-3" for="">Backup Schedule:</label>
                  <div class="d-flex col-md-9">
                    <input type="email" class="form-control mx-2 col-md-3" value="Daily" readonly />
                    At<input type="number" class="form-control col-md-3 mx-2" v-model="selectedHour" />
                    :
                    <input type="number" class="form-control col-md-3 ml-2" v-model="selectedMin" />
                  </div>
                </div>
              </div>
              <div>
                <label>
                  <input type="radio" v-model="backupType" value="weekly" />
                  Weekly Backups
                </label>
                <div v-if="backupType === 'weekly'" class="form-group mt-3 d-flex align-items-center">
                  <label class="text-sm col-md-3" for="">Backup Schedule:</label>
                  <div class="d-flex col-md-9">
                    On
                    <select class="form-select col-md-3 mx-1" v-model="selectedDay">
                      <option v-for="day in days" :key="day" :value="day">
                        {{ day }}
                      </option>
                    </select>
                    At<input type="number" class="form-control col-md-3 mx-1" v-model="selectedHour" />
                    :
                    <input type="number" class="form-control col-md-3 ml-1" v-model="selectedMin" />
                  </div>
                </div>
              </div>
              <div>
                <label>
                  <input type="radio" v-model="backupType" value="monthly" />
                  Monthly Backups
                </label>
                <div v-if="backupType === 'monthly'" class="form-group mt-3 d-flex align-items-center">
                  <label class="text-sm col-md-3" for="">Backup Schedule:</label>
                  <div class="d-flex col-md-9">
                    On
                    <input type="number" class="form-control mx-1 col-md-3" v-model="selectedDate" />
                    At<input type="number" class="form-control col-md-3 mx-1" v-model="selectedHour" />
                    :
                    <input type="number" class="form-control col-md-3 ml-1" v-model="selectedMin" />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-if="loading" class="text-center my-3 d-flex">
            <!-- Show loader while loading -->
            <h6 class="mb-2">Loading...</h6>
            <div class="spinner-border spinner-border-lg p-3 text-secondary" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">
              Close
            </button>
            <button @click="changeRetention()" type="button" class="btn btn-danger" data-dismiss="modal">
              Change
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { API_ENDPOINT } from "@/../apiconfig.js";
import ArgonButton from "@/components/BB_Button.vue"; // Import ArgonButton component
export default {
  name: "server-table",
  components: {
    ArgonButton
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      backups: [],
      server_name: "", // Initialize clusters as an empty array
      newRetentionPeriod: "",
      username: "",
      user_id: "",
      selected_value: "days",
      loading: false,
      successMessage: "",
      isOpen: false,
      clusters: "",
      storage_method: "nfs",
      selectedHour: "12",
      selectedMin: "00",
      selectedDate: "10",
      selectedDay: "Sunday",
      date_time: "",
      backupType: "",
      days: [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
      ],
      daysOfMonth: Array.from({ length: 31 }, (_, i) => i + 1),
    };
  },
  mounted() {
    // Fetch data when the component is mounted
    this.fetchBackups();
  },
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
  created() {
    this.username = sessionStorage.getItem("username");
    this.user_id = sessionStorage.getItem("user_id");
  },
  methods: {
    goBack() {
      window.history.back();
    },
    formateDate(cronExpression) {
      const parts = cronExpression.split(" ");
      const minute = parts[0];
      const hour = parts[1];
      const dayOfMonth = parts[2];
      const month = parts[3];
      const dayOfWeek = parts[4];

      let readableExpression = "";

      // Parse day of month
      if (dayOfMonth !== "*") {
        readableExpression += ` On the ${dayOfMonth}${this.getOrdinalSuffix(
          dayOfMonth)} of every month`;
      }

      // Parse month
      if (month !== "*") {
        readableExpression += ` in ${this.getMonthName(month)}`;
      }

      // Parse day of week
      if (dayOfWeek !== "*") {
        readableExpression += ` On every ${this.getDayName(dayOfWeek)}`;
      }

      // // Parse daily
      if (dayOfWeek == "*" & dayOfMonth == '*' & month == '*') {
        readableExpression += ` Daily`;
      }

      // Parse hour
      readableExpression += ` at ${hour}`;

      // Parse minute
      readableExpression += ` : ${minute}`;


      return readableExpression;
    },

    getOrdinalSuffix(number) {
      const suffixes = ["th", "st", "nd", "rd"];
      const v = number % 100;
      return suffixes[(v - 20) % 10] || suffixes[v] || suffixes[0];
    },
    getMonthName(month) {
      const months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ];
      return months[parseInt(month) - 1];
    },
    getDayName(day) {
      const days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
      ];
      return days[parseInt(day)];
    },

    async fetchBackups() {
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
      try {
        // Make a GET request to the endpoint
        const response = await axios.get(
          `${this.apiUrl}/api/v1/barman/get-scheduled-servers?storage_method=${this.storage_method}`, { headers }
        );
        // Update the clusters data with the fetched data
        this.backups = response.data.message;
        // this.backups = response.data.message.filter(backup => backup.retention_period !== null);
      } catch (error) {
        console.error("Error fetching servers:", error);
      }
    },
    Unschedule(serverName) {
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
          `${this.apiUrl}/api/v1/barman/update-scheduled-backups?storage_method=${this.storage_method}&server_name=${serverName}&remove_job=true`, {}, { headers }
        )
        .then(() => {
          this.$router.push("/scheduled-backups");
          this.fetchBackups();
        })
        .catch(() => { });
    },
    getValue(serverName) {
      this.server_name = serverName;
      this.isOpen = true;
    },
    changeRetention() {
      this.loading = true;
      if (this.backupType == 'weekly') {
        this.date_time = this.selectedDay
      } else if (this.backupType == 'monthly') {
        this.date_time = this.selectedDate
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
          `${this.apiUrl}/api/v1/barman/update-scheduled-backups?server_name=${this.server_name}&retention=${this.newRetentionPeriod}${this.selected_value}&storage_method=${this.storage_method}&schedule_hour=${this.selectedHour}&schedule_minute=${this.selectedMin}${this.date_time !== '' ? '&schedule_day=' + this.date_time : ''}`, {}, { headers }
        )
        .then(() => {
          this.successMessage = "Retention Period changed successfully";
          setTimeout(() => {
            this.$router.push("/scheduled-backups");
            this.successMessage = '';
          }, 5000);
        })
        .catch(() => { })
        .finally(() => {
          this.loading = false; // Set loading to false regardless of success or failure
          this.closeModal();
          this.fetchBackups();
        });
    },
    closeModal() {
      this.isOpen = false; // Close modal using jQuery
    },
    async fetchBackupMethod(serverName) {
      this.server_name = serverName;
      this.isOpen = true;
    },
  },
};
</script>
<style scoped>
.BGdark {
  background-color: #111c44;
  color: #fff;
}
</style>
