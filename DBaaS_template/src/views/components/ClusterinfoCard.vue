<template>
  <div class="card mt-4">
    <div class="card-header pb-0 p-3">
      <div class="row">
        <div class="col-6 d-flex align-items-center">
          <h6 class="mb-0 text-md">Create Cluster</h6>
        </div>
      </div>
    </div>
    <div class="card-body p-3">
      <div class="row">
        <div class="col-md-13 mb-md-0 mb-4">
          <div class="card card-body border card-plain border-radius-lg d-flex align-items-center flex-row">
            <div>
              <ul class="nav justify-content-center mt-4">
                <!-- Adjust mt-4 for the desired top space -->
                <li class="nav-item">
                  <router-link class="nav-link" :class="getRoute() === 'Cluster-Create'
                      ? 'text-success'
                      : 'text-muted'
                    " to="/Cluster-Create">Cluster Info</router-link>
                  <hr :class="getRoute() === 'Cluster-Create'
                      ? 'text-success'
                      : 'text-muted'
                    " />
                </li>&nbsp; &nbsp; &nbsp;
                <li class="nav-item" v-if="providerName !== 'Harvester'">
                  <router-link to="/Cconfiguration" class="nav-link " :class="getRoute() === 'Cconfiguration'
                      ? 'text-success'
                      : 'text-muted'
                    ">DB Configuration </router-link>
                  <hr :class="getRoute() === 'Cconfiguration'
                      ? 'text-success'
                      : 'text-muted'
                    " />
                </li>&nbsp; &nbsp; &nbsp;
                <li class="nav-item">
                  <router-link class="nav-link" :class="getRoute() === 'Cluster-Setting'
                      ? 'text-success'
                      : 'text-muted'
                    " to="/Cluster-Setting">Cluster Settings</router-link>
                  <hr :class="getRoute() === 'Cluster-Setting'
                      ? 'text-success'
                      : 'text-muted'
                    " />
                </li>
                &nbsp; &nbsp; &nbsp;
                <li class="nav-item">
                  <router-link to="" class="nav-link " :class="getRoute() === ''
                      ? 'text-success'
                      : 'text-muted'
                    ">Additional Settings </router-link>
                  <hr :class="getRoute() === ''
                      ? 'text-success'
                      : 'text-muted'
                    " />
                </li>
              </ul>
            </div>
            <!-- <img class="w-10 me-3 mb-0" src="@/assets/img/logos/mastercard.png" alt="logo" /> -->
            <!-- <h6 class="mb-0">****&nbsp;&nbsp;&nbsp;****&nbsp;&nbsp;&nbsp;****&nbsp;&nbsp;&nbsp;7852</h6> -->
            <!-- <i
              class="fas fa-pencil-alt ms-auto text-dark cursor-pointer"
              data-bs-toggle="tooltip"
              data-bs-placement="top"
              title
              aria-hidden="true"
              data-bs-original-title="Edit Card"
              aria-label="Edit Card"
            ></i> -->
            <!-- <span class="sr-only">Edit Card</span> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
// import argonButton from "@/components/BB_Button.vue";
import img1 from "@/assets/img/logos/mastercard.png";
import img2 from "@/assets/img/logos/visa.png";
import { mapState } from 'vuex';
export default {
  name: "payment-card",
  components: {
    // argonButton,
  },
  computed: {
    ...mapState(['providerName']),
  },
  data() {
    return {
      img1,
      img2,
    };
  },
  methods: {
    getRoute() {
      const routeArr = this.$route.path.split("/");
      return routeArr[1];
    },
  },
};
</script>
<style scoped>
.hr_style {
  border: 1px solid green;
}
</style>
