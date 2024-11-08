<template>
    <main>
        <!-- Container for displaying Active Directory groups -->
        <div class="container-fluid mt-7">
            <div class="card shadow-lg mt-n6">
                <div class="card-body p-3">
                    <div class="row gx-4">
                        <div class="col-auto my-auto">
                            <div class=" d-flex align-items-center h-100">
                                <router-link to="/User-Management">
                                    <i class="fas fa-arrow-left mr-2"></i>
                                </router-link>
                                <h5 class="mb-1 text-2xl ml-3">List Of Active Directory Groups</h5>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Display groups and their members -->
        <div class="py-4 container-fluid">
            <div class="row">
                <div class="col-md-12">
                    <div class="card" style="height: 650px; overflow-y: auto;">
                        <div class="card-body">
                            <!-- Iterate over each AD group -->
                            <div v-for="group in adGroups" :key="group.group_name">
                                <!-- Group name with buttons on the same line -->
                                <div class="d-flex justify-content-between align-items-center">
                                    <h6 @click="toggleMembers(group)" class="group-name">{{ group.group_name }}</h6>
                                    <argon-button color="success" size="md" variant="gradient"
                                        @click="prepareAssignRoles(group)" class="ml-4">
                                        Assign Roles
                                    </argon-button>
                                </div>
                                <hr />
                                <!-- Member list -->
                                <ul v-if="group.showMembers">
                                    <li v-for="member in group.members" :key="member">{{ member }}</li>
                                </ul>
                                <!-- Display assigned role for the group -->
                                <div v-if="group.assignedRole">
                                    <p>Assigned Role: {{ group.assignedRole }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Role assignment modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
            aria-hidden="true" :class="{ 'show': isModalVisible }">
            <div class="modal-dialog" role="document">
                <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
                    <div class="modal-header">
                        <h2 class="modal-title" id="exampleModalLabel">Select Role</h2>
                        <button type="button" class="close" @click="closeModal" aria-label="Close"
                            :class="{ 'close-dark': this.$store.state.darkMode }">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <div class="form-check" v-for="role in roles" :key="role.id">
                            <input :class="{ 'dark-mode': isDarkMode }" v-model="selectedRole" class="form-check-input"
                                type="radio" :id="'roleCheckbox_' + role.name" :value="role.name" />
                            <label class="form-check-label" :for="'roleCheckbox_' + role.name">{{ role.name }}</label>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <argon-button color="secondary" size="md" variant="gradient" @click="closeModal">
                            Cancel
                        </argon-button>
                        <argon-button color="success" size="md" variant="gradient" @click.prevent="assignGroupRoles">
                            Assign Role
                        </argon-button>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import { API_ENDPOINT } from '@/../apiconfig.js';
import axios from 'axios';
import ArgonButton from "@/components/BB_Button.vue"; // Import ArgonButton component

export default {
    data() {
        return {
            apiUrl: API_ENDPOINT,
            adGroups: [],
            roles: [{ id: 1, name: 'Admin' }, { id: 2, name: 'Standard' }],
            selectedRole: '',
            selectedGroup: null,
            isModalVisible: false, // Track modal visibility
            username: "", // Track username
        };
    },
    components: {
        ArgonButton,
    },
    created() {
        this.fetchADGroups();
    },
    computed: {
        isDarkMode() {
            return this.$store.state.darkMode;
        },
    },
    methods: {

        fetchADGroups() {
            const authToken = sessionStorage.getItem('token');
            if (!authToken) {
                console.error('User is not authenticated');
                return;
            }

            const headers = {
                'Authorization': `Token ${authToken}`,
                'Content-Type': 'application/json'
            };

            // First API call to fetch AD groups
            axios
                .get(`${this.apiUrl}/api/v1/list-gmember/`, { headers })
                .then(response => {
                    this.adGroups = response.data.groups.map(group => ({
                        ...group,
                        showMembers: false,
                        assignedRole: group.assignedRole || '', // Initialize assignedRole from backend
                    }));

                    // Second API call to save AD groups
                    axios
                        .get(`${this.apiUrl}/api/v1/save-ad-groups/`, { headers })
                        .catch(saveError => {
                            console.error('Error saving AD groups:', saveError);
                        });
                })
                .catch(error => {
                    console.error('Error fetching AD groups:', error);
                });
        },


        fetchGroupRole(group) {
            const authToken = sessionStorage.getItem('token');
            if (!authToken) {
                console.error('User is not authenticated');
                return;
            }

            const headers = {
                'Authorization': `Token ${authToken}`,
                'Content-Type': 'application/json'
            };

            axios
                .get(`${this.apiUrl}/api/v1/fetch-group-role/${encodeURIComponent(group.group_name)}/`, { headers })
                .then(response => {
                    if (response.data.success) {
                        if (response.data.role_name) {
                            this.selectedRole = response.data.role_name; // Set selected role to the returned role name
                        } else {
                            console.error('No role found for the group:', group.group_name);
                        }
                    } else {
                        console.error('Error fetching group role:', response.data.message);
                    }
                })
                .catch(error => {
                    console.error('Error fetching group role:', error);
                });
        },



        toggleMembers(group) {
            group.showMembers = !group.showMembers;
        },
        prepareAssignRoles(group) {
            this.selectedGroup = group;
            this.selectedRole = group.assignedRole || ''; // Set selected role to the assigned role for the group, if available

            // Fetch the role for the selected group (optional)
            this.fetchGroupRole(group);

            this.isModalVisible = true; // Show the modal
        },

        assignGroupRoles() {
            if (!this.selectedGroup || !this.selectedRole) {
                console.error('Group or role not selected.');
                return;
            }

            const authToken = sessionStorage.getItem('token'); // Get the token from sessionStorage

            if (!authToken) {
                console.error('Token not found in session storage.');
                return;
            }

            const headers = {
                'Authorization': `Token ${authToken}`,
                'Content-Type': 'application/json'
            };

            axios
                .post(`${this.apiUrl}/api/v1/assign-role-group/`, {
                    group_name: this.selectedGroup.group_name,
                    role_name: this.selectedRole,
                    sAMAccountNames: this.selectedGroup.members,
                }, {
                    headers: headers // Pass headers in the request
                })
                .then(response => {
                    if (response.data.success) {
                        this.selectedGroup.assignedRole = this.selectedRole; // Update assignedRole in adGroups
                        this.closeModal(); // Hide the modal after role assignment
                    } else {
                        console.error('Error assigning role:', response.data.message);
                    }
                })
                .catch(error => {
                    console.error('Error assigning role:', error);
                });
        },
        closeModal() {
            this.selectedRole = ''; // Reset selected role
            this.isModalVisible = false; // Hide the modal
        },
    },
};
</script>

<style scoped>
.group-name {
    cursor: pointer;
}

.group-name:hover {
    color: blue;
}

.modal.show {
    display: block !important;
}

.dark-mode {
    background-color: #111c44;
    color: #ffffff;
}
.close-dark {
  color: white !important;
}
</style>
