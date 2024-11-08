<template>
  <div class="card">
    <div v-if="successMessage" class="alert alert-success mb-3">
      <!-- Show success message when backup is completed -->
      <div class="text-center">{{ successMessage }}</div>
    </div>
    <div v-if="errorMessage" class="alert alert-danger mb-3">
      <div class="text-center">{{ errorMessage }}</div>
    </div>
    <div class="card-header pb-0 px-3 d-flex align-items-center">
      <div class="me-2" @click="goBack">
        <i class="fas fa-arrow-left"></i>
      </div>
      <h6 class="mb-0">Enter the Database Name and Backup Name</h6>
    </div>

    <div class="card-body pt-4 p-3">
      <ul class="list-group">
        <li class="list-group-item border-0  p-4 mb-2 bg-gray-100 border-radius-lg">
          <div v-if="loading" class="text-center">
            <!-- Show loader while loading -->
            <h6 class="mb-2">
              Backup in progress...
            </h6>
            <div class="spinner-border spinner-border-lg p-3 text-secondary" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
          </div>
          <div class="d-flex">
            <div class="d-flex flex-column col-md-6">
              <form>
                <div class="form-group mt-3 d-flex align-items-center">
                  <label class="mt-1 text-sm col-md-3">Storage Provider:</label>
                  <select :class="{ 'BGdark': isDarkMode }" class="form-select col-md-9"
                    aria-label="Default select example" v-model="backup_method" @click="fetchServers()">
                    <option value="nfs">NFS</option>
                    <option value="s3">S3</option>
                  </select>
                </div>
                <div class="form-group mt-3 d-flex align-items-center">
                  <label class="mt-3 text-sm col-md-3">Select Database:</label>
                  <select :class="{ 'BGdark': isDarkMode }" v-model="serverName" class="form-select col-md-9"
                    aria-label="Default select example">
                    <option v-for="(description, serverName) in servers" :key="serverName" :value=serverName selected>{{
                      serverName }}
                    </option>
                  </select>
                </div>
                <div class="form-check form-switch mt-3 mx-3">
                  <input class="form-check-input" @click="toggleBackupSchedule()" type="checkbox">
                  <label class=" text-sm mt-2" for="backupSwitch">Schedule Backup (Optional)</label>
                </div>
                <div v-if="!isBackupScheduled" class="form-group mt-3 d-flex align-items-center ">
                  <label class="text-sm col-md-3" for="">Backup Name:</label>
                  <input v-model="backup_name" type="email" class="form-control col-md-9" id="backup_name"
                    placeholder="Backup Name" :class="{ 'BGdark': isDarkMode }" />
                </div>

                <div>
                  <div class="form-group mt-3 d-flex align-items-center">
                    <label class="text-sm col-md-3" for="retentionPeriod">Retention Period:</label>
                    <div class="input-group col-md-9">
                      <input type="email" class="form-control" id="retentionPeriod" v-model="retentionPeriod"
                        :class="{ 'BGdark': isDarkMode }">
                      <select class="form-select" :class="{ 'bg_d': isDarkMode, 'bg-light': !isDarkMode }"
                        aria-label="Default select example" v-model="selected_value">
                        <option value="d" selected>days</option>
                        <option value="m">months</option>
                        <option value="y">years</option>
                      </select>
                    </div>
                  </div>

                  <div v-if="isBackupScheduled" class="mx-3">
                    <h6>Scheduled Backup Settings</h6>

                    <div>
                      <label>
                        <input type="radio" v-model="backupType" value="daily" />
                        Daily Backups
                      </label>
                      <div v-if="backupType === 'daily'" class="form-group mt-3 d-flex align-items-center ">
                        <label class="text-sm col-md-3" for="">Backup Schedule:</label>
                        <div class="justify-content-end d-flex col-md-9">
                          <input type="email" class="form-control mx-2 col-md-3" value="Daily" readonly
                            :class="{ 'custom-dark-mode': isDarkMode, 'bg-light text-dark': !isDarkMode }">
                          At<input type="number" class="form-control col-md-3 mx-2" v-model="selectedHour"
                            :class="{ 'BGdark': isDarkMode }"> :
                          <input type="number" class="form-control col-md-3 ml-2" v-model="selectedMin"
                            :class="{ 'BGdark': isDarkMode }">
                        </div>
                      </div>
                    </div>
                    <div>
                      <label>
                        <input type="radio" v-model="backupType" value="weekly" />
                        Weekly Backups
                      </label>
                      <div v-if="backupType === 'weekly'" class="form-group mt-3 d-flex align-items-center ">
                        <label class="text-sm col-md-3" for="">Backup Schedule:</label>
                        <div class="justify-content-end d-flex col-md-9">On
                          <select class="form-select col-md-3 mx-2" v-model="selectedDay"
                            :class="{ 'BGdark': isDarkMode }">
                            <option v-for="day in days" :key="day" :value="day">
                              {{ day }}
                            </option>
                          </select>
                          At<input type="number" class="form-control col-md-3 mx-2" v-model="selectedHour"
                            :class="{ 'BGdark': isDarkMode }"> :
                          <input type="number" class="form-control col-md-3 ml-2" v-model="selectedMin"
                            :class="{ 'BGdark': isDarkMode }">
                        </div>
                      </div>

                    </div>
                    <div>
                      <label>
                        <input type="radio" v-model="backupType" value="monthly" />
                        Monthly Backups
                      </label>
                      <div v-if="backupType === 'monthly'" class="form-group mt-3 d-flex align-items-center ">
                        <label class="text-sm col-md-3" for="">Backup Schedule:</label>
                        <div class="justify-content-end d-flex col-md-9">On
                          <input type="number" class="form-control mx-2 col-md-3" v-model="selectedDate"
                            :class="{ 'BGdark': isDarkMode }">
                          At<input type="number" class="form-control col-md-3 mx-2" v-model="selectedHour"
                            :class="{ 'BGdark': isDarkMode }"> :
                          <input type="number" class="form-control col-md-3 ml-2" v-model="selectedMin"
                            :class="{ 'BGdark': isDarkMode }">
                        </div>
                      </div>

                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </li>
      </ul>
      <div class="px-2">
        <argon-button v-show="!isBackupScheduled" @click="Backup()" color="success" size="md" variant="gradient">
          Create Backup
        </argon-button>
        <argon-button v-show="isBackupScheduled" @click="scheduleBackup()" color="success" size="md" variant="gradient">
          Schedule Backup
        </argon-button>
      </div>
    </div>
  </div>
