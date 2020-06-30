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
                        ['product', '2014', '2015', '2016', '2017', '2018', '2019'],
                        ['Supervised', 6.95, 6.15, 7.55, 6.44, 6.31, 5.88],
                        ['Regularization', 10.85, 7.47, 7.32, 6.99, 7.2, 7.21],
                        ['Reinforcement', 6.61, 6.72, 7.2, 11.5, 16.76, 15.63],
                        ['Linear', 2.37, 1.61, 1.63, 1.93, 1.76, 0.79]
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