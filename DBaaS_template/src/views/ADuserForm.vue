<template>

    <main>

        <div class="container-fluid mt-7">

            <div class="card shadow-lg mt-n6">

                <div class="card-body p-3">

                    <div class="row gx-4">

                        <div class="col-auto my-auto">

                            <div class="d-flex align-items-center h-100">
                                <router-link to="/ADauthprovider">
                                    <i class="fas fa-arrow-left mr-2"></i>
                                </router-link>

                                <h3 class="mb-1 ml-3">Authentication Provider: Active Directory <span class="badge badge-sm"
                                        :class="{ 'bg-green': status === 'Active', 'bg-red': status === 'Inactive' }">{{
                                            status }}</span></h3>

                            </div>

                        </div>
                    </div>

                </div>

            </div>

        </div>

        <div class="py-4 container-fluid">

            <div class="row">

                <div class="col-md-12">

                    <div class="card">

                        <div class="card-body">

                            <p :class="`${this.$store.state.darkMode ? 'w-background' : 'y-background'}`"
                                class="text-sm">The Active Directory authentication provider is

                                currently Disable.</p>

                            <hr>

                            <form @submit.prevent="submitForm">

                                <div class="row">

                                    <h4>Configure an Active Directory account</h4> <br>

                                    <hr>

                                    <div class="col-md-6">

                                        <label class="form-control-label">Server URI <span
                                                class="warning">*</span></label>

                                        <argon-input v-model="ldapServerURI" type="text"
                                            placeholder="ldap://0.0.0.0:Port" @input="validateServerURI" />

                                        <!-- Display error message if Server URI format is invalid -->

                                        <p v-if="errors.ldapServerURI" class="text-danger">{{ errors.ldapServerURI }}

                                        </p>

                                    </div>

                                    <div class="col-md-6">
                                        <label class="form-control-label">Server Connection Timeout (milliseconds)
                                            <span class="warning">*</span></label>
                                        <argon-input v-model="serverConnectionTimeout" type="text" value="10000" />
                                        <p v-if="errors.serverConnectionTimeout" class="text-danger">{{
                                            errors.serverConnectionTimeout }}</p>
                                    </div>

                                    <div class="col-md-6">
                                        <label class="form-control-label">Service Account Distinguished Name <span
                                                class="warning">*</span></label>
                                        <argon-input v-model="ServiceAccountDistinguishedName" type="text"
                                            placeholder="Service Account Name " />
                                        <p v-if="errors.ServiceAccountDistinguishedName" class="text-danger">{{
                                            errors.ServiceAccountDistinguishedName }}</p>
                                    </div>

                                    <div class="col-md-6">
                                        <label for="last_name" class="form-control-label">Service Account Password
                                            <span class="warning">*</span></label>
                                        <argon-input v-model="ServiceAccountPassword" type="password" placeholder="" />
                                        <p v-if="errors.ServiceAccountPassword" class="text-danger">{{
                                            errors.ServiceAccountPassword }}</p>
                                    </div>

                                    <div class="col-md-12">
                                        <label for="username" class="form-control-label">Default Login Domain <span
                                                class="warning">*</span></label>
                                        <argon-input v-model="DefaultLoginDomain" type="text"
                                            placeholder="eg:mycompany" />
                                        <p v-if="errors.DefaultLoginDomain" class="text-danger">{{
                                            errors.DefaultLoginDomain }}</p>
                                    </div>

                                    <div class="col-md-6">
                                        <label for="phone" class="form-control-label">User Search Base <span
                                                class="warning">*</span></label>
                                        <argon-input v-model="ldapServerBIND_DN" type="text"
                                            placeholder="e.g.ou=users,dc=mycompany,dc=com" />
                                        <p v-if="errors.ldapServerBIND_DN" class="text-danger">{{
                                            errors.ldapServerBIND_DN }}</p>
                                    </div>

                                    <div class="col-md-6">
                                        <label for="group_search_base" class="form-control-label">Group Search Base
                                            <span class="warning">*</span></label>
                                        <argon-input v-model="ldapGroupSearch" type="text"
                                            placeholder="e.g. ou=groups,dc=mycompany,dc=com" />
                                        <p v-if="errors.ldapGroupSearch" class="text-danger">{{ errors.ldapGroupSearch
                                            }}</p>
                                    </div>

                                    <h4>Customize Schema</h4> <br>

                                    <hr>

                                    <!-- Users -->

                                    <div class="col-md-6">

                                        <h6>Users</h6>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">Object Class

                                            </label>

                                            <argon-input v-model="userObjectClass" type="text" value="person" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">Username

                                                Attribute</label>

                                            <argon-input v-model="usernameAttribute" type="text" value="name" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">Login

                                                Attribute</label>

                                            <argon-input v-model="userLoginAttribute" type="text"
                                                value="sAMAccountName" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">User Member

                                                Attribute</label>

                                            <argon-input v-model="userMemberAttribute" type="text"
                                                placeholder="e.g.ou=users,dc=mycompany,dc=com" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">Search

                                                Attribute</label>

                                            <argon-input v-model="userData.m11" type="text"
                                                value="sAMAccountName|sn|givenName" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">Search Filter

                                            </label>

                                            <argon-input v-model="userSearchFilter" type="text" placeholder="" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">User Enable

                                                Attribute</label>

                                            <argon-input v-model="userEnableAttribute" type="text"
                                                value="userAccountControl" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">Disabled Status

                                                Bitmask</label>

                                            <argon-input v-model="disabledStatusBitmask" type="text" value="2" />

                                        </div>

                                    </div>
                                    <!-- Groups -->

                                    <div class="col-md-6">

                                        <h6>Groups</h6>

                                        <div class="col-md-12">

                                            <label class="form-control-label">Object Class

                                            </label>

                                            <argon-input v-model="groupObjectClass" type="text" value="group" />

                                        </div>

                                        <div class="col-md-12">

                                            <label class="form-control-label">Name

                                                Attribute</label>

                                            <argon-input v-model="groupNameAttribute" type="text" value="name" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="group_search_base" class="form-control-label">Group Member User

                                                Attribute</label>

                                            <argon-input v-model="groupMemberUserAttribute" type="text"
                                                value="distinguishedName" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="group_search_base" class="form-control-label">Search

                                                Attribute</label>

                                            <argon-input v-model="groupSearchAttribute" type="text"
                                                value="sAMAccountName" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="group_search_base" class="form-control-label">Search

                                                Filter</label>

                                            <argon-input v-model="groupSearchFilter" type="text" placeholder="" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="group_search_base" class="form-control-label">Group Member

                                                Mapping

                                                Attribute</label>

                                            <argon-input v-model="groupMamberMappingAttribute" type="text"
                                                value="member" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="group_search_base" class="form-control-label">Group DN

                                                Attribute</label>

                                            <argon-input v-model="groupDNattribute" type="text"
                                                value="distinguishedName" />

                                        </div><br>

                                        <div class="col-md-12">

                                            <input type="radio" /> Search direct and nested group memberships

                                            <br><input type="radio" /> Search only direct group memberships

                                        </div>

                                    </div>

                                    <h4>Test and Enable Authentication</h4> <br>

                                    <hr>

                                    <div class="col-md-6">

                                        <label class="form-control-label">Username <span
                                                class="warning">*</span></label>

                                        <argon-input v-model="testUsername" type="text" placeholder="username" />
                                        <p v-if="errors.testUsername" class="text-danger">{{
                                            errors.testUsername }}</p>

                                    </div>

                                    <div class="col-md-6">

                                        <label class="form-control-label">Password <span
                                                class="warning">*</span></label>

                                        <argon-input v-model="ldapServerBIND_PASSWORD" type="password"
                                            placeholder="password" />
                                        <p v-if="errors.ldapServerBIND_PASSWORD" class="text-danger">{{
                                            errors.ldapServerBIND_PASSWORD }}</p>

                                    </div>

                                    <div class="modal-footer">

                                        <BB_Button color="danger" size="md" variant="gradient"
                                            @click.prevent="OpenstackModal">

                                            Cancel

                                        </BB_Button>

                                        <BB_Button color="success" size="md" variant="gradient" v-model="True"
                                            @click.prevent="submitForm">

                                            Enable

                                        </BB_Button>

                                    </div>
                                    <div v-if="successMessage" class="alert alert-text-success mb-3">
                                        <!-- Show success message when backup is completed -->
                                        <div class="text-center text-success">{{ successMessage }}</div>
                                    </div>
                                    <div v-if="errorMessage" class="alert alert-text-danger mb-3">
                                        <div class="text-center text-danger">{{ errorMessage }}</div>
                                    </div>

                                    <div v-if="loading" class="text-center">
                                        <!-- Show loader while loading -->
                                        <h6 class="mb-2">
                                            Loading...
                                        </h6>
                                        <div class="spinner-border spinner-border-lg p-3 text-secondary" role="status">
                                            <span class="visually-hidden">Loading...</span>
                                        </div>
                                    </div>

                                </div>

                            </form>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </main>

