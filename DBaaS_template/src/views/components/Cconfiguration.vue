<template>
  <div>
    <!-- Notes Section -->
 
    <!-- cloudstack -->
 
    <div v-if="providerName === 'CloudStack' && clusterType === 'Standalone'" class="alert  custom-note">
      <strong>Note:(CloudStack Stanalone)</strong> The CPU and storage have defined minimum limits: CPU (Min: 2 core),
      Storage (Min: 10 GB).
    </div>
    <div v-if="providerName === 'CloudStack' && clusterType === 'Multiple'" class="alert custom-note">
      <strong>Note:(CloudStack HA)</strong> The CPU and storage have defined minimum limits: CPU (Min: 2 core), Storage
      (Min: 10 GB).
    </div>
 
    <!-- Kubernetes -->
 
    <div v-if="providerName === 'Kubernetes' && clusterType === 'Standalone'" class="alert  custom-note">
      <strong>Note:(Kubernetes Stanalone)</strong> The Custom storage have defined minimum limits: Storage (Min: 10 GB).
    </div>
    <div v-if="providerName === 'Kubernetes' && clusterType === 'Multiple'" class="alert  custom-note">
      <strong>Note:(Kubernetes HA)</strong> The Custom storage have defined minimum limits: Storage (Min: 10 GB).
    </div>
 
    <!-- Openstack -->
 
    <div v-if="providerName === 'OpenStack' && clusterType === 'Standalone'" class="alert custom-note">
      <strong>Note:(OpenStack)</strong> The CPU and storage have defined maximum and minimum limits: CPU (Min: 1 core,
      Max: 64
      cores), Storage (Min: 10 GB, Max: 2 TB).
    </div>
    <div v-if="providerName === 'OpenStack' && clusterType === 'Multiple'" class="alert custom-note">
      <strong>Note:(OpenStack HA wala)</strong> The CPU and storage have defined maximum and minimum limits: CPU (Min: 1
      core, Max: 64
      cores), Storage (Min: 10 GB, Max: 2 TB).
    </div>
 
    <!-- OpenShift -->
 
    <div v-if="providerName === 'OpenShift' && clusterType === 'Standalone'" class="alert custom-note">
      <strong>Note:(OpenShift)</strong> The CPU and storage have defined maximum and minimum limits: CPU (Min: 1 core,
      Max: 64
      cores), Storage (Min: 10 GB, Max: 2 TB).
    </div>
    <div v-if="providerName === 'OpenShift' && clusterType === 'Multiple'" class="alert custom-note">
      <strong>Note:(OpenShift HA wala)</strong> The CPU and storage have defined maximum and minimum limits: CPU (Min: 1
      core, Max: 64
      cores), Storage (Min: 10 GB, Max: 2 TB).
    </div>
 
    <!-- card -->
 
    <div class="card">
      <div class="card-header pb-0 px-3">
        <h6 class="mb-0">Choose you compute resource </h6>
      </div>
      <div class="card-body pt-4 p-3">
        <div class="table-responsive p-0" v-if="providerName === 'CloudStack'">
 
          <table class="table align-items-center mb-0">
 
            <thead>
 
              <tr>
 
 
                <th class="text-uppercase text-secondary font-weight-bolder opacity-7"> </th>
 
                <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
 
                  Compute Offering </th>
 
                <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
 
                  CPU Cores</th>
 
                <th class="text-center  text-secondary  font-weight-bolder opacity-7">
 
                  CPU SPEED (MHz)</th>
 
                <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
 
                  Memory (MB) </th>
 
                <th class="text-secondary opacity-7"> </th>
 
              </tr>
 
            </thead>
 
            <tbody>
 
              <tr v-for="project in computeOfferings" :key="project.name">
 
                <div class="row">
 
                  <input type="radio" :value=project.name v-model="selectedComputeOffering" @change="updateOffering" />
 
                </div>
 
                <td>
 
                  <div class="d-flex flex-column text-center">
 
                    {{ project.name }}
 
                  </div>
 
                </td>
 
                <td class="align-middle text-center">
 
                  <span class="d-flex flex-column text-center">{{ project.cpunumber }}</span>
 
                </td>
 
                <td>
 
                  <div class="d-flex flex-column text-center">
 
                    {{ project.cpuspeed }}
 
                  </div>
 
                </td>
 
                <td class="align-middle text-center">
 
                  <span class="d-flex flex-column text-center">{{ project.memory }}</span>
 
                </td>
 
                <td class="align-middle  text-center">
 
                  <svg xmlns="http://www.w3.org/2000/svg" v-if="isSelected(project.name)"
                    class="myclss  text-success mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
 
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
 
                  </svg>
 
                  <!-- <span v-if="isSelected(project.name)"
 
                                  class="d-flex flex-column text-center text-success">SELECTED</span> -->
 
                </td>
 
              </tr>
 
            </tbody>
 
          </table>
 
          <hr>
 
          <div class="form-group ml-3 mt-2 colo-lg-6 row">
 
            <label class="text-sm col-lg-5" for="retentionPeriod">Custom Storage (GB):</label>
 
            <div class="input-group d-flex">
 
              <input type="text" :class="{ 'dark-mode': isDarkMode }" class="col-lg-6 form-control" id="retentionPeriod"
                v-model="selectedStorageOffering" @change="updateStorage" />
 
              <!-- <span class="text-md mt-1 ml-2"> </span> -->
 
            </div>
 
          </div>
 
        </div>
 
        <div class="table-responsive p-0" v-if="providerName === 'OpenStack'">
          <table class="table align-items-center mb-0">
            <thead>
              <tr>
                <th class="text-uppercase text-secondary font-weight-bolder opacity-7"> </th>
                <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                  Flavours </th>
                <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                  CPU Cores</th>
                <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                  RAM (MB)</th>
                <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                  Root Disk (GB)</th>
                <!-- <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                  Memory (MB) </th> -->
                <th class="text-secondary opacity-7"> </th>
 
              </tr>
            </thead>
            <tbody>
              <tr v-for="project in computeFlavors" :key="project.name">
                <td>
                  <div class="row">
                    <input type="radio" :value=project.flavors v-model="flavorIdInput" @change="updateFlavorId">
                  </div>
                </td>
                <td>
                  <div class="d-flex flex-column text-center">
                    {{ project.flavors.name }}
                  </div>
                </td>
                <td class="align-middle text-center">
                  <span class="d-flex flex-column text-center">{{ project.vcpus }}</span>
                </td>
                <td>
                  <div class="d-flex flex-column text-center">
                    {{ project.ram }}
                  </div>
                </td>
                <td class="align-middle text-center">
                  <span class="d-flex flex-column text-center">{{ project.disk }}</span>
                </td>
                <td class="align-middle  text-center">
                  <svg xmlns="http://www.w3.org/2000/svg" v-if="isFalavours(project.flavors.name)"
                    class="myclss  text-success mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="table-responsive p-0" v-if="providerName === 'OpenShift'">
          <div class="form-group ml-3 mt-2">
            <label class="text-sm col-lg-2" for="storageClass">Storage Class:</label>
            <select v-model="storage_class" class="form-select col-lg-6 ml-3" @change="update_storage_class">
              <option v-for="sc in storageClasses" :key="sc.name" :value="sc.name">
                {{ sc.name }}
              </option>
            </select>
          </div>
          <div class="form-group ml-3 mt-2">
            <label class="text-sm col-lg-2">Service Type:</label>
            <select :class="{ 'BGdark': isDarkMode }" class="form-select col-lg-6 ml-3"
              aria-label="Default select example" v-model="service_type">
              <option value="NodePort">NodePort</option>
              <option value="Loadbalancer">Loadbalancer</option>
              <option value="ClusterIP">ClusterIP</option>
            </select>
          </div>
          <div class="form-group ml-3 mt-2">
            <label class="text-sm col-lg-5">Size (in GB) :</label>
            <div class="input-group d-flex">
              <bbinput type="text" class="col-5" v-model="size" @change="update_size" />
              <!-- <span class="text-md mt-1 ml-2"> </span> -->
            </div>
          </div>
        </div>
        <div v-if="providerName === 'Kubernetes'" class="form-group ml-3 mt-2 mb-5">
          <label class="text-sm col-lg-5" for="k8s-key-name">Select Kubernetes Key Name</label>
          <select id="k8s-key-name" :class="{ 'dark-mode': isDarkMode }" class="form-select col-lg-6 ml-3"
            v-model="selectedK8sKeyName" @change="updateSelectedK8sKeyName">
            <option value="" disabled>Select a key</option>
            <option v-for="key in k8sKeyNames" :key="key" :value="key">{{ key }}</option>
          </select>
        </div>
        <div class="table-responsive p-0 " v-if="providerName === 'Kubernetes'">
          <div class="form-group ml-3 mt-2 mb-5">
            <label class="text-sm col-lg-2" for="storageClass">Storage Class:</label>
            <select v-model="k8s_storage_class" :class="{ 'dark-mode': isDarkMode }" class="form-select col-lg-6 ml-3"
              @change="update_k8sstorage_class">
              <option v-for="sc in k8sstorageClasses" :key="sc.name" :value="sc.name">
                {{ sc.name }}
              </option>
            </select>
          </div>
          <div class="form-group ml-3 mt-2">
            <label class="text-sm col-lg-5">Size (in GB) :</label>
            <div class="input-group d-flex">
              <bbinput type="text" class="col-5" v-model="size" @change="update_size" />
              <!-- <span class="text-md mt-1 ml-2"> </span> -->
            </div>
          </div>
        </div>
 
        <div class="ml-3 mt-2" v-if="providerName != 'Kubernetes' && providerName != 'OpenShift'">
          <div class="form-switch my-3 ml-3 col-lg-6 border  rounded-1">
            <input class="mb-1 form-check-input col-lg-4" type="checkbox" id="airgapToggle" v-model="airgapInstallation"
              @change="updateAirI">
            <label class="text-lg col-lg-8 p-2" for="airgapToggle">
              Airgap Installation
            </label>
          </div>
          <div class="form-group  mt-2 mb-5">
            <label class="text-sm col-lg-2" for="os">Choose OS Type:</label>
            <select v-model="select_os" :class="{ 'dark-mode': isDarkMode }" class="form-select col-lg-6 ml-3"
              @change="updateOS">
              <option value="ub2004kvmimgnodisk">Ubuntu 20.04</option>
              <option value="ub2204kvmimgnodisk">Ubuntu 22.04</option>
              <option value="RedHat Enterprises Linux 8.10">RedHat Enterprises Linux 8.10</option>
              <option value="RehHat Enterprises Linux 9.7">RehHat Enterprises Linux 9.7</option>
            </select>
          </div>
        </div>
        <div v-if="showError" class="alert alert-danger alert-dismissible fade show custom-alert">
          <strong>Error!</strong> {{ errorMessage }}
        </div>
        <argon-button @click="Next()" color="success" size="md" variant="gradient">
          NEXT
        </argon-button>
      </div>
    </div>
  </div>
