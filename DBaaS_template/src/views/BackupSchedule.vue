<template>
    <div class="py-4 container-fluid">
      <div class="row">
        <div class="col-lg-12">
          <ButtonCard />
  
            <div class="py-4 container-fluid">
              <div class="row">
                <div class="col-12">
                  <scheduleList />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    
  </template>
  
  <script>
  import scheduleList from "./components/scheduleList.vue";
  import ButtonCard from "./components/ButtonCard.vue";

  
  export default {
    name: "Cluster",
    components: {
      scheduleList,
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
  
