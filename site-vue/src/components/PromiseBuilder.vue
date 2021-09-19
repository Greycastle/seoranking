<template>
  <div>
    <slot
      :pending="pending"
      :fulfilled="fulfilled"
      :rejected="rejected"
      :settled="settled"
      :result="result"
      :error="error"
    />

    <slot v-if="pending" name="pending" />
    <slot v-else-if="fulfilled" name="fulfilled" :result="result" />
    <slot v-else-if="rejected" name="rejected" :error="error" />

    <slot v-if="settled" name="settled" :result="result" :error="error" />
  </div>
</template>

<script>

const PromiseStatus = Object.freeze({
  pending: Symbol('pending'),
  fulfilled: Symbol('fulfilled'),
  rejected: Symbol('rejected')
})

export default {
  props: {
    promise: {
      type: Promise,
      required: true,
    },
  },
  data() {
    return {
      status: PromiseStatus.pending,
      result: null,
      error: null,
    }
  },
  computed: {
    pending() { return this.status === PromiseStatus.pending },
    fulfilled() { return this.status === PromiseStatus.fulfilled },
    rejected() { return this.status === PromiseStatus.rejected },
    settled() { return this.status === PromiseStatus.rejected || this.status === this.fulfilled }
  },
  created() {
    this.trackPromise(this.promise)
  },
  methods: {
    async trackPromise(promise) {
      this.status = PromiseStatus.pending
      this.result = null
      this.error = null

      try {
        this.result = await promise
        this.status = PromiseStatus.fulfilled
      } catch (error) {
        this.error = error
        this.status = PromiseStatus.rejected

        throw error
      }
    }
  },
  watch: {
    promise(promise) {
      this.trackPromise(promise)
    }
  }
}
</script>