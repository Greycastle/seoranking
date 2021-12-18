<template>
  <div class="canvasContainer">
    <canvas ref="chartCanvas"></canvas>
  </div>
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
    },
    initiatives: {
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

    const activitiesPlugin = {
      id: 'activitiesPlugin',
      beforeDraw(chart) {
        const { ctx, config: { options }, chartArea: { top, bottom }, scales: { x } } = chart
        const actions = options.scales.x.actions
        ctx.save()

        ctx.strokeStyle = 'red'
        ctx.setLineDash([8, 8])

        for (var action of actions) {

          const posX = x.getPixelForValue(action.value)
          ctx.textAlign = 'center';
          ctx.fillText(action.title, posX, top + 5);

          ctx.beginPath()
          ctx.moveTo(posX, top + 20)
          ctx.lineTo(posX, bottom)
          ctx.stroke()
        }

        ctx.restore()
      }
    }

    const actions = this.initiatives.map((initiative) => {
      return {
        title: initiative.title,
        value: moment(initiative.date).format('LL')
      }
    })

    // ctx.height = 300
    new Chart(ctx, {
      type: 'line',
      data,
      plugins: [ activitiesPlugin ],
      options: {
        response: true,
        maintainAspectRatio: false,
        scales: {
          x: { actions },
          y: {
            suggestedMin: 1,
            suggestedMax: 50
          }
        }
      }
    })
  }
}
</script>

<style scoped>
.canvasContainer {
  height: 300px;
}
</style>