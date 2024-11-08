<template>
  <nav aria-label="breadcrumb">
    <ol class="me-sm-6 text-white px-0 pt-1 pb-0 mb-0 bg-transparent breadcrumb">
      <li class="text-sm breadcrumb-item">
        <a
          v-if="isRTL"
          class="opacity-5 ps-2"
          href="#"
          :class="navClass"
        >لوحات القيادة</a>
        <a v-else 
          :class="navClass"
          class="opacity-8 cursor-pointer"
          @click="navigateToDashboard"
        >Home</a>
      </li>
      <li
        class="text-sm breadcrumb-item active"
        :class="navClass"
        aria-current="page"
      >
        {{ currentPage }}
      </li>
    </ol>
    <h6 class="mb-0 font-weight-bolder" :class="navClass">
      {{ currentPage }}
    </h6>
  </nav>
</template>

<script>
export default {
  name: "breadcrumbs",
  props: {
    currentPage: {
      type: String,
      required: true
    }
  },
  computed: {
    isRTL() {
      return this.$store.state.isRTL;
    },
    navClass() {
      return this.$store.state.isNavFixed ? 'text-dark' : 'text-white';
    },
    role() {
      return sessionStorage.getItem('role');
    }
  },
  methods: {
    navigateToDashboard() {
      if (this.role === 'Admin') {
        this.$router.push('/admin-dashboard');
      } else if (this.role === 'Standard') {
        this.$router.push('/User-dashboard');
      } else {
        this.$router.push('/User-dashboard'); // Default route if role is not defined
      }
    }
  }
};
</script>
<style scoped>
.cursor-pointer {
  cursor: pointer;
}
</style>
