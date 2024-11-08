<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <ButtonCard />

        <div class="py-4 container-fluid">
          <div class="row">
            <div class="col-12">
              <div class="card">
                <div class="card-header pb-0">
                  <h6> Backup List</h6>
                </div>


                <div class="card-body px-0 pt-0 pb-2">
                  <div class="pl-4">
                    <h6>{{ server_name }}</h6>
                  </div>
                  <div v-if="backupList.length === 0" class="text-center">No Backups are found</div>
                  <div v-else class="table-responsive p-0">
                    <table class="table align-items-center mb-0">
                      <thead>
                        <tr>
                          <th class="text-uppercase text-secondary font-weight-bolder opacity-7">Backup Id
                          </th>
                          <th class="text-uppercase text-secondary font-weight-bolder opacity-7">Backup Name</th>
                          <th class="text-uppercase text-secondary font-weight-bolder opacity-7">Status</th>
                          <th class="text-uppercase text-secondary font-weight-bolder opacity-7">Time</th>
                          <th class="text-uppercase text-secondary font-weight-bolder opacity-7">Size</th>
                        </tr>
                      </thead>
                      <tbody v-for="backup in backupList[server_name]" :key="backup.backup_id">
                        <tr>
                          <td>
                            <div class="d-flex px-2 py-1">
                              <div>
                                <img src="../assets/img/db-png.png" class="avatar avatar-sm me-3" alt="user1" />
                              </div>
                              <div class="d-flex flex-column justify-content-center">
                                <h6 class="mb-0 text-sm">{{ backup.backup_id }}</h6>
                                <p class="text-xs text-secondary mb-0"></p>
                              </div>
                            </div>
                          </td>
                          <td class="align-middle pl-4">
                            {{ backup.backup_name }}
                          </td>
                          <td class="align-middle">
                            {{ backup.status }}
                          </td>
                          <td class="align-middle">
                            {{ backup.end_time }}
                          </td>
                          <td class="align-middle">
                            {{ backup.size }}
                          </td>
                        </tr>

                      </tbody>
                    </table>
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

import axios from "axios";
import { API_ENDPOINT } from '@/../apiconfig.js';
import ButtonCard from "./components/ButtonCard.vue";


export default {
  name: "BackupDetails",

  components: {
    ButtonCard
  },

  data() {
    return {
      apiUrl: API_ENDPOINT,
      backupList: [],
      backup_method: '',
      server_name: '',
      username: '',
      stats: {
        money: {
          title: "All Backups",
          value: "2",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "",
          iconBackground: "bg-gradient-primary",
        },
      },
    };
  },
  mounted() {
    const { serverName, backupMethod } = this.$route.params;
    this.backup_method = backupMethod;
    this.server_name = serverName;
    this.fetchBackups();
  },
  created() {
    this.username = sessionStorage.getItem('username');
  },
  methods: {

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

        const response = await axios.get(`${this.apiUrl}/api/v1/barman/list-backups?server_name=${this.server_name}&storage_method=${this.backup_method}`, { headers });

        // Update the clusters data with the fetched data
        this.backupList = response.data.message;

      } catch (error) {
        console.error('Error fetching servers:', error);
      }
    },

  },
};
</script>
