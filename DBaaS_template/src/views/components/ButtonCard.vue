
<template>
<div class="container-fluid mt-7">
 
<div class="card shadow-lg mt-n6">
 
    <div class="card-body p-3">
 
        <div class="row gx-4">
            <div class="col-auto my-auto">
 
                <div class="h-100 py-2">
 
 
                    <argon-button class="mx-2" color="success" @click="ScheduledBackups" size="md" variant="gradient"
                        >Backup/Schedule</argon-button
                      >
 
                    <argon-button class="mx-2" color="success" @click="RestoreBackup" size="md" variant="gradient"
                        >Restore</argon-button
                    >
                    <argon-button class="mx-2" color="success" @click="BackupList" size="md" variant="gradient"
                        >Backups List</argon-button
                      >
 
                    <argon-button class="mx-2" color="success" size="md" @click="scheduledBackupslist" variant="gradient"
                        >Schedule Backups List</argon-button
                      >
 
                </div>
 
            </div>
 
        </div>
 
    </div>
 
</div>
 
</div>
    
 
</template>
 
<script>
 
import argonButton from "@/components/BB_Button.vue";
 
export default {
  name: "Cluster",
  components: {
    argonButton,
  },
  methods:{
    ScheduledBackups(){
        this.$router.push('/admin-backup/form');
    },
    RestoreBackup(){
        this.$router.push('/admin-backup/restore-backup');
    },
    BackupList(){
        this.$router.push('/admin-backup');
    },
    scheduledBackupslist(){
        this.$router.push('/scheduled-backups');
    }
    
  }
}
 
</script>