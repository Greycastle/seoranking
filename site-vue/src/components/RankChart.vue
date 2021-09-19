<template>
  <canvas ref="chartCanvas"></canvas>
</template>
<script>
import { Chart, registerables } from 'chart.js'
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
      labels: this.dataPoints.map((point) => point.date),
      datasets: [
        {
          label: 'Ranking',
          data: this.dataPoints.map((point) => point.rank),
          borderColor: 'rgb(75, 192, 192)',
        }
      ]
    }

    new Chart(ctx, {
      type: 'line',
      data,
      options: {
        response: true,
        scales: {
          x: {
            type: 'time',
            title: {
              display: true,
              text: 'Date'
            }
          },
          y: {
            title: {
              display: true,
              text: 'Rank'
            },
            suggestedMax: 1,
            suggestedMin: 50
          }
        }
      }
    })
  }
}
</script>
