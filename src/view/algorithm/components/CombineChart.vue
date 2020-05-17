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
      default: "CombineChart"
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
      type: Array,
      default:function(){
        return []
      }
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
  watch:{
    data:function(val){
      console.log(val)
      this.initChart();
    }
  },
  methods: {
    
    initChart() {
      let callback = function(params){
          // const searchWords = params.name;
          // this.$router.push(
          //       `algorithm/search=${searchWords}`,
          //   );
            this.$emit('clickPie',params)
      }
      callback = callback.bind(this)
      this.chart = echarts.init(document.getElementById(this.id));
     
      
      const option = {
                legend: {},
                tooltip: {
                    trigger: 'axis',
                    showContent: false
                },
                dataset: {
                    source: [
                        ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
                        ['Matcha Latte', 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
                        ['Milk Tea', 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
                        ['Cheese Cocoa', 24.1, 67.2, 79.5, 86.4, 65.2, 82.5],
                        ['Walnut Brownie', 55.2, 67.1, 69.2, 72.4, 53.9, 39.1]
                    ]
                },
                xAxis: {type: 'category'},
                yAxis: {gridIndex: 0},
                grid: {top: '55%'},
                series: [
                    {type: 'line', smooth: true, seriesLayoutBy: 'row'},
                    {type: 'line', smooth: true, seriesLayoutBy: 'row'},
                    {type: 'line', smooth: true, seriesLayoutBy: 'row'},
                    {type: 'line', smooth: true, seriesLayoutBy: 'row'},
                    {
                        type: 'pie',
                        id: 'pie',
                        radius: '30%',
                        center: ['50%', '25%'],
                        label: {
                            formatter: '{b}: {@2012} ({d}%)'
                        },
                        encode: {
                            itemName: 'product',
                            value: '2012',
                            tooltip: '2012'
                        }
                    }
                ]
            };
        //   option.series[0].data = this.data
      //option.series[0].data[1].name='12312312';
      //在这一段地方书写东西来改变上面data里的值。
      let myChart = this.chart
      this.chart.on('updateAxisPointer', function (event) {
          console.log(event)
            var xAxisInfo = event.axesInfo[0];
            if (xAxisInfo) {
                var dimension = xAxisInfo.value + 1;
                myChart.setOption({
                    series: {
                        id: 'pie',
                        label: {
                            formatter: '{b}: {@[' + dimension + ']} ({d}%)'
                        },
                        encode: {
                            value: dimension,
                            tooltip: dimension
                        }
                    }
                });
            }
        });

        this.chart.setOption(option);
      
        this.chart.setOption(option);
        this.chart.on('click',callback)
    },
    
  }
};
</script>
<style scoped>
.chartsClass {
  padding-left: 1.2rem;
}
</style>