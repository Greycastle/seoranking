<template>
  <canvas ref="chartCanvas"></canvas>
</template>
<script>
import { Chart, registerables } from 'chart.js'
import moment from 'moment'
import 'chartjs-adapter-moment';

export default {
  props: {
    dataPoints: {
      type: Array,
      required: true
    }
  },
  created() {
    Chart.register(...registerables)
  },
  mounted() {
    let ctx = this.$refs.chartCanvas.getContext("2d")

    const data = {
      labels: this.dataPoints.map((point) => moment(point.date).format('LL')),
      datasets: [
        {
          label: 'Ranking',
          data: this.dataPoints.map((point) => point.rank),
          borderColor: '#33F09E',
          backgroundColor: '#33F09E',
        }
      ]
    }

    new Chart(ctx, {
      type: 'bar',
      data,
      options: {
        response: true
      }
    })
  }
}
</script>
