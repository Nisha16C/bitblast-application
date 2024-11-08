<template>
    <div class="py-7">
        <div class="card">
            <div class="card-header d-flex align-items-center">

                <div @click="goBack">
                    <i class="fas fa-arrow-left mr-2"></i>
                </div><br>
                <h6 class="text-2xl ml-3">Kubernetes Provider Info</h6>
            </div>
            <div class="card-body px-0 pt-0 pb-2">
                <div class="table-responsive p-0">
                    <table class="table align-items-center mb-0">
                        <thead>
                            <tr>
                                <th class="text-uppercase text-secondary text-md font-weight-bolder opacity-7">Connected
                                    Key Name
                                </th>
                                <th
                                    class="text-uppercase text-secondary text-md font-weight-bolder opacity-7 text-center">
                                    Kube Config Data
                                </th>
                                <th
                                    class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">
                                    Delete Key</th>
                                <th class="text-secondary opacity-7"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-if="loading">
                                <td colspan="4" class="text-center">Loading...</td>
                            </tr>
                            <tr v-else-if="localProjects.length === 0">
                                <td colspan="4" class="text-center">No keys are connected to the Kubernetes provider.
                                </td>
                            </tr>
                            <tr v-else v-for="(provider, index) in localProjects" :key="index">
                                <td>
                                    <div class="provider-info">
                                        <img :src="isDarkMode ? require('@/assets/img/Cloud-Provider1.png') : require('@/assets/img/Cloud-Provider.png')"
                                            class="avatar-xs me-3" alt="providerImage" />
                                        <span>{{ provider }}</span>
                                    </div>
                                </td>
                                <td class="text-center">
                                    <button @click="openKubeconfigModal(provider)" class="btn btn-success">View
                                    </button>
                                </td>
                                <td class="align-middle text-center">
                                    <button @click="openConfirmModal(provider)" class="btn btn-danger">Delete</button>
                                </td>
                                <td class="align-middle text-center">
                                    <!-- Optionally add more actions or info here -->
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    <!-- Kubeconfig Modal -->
    <div v-if="kubeconfigModal" class="modal fade show" id="kubeconfigModal" tabindex="-1" role="dialog"
        aria-labelledby="kubeconfigModalLabel" aria-hidden="true" style="display: block;">
        <div class="modal-dialog mdialog" role="document">
            <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
                <div class="modal-header">
                    <h5 class="modal-title" id="kubeconfigModalLabel">Kubeconfig Data of <b>{{ keyToShow }}</b></h5>
                    <button type="button" class="close" @click="closeKubeconfigModal" aria-label="Close"
                        :class="{ 'close-dark': this.$store.state.darkMode }">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body mbody">
                    <div>{{ formattedKubeconfigData }}</div>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" @click="closeKubeconfigModal">Close</button>
                </div>
            </div>
        </div>
    </div>
    <!-- Delete Modal -->
    <div v-if="deleteModal" class="modal fade show" id="exampleModal" tabindex="-1" role="dialog"
        aria-labelledby="exampleModalLabel" aria-hidden="true" style="display: block;">
        <div class="modal-dialog" role="document">
            <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Key Delete</h5>
                    <button type="button" class="close" @click="closeConfirmModal" aria-label="Close"
                        :class="{ 'close-dark': this.$store.state.darkMode }">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    Are you sure you want to delete this key <b>{{ keyToDelete }}</b> ?
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" @click="closeConfirmModal">Close</button>
                    <button @click="confirmDelete" type="button" class="btn btn-danger">Delete</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import { API_ENDPOINT } from "@/../apiconfig.js";
export default {
    data() {
        return {
            localProjects: [],
            apiUrl: API_ENDPOINT,
            loading: true,
            deleteModal: false,
            kubeconfigModal: false,
            keyToDelete: null,
            keyToShow: null,
            kubeconfigData: "",
        };
    },
    created() {
        this.fetchKeyNames();
    },
    computed: {
        formattedKubeconfigData() {
            return this.kubeconfigData.replace(/\n\s*\n/g, '\n'); // Removes empty lines
        },
        isDarkMode() {
            // Use your method or state to check if dark mode is active
            return this.$store.state.darkMode;
        }
    },
    methods: {
        goBack() {
            window.history.back();
        },
        async fetchKeyNames() {
            try {
                const token = sessionStorage.getItem('token');
                if (!token) {
                    console.error('No token found in sessionStorage.');
                    return;
                }
                const headers = {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                };
                const response = await axios.get(`${this.apiUrl}/api/v1/provider/k8s-key-names/`, { headers });
                console.log('API response:', response);
                this.localProjects = response.data.filter(keyName => keyName !== null);
                console.log('Fetched key names:', this.localProjects);
            } catch (error) {
                console.error('Error fetching key names:', error);
                if (error.response && error.response.status === 401) {
                    console.error('Unauthorized access - possibly invalid token.');
                }
            } finally {
                this.loading = false;
            }
        },
        async openKubeconfigModal(keyName) {
            this.keyToShow = keyName;
            try {
                const token = sessionStorage.getItem('token');
                if (!token) {
                    console.error('No token found in sessionStorage.');
                    return;
                }
                const headers = {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                };
                const response = await axios.get(`${this.apiUrl}/api/v1/provider/${keyName}/`, { headers });
                console.log('Kubeconfig response:', response);
                this.kubeconfigData = response.data.kubeconfig_data;
                this.kubeconfigModal = true;
            } catch (error) {
                console.error('Error fetching kubeconfig data:', error);
                if (error.response && error.response.status === 401) {
                    console.error('Unauthorized access - possibly invalid token.');
                }
            }
        },
        closeKubeconfigModal() {
            this.kubeconfigModal = false;
            this.kubeconfigData = null;
            this.keyToShow = null;
        },
        openConfirmModal(keyName) {
            this.keyToDelete = keyName;
            this.deleteModal = true;
        },
        closeConfirmModal() {
            this.deleteModal = false;
            this.keyToDelete = null;
        },
        async confirmDelete() {
            try {
                const token = sessionStorage.getItem('token');
                if (!token) {
                    console.error('No token found in sessionStorage.');
                    return;
                }
                const headers = {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                };
                const response = await axios.delete(`${this.apiUrl}/api/v1/provider/k8s-key-names/${this.keyToDelete}/`, { headers });
                console.log('Delete response:', response);
                this.localProjects = this.localProjects.filter(provider => provider !== this.keyToDelete);
            } catch (error) {
                console.error('Error deleting provider:', error);
            } finally {
                this.closeConfirmModal();
            }
        }
    }
};
</script>
<style scoped>
.provider-info {
    display: flex;
    align-items: center;
}

.provider-info span {
    font-size: 20px;
    /* Adjust text size as needed */
}

.mdialog {
    max-width: 45%;
}

.mbody {
    white-space: pre-wrap;
    /* Preserve formatting of kubeconfig data */
}

.close-dark {
    color: white !important;
}

.dark-mode {
    background-color: #111c44;
    color: #ffffff;
}
</style>
