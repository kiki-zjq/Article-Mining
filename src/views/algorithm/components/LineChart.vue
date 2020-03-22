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
  watch:{
    data:function(newData){
      console.log(newData)
      this.initChart();
    }
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
      let callback = function(params){
          // const searchWords = params.name;
          // this.$router.push(
          //       `algorithm/search=${searchWords}`,
          //   );
            this.$emit('clickLine',params)
      }
      callback = callback.bind(this)
      this.chart = echarts.init(document.getElementById(this.id));
      const option = {
                 title:{
                    left: 'center',
                    text: '2013-2019热度趋势',
                 },
                 tooltip: {
                    trigger: 'axis',
                    axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                        type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                    },
                     formatter: `<b>年份</b>:{b}<br/>
                                 <b>论文占比</b>:{c}<br/>
                                 `
                    // formatter(params){
                
                    //   return `<b>年份</b>:${params.name}<br/>
                    //              <b>论文占比</b>:${params.data}<br/>
                    //              <b>论文数目</b>`
                    // }
                },
                 xAxis: {
                    type: 'category',
                    data: ['2014','2015', '2016', '2017', '2018', '2019'],
                    axisTick: {
                        alignWithLabel: true
                    }
                },
                yAxis: {
                    type: 'value',
                    // boundaryGap: [0, '100%']
                },
                series: [{
                    data: [ 123, 101, 534, 1290, 760, 1320],
                    type: 'line',
                    smooth: true,
                    animationEasing: 'cubicInOut',
                    animationDuration: 2600
                },{
                    data: [ 123, 101, 534, 1290, 760, 1320],
                    type: 'bar',
                    color:"#00C9FF"
                }]  
      };
      option.series[0].data = this.data
      option.series[1].data = this.data
      //option.series[0].data[1].name='12312312';
      //在这一段地方书写东西来改变上面data里的值。
      
      this.chart.setOption(option);
      this.chart.on('click',callback)
    },
    
  }
};
</script>
<style lang='scss' scoped>
.chartsClass {
  padding-left: 1.2rem;
}
</style>