</template>
<script>
import argonButton from "@/components/BB_Button.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';
import axios from "axios";
export default {
  name: "backup-card",
  components: {
    argonButton,
  },
  data() {
    return {
      servers: [],
      serverName: '',
      backup_name: '',
      isBackupScheduled: false,
      selectedHour: '12',
      selectedMin: "00",
      selectedDate: '10',
      selectedDay: 'Sunday',
      backup_method: '',
      username: '',
      loading: false,
      successMessage: "",
      errorMessage: "",
      retentionPeriod: '',
      selected_value: '',
      date_time: '',
      backupType: '',
      dailyTime: 14,
      weeklyDay: 'Friday',
      apiUrl: API_ENDPOINT,
      days: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      daysOfMonth: Array.from({ length: 31 }, (_, i) => i + 1),
    };
  },
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    }
  },
  created() {
    this.username = sessionStorage.getItem('username');
  },
  methods: {
    goBack() {
      window.history.back();
    },
    toggleBackupSchedule() {
      this.isBackupScheduled = !this.isBackupScheduled;
    },
    async fetchServers() {
      try {
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

        const response = await axios.get(`${this.apiUrl}/api/v1/barman/list-servers?storage_method=${this.backup_method}`,
          { headers });
        this.servers = response.data.message;
      } catch (error) {
        console.error('Error fetching servers:', error);
      }
    },
    Backup() {
      this.loading = true;
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
          `${this.apiUrl}/api/v1/barman/backup?server_name=${this.serverName}&backup_name=${this.backup_name}&storage_method=${this.backup_method}&retention=${this.retentionPeriod}${this.selected_value}`, {},
          { headers }
        )
        .then(() => {
          this.successMessage = "Backup done successfully";
          setTimeout(() => {
            this.$router.push("/admin-backup");
          }, 5000);
        })
        .catch(() => {
          // Handle error
        })
        .finally(() => {
          this.loading = false;
        });
    },
    scheduleBackup() {
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
          `${this.apiUrl}/api/v1/barman/schedule-backup?server_name=${this.serverName}&retention=${this.retentionPeriod}${this.selected_value}&storage_method=${this.backup_method}&schedule_hour=${this.selectedHour}&schedule_minute=${this.selectedMin}${this.date_time !== '' ? '&schedule_day=' + this.date_time : ''}`, {}, { headers }
        )
        .then(() => {
          this.successMessage = "Backup scheduled successfully";
          setTimeout(() => {
            this.$router.push("/scheduled-backups");
          }, 5000);
        })
        .catch((error) => {
          this.errorMessage = error
          setTimeout(() => {
            this.$router.push("/scheduled-backups");
          }, 5000);
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>
<style scoped>
.BGdark {
  background-color: #111c44;
  color: #fff;
}

.dropdown-wrapper {
  position: relative;
  max-height: 50px;
}

.dropdown-wrapper select {
  position: absolute;
  bottom: 0;
  max-height: calc(100vh - 50vh);
  /* Adjust 120px according to your label height and other spacing */
  overflow-y: auto;
}

.time-field,
.day-and-time-field {
  margin-left: 20px;
}

.bg-dark {
  color: #fff;
}

.bg_d {
  background-color: #1d1e52;
  color: #fff;

}

.custom-dark-mode {
  background-color: #111c44 !important;
  color: #fff !important;
  /* Text color ko white set karne ke liye */
}
</style>