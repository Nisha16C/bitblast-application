import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
// import Tables from "../views/Tables.vue";
import ClusterCreate from "../views/UserDashboard/Clusterinfo.vue";
import ClusterSetting from "../views/UserDashboard/ClusterSetting.vue";
import Clusterss from "../views/UserDashboard/Clusters.vue";
import Projectss from "../views/UserDashboard/Projects.vue";
import Providers from "../views/UserDashboard/Providers.vue";
import providercard from "../views/UserDashboard/providercard.vue";
import UserDashboard from "../views/UserDashboard/UserDashboard.vue";
import Result from "../views/UserDashboard/Result.vue";
import Delete from "../views/UserDashboard/delete.vue";
import ClustersManagement from "../views/Clusters.vue";
import ProjectManagement from "../views/Projects.vue";
import UserManagement from "../views/UserMgmt.vue";
import Signin from "../views/Signin.vue";
import Backup from "../views/Backup.vue";
import BackupForm from "../views/BackupForm.vue";
import Cconfiguration from "../views/UserDashboard/Dbconfig.vue";
import RestoreBackup from "../views/RestoreBackup.vue";
import BackupDetails from "../views/BackupDetails.vue";
import StorageMethod from "../views/StorageMethod.vue";
import AdminMonitoring from "../views/adminMonitoring.vue";
import ProjectSelect from "../views/UserDashboard/ProjectSelect.vue";
import ActivityLog from "../views/ActivityLog.vue";
import USER from "../views/USER.vue";
import manageProvider from "../views/ManageProvider.vue";
import Documentation from "../Documentation/Documentation.vue";
import BackupSchedule from "../views/BackupSchedule.vue";
import ADauthprovider from "../views/ADauthprovider.vue";
import ADuserForm from "../views/ADuserForm.vue";
import ADuserlist from "../views/ADuserlist.vue";
import ADsave from "../views/ADsave.vue";
import ADgrouplist from "../views/ADgrouplist.vue";
import UserMonitoring from "../views/userMonitoring.vue";
import PageNotFound from "../views/PageNotFound.vue";
import Unauthorize from "../views/Unauthorize.vue";
import terminal from "../views/components/terminal.vue";



 
const routes = [
  {
    path: "/",
    name: "/",
    redirect: "/signin",
  },
 
  // Admin route
 
  {
    path: "/scheduled-backups",
    name: "Schedule Backup",
    component: BackupSchedule,
    meta: { roles: ['Standard'] },
 
  },
  {
    path: "/admin-dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: { roles: ['Admin'] },
    
 
  },
  {
    path: "/Cconfiguration",
    name: "Cconfiguration",
    component: Cconfiguration,
    meta: { roles: ['Standard'] },
 
  },
  {
    path: "/admin-backup",
    name: "Backup",
    component: Backup,
    meta: { roles: ['Standard'] },
 
  },
  {
    path: "/mount-backup-method",
    name: "Backup Method",
    component: StorageMethod,
    meta: { roles: ['Standard'] },
 
  },
  {
    path: "/admin-backup/form",
    name: "Create Backup",
    component: BackupForm,
    meta: { roles: ['Standard'] },
 
  },
  {
    path: "/admin-backup/restore-backup",
    name: "Restore Backup",
    component: RestoreBackup,
    meta: { roles: ['Standard'] },
 
  },
  {
    path: "/backup/:serverName",
    name: "BackupDetails",
    component: BackupDetails,
    meta: { roles: ['Standard'] },
    props:true,
  }
,
  {
    path: "/User-dashboard",
    name: "User Dashboard",
    component: UserDashboard,
    meta: { roles: ['Standard'] },
 
  },
 
  {
    path: "/Clusters-Management",
    name: "Clusters-Management",
    component: ClustersManagement,
    meta: { roles: ['Admin'] },
 
  },
 
  {
    path: "/Cluster-Setting",
    name: "Cluster-Setting",
    component: ClusterSetting,
    meta: { roles: ['Standard'] },
 
  },
 
  // User Route
  {
    path: "/Clusters",
    name: "Clusters",
    component: Clusterss,
    meta: { roles: ['Standard'] },
 
  },
  {
    path: "/result",
    name: "Result",
    component: Result,
    meta: { roles: ['Standard'] },
 
  },
  {
    path: "/delete",
    name: "Delete",
    component: Delete,
    meta: { roles: ['Standard'] },
 
  },
  {
    path: "/Cluster-Create",
    name: "Cluster-Create",
    component: ClusterCreate,
    meta: { roles: ['Standard'] },
 
  },
  {
    path: "/Projects",
    name: "Projects",
    component: Projectss,
    meta: { roles: ['Standard'] },
 
  },
 
  {
    path: "/Provider",
    name: "Providers",
    component: Providers,
    meta: { roles: ['Standard'] },
 
  },
  {
    path: "/providercard",
    name: "providercard",
    component: providercard,
    meta: { roles: ['Standard'] },
 
  },
 
  {
    path: "/User-Management",
    name: "User-Management",
    component: UserManagement,
    meta: { roles: ['Admin'] },
 
  },
  {
    path: "/Project-Management",
    name: "Project-Management",
    component: ProjectManagement,
    meta: { roles: ['Admin'] },
 
  },
 
  {
    path: "/user-monitoring",
    name: "user-monitoring",
    component: UserMonitoring ,
    meta: { roles: ['Standard'] },
 
  },
  {
    path: "/admin-monitoring",
    name: "Admin Monitoring",
    component: AdminMonitoring,
    meta: { roles: ['Admin'] },
 
  },
  {
    path: "/signin",
    name: "Signin",
    component: Signin,
  },
  {
    path: "/manage-provider",
    name: "Provider Management",
    component: manageProvider,
    meta: { roles: ['Admin'] },
  },
  {
    path: "/Project-Select",
    name: "Project Select",
    component: ProjectSelect,
    meta: { roles: ['Standard'] },
 
  },
 
  {
    path: "/ActivityLog",
    name: "ActivityLog",
    component: ActivityLog,
    meta: { roles: ['Admin'] },
 
  },
  {
    path: "/USER",
    name: "user",
    component: USER,
    meta: { roles: ['Admin'] },
 
  },
  {
    path: "/Documentation",
    name: "Documentation",
    component: Documentation,
  },
  {
    path: "/ADauthprovider",
    name: "ad-auth-provider",
    component: ADauthprovider,
    meta: { roles: ['Admin'] },
 
   },
   {
    path: "/ADuserForm",
    name: "ad-user-form",
    component: ADuserForm,
    meta: { roles: ['Admin'] },
 
   },
   {
    path: "/ADuserlist",
    name: "ad-user-list",
    component: ADuserlist,
    meta: { roles: ['Admin'] },
 
   },
   {
    path: "/ADgrouplist",
    name: "ad-group-list",
    component: ADgrouplist,
    meta: { roles: ['Admin'] },
 
   },
   {
     path: "/ADsave",
     name: "ad-configuration-save",
     component: ADsave,
     meta: { roles: ['Admin'] },
 
   },
   {
    path: '/:pathMatch(.*)*',  // Updated wildcard route
    name: "page-not-found",
    component: PageNotFound,
    // meta: { roles: ['Admin'] },

  },
  {
    path: "/Unauthorize",
    name: "unauthorize",
    component: Unauthorize,
    // meta: { roles: ['Admin'] },

  },
  {
    path: "/terminal",
    name: "terminal",
    component: terminal,
    // meta: { roles: ['Admin'] },

  },
];
 
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "active",
});
 
// Function to check if the user is authenticated
function isAuthenticated() {
  return sessionStorage.getItem('token') !== null;
}
 
function getUserRole() {
  const role = sessionStorage.getItem('role'); // Retrieve the user role from sessionStorage
  return role;
}
 
 
// Global navigation guard to check authentication status and roles
router.beforeEach((to, from, next) => {
  if (to.name !== 'Signin' && !isAuthenticated()) {
    // Redirect the user to the signin page if not authenticated
    next({ name: 'Signin' });
  } else if (to.meta.roles && !to.meta.roles.includes(getUserRole())) {
    // Redirect the user if they do not have the required role
    next({ name: 'unauthorize' });
  } else {
    // Proceed to the requested route
    next();
  }
});
 
export default router;
 