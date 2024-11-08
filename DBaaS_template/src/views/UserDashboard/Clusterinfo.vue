<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-8">
        <div class="row mt-4">
          <!-- <div class="col-xl-6 mb-xl-0 mb-4">
            <master-card />
          </div> -->

          <div class="col-md-12 mb-4">
            <info-card />
          </div>
        </div>
      </div>
      <!-- <div class="col-lg-4">
        <invoice-card class="mt-4" />
      </div> -->
    </div>
    <div class="row">
      <div class="col-md-7">
        <Cluster-card />
      </div>
      <div class="col-md-5">
        <transaction-card />
      </div>
    </div>
  </div>
</template>

<script>

import InfoCard from "@/views/components/ClusterinfoCard.vue";
import ClusterCard from "@/views/components/CclusterCard.vue";
import TransactionCard from "@/views/components/CSummaryCard.vue";

export default {
  name: "Billing",
  components: {
    // MasterCard,
    // DefaultInfoCard,
    InfoCard,
    
    ClusterCard,
    TransactionCard,
  },
  data() {
    return {
      salary: {
        classIcon: "text-white fas fa-landmark",
        title: "Salary",
        desc: "Belong Interactive",
        price: "+$2000",
      },
      paypal: {
        classIcon: "text-white fab fa-paypal",
        title: "Paypal",
        desc: "Freelance Payment",
        price: "$455.00",
      },
    };
  },
};
</script>
