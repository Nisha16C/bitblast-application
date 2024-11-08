<template>
  <main>

    <div class="container-fluid py-10">

      <div v-if="loading" class="loading-container">
        <div class="text-center">
          <div class="spinner-border text-primary" role="status">
            <span class="visually-hidden">Loading...</span>
          </div>
          <div class="loading-text mt-2">Loading...</div>
        </div>
      </div>

      <div class="card  shadow-lg mt-n6 py-3">
        <div class="text-right p-2 m-2 ml-2">
          <router-link to="/providercard">
            <argon-button color="success" size="md" variant="gradient">Kubernetes Provider Details</argon-button>
          </router-link>
        </div>


        <div class="row mt-4 ml-5">

          <BB_Button @click.prevent="toggleModal('CloudStack')" v-if="isProviderEnabled('CloudStack')"
            class="btn col-lg-5 col-md-12 mx-5">

            <div class="card-body p-3">
              <div class="row gx-4">
                <div class="col-auto">
                  <div class="avatar avatar-xl position-relative">

                    <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/cloudstack.png " alt="CloudStack" />

                  </div>
                </div>

                <div class="col-auto my-auto">
                  <div class="h-100">
                    <h5 class="mb-1">CloudStack</h5>
                    <p class="mb-0 font-weight-bold text-sm"></p>
                  </div>
                </div>
                <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                  <div class="nav-wrapper position-relative end-0">
                    <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                      <li class="nav-item">
                        <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                          aria-selected="false">
                          <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('CloudStack')"
                            class="h-15 w-15 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                          </svg>
                          <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                            viewBox="0 0 100 100">
                            
                            <line x1="20" y1="20" x2="80" y2="80" stroke="currentColor" stroke-width="8" />
                            <line x1="20" y1="80" x2="80" y2="20" stroke="currentColor" stroke-width="8" />
                          </svg>
                          <div class="provider_stat">
                            <div class="text-green-500" v-if="isProviderConnected('CloudStack')">Connected</div>
                            <div class="text-red-500" v-else>Not Connected </div>
                          </div>
                        </a>
                      </li>

                    </ul>
                  </div>
                </div>



              </div>
            </div>

          </BB_Button>
          <!-- vmware -->

          <BB_Button @click.prevent="toggleModal('Vmware')" v-if="isProviderEnabled('Vmware')"
            class="btn col-lg-5 col-md-12 mx-5">


            <div class="card-body p-3">
              <div class="row gx-4">
                <div class="col-auto">
                  <div class="avatar avatar-xl position-relative">
                    <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/Vmware.png " alt="Vmware" />
                  </div>
                </div>

                <div class="col-auto my-auto">
                  <div class="h-100">
                    <h5 class="mb-1">VMware</h5>
                    <p class="mb-0 font-weight-bold text-sm"></p>
                  </div>
                </div>
                <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                  <div class="nav-wrapper position-relative end-0">
                    <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                      <li class="nav-item">
                        <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                          aria-selected="false">
                          <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Vmware')"
                            class="h-15 w-15 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                          </svg>
                          <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                            viewBox="0 0 100 100">
                            
                            <line x1="20" y1="20" x2="80" y2="80" stroke="currentColor" stroke-width="8" />
                            <line x1="20" y1="80" x2="80" y2="20" stroke="currentColor" stroke-width="8" />
                          </svg>
                          <div class="provider_stat">
                            <div class="text-green-500" v-if="isProviderConnected('Vmware')">Connected</div>
                            <div class="text-red-500" v-else>Not Connected </div>
                          </div>
                        </a>
                      </li>

                    </ul>
                  </div>
                </div>



              </div>
            </div>
          </BB_Button>
          <!--  -->
          <BB_Button @click.prevent="toggleModals('Kubernetes')" v-if="isProviderEnabled('Kubernetes')"
            class="btn col-lg-5 col-md-12 mx-5">
            <div class="card-body p-3">
              <div class="row gx-4">
                <div class="col-auto">
                  <div class="avatar avatar-xl position-relative">
                    <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/k8s.png " alt="Kubernetes" />
                  </div>
                </div>

                <div class="col-auto my-auto">
                  <div class="h-100">
                    <h5 class="mb-1">Kubernetes</h5>
                    <p class="mb-0 font-weight-bold text-sm"></p>
                  </div>
                </div>
                <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                  <div class="nav-wrapper position-relative end-0">
                    <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                      <li class="nav-item">
                        <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                          aria-selected="false">
                          <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Kubernetes')"
                            class="h-15 w-15 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                          </svg>
                          <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                            viewBox="0 0 100 100">
                            <!--  -->
                            <line x1="20" y1="20" x2="80" y2="80" stroke="currentColor" stroke-width="8" />
                            <line x1="20" y1="80" x2="80" y2="20" stroke="currentColor" stroke-width="8" />
                          </svg>
                          <div class="provider_stat">
                            <div class="text-green-500" v-if="isProviderConnected('Kubernetes')">Connected</div>
                            <div class="text-red-500" v-else>Not Connected</div>
                          </div>


                          <!-- <span class="ms-1">Connected</span> -->
                        </a>
                      </li>

                    </ul>
                  </div>
                </div>



              </div>
            </div>
          </BB_Button>
          <!-- d -->
          <!-- openstack -->
          <!-- <BB_Button @click.prevent="toggleModal('Openstack')" class="btn "> -->
          <BB_Button @click.prevent="OpenstackModal('OpenStack')" v-if="isProviderEnabled('OpenStack')"
            class="btn col-lg-5 col-md-12 mx-5">


            <div class="card-body p-3">
              <div class="row gx-4">
                <div class="col-auto">
                  <div class="avatar avatar-xl position-relative">
                    <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/Openstack.png " alt="OpenStack" />
                  </div>
                </div>

                <div class="col-auto my-auto">
                  <div class="h-100">
                    <h5 class="mb-1">OpenStack</h5>
                    <p class="mb-0 font-weight-bold text-sm"></p>
                  </div>
                </div>
                <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                  <div class="nav-wrapper position-relative end-0">
                    <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                      <li class="nav-item">
                        <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                          aria-selected="false">
                          <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('OpenStack')"
                            class="h-15 w-15 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                          </svg>
                          <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                            viewBox="0 0 100 100">
                            
                            <line x1="20" y1="20" x2="80" y2="80" stroke="currentColor" stroke-width="8" />
                            <line x1="20" y1="80" x2="80" y2="20" stroke="currentColor" stroke-width="8" />
                          </svg>
                          <div class="provider_stat">
                            <div class="text-green-500" v-if="isProviderConnected('OpenStack')">Connected</div>
                            <div class="text-red-500" v-else>Not Connected</div>
                          </div>


                          <!-- <span class="ms-1" v-if="isProviderConnected">Connected</span>
                        <span class="ms-1 v-else">Not connected</span> -->
                        </a>
                      </li>

                    </ul>
                  </div>
                </div>



              </div>
            </div>
          </BB_Button>
          <!-- harvester -->
          <BB_Button @click.prevent="toggleModal('Harvester')" v-if="isProviderEnabled('Harvester')"
            class="btn col-lg-5 col-md-12 mx-5">
            <div class="card-body p-3">
              <div class="row gx-4">
                <div class="col-auto">
                  <div class="avatar avatar-xl position-relative">
                    <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/harvester.jpg " alt="harvester" />
                  </div>
                </div>

                <div class="col-auto my-auto">
                  <div class="h-100">
                    <h5 class="mb-1">Harvester</h5>
                    <p class="mb-0 font-weight-bold text-sm"></p>
                  </div>
                </div>
                <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                  <div class="nav-wrapper position-relative end-0">
                    <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                      <li class="nav-item">
                        <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                          aria-selected="false">
                          <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Harvester')"
                            class="h-15 w-15 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                          </svg>
                          <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                            viewBox="0 0 100 100">
                            
                            <line x1="20" y1="20" x2="80" y2="80" stroke="currentColor" stroke-width="8" />
                            <line x1="20" y1="80" x2="80" y2="20" stroke="currentColor" stroke-width="8" />
                          </svg>
                          <div class="provider_stat">
                            <div class="text-green-500" v-if="isProviderConnected('Harvester')">Connected</div>
                            <div class="text-red-500" v-else>Not Connected</div>
                          </div>
                        </a>
                      </li>

                    </ul>
                  </div>
                </div>



              </div>
            </div>
          </BB_Button>
          <!-- nutanix -->
          <BB_Button @click.prevent="toggleModal('Nutanix')" v-if="isProviderEnabled('Nutanix')"
            class="btn col-lg-5 col-md-12 mx-5">
            <div class="card-body p-3">
              <div class="row gx-4">
                <div class="col-auto">
                  <div class="avatar avatar-xl position-relative">
                    <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/nutanix.png " alt="Nutanix" />
                  </div>
                </div>

                <div class="col-auto my-auto">
                  <div class="h-100">
                    <h5 class="mb-1">Nutanix</h5>
                    <p class="mb-0 font-weight-bold text-sm"></p>
                  </div>
                </div>
                <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                  <div class="nav-wrapper position-relative end-0">
                    <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                      <li class="nav-item">
                        <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                          aria-selected="false">
                          <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Nutanix')"
                            class="h-15 w-15 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                          </svg>
                          <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                            viewBox="0 0 100 100">
                            
                            <line x1="20" y1="20" x2="80" y2="80" stroke="currentColor" stroke-width="8" />
                            <line x1="20" y1="80" x2="80" y2="20" stroke="currentColor" stroke-width="8" />
                          </svg>
                          <div class="provider_stat">
                            <div class="text-green-500" v-if="isProviderConnected('Nutanix')">Connected</div>
                            <div class="text-red-500" v-else>Not Connected</div>
                          </div>
                        </a>
                      </li>

                    </ul>
                  </div>
                </div>



              </div>
            </div>
          </BB_Button>

          <!-- openshift -->
          <BB_Button @click.prevent="openForm('OpenShift')" v-if="isProviderEnabled('OpenShift')"
            class="btn col-lg-5 col-md-12 mx-5">
            <div class="card-body p-3">
              <div class="row gx-4">
                <div class="col-auto">
                  <div class="avatar avatar-xl position-relative">
                    <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/openshift.png " alt="OpenShift" />
                    <!-- <img class="shadow-sm" 
                      :src="this.$store.state.darkMode ? require('@/assets/img/os-white.png') : require('@/assets/img/openshift.png')"
                      alt="" style="width: 100px; height: 100px" /> -->
                  </div>
                </div>

                <div class="col-auto my-auto">
                  <div class="h-100">
                    <h5 class="mb-1">OpenShift</h5>
                    <p class="mb-0 font-weight-bold text-sm"></p>
                  </div>
                </div>
                <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                  <div class="nav-wrapper position-relative end-0">
                    <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                      <li class="nav-item">
                        <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                          aria-selected="false">
                          <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('OpenShift')"
                            class="h-15 w-15 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                          </svg>
                          <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                            viewBox="0 0 100 100">
                            <line x1="20" y1="20" x2="80" y2="80" stroke="currentColor" stroke-width="8" />
                            <line x1="20" y1="80" x2="80" y2="20" stroke="currentColor" stroke-width="8" />
                          </svg>
                          <div class="provider_stat">
                            <div class="text-green-500" v-if="isProviderConnected('Nutanix')">Connected</div>
                            <div class="text-red-500" v-else>Not Connected</div>
                          </div>
                        </a>
                      </li>

                    </ul>
                  </div>
                </div>



              </div>
            </div>
          </BB_Button>
        </div>

      </div>



      <!--1st working cloudstack other modal -->
      <div>
        <div v-show="isModalVisible" class="modal-container" tabindex="-1" role="dialog">
          <div class="modal-dialog modal-dialog-centered" role="document">
            <div :class="modalClasses"> <!-- Modal Header -->
              <div class="modal-header">
                <h5 class="modal-title">Add Provider</h5>
                <button type="button" class="close" @click.prevent="toggleModal" aria-label="Close" :class="{ 'close-dark': this.$store.state.darkMode }">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>

              <!-- Modal Body -->
              <div class="modal-body">
                <!-- Form with 5 fields -->
                <form>
                  <h3 class="mb-5 text-lg font-normal text-dark dark:text-gray-400">
                    {{ selectedProvider }}
                  </h3>
                  <div class="mb-3">
                    <label for="api_name" class="form-label">API Name</label>
                    <bb-input type="text" class="" id="api_name" v-model="api_name" placeholder="Api Name " required />
                    <argon-alert v-if="!api_name && showErrorMessages"
                      class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong> API
                      Name is required
                    </argon-alert>
                  </div>

                  <div class="mb-3">
                    <label for="api_endpoint" class="form-label">API Endpoint</label>
                    <bb-input type="text" class="" id="api_endpoint" v-model="api_endpoint" placeholder="Api Endpoint "
                      required />
                    <argon-alert v-if="!api_endpoint && showErrorMessages"
                      class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong> API
                      Endpoint is required
                    </argon-alert>
                  </div>

                  <div class="mb-3">
                    <label for="access_key" class="form-label">Access Key</label>
                    <bb-input type="text" class="" id="access_key" v-model="access_key" placeholder="Access Key "
                      required />
                    <argon-alert v-if="!access_key && showErrorMessages"
                      class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong> Access
                      Key is required
                    </argon-alert>
                  </div>

                  <div class="mb-3">
                    <label for="secret_key" class="form-label">Secret Key</label>
                    <bb-input type="text" class="" id="secret_key" v-model="secret_key" placeholder="Secret Key "
                      required />
                    <!-- <span class="text-danger" v-if="!secret_key && showErrorMessages">Secret Key is required</span> -->
                    <argon-alert v-if="!secret_key && showErrorMessages"
                      class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong> Secret
                      Key is required
                    </argon-alert>

                  </div>

                  <!-- Modal Footer with Add Provider and Close buttons -->
                  <div class="modal-footer">
                    <argon-button color="success" size="md" variant="gradient" @click.prevent="addProvider"
                      type="submit">
                      Add Provider
                    </argon-button>

                    <argon-button color="danger" size="md" variant="gradient" @click.prevent="toggleModal">
                      Close
                    </argon-button>
                  </div>

                </form>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- working k8s modal -->
      <div>

        <!-- Modal -->
        <div v-show="isModalVisibles && (selectedModal === 'Kubernetes')" class="modal-container" tabindex="-1"
          role="dialog" aria-labelledby="modalTitle" aria-describedby="modalBody">
          <div class="modal-dialog modal-dialog-centered" role="document">
            <div :class="modalClasses">
              <!-- Modal Header -->
              <div class="modal-header">
                <h5 id="modalTitle" class="modal-title">Add Provider</h5>
                <button type="button" class="close" @click.prevent="toggleModals" aria-label="Close" :class="{ 'close-dark': this.$store.state.darkMode }">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>

              <!-- Modal Body -->
              <div id="modalBody" class="modal-body">
                <!-- Form with 5 fields -->
                <form>
                  <h3 class="mb-5 text-lg font-normal text-dark dark:text-gray-400">
                    {{ selectedModal }}
                  </h3>

                  <div class="mb-3">
                    <label for="Api_name" class="form-label">K8s Key name</label>
                    <bb-input type="text" v-model="k8s_name" placeholder="Key Name" />
                    <argon-alert v-if="!k8s_name && showErrorMessages"
                      class="alert alert-danger alert-dismissible fade show custom-alert">
                      <strong>Error!</strong> K8s Key name is required.
                    </argon-alert>
                  </div>

                  <div class="mb-3">
                    <label for="kubeconfigData" class="form-label">Kubeconfig Data</label>
                    <textarea :class="{ 'bg-dark-mode': isDarkMode }" class="form-control" v-model="kubeconfigData"
                      placeholder="Kubeconfig Data" required></textarea>
                    <argon-alert v-if="!kubeconfigData && showErrorMessages"
                      class="alert alert-danger alert-dismissible fade show custom-alert">
                      <strong>Error!</strong> Kubeconfig Data is required.
                    </argon-alert>
                  </div>

                  <!-- Modal Footer with Add Provider and Close buttons -->
                  <div class="modal-footer">
                    <argon-button color="success" size="md" variant="gradient" type="submit" @click.prevent="addProviderk8s">
                      Add Provider
                    </argon-button>

                    <argon-button color="danger" size="md" variant="gradient" @click.prevent="toggleModals">
                      Close
                    </argon-button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!--openshift Modal -->
      <div v-show="isOpen && (selectedModal === 'OpenShift')" class="modal-container" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div :class="modalClasses"> <!-- Modal Header -->
            <div class="modal-header">
              <h5 class="modal-title">Add Provider</h5>
              <button type="button" class="close" @click.prevent="openForm" aria-label="Close" :class="{ 'close-dark': this.$store.state.darkMode }">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>

            <!-- Modal Body -->
            <div class="modal-body">
              <!-- Form with 5 fields -->
              <form>
                <h3 class="mb-5 text-lg font-normal text-dark dark:text-gray-400">
                  {{ selectedModal }}
                </h3>

                <div class="mb-3">
                  <label for="Api_name" class="form-label">Key name</label>
                  <bb-input type="text" class="" v-model="api_name" placeholder="Key Name" />
                  <argon-alert v-if="!api_name && showErrorMessages"
                    class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong> Key name
                    is required
                  </argon-alert>

                </div>
                <div class="mb-3">
                  <label for="Api_name" class="form-label">Username</label>
                  <bb-input type="text" class="" v-model="OpenShift_username" placeholder="Username" />
                  <argon-alert v-if="!OpenShift_username && showErrorMessages"
                    class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong> Username
                    is required
                  </argon-alert>

                </div>
                <div class="mb-3">
                  <label for="Api_name" class="form-label">Password</label>
                  <bb-input type="password" class="" v-model="OpenShift_password" placeholder="Password" />
                  <argon-alert v-if="!OpenShift_password && showErrorMessages"
                    class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong> Password
                    is required
                  </argon-alert>

                </div>
                <div class="mb-3">
                  <label for="Api_name" class="form-label">API Url</label>
                  <bb-input type="text" class="" v-model="api_url" placeholder="API Url" />
                  <argon-alert v-if="!api_url && showErrorMessages"
                    class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong> API Url
                    is required
                  </argon-alert>

                </div>



                <!-- Modal Footer with Add Provider and Close buttons -->

                <div class="modal-footer">
                  <argon-button color="success" size="md" variant="gradient" @click.prevent="addOpenShift"
                    type="submit">
                    Add Provider
                  </argon-button>

                  <argon-button color="danger" size="md" variant="gradient" @click.prevent="toggleModals">
                    Close
                  </argon-button>
                </div>

              </form>
            </div>
          </div>
        </div>
      </div>


      <!-- Openstack mOdel -->
      <div>

        <!-- Modal -->
        <div v-show="isModalVisibles && selectedModal === 'OpenStack'" class="modal-container" tabindex="-1"
          role="dialog">
          <div class="modal-dialog modal-dialog-centered" role="document">
            <div :class="modalClasses"> <!-- Modal Header -->
              <div class="modal-header">
                <h5 class="modal-title">Add Provider</h5>
                <button type="button" class="close" @click.prevent="OpenstackModal" aria-label="Close" :class="{ 'close-dark': this.$store.state.darkMode }">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>

              <!-- Modal Body -->
              <div class="modal-body">
                <!-- Form with 5 fields -->
                <form>
                  <h3 class="mb-5 text-lg font-normal text-dark dark:text-gray-400">
                    {{ selectedModal }}
                  </h3>

                  <div class="mb-3">
                    <label for="Api_name" class="form-label">API Name</label>
                    <bb-input type="text" class="" v-model="api_name" placeholder="Api Name" />
                    <argon-alert v-if="!api_name && showErrorMessages"
                      class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong> Api
                      Name is required
                    </argon-alert>

                  </div>

                  <div class="mb-3">
                    <label for="Api_name" class="form-label">Username</label>
                    <bb-input type="text" class="" v-model="OpenstackUser" placeholder="Username" />
                    <argon-alert v-if="!OpenstackUser && showErrorMessages"
                      class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong>
                      Username name is required
                    </argon-alert>

                  </div>
                  <div class="mb-3">
                    <label for="Api_name" class="form-label">Tenant/Project Name</label>
                    <bb-input type="text" class="" v-model="tenant_name" placeholder="Tenant/Project Name" />
                    <argon-alert v-if="!tenant_name && showErrorMessages"
                      class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong>
                      Tenant/Project Name is required
                    </argon-alert>

                  </div>
                  <div class="mb-3">
                    <label for="Api_name" class="form-label">Password</label>
                    <bb-input type="password" class="" v-model="OpenstackPassword" placeholder="Password" />
                    <argon-alert v-if="!OpenstackPassword && showErrorMessages"
                      class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong>
                      Password is required
                    </argon-alert>

                  </div>
                  <div class="mb-3">
                    <label for="Api_name" class="form-label">Auth URL</label>
                    <bb-input type="text" class="" v-model="auth_url" placeholder="Auth URL" />
                    <argon-alert v-if="!auth_url && showErrorMessages"
                      class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong> AUTH
                      URL name is required
                    </argon-alert>

                  </div>
                  <div class="mb-3">
                    <label for="Api_name" class="form-label">Region</label>
                    <bb-input type="text" class="" v-model="region" placeholder="Region" />
                    <argon-alert v-if="!region && showErrorMessages"
                      class="alert alert-danger alert-dismissible fade show custom-alert"><strong>Error!</strong> Region
                      is required
                    </argon-alert>

                  </div>





                  <!-- Modal Footer with Add Provider and Close buttons -->

                  <div class="modal-footer">
                    <argon-button color="success" size="md" variant="gradient" @click="addOpenstack" type="submit">
                      Add Provider
                    </argon-button>

                    <argon-button color="danger" size="md" variant="gradient" @click="OpenstackModal">
                      Close
                    </argon-button>

                  </div>

                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </main>
