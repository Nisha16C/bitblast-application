
 
 

<template>
    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-8">
          <div class="row mt-4">
            <div class="col-md-12 mb-4">
              <info-card />
            </div>
          </div>
        </div>
 
      </div>
      <div class="row">
        <div class="col-md-7">
          <cluster-card />
        </div>
        <div class="col-md-5">
          <transaction-card />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  
  import InfoCard from "@/views/components/ClusterinfoCard.vue";
  import ClusterCard from "@/views/components/Cconfiguration.vue";
  import TransactionCard from "@/views/components/CSummaryCard.vue";
  
  export default {
    name: "Billing",
    components: {
      InfoCard,
      ClusterCard,
      TransactionCard,
    },
    data() {
      return {
        
   
     };
    },
  };
  </script>
  