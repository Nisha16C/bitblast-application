<template>
  <div class="card">
    <div class="card-header pb-0 px-3">
      <h6 class="mb-0">Select the type of cluster you want to use</h6>
    </div>
    <div class="card-body pt-4 p-3">
      <ul class="list-group">
        <li class="list-group-item border-0 d-flex p-4 mb-2 bg-gray-100 border-radius-lg">
          <div class="d-flex flex-column">
            <h6 class="mb-3 text-sm">Cluster type</h6>

            <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4" style="width: 106.6667%">
              <div class="col mx-auto">
                <div class="h-100 w-100 border border-success rounded-md text-center text-wrap p-3" :class="{
                  'bg-light': selectedType === 'Standalone',
                  'bg-dark': selectedType === 'Standalone' && isDarkMode,
                }">
                  <label for="Standalone">
                    <input type="radio" id="Standalone" class="visually-hidden" value="Standalone"
                      v-model="selectedType" @change="updateType" />
                    <p class="pt-2 text-info font-size-18 text-wrap">
                      Standalone Node
                    </p>
                    <p class="pt-4 text-gray-500 text-sm text-wrap">
                      A Standalone Node refers to a cluster configuration in a
                      distributed computing environment where all cluster
                      components, such as databases, services, or applications,
                      run on a standalone node or machine.
                    </p>
                  </label>
                </div>
              </div>
              <div class="col mx-auto">
                <div :class="{
                  'bg-light': selectedType === 'Multiple',
                  'bg-dark': selectedType === 'Multiple' && isDarkMode,
                }" class="h-100 border border-success rounded-md text-center p-3">
                  <label for="Multiple">
                    <input type="radio" class="visually-hidden" id="Multiple" value="Multiple" v-model="selectedType"
                      @change="updateType" />
                    <p class="pt-2 text-info font-size-18 text-wrap">
                      Primary/Standby <br />
                      High Availability
                    </p>

                    <p class="text-gray-500 text-sm text-wrap">
                      A Primary/Standby High Availability (HA) Cluster refers to
                      a configuration in a distributed computing environment
                      where two nodes (or more) operate in tandem to provide
                      fault tolerance and redundancy.
                    </p>
                  </label>
                </div>
              </div>
            </div>
          </div>
        </li>
        <div v-if="typeError" class="alert alert-danger alert-dismissible fade show custom-alert">
          <strong>Error!</strong> {{ typeError }}
        </div>

        <!-- Providers Lists row 1 -->
        <li class="list-group-item border-0 border-success d-flex pb-5 mb-2 mt-3 bg-gray-100 border-radius-lg">
          <div class="">
            <h6 class="mb-3 text-sm">Providers</h6>

            <!-- Add your rows and columns here -->
            <div class="row ">
              <div class="col-lg-4 col-md-6 mx-auto d-flex justify-content-center align-items-center border " :class="{
                'bg-light': selectedProvider === 'Kubernetes',
                'bg-dark': selectedProvider === 'Kubernetes' && isDarkMode,
              }" @click="$refs.KubernetesInput.click()" v-if="isProviderEnabled('Kubernetes')">
                <div class="text-center {{ providerName === 'Kubernetes' ? 'selected' : '' }}"
                  style="width: 190px; height: 190px">
                  <label for="">
                    <input ref="KubernetesInput" class="invisible" type="radio" value="Kubernetes"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img class="mt-5" src="@/assets/img/k8s.png" alt="" style="width: 100px; height: 100px" />
                  </label>
                </div>
              </div>
              <div class="col-lg-4 col-md-6  mx-auto d-flex justify-content-center align-items-center border " :class="{
                'bg-light': selectedProvider === 'Harvester',
                'bg-dark': selectedProvider === 'Harvester' && isDarkMode,
              }" @click="$refs.HarvesterInput.click()" v-if="isProviderEnabled('Harvester')">
                <div class="text-center {{ providerName === 'Harvester' ? 'selected' : '' }}"
                  style="width: 190px; height: 190px">
                  <label for="">
                    <input type="radio" ref="HarvesterInput" class="invisible" value="Harvester"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img class="mt-5" src="@/assets/img/wh1.webp" alt="" style="width: 100px; height: 100px" />
                  </label>
                </div>
              </div>
              <!-- CloudStack -->
              <div class="col-lg-4 col-md-6 d-flex justify-content-center align-items-center border " :class="{
                'bg-light': selectedProvider === 'CloudStack',
                'bg-dark': selectedProvider === 'CloudStack' && isDarkMode,
              }" @click="$refs.CloudstackInput.click()" v-if="isProviderEnabled('CloudStack')">
                <div class="text-center {{ providerName === 'CloudStack' ? 'selected' : '' }}"
                  style="width: 190px; height: 190px">
                  <label for="">
                    <input ref="CloudstackInput" class="invisible" type="radio" value="CloudStack"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img class="mt-5" src="@/assets/img/withoutcloud.png" alt="" style="width: 100px; height: 100px" />
                  </label>
                </div>
              </div>
              <!-- </div> -->
              <!-- <br /> -->
              <!-- <div class="row"> -->
              <!-- Nutanix -->
              <div class="col-lg-4 col-md-6 d-flex justify-content-center align-items-center border " :class="{
                'bg-light': selectedProvider === 'Nutanix',
                'bg-dark': selectedProvider === 'Nutanix' && isDarkMode,
              }" @click="$refs.NutanixInput.click()" v-if="isProviderEnabled('Nutanix')">
                <div class="text-center {{ providerName === 'Nutanix' ? 'selected' : '' }}"
                  style="width: 190px; height: 190px">
                  <label for="Nutanix">
                    <input ref="NutanixInput" type="radio" id="Nutanix" value="Nutanix" class="invisible"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img class="mt-5" src="@/assets/img/nutanix.png" alt="" style="width: 100px; height: 100px" />
                  </label>
                </div>
              </div>

              <!-- OpenStack -->
              <div class="col-lg-4 col-md-6 d-flex justify-content-center align-items-center border" :class="{
                'bg-light': selectedProvider === 'OpenStack',
                'bg-dark': selectedProvider === 'OpenStack' && isDarkMode,
              }" @click="$refs.OpenStackInput.click()" v-if="isProviderEnabled('OpenStack')">
                <div class="text-center {{ providerName === 'OpenStack' ? 'selected' : '' }}"
                  style="width: 190px; height: 190px">
                  <label for="">
                    <input ref="OpenStackInput" class="invisible" type="radio" id="OpenStack" value="OpenStack"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img class="mt-5" src="@/assets/img/Openstack.png" alt="" style="width: 100px; height: 100px" />
                  </label>
                </div>
              </div>
              <!-- VMware -->
              <div class="col-lg-4 col-md-6 d-flex justify-content-center align-items-center border" :class="{
                'bg-light': selectedProvider === 'VMware',
                'bg-dark': selectedProvider === 'VMware' && isDarkMode,
              }" @click="$refs.VMwareInput.click()" v-if="isProviderEnabled('VMware')">
                <div class="text-center {{ providerName === 'VMware' ? 'selected' : '' }}"
                  style="width: 190px; height: 190px">
                  <label for="">
                    <input ref="VMwareInput" class="invisible" type="radio" id="VMware" value="VMware"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img class="mt-5" src="@/assets/img/wv1.jpg" alt="" style="width: 100px; height: 100px" />
                  </label>
                </div>
              </div>
              <!-- </div> -->

              <!-- <br /> -->
              <!-- <div class="row"> -->
              <!-- OpenShift -->
              <div class="col-lg-4 col-md-6 d-flex justify-content-center align-items-center border" :class="{
                'bg-light': selectedProvider === 'OpenShift',
                'bg-dark': selectedProvider === 'OpenShift' && isDarkMode,
              }" @click="$refs.OpenShiftInput.click()" v-if="isProviderEnabled('OpenShift')">
                <div class="text-center {{ providerName === 'OpenShift' ? 'selected' : '' }}"
                  style="width: 190px; height: 190px">
                  <label for="">
                    <input ref="OpenShiftInput" class="invisible" type="radio" id="OpenShift" value="OpenShift"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img class="mt-5"
                      :src="this.$store.state.darkMode ? require('@/assets/img/os-white.png') : require('@/assets/img/openshift.png')"
                      alt="" style="width: 100px; height: 100px" /> </label>
                </div>
              </div>
            </div>

            <!-- End of rows and columns -->

            <argon-alert v-if="error"
              class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong> This Provider
              is not connected.
              <router-link to="/Providers" class="text-danger">Click here</router-link>
            </argon-alert>
          </div>
        </li>

        <div v-if="providerError" class="alert alert-danger alert-dismissible fade show custom-alert">
          <strong>Error!</strong> {{ providerError }}
        </div>
      </ul>

      <argon-button @click="Next()" color="success" size="md" variant="gradient">
        NEXT
      </argon-button>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import argonButton from "@/components/BB_Button.vue";
