<template>
  <div class="card h-100 mb-4">
    <div class="card-header pb-0 px-3">
      <div class="row">
        <div class="col-md-6">
          <h6 class="mb-0">Your Cluster Summary </h6>
        </div>
        <div class="col-md-6 d-flex justify-content-end align-items-center">
          <i class="far fa-calendar-alt me-2" aria-hidden="true"></i>
          <small>{{ currentDateTime }}</small>
        </div>
      </div>
    </div>
    <div class="card-body pt-4 p-3">
      <div class="table-responsive">
        <table class="table table-borderless custom-table">
          <tbody>
            <tr>
              <th>Cluster Type</th>
              <td>{{ clusterType }}</td>
            </tr>
            <tr>
              <th>Cluster Nodes</th>
              <td v-if="clusterType == 'Standalone'"> 1 Node</td>
              <td v-if="clusterType == 'Multiple'"> 3 Node</td>
            </tr>
            <tr>
              <th>Provider</th>
              <td>{{ providerName }}</td>
            </tr>
            <tr>
              <th>Cluster Name</th>
              <td>{{ clusterName }}</td>
            </tr>
            <tr>
              <th>Postgres Type</th>
              <td>PostgreSQL</td>
            </tr>
            <tr>
              <th>Postgres Versions</th>
              <td>{{ postgres_version }}</td>
            </tr>
            <!-- Inside the Cluster Summary Template -->
            <tr v-if="providerName == 'Cloudstack' || providerName == 'OpenStack'">
              <th>Instance Type</th>
              <td v-if="providerName === 'Cloudstack'">{{ computeOfferings }} </td>
              <td v-if="providerName === 'OpenStack'"> {{ flavors.name }} </td>
            </tr>
            <tr v-if="providerName == 'OpenShift'">
              <th>Storage Class</th>
              <td>{{storageClass}}</td>
            </tr>
            <tr v-if="providerName == 'Kubernetes'">
              <th>Storage Class</th>
              <td>{{k8sClass}}</td>
            </tr>
            <tr v-if="providerName != 'Kubernetes' && providerName != 'OpenShift'">
              <th>OS Type</th>
              <td>{{osType}}</td>
            </tr>
            <tr v-if="providerName != 'Kubernetes' && providerName != 'OpenShift'">
              <th>Airgap Installation</th>
              <td v-show="airgap" > {{airgap}}</td>
              <td v-show="!airgap" > no</td>
            </tr>
             <!-- PgAdmin Enable -->
             <tr v-if="providerName === 'CloudStack'">
              <th>PgAdmin Enable</th>
              <td>{{ getPgAdminStatus }}</td> <!-- Directly use the getter -->
            </tr>
            <!-- <tr v-if="providerName !== 'Kubernetes'">
              <th>Volume Properties</th>
              <td>{{ selectedStorageOffering }} Gi, 3000 IOPS, 125 Mb/s Disk</td>
            </tr>
            <tr>
              <th>Networking</th>
              <td> Private </td>
            </tr> -->
          </tbody>
        </table>
        <ul>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
// import argonButton from "@/components/BB_Button.vue";
import { mapState } from 'vuex';
import { mapGetters } from 'vuex';

export default {
  name: "transaction-card",
  components: {
    // argonButton,
  },
  data() {
    return {
      currentDateTime: new Date().toLocaleString(),
      pgAdminStatus: 'no', // Default status of PgAdmin is 'no'
    };
  },
  mounted() {
    this.updateDateTime();
    setInterval(this.updateDateTime, 1000);
  },
  methods: {
    updateDateTime() {
      const options = { day: '2-digit', month: '2-digit', year: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' };
      this.currentDateTime = new Date().toLocaleString('en-GB', options);
    },
    // Method to update PgAdmin status
    updatePgAdminStatus(status) {
      this.pgAdminStatus = status;
    },
  },
  computed: {
    ...mapGetters(['getPgAdminStatus']),
    ...mapState([
      'clusterType', 'providerName', 'postgres_version',
      'computeOfferings', 'selectedStorageOffering',
      'flavors','clusterName', 'storageClass',"k8sClass",
      "osType","airgap"]),
  },
};
</script>
<style scoped>
.custom-table tr {
  border-bottom: 1px solid #dee2e6;
}
.custom-table td,
.custom-table th {
  border-bottom: none; /* To ensure no extra border lines */
}
</style>
