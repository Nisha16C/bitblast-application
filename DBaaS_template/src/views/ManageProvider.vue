<template>
    <main>
        <div class="container-fluid">
            <div v-if="loading" class="loading-container">
                <div class="text-center">
                    <div class="spinner-border text-primary" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <div class="loading-text mt-2">Loading...</div>
                </div>
            </div>

            <div v-else class="container mt-6 p-5 card">
                <div class="row">
                    <div class="col-lg-6 col-md-12" v-for="provider in providers" :key="provider.id">
                        <div
                            :class="['provider-card', isDarkMode ? 'bg-dark1 text-white' : 'bg-white', 'rounded-lg', 'p-4']">
                            <img :src="require(`@/assets/img/${provider.img_name}`)" :alt="provider.provider_name"
                                class="provider-img w-24 h-24 object-cover" />
                            <h5 class="text-lg font-semibold">
                                {{ provider.provider_name }}
                            </h5>
                            <p class="m-2">
                                Status:
                                <span :class="{
                                    'text-green-500': provider.is_enabled && !isDarkMode,
                                    'text-red-500': !provider.is_enabled && !isDarkMode,
                                    'text-white': provider.is_enabled && isDarkMode,  // Darker green in dark mode
                                    'text-red-700': !provider.is_enabled && isDarkMode    // Darker red in dark mode
                                }">
                                    {{ provider.is_enabled ? "Enabled" : "Disabled" }}
                                </span>
                            </p>

                            <button @click="toggleProviderStatus(provider.id)" :class="{
                                'btn-danger': provider.is_enabled,
                                'bg-success': !provider.is_enabled,
                            }" class="btn mt-4 text-white py-2 px-4 rounded">
                                {{ provider.is_enabled ? "Disable" : "Enable" }}
                            </button>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import { API_ENDPOINT } from '@/../apiconfig.js';
import axios from "axios";

export default {
    data() {
        return {
            apiUrl: API_ENDPOINT,
            providers: [],
            defaultImgPath: "harvester.jpg", // Default image path in case img_path is empty
            loading: false,
        };
    },
    computed: {
        // Check if dark mode is enabled
        isDarkMode() {
            return this.$store.state.darkMode; // Assumes darkMode is stored in Vuex state
        },
    },
    methods: {
        fetchProviders() {
            this.loading = true;
            // Retrieve token from session storage
            const token = sessionStorage.getItem('token');

            // Set headers with token
            const headers = {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json' // Assuming JSON content type
            };

            axios
                .get(`${this.apiUrl}/api/v1/provider-list/`,
                    { headers })
                .then((response) => {
                    this.providers = response.data;
                    console.log("response", response);
                })
                .catch((error) => {
                    console.error("Error fetching providers:", error);
                })
                .finally(() => {
                    setTimeout(() => {
                        this.loading = false;
                    }, 500); // Ensures loader shows for at least 2 seconds
                });
        },
        toggleProviderStatus(providerId) {
            // Retrieve token from session storage
            const token = sessionStorage.getItem('token');

            // Set headers with token
            const headers = {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json' // Assuming JSON content type
            };
            axios
                .post(
                    `${this.apiUrl}/api/v1/toggle-provider-status/${providerId}/`, {},
                    { headers }
                )
                .then((response) => {
                    const updatedProvider = response.data;
                    const index = this.providers.findIndex(
                        (p) => p.id === updatedProvider.provider_id
                    );
                    if (index !== -1) {
                        this.providers[index].is_enabled = updatedProvider.is_enabled;
                    }
                })
                .catch((error) => {
                    console.error("Error toggling provider status:", error);
                });
        },
    },
    created() {
        this.fetchProviders();
    },
};
</script>

<style scoped>
.loading-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.provider-card {
    border: 1px solid #ccc;
    padding: 16px;
    margin: 16px;
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.provider-info {
    display: flex;
    align-items: center;
}

.provider-img {
    width: 60px;
    height: 60px;
    margin-right: 16px;
    border-radius: 30%;
    object-fit: cover;
}

.text-green-500 {
    color: green;
}

.text-red-500 {
    color: red;
}

.btn {
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
}

.btn:hover {
    background-color: #0056b3;
}

.loading-text {
    font-size: 1.5rem;
    color: #007bff;
}

.bg-dark1 {
    background-color: #111c44;
    /* Dark background */
    color: white;
    /* White text in dark mode */
}
</style>
