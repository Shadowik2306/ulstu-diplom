<template>
  <div class="pagination">
    <button @click="prevPage" :disabled="currentPage === 1">&lt;</button>
    <button
        v-for="page in pages_buttons"
        :key="page"
        @click="goToPage(page)"
        :class="{ active: page === currentPage }"
    >
      {{ page }}
    </button>
    <button @click="nextPage" :disabled="currentPage === totalPages">&gt;</button>
  </div>
</template>

<script>
export default {
  name: "PaginationComponent",
  props: {
    totalPages: {
      type: Number,
      required: true,
    },
    currentPage: {
      type: Number,
      required: true,
    },
    url: {
      type: String,
      default: "/presets",
    }
  },
  computed: {
    pages_buttons() {
      let start = Math.max(this.currentPage - 2, 1)
      let end = Math.min(this.currentPage + 2, this.totalPages)

      if (end - start < 4) {
        if (start === 1) {
          end = Math.min(5, this.totalPages);
        } else if (end === this.totalPages) {
          start = Math.max(this.totalPages - 4, 1);
        }
      }

      const res = []
      for (let i = start; i <= end; i++) {
        res.push(i);
      }
      return res
    }
  },
  methods: {
    prevPage() {
      window.location.href = this.url + "?" + new URLSearchParams({
        page: this.currentPage - 1
      })
    },
    nextPage() {
      window.location.href = this.url + "?" + new URLSearchParams({
        page: this.currentPage + 1
      })
    },
    goToPage(page) {
      window.location.href = this.url + "?" + new URLSearchParams({
        page: page
      })
    },
  },
};
</script>

<style>
.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 10px;
  border-radius: 5px;
}

button {
  border: 1px solid #8b5a5a;
  background-color: #D9D9D9;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
  transition: background-color 0.3s;
  color: black;
}

button.active {
  filter: brightness(0.8);
}

button:hover:not(.active) {
  background-color: #eee;
}

button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}
</style>
