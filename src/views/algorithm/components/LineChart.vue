<template>
  <div :id="id" :class="className" :style="{ height:height,width:width }" />
</template>


<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme

export default {
  props: {
    className: {
      type: String,
      default: "chart"
    },
    id: {
      type: String,
      default: "LineChart"
    },
    width: {
      type: String,
      default: "100%"
    },
    height: {
      type: String,
      default: "350px"
    },
    data: {
      type: Function,
    },
    title: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      chart: null
    };
  },
  mounted() {
    this.initChart();
  },
  beforeDestroy() {
    if (!this.chart) {
      return;
    }
    this.chart.dispose();
    this.chart = null;
  },
  methods: {
    initChart() {
      this.chart = echarts.init(document.getElementById(this.id));
      const option = {
                 title:{
                    left: 'center',
                    text: '2013-2019热度趋势',
                 },
                 xAxis: {
                    type: 'category',
                    data: ['2013','2014','2015', '2016', '2017', '2018', '2019']
                },
                yAxis: {
                    type: 'value',
                    boundaryGap: [0, '100%']
                },
                series: [{
                    data: [820, 123, 101, 534, 1290, 760, 1320],
                    type: 'line',
                    smooth: true,
                    animationEasing: 'cubicInOut',
                    animationDuration: 2600
                }]
      };
  
      //option.series[0].data[1].name='12312312';
      //在这一段地方书写东西来改变上面data里的值。
      
      this.chart.setOption(option);
      this.chart.on('click',function(param){
          console.log(param);
      })
    },
    
  }
};
</script>
<style lang='scss' scoped>
.chartsClass {
  padding-left: 1.2rem;
}
</style>