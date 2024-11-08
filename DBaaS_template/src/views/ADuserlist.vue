<template>

    <main>

        <div class="container-fluid mt-7">

            <div class="card shadow-lg mt-n6">

                <div class="card-body p-3">

                    <div class="row gx-4">

                        <div class="col-auto my-auto">

                            <div class="h-100">

                                <h5 class="mb-1 text-2xl">List Of Active Directory Users</h5>

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

                        <div class="card-body ">

                            <h6 class="text-2xl">Active Directory Users Info</h6>

                            <div class="table-responsive p-0 mt-3">

                                <table class="table align-items-center mb-0">

                                    <thead>

                                        <tr>

                                            <th
                                                class="text-uppercase text-secondary text-md font-weight-bolder opacity-7">

                                                User Name

                                            </th>

                                        </tr>

                                    </thead>

                                    <tbody>

                                        <tr v-for="user in adUsers" :key="user.username">
                                            <td>
                                                <div>
                                                    <img :src="this.$store.state.darkMode || this.$store.state.sidebarType === 'bg-default' ? logoWhite : logo"
                                                        class="avatar avatar-sm me-3" />
                                                    {{ user }}
                                                </div>

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

    </main>

</template>

<script>
import { API_ENDPOINT } from '@/../apiconfig.js';
import logo from "@/assets/img/userTable.png";
import logoWhite from "@/assets/img/user.png";



export default {

    data() {

        return {
            apiUrl: API_ENDPOINT,


            adUsers: [],
            logo,
            logoWhite,

        };

    },

    created() {

        this.fetchADUsers();

    },

    methods: {

        fetchADUsers() {
            // Retrieve token from session storage
            const token = sessionStorage.getItem('token');

            fetch(`${this.apiUrl}/api/v1/ad-users/`, {
                method: 'GET',
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    // Update adUsers array with fetched data
                    this.adUsers = data.user_names;
                })
                .catch(error => {
                    console.error('Error fetching AD users:', error);
                });
        }


    }

};

</script>

<style scoped>
.custom-age {

    width: 300px;

    height: 150px;

}
</style>