</template>

<script>
// import setNavPills from "@/assets/js/nav-pills.js";
// import setTooltip from "@/assets/js/tooltip.js";
import axios from 'axios';
import { API_ENDPOINT } from '@/../apiconfig.js';

import BbInput from "../../components/BB_Input.vue";

// import ProfileCard from "@/views/components/profileCard.vue";
import ArgonAlert from "@/components/BB_Alert.vue";
import argonButton from "@/components/BB_Button.vue";

const body = document.getElementsByTagName("body")[0];

export default {
  name: "profile",
  data() {
    return {
      loading: true,
      apiUrl: API_ENDPOINT,
      OpenstackUser: '',
      tenant_name: '',
      OpenstackPassword: '',
      auth_url: '',
      region: '',
      providers: [],
      isModalVisibles: false, selectedModal: '', kubeconfigData: '',
      isModalVisible: false, user_id: '',
      selectedProvider: '',
      api_name: '', api_endpoint: '', secret_key: '', access_key: '', error: '',
      showErrorMessages: false,

      provider_info: [],
      showMenu: false,
      OpenShift_username: "", // Ensure this property is defined in data
      OpenShift_password: "",
      api_url: "",
      isOpen: "",

    };
  },
  components: {
    BbInput,
    // ProfileCard,
    ArgonAlert,
    argonButton,

  },


  mounted() {


    this.$store.state.isAbsolute = true;
    // setNavPills();
    // setTooltip();
  },
  
  beforeMount() {
    this.$store.state.imageLayout = "profile-overview";
    this.$store.state.showNavbar = true;
    this.$store.state.showFooter = true;
    // this.$store.state.hideConfigButton = true;
    body.classList.add("profile-overview");
  },
  beforeUnmount() {
    this.$store.state.isAbsolute = false;
    this.$store.state.imageLayout = "default";
    this.$store.state.showNavbar = true;
    this.$store.state.showFooter = true;
    // this.$store.state.hideConfigButton = false;
    body.classList.remove("profile-overview");
  },
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode; // Assuming you're using Vuex to manage state
    },
    modalClasses() {
      return {
        'modal-content': true, // Always apply modal-content class
        'modal-content-dark': this.isDarkMode // Apply modal-content-dark class only if dark mode is active
      };
    },
    isProviderConnected() {
      return (providerName) => {
        return this.provider_info.some(
          (provider) =>
            provider.provider_name.toLowerCase() === providerName.toLowerCase() &&
            provider.is_connected
        );
      };
    },
  },


  created() {
    this.user_id = sessionStorage.getItem("user_id");
    this.getAllProviderData();
    this.fetchProviders();
  },
  methods: {
    fetchProviders() {
      // Retrieve token from session storage
      const token = sessionStorage.getItem('token');

      // Set headers with token
      const headers = {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json' // Assuming JSON content type
      };
      axios.get(`${this.apiUrl}/api/v1/provider-list/`,
        { headers })
        .then(response => {
          this.providers = response.data;
          this.loading = false; // Set loading to false once data is fetched

        })
        .catch(error => {
          console.error('Error fetching providers:', error);
        });
    },
    isProviderEnabled(providerName) {
      const provider = this.providers.find(p => p.provider_name === providerName);
      return provider ? provider.is_enabled : false;
    },
    toggleModal(selectedProvider) {
      // Reset form fields
      this.api_name = '';
      this.api_endpoint = '';
      this.secret_key = '';
      this.access_key = '';
      this.error = '';
      this.selectedProvider = selectedProvider
      this.isModalVisible = !this.isModalVisible;
    },
    // New method to open kubeconfig_data modal
    toggleModals(selectedProvider) {
      this.kubeconfigData = '';
      this.error = ''; // Assuming you have an error property for validation messages
      this.api_name = '';


      this.selectedProvider = selectedProvider;
      this.selectedModal = selectedProvider;
      this.isModalVisibles = !this.isModalVisibles;
      if (!this.isModalVisibles) {
        // Reset k8s_name and kubeconfigData when closing the modal
        this.k8s_name = '';
        this.kubeconfigData = '';
      }
    },


    openForm(selectedProvider) {
      this.kubeconfigData = '';
      this.error = ''; // Assuming you have an error property for validation messages
      this.api_name = '';


      this.selectedProvider = selectedProvider;
      this.selectedModal = selectedProvider;
      this.isOpen = !this.isOpen;

    },

    OpenstackModal(selectedProvider) {
      this.OpenstackUser = '';
      this.tennat_name = '';
      this.OpenstackPassword = '';
      this.auth_url = '';
      this.region = '';

      this.selectedProvider = selectedProvider;
      this.selectedModal = 'OpenStack';
      this.isModalVisibles = !this.isModalVisibles;

    },
    async addProviderk8s() {
      if (!this.kubeconfigData || !this.k8s_name) {
        this.showErrorMessages = true; // Show error messages
        setTimeout(() => {
          this.showErrorMessages = false; // Hide error messages after 5 seconds
        }, 5000);
        return;
      }

      // Save kubeconfig data to session storage
      sessionStorage.setItem('kubeconfigData', this.kubeconfigData);

      // Retrieve token from session storage
      const token = sessionStorage.getItem('token');

      // Set headers with token
      const headers = {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json' // Assuming JSON content type
      };

      const fromData = {
        // user_id: this.user_id,
        provider_name: this.selectedProvider,
        K8s_key_name: this.k8s_name,
        kubeconfig_data: this.kubeconfigData,
      };


      try {
        await axios.post(`${this.apiUrl}/api/v1/provider/`, fromData, { headers });
        this.getAllProviderData();
        this.isModalVisibles = !this.isModalVisibles;
      } catch (error) {
        this.error = "Error adding provider: " + error.message;
      }
    },

    async addOpenShift() {
      if (!this.api_name || !this.OpenShift_username || !this.OpenShift_password || !this.api_url) {
        this.showErrorMessages = true; // Show error messages
        setTimeout(() => {
          this.showErrorMessages = false; // Hide error messages after 5 seconds
        }, 5000);
        return;
      }
      const fromData = {
        user_id: this.user_id,
        provider_name: this.selectedProvider,
        key_name: this.api_name,
        OpenShift_username: this.OpenShift_username,
        OpenShift_password: this.OpenShift_password,
        api_url: this.api_url,


      };
      await axios.post(`${this.apiUrl}/api/v3/providers/`, fromData)
        .then(() => {
          this.getAllProviderData();
          this.isOpen = !this.isOpen;
        })
        .catch((error) => {
          this.error = "Error adding provider: " + error.message;
        });
    },


    async addProvider() {
      if (!this.api_name || !this.api_endpoint || !this.access_key || !this.secret_key) {
        this.showErrorMessages = true; // Show error messages
        setTimeout(() => {
          this.showErrorMessages = false; // Hide error messages after 5 seconds
        }, 5000);
        return;
      }

      // Retrieve token from session storage
      const token = sessionStorage.getItem('token');

      // Set headers with token
      const headers = {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json' // Assuming JSON content type
      };

      const fromData = {
        "provider_name": this.selectedProvider,
        "key_name": this.api_name,
        "provider_url": this.api_endpoint,
        "secret_key": this.secret_key,
        "access_token": this.access_key,
      };

      await axios.post(`${this.apiUrl}/api/v1/providers/`, fromData, { headers })
        .then(() => {
          this.getAllProviderData();
          this.isModalVisible = !this.isModalVisible;
        })
        .catch((error) => {
          this.error = "Error adding provider: " + error.message;
        });
    },

    async addOpenstack() {
      // Check if required fields are provided
      if (!this.api_name || !this.OpenstackUser || !this.tenant_name || !this.OpenstackPassword || !this.auth_url || !this.region) {
        this.showErrorMessages = true; // Show error messages
        setTimeout(() => {
          this.showErrorMessages = false; // Hide error messages after 5 seconds
        }, 5000);
        return;
      }

      // Retrieve token from session storage
      const token = sessionStorage.getItem('token');

      // Set headers with token
      const headers = {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json' // Assuming JSON content type
      };

      const fromData = {
        "provider_name": this.selectedProvider,
        "key_name": this.api_name,
        "OpenstackUsername": this.OpenstackUser,
        "tenant_name": this.tenant_name,
        "OpenstackPassword": this.OpenstackPassword,
        "auth_url": this.auth_url,
        "region": this.region,
      };

      try {
        await axios.post(`${this.apiUrl}/api/v1/providers/`, fromData, { headers });
        this.getAllProviderData();
        this.isModalVisible = !this.isModalVisible;
      } catch (error) {
        this.error = "Error adding provider: " + error.message;
      }
    },

    async getAllProviderData() {
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
    }

  },
};
</script>

<style scoped>
.loading-container {
  position: fixed;
  top: 0;
  left: 2px;
  right: 0;
  bottom: 0;
  /* background-color: rgba(255, 255, 255, 0.8);  */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  /* Ensure it's on top of everything */
}

.spinner-border {
  width: 3rem;
  height: 3rem;
  /* Adjust size if necessary */
}

.loading-text {
  margin-top: 1rem;
  font-size: 1.25rem;
  color: #007bff;
  /* Adjust color if necessary */
}

.modal-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 130%;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1050;
  overflow: auto;
}

.modal-content-dark {
  background-color: #111c44;
  /* Change background color for dark mode */
  color: #fff;
  /* Change text color for dark mode */
}

.bg-dark-mode {
  /* Define dark mode styles */
  background-color: #111c44;
  color: #ffffff;
}

.custom-alert {
  color: white;
  padding: 0.5rem;
  /* Reduce padding */

}
.close-dark {
  color: white !important;
}
</style>
