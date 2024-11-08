<template>
    <div class="card d-flex justify-content-center align-items-center vh-100">
      <div class="text-center">
        <div class="card-header pb-0">
          <h1 class="display-1">401</h1>
          <h1>Unauthorized</h1>
          <p>You do not have permission to view this page.</p>
          <button @click="goBack" class="btn btn-primary mt-3">Go Back</button>
        </div>
      </div>
    </div>
  </template>
  <script>
  export default {
    name: 'Unauthorize',
    methods: {
      goBack() {
        window.history.back();
      }
    }
  };
  </script>
  
  <style scoped>
  .vh-100 {
    height: 100vh;
  }
  .unauthorized {
    text-align: center;
    margin-top: 50px;
  }
  </style>
  