<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <ButtonCard />
          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <RestoreCard />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  
</template>

<script>
import RestoreCard from "./components/RestoreCard.vue";
import ButtonCard from "./components/ButtonCard.vue";


export default {
  name: "Cluster",
  components: {
    RestoreCard,
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

