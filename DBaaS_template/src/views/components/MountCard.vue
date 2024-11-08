<template>
    <div v-if="successMessage" class="alert alert-success mb-3">
        <!-- Show success message when backup is completed -->
        <div class="text-center">
            {{ successMessage }}
        </div>
    </div>
    <div class="card">
        <div class="card-header pb-0 px-3">
            <h6 class="mb-0">Backup Method</h6>
        </div>

        <div class="card-body pt-4 p-3">

            <ul class="list-group">
                <li class="list-group-item border-0  p-4 mb-2 bg-gray-100 border-radius-lg">
                    <div class="row gx-4 my-2 py-4">
                        <div class="d-flex justify-content-between align-items-center w-100">
                            <div class="d-flex">
                                <svg :fill="svgFillColor" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg"
                                    xmlns:xlink="http://www.w3.org/1999/xlink" width="40px" height="40px"
                                    viewBox="0 0 165.26 165.26" xml:space="preserve">
                                    <g>
                                        <g>
                                            <path d="M153.829,72.723c-2.879-10.314-11.098-17.819-20.893-17.819c-0.114,0-0.217,0.035-0.328,0.041
            c-1.574-19.6-15.573-34.999-32.797-34.999c-9.693,0-18.334,4.952-24.396,12.693c-3.822-3.689-8.662-5.998-14.003-5.998
            c-11.99,0-21.707,11.168-22.024,25.053c-2.102-0.93-4.361-1.502-6.743-1.502c-10.563,0-19.119,9.978-19.119,22.284
            C6.052,72.477,0,79.531,0,88.235c0,8.702,6.052,15.754,13.527,15.754c0.285,0,11.812,0,28.08,0V88.248
            c0-10.688,8.696-19.38,19.382-19.38h6.595c2.986-6.982,9.934-11.806,17.77-11.806h18.922c10.694,0,19.382,8.689,19.382,19.376
            v24.591c0,1.007-0.203,1.981-0.354,2.955c16.463,0,28.184,0,28.431,0c7.475,0,13.526-7.06,13.526-15.759
            C165.26,80.367,160.297,73.9,153.829,72.723z" />
                                            <rect x="59.032" y="88.739" width="26.2" height="2.95" />
                                            <rect x="59.032" y="101.867" width="20.183" height="2.948" />
                                            <rect x="59.032" y="114.979" width="20.183" height="2.948" />
                                            <rect x="59.032" y="128.1" width="26.2" height="2.955" />
                                            <path d="M104.274,62.671H85.353c-6.917,0-12.61,5.149-13.574,11.806H60.988c-7.6,0-13.779,6.186-13.779,13.771v43.293
            c0,7.596,6.179,13.773,13.779,13.773h35.417c7.596,0,13.773-6.178,13.773-13.773v-18.14c4.635-2.21,7.863-6.889,7.863-12.36
            V76.444C118.054,68.852,111.881,62.671,104.274,62.671z M106.246,131.547c0,5.423-4.401,9.84-9.833,9.84H60.995
            c-5.437,0-9.842-4.417-9.842-9.84V88.258c0-5.428,4.405-9.841,9.842-9.841h35.418c5.432,0,9.833,4.413,9.833,9.841V131.547z
             M114.124,101.041c0,3.2-1.565,6.029-3.938,7.825V88.258c0-7.595-6.186-13.775-13.773-13.775H75.724
            c0.915-4.481,4.881-7.871,9.641-7.871h18.92c5.431,0,9.847,4.416,9.847,9.838v24.591H114.124z" />
                                        </g>
                                    </g>
                                </svg>
                                <h4 class="mx-5">NFS</h4>
                            </div>
                            <div class="d-flex">
                                <div class="mx-5" :class="{ 'text-success': !isDarkMode, 'text-info': isDarkMode }"
                                    v-if="nfsMountpoints.length > 0">
                                    Connected
                                </div>
                                <div class="mx-5" :class="{ 'text-danger': !isDarkMode, 'text-info': isDarkMode }"
                                    v-else>
                                    Not Connected
                                </div>
                                <a @click="toggleOptions()">
                                    <svg width="30px" height="30px" viewBox="0 0 16 16"
                                        xmlns="http://www.w3.org/2000/svg" :fill="svgFillColor"
                                        class="bi bi-three-dots-vertical">
                                        <path
                                            d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z" />
                                    </svg>
                                </a>

                            </div>
                        </div>
                    </div>
                    <div v-show='showDropdown' class="z-100 text-end">
                        <div>
                            <div><a data-toggle="modal" class="cursor" id="link" data-target="#mountnfsModal">Mount
                                    NFS</a></div>
                            <div><a data-toggle="modal" class="cursor" id="link" data-target="#nfsviewModal"
                                    @click="listMountpoints()">View
                                    NFS</a>
                            </div>
                            <div><a data-toggle="modal" class="cursor" id="link" data-target="#nfsModal">Unmount NFS</a>
                            </div>

                        </div>
                    </div>
                    <div class="row gx-4  my-2 py-4">
                        <div class="d-flex justify-content-between align-items-center w-100">
                            <div class="d-flex">
                                <svg :fill="svgFillColor" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg"
                                    xmlns:xlink="http://www.w3.org/1999/xlink" width="40px" height="40px"
                                    viewBox="0 0 165.26 165.26" xml:space="preserve">
                                    <g>
                                        <g>
                                            <path d="M153.829,72.723c-2.879-10.314-11.098-17.819-20.893-17.819c-0.114,0-0.217,0.035-0.328,0.041
            c-1.574-19.6-15.573-34.999-32.797-34.999c-9.693,0-18.334,4.952-24.396,12.693c-3.822-3.689-8.662-5.998-14.003-5.998
            c-11.99,0-21.707,11.168-22.024,25.053c-2.102-0.93-4.361-1.502-6.743-1.502c-10.563,0-19.119,9.978-19.119,22.284
            C6.052,72.477,0,79.531,0,88.235c0,8.702,6.052,15.754,13.527,15.754c0.285,0,11.812,0,28.08,0V88.248
            c0-10.688,8.696-19.38,19.382-19.38h6.595c2.986-6.982,9.934-11.806,17.77-11.806h18.922c10.694,0,19.382,8.689,19.382,19.376
            v24.591c0,1.007-0.203,1.981-0.354,2.955c16.463,0,28.184,0,28.431,0c7.475,0,13.526-7.06,13.526-15.759
            C165.26,80.367,160.297,73.9,153.829,72.723z" />
                                            <rect x="59.032" y="88.739" width="26.2" height="2.95" />
                                            <rect x="59.032" y="101.867" width="20.183" height="2.948" />
                                            <rect x="59.032" y="114.979" width="20.183" height="2.948" />
                                            <rect x="59.032" y="128.1" width="26.2" height="2.955" />
                                            <path d="M104.274,62.671H85.353c-6.917,0-12.61,5.149-13.574,11.806H60.988c-7.6,0-13.779,6.186-13.779,13.771v43.293
            c0,7.596,6.179,13.773,13.779,13.773h35.417c7.596,0,13.773-6.178,13.773-13.773v-18.14c4.635-2.21,7.863-6.889,7.863-12.36
            V76.444C118.054,68.852,111.881,62.671,104.274,62.671z M106.246,131.547c0,5.423-4.401,9.84-9.833,9.84H60.995
            c-5.437,0-9.842-4.417-9.842-9.84V88.258c0-5.428,4.405-9.841,9.842-9.841h35.418c5.432,0,9.833,4.413,9.833,9.841V131.547z
             M114.124,101.041c0,3.2-1.565,6.029-3.938,7.825V88.258c0-7.595-6.186-13.775-13.773-13.775H75.724
            c0.915-4.481,4.881-7.871,9.641-7.871h18.92c5.431,0,9.847,4.416,9.847,9.838v24.591H114.124z" />
                                        </g>
                                    </g>
                                </svg>
                                <h4 class="mx-5">S3</h4>
                            </div>
                            <div class="d-flex">
                                <div class="mx-5" :class="{ ' text-success': !isDarkMode, 'text-info': isDarkMode }"
                                    v-if="s3Mountpoints.length > 0">
                                    Connected
                                </div>
                                <div class="mx-5" :class="{ 'text-danger': !isDarkMode, 'text-info': isDarkMode }"
                                    v-else>
                                    Not Connected
                                </div>
                                <a @click="toggleOptions1()">
                                    <svg width="30px" height="30px" viewBox="0 0 16 16"
                                        xmlns="http://www.w3.org/2000/svg" :fill="svgFillColor"
                                        class="bi bi-three-dots-vertical">
                                        <path
                                            d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z" />
                                    </svg></a>
                            </div>
                        </div>
                    </div>
                    <div v-show='showDropdown1' class="z-100 text-end">
                        <div>
                            <div><a data-toggle="modal" class="cursor" id="link" data-target="#mounts3Modal">Mount
                                    S3</a></div>
                            <div><a data-toggle="modal" class="cursor" id="link" data-target="#s3viewModal"
                                    @click="listMountpoints()">View
                                    S3</a></div>
                            <div><a data-toggle="modal" class="cursor" id="link" data-target="#s3Modal">Unmount S3</a>
                            </div>

                        </div>
                    </div>
                </li>
            </ul>

        </div>

    </div>
    <!-- Mount Modal for nfs-->
    <div class="modal fade" id="mountnfsModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Mount NFS</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close" :class="{ 'close-dark': this.$store.state.darkMode }">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form>
                        <div>
                            <div class="form-group mt-3">
                                <label class="text-sm" for="">Remote Host</label>
                                <bb-input v-model="remote_host" type="email" class="" id="remote_host"
                                    placeholder="Remote Host" />
                            </div>
                            <div class="form-group mt-3">
                                <label class="text-sm" for="">Remote Path</label>
                                <bb-input v-model="remote_path" type="email" class="" id="remote_path"
                                    placeholder="Remote Path" />
                            </div>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-danger" data-dismiss="modal" @click="MountNFS()">
                        Mount</button>
                </div>
            </div>
        </div>
    </div>
    <!-- Mount Modal for s3-->
    <div class="modal fade" id="mounts3Modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Mount S3</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close" :class="{ 'close-dark': this.$store.state.darkMode }">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form>
                        <div>
                            <div class="form-group mt-3">
                                <label class="text-sm" for="">Bucket Name</label>
                                <bb-input v-model="bucket_name" type="email" class="" id="bucket_name"
                                    placeholder="Bucket Name" />
                            </div>
                            <div class="form-group mt-3">
                                <label class="text-sm" for="">Access Key</label>
                                <bb-input v-model="access_key" type="email" class="" id="access_key"
                                    placeholder="Access Key" />
                            </div>
                            <div class="form-group mt-3">
                                <label class="text-sm" for="">Secret Key</label>
                                <bb-input v-model="secret_key" type="email" class="" id="secret_key"
                                    placeholder="Secret Key" />
                            </div>
                            <div class="form-group mt-3">
                                <label class="text-sm" for="">URL</label>
                                <bb-input v-model="url" type="email" class="" id="url" placeholder="URL" />
                            </div>
                        </div>
                    </form>

                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-danger" data-dismiss="modal" @click="MountS3()"> Mount</button>
                </div>
            </div>
        </div>
    </div>
    <!-- nfs View Modal -->
    <div class="modal fade" id="nfsviewModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Mount Details</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close" :class="{ 'close-dark': this.$store.state.darkMode }">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body" v-for="nfs in nfsMountpoints" :key="nfs.host_path">
                    <div><b>Host Name: </b>{{ nfs.host_path }}</div>
                    <div><b>Mount Point: </b>{{ nfs.mount_point }}</div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>

                </div>
            </div>
        </div>
    </div>
    <!-- s3 View Modal -->
    <div class="modal fade" id="s3viewModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Mount Details</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close" :class="{ 'close-dark': this.$store.state.darkMode }">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body" v-for="s3 in s3Mountpoints" :key="s3.access_key">
                    <div><b>Access Key: </b>{{ s3.access_key }}</div>
                    <div><b>Secret Key: </b>{{ s3.secret_key }}</div>
                    <div><b>Mount Point: </b>{{ s3.mount_point }}</div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>

                </div>
            </div>
        </div>
    </div>
    <!-- Unmount Modal for nfs-->
    <div class="modal fade" id="nfsModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Unmount NFS</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close" :class="{ 'close-dark': this.$store.state.darkMode }">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    Are You Sure Want to unmount NFS !!
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-danger" data-dismiss="modal" @click="unmountNFS">
                        Unmount</button>
                </div>
            </div>
        </div>
    </div>
    <!-- Unmount Modal for s3-->
    <div class="modal fade" id="s3Modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Unmount S3</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close" :class="{ 'close-dark': this.$store.state.darkMode }">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    Are You Sure Want to unmount S3 !!
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-danger" data-dismiss="modal" @click="unmountS3">
                        Unmount</button>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import BbInput from "../../components/BB_Input.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';
