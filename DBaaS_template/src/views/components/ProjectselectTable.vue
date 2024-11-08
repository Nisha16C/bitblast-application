<template>
    <div class="card">
        <div class="card-header pb-0">
            <h6> Selected Projects Info : {{ project_name }} </h6>
        </div>

        <div class="card-body px-0 pt-0 pb-2">
            <div class="table-responsive p-0">
                <table class="table align-items-center mb-0">
                    <thead>
                        <tr>
                            <th class="text-uppercase text-secondary font-weight-bolder opacity-7"> Select</th>
                            <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                                project id & Name</th>
                            <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                                CREATE DATE </th>
                            <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                                Update Date </th>
                            <th class="text-secondary opacity-7"> </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(project, index) in projects" :key="index">
                            <td>
                                <button @click="selectProject(project)" class="btn  mb-0  btn-info">Select</button>
                            </td>
                            <td>
                                <div class="d-flex flex-column text-center">
                                    <h6 class="mb-0 text-sm">{{ project.id }}</h6>
                                    {{ project.project_name }}
                                </div>
                            </td>
                            <td>
                                <div class="d-flex flex-column text-center">
                                    {{ formatDate(project.created_date) }}
                                </div>
                            </td>
                            <td class="align-middle text-center">
                                <span class="d-flex flex-column text-center">{{ formatDate(project.updated_date) }}</span>
                            </td>
                            <td class="align-middle  text-center">
                                <span v-if="isSelected(project.project_name)"
                                    class="d-flex flex-column text-center text-success"><svg width="50px" height="50px" viewBox="0 0 24 24" id="_24x24_On_Light_Checkmark" data-name="24x24/On Light/Checkmark" xmlns="http://www.w3.org/2000/svg" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <rect id="view-box" width="24" height="24" fill="#141124" opacity="0"></rect> <path id="Shape" d="M5.341,12.247a1,1,0,0,0,1.317,1.505l4-3.5a1,1,0,0,0,.028-1.48l-9-8.5A1,1,0,0,0,.313,1.727l8.2,7.745Z" transform="translate(19 6.5) rotate(90)" fill="#2dce89"></path> </g></svg></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>


        </div>
    </div>
</template>
  
<script>
import { mapState, mapActions } from 'vuex';

export default {
    name: "projects-table",
    props: {
        projects: {
            type: Array,
            required: true,
        },
    },
    created() {
        // this.updateGlobalProjectName()
    },
    data() {
        return {
            currentProject: '',
        }
    },

    computed: {
        ...mapState(['project_name', 'project_id']),
    },
    methods: {
        ...mapActions(['updateGlobalProjectName', 'updateGlobalProjectId']),
        async selectProject(project) {
            try {
                await this.updateGlobalProjectName(project.project_name);

                await this.updateGlobalProjectId(project.id);
            } catch (error) {
                console.error(error);
            }
        },

        isSelected(projectName) {
            if (this.project_name === projectName) {
                return true
            } else {
                return false;
            }

        },

        formatDate(dateString) {
            const options = { year: 'numeric', month: 'short', day: 'numeric' };
            return new Date(dateString).toLocaleDateString('en-US', options);
        },

    },
};
</script>
    