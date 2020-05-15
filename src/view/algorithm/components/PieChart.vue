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
      default: "PieChart"
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
            title : {
                text: '相关会议中占比',
                //subtext: '纯属虚构',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                left: 'left',
                data: ['会议1','会议2','会议3','会议4','会议5']
            },
            series : [
                {
                    name: '会议1',
                    type: 'pie',
                    radius : '55%',
                    center: ['50%', '60%'],
                    data:[
                        {value:335, name:'会议1'},
                        {value:310, name:'会议2'},
                        {value:234, name:'会议3'},
                        {value:135, name:'会议4'},
                        {value:1548, name:'会议5'}
                    ],
                    itemStyle: {
                        emphasis: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            ]
        };

      option.series[0].name =this.$route.params.search;
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
<style  scoped>
.chartsClass {
  padding-left: 1.2rem;
}
</style>