import { API_ENDPOINT } from "@/../apiconfig.js";

import ArgonAlert from "@/components/BB_Alert.vue";

// import { useInputStore } from '../../store/clusterStore';
import axios from "axios";

export default {
  name: "billing-card",
  components: {
    argonButton,
    ArgonAlert,
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      selectedType: "",
      selectedProvider: "",
      typeError: "",
      providerError: "",
      provider_info: [],
      user_id: "",
      providers: [],
      error: "",
    };
  },
  created() {
    this.user_id = sessionStorage.getItem("user_id");
    this.getAllProviderData();
    this.fetchProviders();
  },
  methods: {
    ...mapActions(["updateSelectedType", "updateSelectedProvider"]),
    updateType() {
      this.updateSelectedType(this.selectedType);
    },
    updateProvider() {
      this.updateSelectedProvider(this.selectedProvider);
    },

    Next() {
      if (!this.clusterType) {
        this.typeError = "Cluster type is required";
        setTimeout(() => {
          this.typeError = "";
        }, 5000);
        return;
      }
      if (!this.providerName) {
        this.providerError = "Provider is required";
        setTimeout(() => {
          this.providerError = "";
        }, 5000);
        return;
      }
      const selectedProviderInfo = this.provider_info.find(
        (provider) =>
          provider.provider_name.toLowerCase() ===
          this.providerName.toLowerCase()
      );

      if (selectedProviderInfo && selectedProviderInfo.is_connected) {
        if (
          this.providerName === "Harvester"
        ) {
          this.$router.push("/Cluster-Setting");
        } else {
          this.$router.push("/Cconfiguration");
        }
      } else {
        this.error = "This provider is not connected";
        setTimeout(() => {
          this.error = "";
        }, 5000);
      }
    },

    // getAllProviderData() {
    //   axios
    //     .get(`${this.apiUrl}/api/v1/providers/by-user/${this.user_id}/`)
    //     .then((response) => {
    //       this.providers = response.data;
    //     });
    // },
    async getAllProviderData() {
      // Retrieve token from session storage
      const token = sessionStorage.getItem('token');

      // Set headers with token
      const headers = {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json' // Assuming JSON content type
      };

      try {
        const response = await axios.get(`${this.apiUrl}/api/v1/provider-list/`, { headers });
        this.providers = response.data;
      } catch (error) {
        console.error("Error fetching provider data:", error);
        // Handle error here
      }
    },

    isProviderEnabled(providerName) {
      const provider = this.providers.find(p => p.provider_name === providerName);
      return provider ? provider.is_enabled : false;
    },

    async fetchProviders() {
      // Retrieve token from session storage
      const token = sessionStorage.getItem('token');

      // Set headers with token
      const headers = {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json' // Assuming JSON content type
      };

      try {
        const response = await axios.get(`${this.apiUrl}/api/v1/providers/user-providers/`, { headers });
        this.provider_info = response.data;
      } catch (error) {
        console.error("Error fetching provider data:", error);
        // Handle error here
      }
    },
  },


  computed: {
    ...mapState(["clusterType", "providerName"]),
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
};
</script>
<style scoped>
/* Define styles for dark mode */
.bg-dark {
  background-color: #343a40;
  /* Choose your dark mode background color */
  color: #fff;
  /* Choose your dark mode text color */
}

.pointer-hover:hover {
  cursor: pointer;
}

.custom-alert {
  color: white;
  padding: 0.5rem;
  /* Reduce padding */

}
</style>