import axios from "axios";
export default {
    name: "backup-card",
    components: { BbInput },
    data() {
        return {
            remote_host: '',
            remote_path: '',
            bucket_name: '',
            access_key: '',
            secret_key: '',
            url: '',
            loading: false, // Track loading state
            successMessage: "", // Success message
            errorMessage: '',
            apiUrl: API_ENDPOINT,
            username: '',
            showDropdown: false,
            showDropdown1: false,
            nfsMountpoints: [],
            s3Mountpoints: [],
        };
    },
    created() {
        this.username = sessionStorage.getItem('username');
        this.listMountpoints();
    },
    computed: {

        svgFillColor() {
            return this.$store.state.darkMode ? '#ffffff' : '#000000';
        },

        isDarkMode() {
            return this.$store.state.darkMode;
        }
    },
    methods: {
        toggleOptions() {
            this.showDropdown = !this.showDropdown;
            this.showDropdown1 = false;
        },
        toggleOptions1() {
            this.showDropdown1 = !this.showDropdown1;
            this.showDropdown = false;
        },

        MountNFS() {
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
            axios.post(
                `${this.apiUrl}/api/v1/barman/mount-nfs?remote_host=${this.remote_host}&remote_path=${this.remote_path}`,{},
                { headers }
            )
                .then(() => {
                    this.successMessage = "NFS mount successfully";
                    setTimeout(() => {
                        this.successMessage = ''
                    }, 5000);
                    this.listMountpoints();
                })
                .catch((error) => {
                    console.error('Error mounting nfs:', error);
                })
                .finally(() => {
                    this.loading = false;
                    this.closeModal();
                });
        },
        MountS3() {
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
            axios.post(
                `${this.apiUrl}/api/v1/barman/mount-s3?bucket_name=${this.bucket_name}&access_key=${this.access_key}&secret_key=${this.secret_key}&url=${this.url}`,{},
                { headers }
            )
                .then(() => {
                    this.successMessage = "S3 mount successfully";
                    setTimeout(() => {
                        this.successMessage = ''
                    }, 5000);
                    this.listMountpoints();
                })
                .catch((error) => {
                    console.error('Error mounting s3:', error);
                })
                .finally(() => {
                    this.loading = false;
                    this.closeModal();
                });
        },
        unmountNFS() {
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
            axios.post(
                `${this.apiUrl}/api/v1/barman/unmount?storage_method=nfs`,{}, { headers }
            )
                .then(() => {
                    this.successMessage = "NFS unmount successfully";
                    setTimeout(() => {
                        this.successMessage = ''
                    }, 5000);
                    this.listMountpoints();
                })
                .catch((error) => {
                    console.error('Error mounting s3:', error);
                })
                .finally(() => {
                    this.loading = false;
                    this.closeModal();
                });
        },
        unmountS3() {
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
            axios.post(
                `${this.apiUrl}/api/v1/barman/unmount?storage_method=s3`,{}, { headers }
            )
                .then(() => {
                    this.successMessage = "S3 unmount successfully";
                    setTimeout(() => {
                        this.successMessage = ''
                    }, 5000);
                    this.listMountpoints();
                })
                .catch((error) => {
                    console.error('Error mounting s3:', error);
                })
                .finally(() => {
                    this.loading = false;
                    this.closeModal();
                });
        },
        listMountpoints() {
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
            axios.get(
                `${this.apiUrl}/api/v1/barman/list-mount-points`, { headers }
            )
                .then((response) => {
                    this.nfsMountpoints = response.data.nfs_mount_points;
                    this.s3Mountpoints = response.data.s3_mount_points;

                })
                .catch((error) => {
                    console.error('Error mounting s3:', error);
                })
                .finally(() => {
                    this.loading = false;
                });
        },

        clearErrorMessageAfterDelay(delay) {
            setTimeout(() => {
                this.errorMessage = "";
            }, delay);
        },

        closeModal() {
            this.isOpen = false; // Close modal using jQuery
        },
    },
};
</script>

<style scoped>
.cursor {
    cursor: pointer;

}

#link:hover {
    color: rgb(42, 235, 42);
}

.dark-mode {
    background-color: #111c44;
    color: #ffffff;
}
.close-dark {
    color: white !important;
}
</style>