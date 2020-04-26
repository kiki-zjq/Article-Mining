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
      default: "RadarChart"
    },
    width: {
      type: String,
      default: "100%"
    },
    height: {
      type: String,
      default: "550px"
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
            title: {
                text: '基础雷达图'
            },
            tooltip: {},
            legend: {
                data: ['预算分配（Allocated Budget）', '实际开销（Actual Spending）']
            },
            radar: {
                // shape: 'circle',
                name: {
                    textStyle: {
                        color: '#fff',
                        backgroundColor: '#999',
                        borderRadius: 3,
                        padding: [3, 5]
                    }
                },
                indicator: [
                    { name: '销售（sales）', max: 6500},
                    { name: '管理（Administration）', max: 16000},
                    { name: '信息技术（Information Techology）', max: 30000},
                    { name: '客服（Customer Support）', max: 38000},
                    { name: '研发（Development）', max: 52000},
                    { name: '市场（Marketing）', max: 25000}
                ]
            },
            series: [{
                name: '预算 vs 开销（Budget vs spending）',
                type: 'radar',
                // areaStyle: {normal: {}},
                data: [
                    {
                        value: [4300, 10000, 28000, 35000, 50000, 19000],
                        name: '预算分配（Allocated Budget）'
                    },
                    {
                        value: [5000, 14000, 28000, 31000, 42000, 21000],
                        name: '实际开销（Actual Spending）'
                    }
                ]
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