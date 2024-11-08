import { createStore } from "vuex";
import { API_ENDPOINT } from '@/../apiconfig.js';
import axios from "axios";
export default createStore({
  state: {
    hideConfigButton: false,
    isPinned: true,
    showConfig: false,
    sidebarType: "bg-white",
    isRTL: false,
    mcolor: "",
    darkMode: false,
    isNavFixed: false,
    isAbsolute: false,
    showNavs: true,
    showSidenav: true,
    showNavbar: true,
    showFooter: true,
    showMain: true,
    layout: "default",
    username: null,
    clusterType: "",
    clusterName: "",
    dbUsername: "",
    dbPassword: "",
    backupMethod: "",
    providerName: "",
    postgres_version: "",
    flavors: [],
    project_name: "",
    project_id: "",
    computeOfferings: null,
    storageClass: null,
    size: null,
    k8sClass: "",
    osType: "",
    airgap: "",
    PgAdmin: "",
    selectedStorageOffering: null,
    selectedComputeOffering: null,
    isLogoToggled: false,
    observabilityBackupVisible: true,
    databaseBackupVisible: true,
    hideProjectSelect: false,
    showdocx: false,
    apiUrl: API_ENDPOINT,
    selectedK8sKeyName: '' ,// Default value
    schedule_backup: false,
    retention: "",
    selectedValue: "",
    selected_min: "",
    selected_hour: "",
    selected_day: "",
    selected_date: "",
    backup_type: "",
    pgAdminStatus: 'no', // Initial PgAdmin status
 
  },
  mutations: {
    SET_PGADMIN_STATUS(state, status) {
      state.pgAdminStatus = status;
    },
    SET_K8S_KEY_NAME(state, keyName) {
      state.selectedK8sKeyName = keyName;
    },
    TOGGLE_LOGO(state) {
      state.isLogoToggled = !state.isLogoToggled;
    },
    toggleObservabilityBackupVisibility(state) {
      state.observabilityBackupVisible = !state.observabilityBackupVisible;
    },
    toggleDatabaseBackupVisibility(state) {
      state.databaseBackupVisible = !state.databaseBackupVisible;
    },
    toggleProjectSelect(state) {
      state.hideProjectSelect = !state.hideProjectSelect;
    },
    toggleshowdocx(state) {
      state.showdocx = !state.showdocx;
    },
    setGlobalProjectName(state, project_name) {
      state.project_name = project_name;
    },
    setGlobalProjectId(state, project_id) {
      state.project_id = project_id;
    },
    setSelectedType(state, clusterType) {
      state.clusterType = clusterType;
    },
    setSelectedProvider(state, providerName) {
      state.providerName = providerName;
    },
    setClusterName(state, clusterName) {
      state.clusterName = clusterName;
    },
    setDbUsername(state, dbUsername) {
      state.dbUsername = dbUsername;
    },
    setPassword(state, dbPassword) {
      state.dbPassword = dbPassword;
    },
    setBackupMethod(state, backupMethod) {
      state.backupMethod = backupMethod;
    },
    setSelectedVersion(state, postgres_version) {
      state.postgres_version = postgres_version;
    },
    setStorageClass(state, storageClass) {
      state.storageClass = storageClass;
    },
    setK8sClass(state, k8sClass) {
      state.k8sClass = k8sClass;
    },
    setOsType(state, osType) {
      state.osType = osType;
    },
    setAirgap(state, airgap) {
      state.airgap = airgap;
    },
    setPgAdmin(state, PgAdmin) {
      state.PgAdmin = PgAdmin;
    },
    setSchedule(state, schedule_backup) {
      state.schedule_backup = schedule_backup;
    },
    setSize(state, size) {
      state.size = size;
    },
    toggleConfigurator(state) {
      state.showConfig = !state.showConfig;
    },
    setSelectedOffering(state, computeOfferings) {
      state.computeOfferings = computeOfferings;
    },
    setSelectedStorage(state, selectedStorageOffering) {
      state.selectedStorageOffering = selectedStorageOffering;
    },
    setRetention(state, retention) {
      state.retention = retention;
    },
    setSelectedValue(state, selectedValue) {
      state.selectedValue = selectedValue;
    },
    setSelectedMin(state, selected_min) {
      state.selected_min = selected_min;
    },
    setSelectedHour(state, selected_hour) {
      state.selected_hour = selected_hour;
    },
    setSelectedDay(state, selected_day) {
      state.selected_day = selected_day;
    },
    setSelectedDate(state, selected_date) {
      state.selected_date = selected_date;
    },
    setBackupType(state, backup_type) {
      state.backup_type = backup_type;
    },
    navbarMinimize(state) {
      const sidenav_show = document.querySelector(".g-sidenav-show");
      if (sidenav_show.classList.contains("g-sidenav-hidden")) {
        sidenav_show.classList.remove("g-sidenav-hidden");
        sidenav_show.classList.add("g-sidenav-pinned");
        state.isPinned = true;
      } else {
        sidenav_show.classList.add("g-sidenav-hidden");
        sidenav_show.classList.remove("g-sidenav-pinned");
        state.isPinned = false;
      }
    },
    sidebarType(state, payload) {
      state.sidebarType = payload;
    },
    navbarFixed(state) {
      if (state.isNavFixed === false) {
        state.isNavFixed = true;
      } else {
        state.isNavFixed = false;
      }
    },
    setUsername(state, username) {
      state.username = username;
    },
    updateFlavors(state, newFlavors) {
      state.flavors = newFlavors;
    },
  },
  actions: {
    updatePgAdminStatus({ commit }, status) {
      commit('SET_PGADMIN_STATUS', status);
    },
    setK8sKeyName({ commit }, keyName) {
      commit('SET_K8S_KEY_NAME', keyName);
    },
    toggleLogo({ commit }) {
      commit('TOGGLE_LOGO');
    },
    toggleProjectSelect({ commit }) {
      commit('toggleProjectSelect');
    },
    toggleshowdocx({ commit }) {
      commit('toggleshowdocx');
    },
    setFlavors({ commit }, newFlavors) {
      commit("updateFlavors", newFlavors);
    },
    updateGlobalProjectName(context, project_name) {
      context.commit("setGlobalProjectName", project_name);
    },
    updateGlobalProjectId(context, project_id) {
      context.commit("setGlobalProjectId", project_id);
    },
    updateSelectedType(context, clusterType) {
      context.commit("setSelectedType", clusterType);
    },
    updateSelectedProvider(context, providerName) {
      context.commit("setSelectedProvider", providerName);
    },
    updateClusterName(context, clusterName) {
      context.commit("setClusterName", clusterName);
    },
    updateUsername(context, dbUsername) {
      context.commit("setDbUsername", dbUsername);
    },
    updatePassword(context, dbPassword) {
      context.commit("setPassword", dbPassword);
    },
    updateBackupMethod(context, backupMethod) {
      context.commit("setBackupMethod", backupMethod);
    },
    updateSelectedVersion(context, postgres_version) {
      context.commit("setSelectedVersion", postgres_version);
    },
    updateSelectedStorage(context, selectedStorageOffering) {
      context.commit("setSelectedStorage", selectedStorageOffering);
    },
    updateStorageClass(context, storageClass) {
      context.commit("setStorageClass", storageClass);
    },
    updateK8sClass(context, k8sClass) {
      context.commit("setK8sClass", k8sClass);
    },
    update_os(context, osType) {
      context.commit("setOsType", osType);
    },
    update_AI(context, airgap) {
      context.commit("setAirgap", airgap);
    },
    update_PgAdmin(context, PgAdmin) {
      context.commit("setPgAdmin", PgAdmin);
    },
    update_schedule(context, schedule_backup) {
      context.commit("setSchedule", schedule_backup);
    },
    updateSize(context, size) {
      context.commit("setSize", size);
    },
    updateComputeOffering(context, computeOfferings) {
      context.commit("setSelectedOffering", computeOfferings);
    },
    toggleSidebarColor({ commit }, payload) {
      commit("sidebarType", payload);
    },
    updateRetention(context, retention) {
      context.commit("setRetention", retention);
    },
    updateMin(context, selected_min) {
      context.commit("setSelectedMin", selected_min);
    },
    updateHour(context, selected_hour) {
      context.commit("setSelectedHour", selected_hour);
    },
    updateDay(context, selected_day) {
      context.commit("setSelectedDay", selected_day);
    },
    updateDate(context, selected_date) {
      context.commit("setSelectedDate", selected_date);
    },
    updateBackupType(context, backup_type) {
      context.commit("setBackupType", backup_type);
    },
    updateSelectedValue(context, selectedValue) {
      context.commit("setSelectedValue", selectedValue);
    },
    fetchFirstProject({ commit }, authToken) {
      if (!authToken) {
        console.error('User is not authenticated');
        return;
      }
      const headers = {
        'Authorization': `Token ${authToken}`,
        'Content-Type': 'application/json',
      };
      axios.get(`${API_ENDPOINT}/api/v1/project/user/`, { headers })
        .then(response => {
          if (response.data.length > 0) {
            const firstProject = response.data[0];
            commit("setGlobalProjectName", firstProject.project_name);
            commit("setGlobalProjectId", firstProject.id);
          } else {
            console.error('No projects found for the user');
          }
        })
        .catch(error => {
          console.error('Error fetching projects:', error.response ? error.response.data : error.message);
        });
    },
  },
  getters: {
    getPgAdminStatus: (state) => state.pgAdminStatus,
    getUsername: (state) => state.username,
    getSelectedCPUNumber: (state) => state.selectedCPUNumber,
    getSelectedMemory: (state) => state.selectedMemory,
  },
});
 
 