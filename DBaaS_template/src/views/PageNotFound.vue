<template>
    <div class="card d-flex justify-content-center align-items-center vh-100">
      <div class="text-center">
        <div class="card-header pb-0">
          <h1 class="display-1">404</h1>
          <h1>Page Not Found</h1>
          <p>The page you are looking for doesn't exist.</p>
          <button @click="goBack" class="btn btn-primary mt-3">Go Back</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'NotFound',
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
  </style>
  