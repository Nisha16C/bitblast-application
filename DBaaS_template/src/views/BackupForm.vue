<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <ButtonCard />

          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <BackupCard />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  
</template>

<script>
import ButtonCard from "./components/ButtonCard.vue";
import BackupCard from "./components/BackupCard.vue";

export default {
  name: "Cluster",
  components: {
    BackupCard,
    ButtonCard
  },
  data() {
    return {
      stats: {
        money: {
          title: "All Backups",
          value: "2",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "",
          iconBackground: "bg-gradient-primary",
        },
      },
    };
  },
};
</script>
