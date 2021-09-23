<template>
  <div><a @click="toggle" class="sorter"><slot/> <span class="icon" :class="selected ? 'selected' : ''">{{ content }}</span></a></div>
</template>

<script>
export default {
  emits: ['sorted'],
  props: {
    sortKey: {
      type: String,
      required: true,
    },
    selectedKey: {
      type: String,
      required: true
    },
  },
  data() {
    return {
      direction: 'down'
    }
  },
  methods: {
    toggle() {
      if (this.selected) {
        this.direction = this.direction === 'down' ? 'up' : 'down'
      }
      this.$emit('sorted', { key: this.sortKey, direction: this.direction })
    }
  },
  computed: {
    selected() {
      return this.sortKey === this.selectedKey
    },
    content() {
      return this.direction === 'down' ? '▼' : '▲'
    }
  }
}
</script>


<style scoped>
a.sorter {
  color: #222;
  text-decoration: none;
}

a.sorter .icon {
  opacity: 0.2;
}

a:hover.sorter .icon, .sorter .icon.selected {
  opacity: 1.0;
}

</style>