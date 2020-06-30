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
                text: '会议总览图'
            },
            tooltip: {},
            legend: {
                data: ['AAAI','ACM','MK','MIT','ACL']
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
                    { name: '权重因子', max: 5},
                    { name: '投稿量', max: 10000},
                    { name: '录取量', max: 5000},
                    { name: '引用量', max: 20000},
                    { name: '涉及算法数量', max: 100},

                ]
            },
            series: [{
                name: '预算 vs 开销（Budget vs spending）',
                type: 'radar',
                // areaStyle: {normal: {}},
                data: [
                    {
                        value: [5, 9431, 3800, 14233, 92],
                        name: 'AAAI'
                    },
                    {
                        value: [4, 9911, 4233, 16711, 88],
                        name: 'ACM'
                    },
                    {
                        value: [2, 7661, 3112, 8790, 66],
                        name: 'MK'
                    },
                    {
                        value: [3, 8023, 4561, 10023, 84],
                        name: 'MIT'
                    },
                    {
                        value: [4, 8609, 3712, 9234, 78],
                        name: 'ACL'
                    },
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
<style scoped>
.chartsClass {
  padding-left: 1.2rem;
}
</style>