</template>
<script>
import { mapState, mapActions } from 'vuex';
import argonButton from "@/components/BB_Button.vue";
import bbinput from '../../components/BB_Input.vue';
import { API_ENDPOINT } from '@/../apiconfig.js';
import axios from 'axios'
export default {
  components: {
    argonButton,
    bbinput
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      selected_value: "",
      storage_class: "",
      k8s_storage_class: '',
      k8sstorageClasses: [],
      storageClasses: [],
      size: "",
      selectedStorageOffering: null,
      computeOfferings: [],
      computeFlavors: [],
      selectedComputeOffering: null,
      flavorIdInput: null,
      Username: '',
      select_os: '',
      airgapInstallation: false,
      k8sKeyNames: [],
      selectedK8sKeyName: '',
      showError: false,
      errorMessage: '',
    };
  },
  created() {
    this.executeProviderSpecificMethods();
  },
  computed: {
    ...mapState(['providerName', 'flavors', 'clusterType']),
 
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
  mounted() {
    this.fetchK8sKeyNames(); // Fetch key names when the component is mounted
 
    const authToken = sessionStorage.getItem('token');
    if (!authToken) {
      console.error('Token not found in session storage');
      // Handle the absence of token as needed
    } else {
      const headers = new Headers({
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json'
      });
      fetch(`${this.apiUrl}/api/v1/compute_offerings/`, {
        method: 'GET',
        headers: headers
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          this.computeOfferings = data.compute_offerings || [];
        })
        .catch(error => {
          console.error('Error fetching data:', error);
          // Handle the error as needed
        });
    }
  },
  watch: {
    selectedK8sKeyName(newKey) {
      if (newKey) {
        this.fetchK8sStorageClasses();
      }
    }
  },
  methods: {
    ...mapActions([
      "updateComputeOffering",
      "updateSelectedStorage",
      "setFlavors",
      "updateflavorId",
      "updateStorageClass",
      "updateSize",
      "updateK8sClass",
      "update_os",
      "update_AI",
      "setK8sKeyName"
 
    ]),
    executeProviderSpecificMethods() {
      if (this.providerName === 'OpenShift') {
        this.fetchStorageClasses();
        //} else if (this.providerName === 'Kubernetes') {
        // this.fetchK8sStorageClasses();
      } else if (this.providerName === 'OpenStack') {
        this.fetchFlavors();
      }
    },
    updateOffering() {
      this.updateComputeOffering(this.selectedComputeOffering);
    },
    update_storage_class() {
      this.updateStorageClass(this.storage_class);
    },
    update_k8sstorage_class() {
      this.updateK8sClass(this.k8s_storage_class);
    },
    updateOS() {
      this.update_os(this.select_os);
      const airgapInstallation = this.airgapInstallation ? 'yes' : 'no';
      this.update_AI(airgapInstallation);
    },
    updateAirI() {
      const airgapInstallation = this.airgapInstallation ? 'yes' : 'no';
      this.update_AI(airgapInstallation);
    },
    update_size() {
      this.updateSize(this.size);
    },
    updateFlavorId() {
      this.$store.dispatch("setFlavors", this.flavorIdInput);
    },
    async fetchFlavors() {
      try {
        const authToken = sessionStorage.getItem('token');
        // Log the retrieved token
        const headers = {
          'Authorization': `Token ${authToken}`,
          'Content-Type': 'application/json'
        };
        const response = await axios.get(`${this.apiUrl}/api/v1/flavors/`, { headers });
        this.computeFlavors = response.data;
      } catch (error) {
        console.error('Error fetching flavors:', error);
        // Handle error as needed
      }
    },
    updateStorage() {
      this.updateSelectedStorage(this.selectedStorageOffering)
    },
    fetchStorageClasses() {
      const authToken = sessionStorage.getItem('token');
      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json'
      };
      axios
        .get(
          `${this.apiUrl}/api/v1/providers/by-username-and-name/${this.providerName}/`,
          { headers }
        )
        .then((response) => {
          this.provider_info = response.data;
          const formData = {
            OpenShift_username: this.provider_info.OpenShift_username,
            OpenShift_password: this.provider_info.OpenShift_password,
            api_url: this.provider_info.api_url,
          };
          axios
            .post(`${this.apiUrl}/api/v1/list_storage_classes/`, formData, { headers })
            .then((response) => {
              this.storageClasses = response.data;
            })
            .catch((error) => {
              console.error("Error fetching storage classes:", error);
            });
        })
        .catch((error) => {
          console.error("Error fetching provider info:", error);
        });
    },
    fetchK8sStorageClasses() {
      const authToken = sessionStorage.getItem('token');
      const csrfTokenMeta = document.querySelector('meta[name="csrf-token"]');
      const csrfToken = csrfTokenMeta ? csrfTokenMeta.getAttribute('content') : ''; // Fallback to empty string
 
      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,  // Add CSRF token here
      };
 
      const data = {
        selectedK8sKeyName: this.selectedK8sKeyName
      };
 
      axios
        .post(`${this.apiUrl}/api/v1/K8s_storage_classes/`, data, { headers })
        .then((response) => {
          if (response.data && response.data.storage_classes) {
            this.k8sstorageClasses = response.data.storage_classes;
 
            // Check if storage classes are empty and set error message
            if (this.k8sstorageClasses.length === 0) {
              this.setErrorMessage('Please update your kubeconfig data to access storage classes.');
            }
          } else {
            console.error('Unexpected response format:', response.data);
          }
        })
        .catch((error) => {
          console.error('Error fetching storage classes:', error.response ? error.response.data : error.message);
        });
    },
 
 
    Next() {
      // Check required fields
      if (this.providerName === 'CloudStack' && !this.selectedComputeOffering) {
        this.setErrorMessage('Please select a compute offering.');
        return;
      }
      if (this.providerName === 'CloudStack' && !this.selectedStorageOffering) {
        this.setErrorMessage('Please enter custom storage size.');
        return;
      }
      if (this.providerName === 'OpenShift' && !this.storage_class) {
        this.setErrorMessage('Please select a storage class.');
        return;
      }
      if (this.providerName === 'CloudStack' && !this.select_os) {
        this.setErrorMessage('Please select a os type.');
        return;
      }
      if (this.providerName === 'Kubernetes' && !this.selectedK8sKeyName) {
        this.setErrorMessage('Please select a Kubernetes key name.');
        return;
      }
      if (this.providerName === 'Kubernetes' && !this.k8s_storage_class) {
        this.setErrorMessage('Please select a storage class.');
        return;
      }
      if (this.providerName === 'Kubernetes' && !this.size) {
        this.setErrorMessage('Please select a custom storage size.');
        return;
      }
 
      this.$router.push('/Cluster-Setting');
    },
 
    setErrorMessage(message) {
      this.errorMessage = message;
      this.showError = true;
 
      setTimeout(() => {
        this.showError = false;
        this.errorMessage = '';
      }, 5000);
    },
 
    isSelected(projectName) {
      if (this.selectedComputeOffering === projectName) {
        return true
      } else {
        return false;
      }
    },
    isFalavours(projectName) {
      if (this.flavors.name === projectName) {
        return true
      } else {
        return false;
      }
    },
    async fetchK8sKeyNames() {
      const token = sessionStorage.getItem('token');
      const headers = {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json'
      };
 
      try {
        // Fetch the providers
        const response = await axios.get(`${this.apiUrl}/api/v1/provider/`, { headers });
        const providers = response.data;
 
        // Filter and map to get K8s key names
        this.k8sKeyNames = providers
          .filter(provider => provider.provider_name === 'Kubernetes')
          .map(provider => provider.K8s_key_name);
 
      } catch (error) {
        console.error('Error fetching K8s key names:', error);
      }
    },
 
    updateSelectedK8sKeyName() {
      this.fetchK8sStorageClasses(this.selectedK8sKeyName);
 
      this.setK8sKeyName(this.selectedK8sKeyName); // Update Vuex store with selected key name
    }
  }
};
</script>
<style scoped>
/* Hide horizontal scrollbar */
.card-body {
  overflow-x: hidden;
}
 
/* Ensure no horizontal overflow within table-responsive */
.table-responsive {
  overflow-x: hidden;
  width: 100%;
}
 
/* Ensure table and its cells do not cause overflow */
.table {
  width: 100%;
  table-layout: auto;
}
 
.table th,
.table td {
  white-space: nowrap;
  /* Prevents wrapping */
  overflow: hidden;
  /* Ensures no overflow */
  text-overflow: ellipsis;
  /* Ellipsis for overflowing text */
}
 
.custom-note {
  color: #000;
  /* Example color, change as needed */
  background-color: rgb(138, 223, 159);
}
 
.dark-mode {
  background-color: #111c44;
  color: #ffffff;
}
.custom-alert {
  color: white;
  padding: 0.5rem;
  /* Reduce padding */
}
</style>
 
 