</template>

[12:51] Nisha Chaurasiya
<script>

import setNavPills from "@/assets/js/nav-pills.js";

import setTooltip from "@/assets/js/tooltip.js";

import ArgonInput from "@/components/BB_Input.vue";

import BB_Button from "@/components/BB_Button.vue";

import { API_ENDPOINT } from '@/../apiconfig.js';

import axios from 'axios';

const body = document.getElementsByTagName("body")[0];

export default {

    name: "USER",

    data() {

        return {

            apiUrl: API_ENDPOINT,

            showMenu: false,

            ldapServerURI: "",

            userData: {

                first_name: '',

                username: '',

                email: '',

                phone: '',

                password: '',

                cpassword: '',

            },

            errors: {},

            successMessage: '',
            errorMessage: '',

            agreeTerms: false,

            ldapGroupSearch: '', // Initialize ldapGroupSearch data property
            serverConnectionTimeout: 10000,
            userObjectClass: 'person',
            usernameAttribute: 'name',
            userLoginAttribute: 'sAMAccountName',
            userSearchAttribute: 'sAMAccountName|sn|givenName',
            userEnableAttribute: 'userAccountControl',
            disabledStatusBitmask: 2, // Default value for Disabled Status Bitmask

            groupObjectClass: 'group',
            groupNameAttribute: 'name',
            groupMemberUserAttribute: 'distinguishedName',
            groupSearchAttribute: 'sAMAccountName',
            groupMamberMappingAttribute: 'member',
            groupDNattribute: 'distinguishedName',
            True: 'True',
            status: '',
            loading: false,
            // errors: {} // Object to track errors



        };

    },

    components: { ArgonInput, BB_Button },

    mounted() {
        this.fetchIsConnectedStatus();
        // Other mounted lifecycle actions
    },

    methods: {
        fetchIsConnectedStatus() {
            const token = sessionStorage.getItem('token'); // Or however you store your token
            if (!token) {
                console.error('No token found');
                this.status = 'Error';
                return;
            }

            axios.get(`${this.apiUrl}/api/v1/is-connected/`, {
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    if (response.status === 200 && response.data && response.data.is_connected) {
                        this.status = response.data.is_connected === 'True' ? 'Active' : 'Inactive';
                    } else {
                        console.error('Unexpected response format:', response);
                        this.status = 'Error';
                    }
                })
                .catch(error => {
                    console.error('Error fetching status:', error);
                    this.status = 'Error';
                });
        },

        // Method to handle form validation
        validateForm() {
            this.errors = {}; // Reset errors
            let isValid = true;

            const fieldsToValidate = [
                // { field: 'ldapServerURI', message: 'This field is required' },
                { field: 'serverConnectionTimeout', message: 'This field is required' },
                { field: 'ServiceAccountDistinguishedName', message: 'This field is required' },
                { field: 'ServiceAccountPassword', message: 'This field is required' },
                { field: 'DefaultLoginDomain', message: 'This field is required' },
                { field: 'ldapServerBIND_DN', message: 'This field is required' },
                { field: 'ldapGroupSearch', message: 'This field is required' },
                { field: 'testUsername', message: 'This field is required' },
                { field: 'ldapServerBIND_PASSWORD', message: 'This field is required' },

            ];

            fieldsToValidate.forEach(({ field, message }) => {
                if (!this[field]) {
                    this.errors[field] = message;
                    isValid = false;
                }
            });

            if (!isValid) {
                setTimeout(() => {
                    this.errors = {};
                }, 5000);
            }

            return isValid;
        },


        submitForm() {
            // Check if the Server URI is valid before submitting the form
            if (!this.isValidUri(this.ldapServerURI)) {
                this.errors.ldapServerURI = 'Please enter a valid Server URI in the format ldap://0.0.0.0:Port';
                return; // Prevent form submission if input is invalid
            }
            if (!this.validateForm()) {
                return; // Prevent form submission if validation fails
            }
            this.loading = true;

            // Retrieve token from session storage
            const token = sessionStorage.getItem('token');

            const formdata = {
                ldapServerURI: this.ldapServerURI,
                ldapServerBIND_DN: this.ldapServerBIND_DN,
                ldapServerBIND_PASSWORD: this.ldapServerBIND_PASSWORD,
                ldapGroupSearch: this.ldapGroupSearch,
                serverConnectionTimeout: this.serverConnectionTimeout,
                ServiceAccountDistinguishedName: this.tuy,
                DefaultLoginDomain: this.DefaultLoginDomain,
                userObjectClass: this.userObjectClass,
                usernameAttribute: this.usernameAttribute,
                userLoginAttribute: this.userLoginAttribute,
                userMemberAttribute: this.userMemberAttribute,
                userSearchAttribute: this.userSearchAttribute,
                userSearchFilter: this.userSearchFilter,
                userEnableAttribute: this.userEnableAttribute,
                disabledStatusBitmask: this.disabledStatusBitmask,
                // ------------ group ------------------------
                groupObjectClass: this.groupObjectClass,
                groupNameAttribute: this.groupNameAttribute,
                groupMemberUserAttribute: this.groupMemberUserAttribute,
                groupSearchAttribute: this.groupSearchAttribute,
                groupSearchFilter: this.groupSearchFilter,
                groupMamberMappingAttribute: this.groupMamberMappingAttribute,
                groupDNattribute: this.groupDNattribute,
                testUsername: this.testUsername,
                testPassword: this.testPassword,
                True: this.True,
            };

            axios.post(`${this.apiUrl}/api/v1/update_ldap_settings/`, formdata, {
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                }
            })
                .then(() => {
                    this.successMessage = "ADuser Enabled successfully, Please wait few seconds.";
                    setTimeout(() => {
                        this.$router.push("/ADsave");
                    }, 5000);
                })
                .catch(() => {
                    this.errorMessage = `error`
                    setTimeout(() => {
                        this.$router.push("/ADsave");
                    }, 1000);
                })
                .finally(() => {
                    this.loading = false; // Set loading to false regardless of success or failure
                });
        },


        // Method to validate Server URI input format using regular expression

        isValidUri(uri) {

            const uriPattern = /^ldap:\/\/\d+\.\d+\.\d+\.\d+:\d+$/;

            return uriPattern.test(uri);

        },

        // Method to validate Server URI on input

        validateServerURI() {

            if (!this.isValidUri(this.ldapServerURI)) {

                this.errors.ldapServerURI = 'Please enter a valid Server URI in the format ldap://0.0.0.0:Port';

            } else {

                this.errors.ldapServerURI = '';

            }

        },

        disableLDAP() {
            // Retrieve token from session storage
            const token = sessionStorage.getItem('token');

            axios.post(`${this.apiUrl}/api/v1/reset_ldap_settings/`, {}, {
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                }
            })
                .then(() => {
                    this.$router.push('/signin');
                    // handle success
                })
                .catch(error => {
                    console.error(error);
                    // handle error
                });
        },


        mounted() {


            this.$store.state.isAbsolute = true;

            setNavPills();

            setTooltip();

        },

        beforeMount() {

            this.$store.state.imageLayout = "profile-overview";

            this.$store.state.showNavbar = false;

            this.$store.state.showFooter = true;

            this.$store.state.hideConfigButton = true;

            body.classList.add("profile-overview");

        },

        beforeUnmount() {

            this.$store.state.isAbsolute = false;

            this.$store.state.imageLayout = "default";

            this.$store.state.showNavbar = true;

            this.$store.state.showFooter = true;

            this.$store.state.hideConfigButton = false;

            body.classList.remove("profile-overview");

        },

    },


};

</script>


<style scoped>
.warning {
    color: red;
    font-weight: bold;
}

.y-background {

    background-color: rgb(252, 252, 128);

    color: black;

}

.r-background {

    background-color: rgb(255, 183, 116);

    color: black;

}

.w-background {
    background-color: rgb(29, 31, 129);
    color: rgb(255, 255, 255);
}

.bg-green {
    background-color: green;
    border-radius: 20px;
}

.bg-red {
    background-color: red;
    border-radius: 20px;
}
</style>