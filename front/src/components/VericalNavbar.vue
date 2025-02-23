<template>
  <nav class="vertical-navbar">
    <div class="logo">
      MyLogo
    </div>
    <ul>
      <li v-for="item in navItems" :key="item.name" @click="navigate(item.path)">
        {{ item.name }}
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'VerticalNavbar',
  data() {
    return {
      navItems: [
        { name: 'Home', path: '/' },
        { name: 'About', path: '/about' },
        { name: 'Services', path: '/services' },
        { name: 'Contact', path: '/contact' }
      ]
    };
  },
  methods: {
    navigate(path) {
      this.$router.push(path);
    }
  }
}
</script>

<style scoped>
.vertical-navbar {
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 200px;
  background-color: #D9D9D9; /* Updated background color for the whole navbar */
  color: black; /* Updated text color for the whole navbar */
  border-right: 1px solid #ddd;
  padding: 10px;
  overflow-y: auto;
}

.logo {
  font-size: 20px;
  font-weight: bold;
  padding: 20px 10px;
  text-align: center;
}

.vertical-navbar ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.vertical-navbar li {
  padding: 10px;
  cursor: pointer;
  text-align: left;
}

.vertical-navbar li:hover {
  background-color: #e2e6ea;
}
</style>
