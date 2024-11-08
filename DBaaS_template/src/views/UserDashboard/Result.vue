<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <!-- <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.money.title"
              :value="stats.money.value"
              :percentage="stats.money.percentage"
              :iconClass="stats.money.iconClass"
              :iconBackground="stats.money.iconBackground"
              :detail="stats.money.detail"
              directionReverse
            >
            </card>
          </div> -->


          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <progress-table />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import Card from "@/examples/Cards/Card.vue";
import ProgressTable from "@/views/components/ProgressTable.vue";

export default {
  name: "Cluster",
  components: {
    // Card,
    ProgressTable,
  },

  data() {
    return {
      formData: {},
      stats: {
        money: {
          title: "All Clusters",
          value: "12",
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
