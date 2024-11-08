<template>
    <div class="py-4 container-fluid">
      <div class="row">
        <div class="col-lg-12">
          <div class="row">
            
  
  
            <div class="py-4 container-fluid">
              <div class="row">
                <div class="col-12">
                  <delete-table />
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
  import DeleteTable from "@/views/components/DeleteTable.vue";
  
  export default {
    name: "Cluster",
    components: {
      // Card,
      DeleteTable,
    },
    data() {
      return {
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
  