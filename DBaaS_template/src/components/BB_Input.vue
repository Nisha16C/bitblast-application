[10:40 AM] Nisha Chaurasiya
<template>
  <div class="form-group">
    <div :class="hasIcon(icon)">
      <span v-if="iconDir === 'left'" class="input-group-text">
        <i :class="getIcon(icon)"></i>
      </span>
      <input
        :type="type"
        class="form-control"
        :class="[getClasses(size, valid), darkModeClass]"
        :name="name"
        :id="id"
        :value="modelValue"
        :placeholder="placeholder"
        :isRequired="isRequired"
        @input="$emit('update:modelValue', $event.target.value)"
        v-bind="$attrs"
      />
      <span v-if="iconDir === 'right'" class="input-group-text">
        <i :class="getIcon(icon)"></i>
      </span>
    </div>
  </div>
</template>
 
<script>
export default {
  name: "argon-input",
  props: {
    modelValue: {
      type: [String, Number],
      default: "",
    },
    size: {
      type: String,
      default: "default",
    },
    valid: {
      type: Boolean,
      default: false,
    },
    icon: String,
    iconDir: String,
    name: String,
    id: String,
    placeholder: String,
    type: String,
    isRequired: Boolean,
  },
  computed: {
    darkModeClass() {
      return this.$store.state.darkMode ? 'dark-mode' : ''; // Add dark mode class conditionally
    }
  },
  methods: {
    getClasses: (size, valid) => {
      let sizeValue, isValidValue;
 
      sizeValue = size ? `form-control-${size}` : null;
 
      isValidValue = valid ? `${valid}` : "invalid";
 
      return `${sizeValue} ${isValidValue}`;
    },
    getIcon: (icon) => (icon ? icon : null),
    hasIcon: (icon) => (icon ? "input-group" : null),
  },
};
</script>
<style scoped>
.dark-mode { /* Define dark mode styles */
  background-color: #111c44;
  color: #ffffff;
}
</style>
 
 