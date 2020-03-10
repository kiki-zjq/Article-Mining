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
      default: "CirclePieChart"
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
  watch:{
    data:function(val){
      console.log(val)
      this.initChart();
    }
  },
  methods: {
    initChart() {
      this.chart = echarts.init(document.getElementById(this.id));
      const option = {
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)"
                },
                legend: {
                    orient: 'vertical',
                    x: 'left',
                    data:['会议1','会议2','会议3','会议4','会议5']
                },
                series: [
                    {
                        name:'访问来源',
                        type:'pie',
                        radius: ['50%', '70%'],
                        avoidLabelOverlap: false,
                        label: {
                            normal: {
                                show: false,
                                position: 'center'
                            },
                            emphasis: {
                                show: true,
                                textStyle: {
                                    fontSize: '30',
                                    fontWeight: 'bold'
                                }
                            }
                        },
                        labelLine: {
                            normal: {
                                show: false
                            }
                        },
                        data:this.data,
                        animationEasing: 'cubicInOut',
                        animationDuration: 2600
                    }
                ]
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