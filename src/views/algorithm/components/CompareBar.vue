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
                legend: {},
                tooltip: {
                    trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        },
                     

                },
                dataset: {
                    dimensions: ['product', '2015', '2016', '2017'],
                    source: [
                        {product: 'Matcha Latte', '2015': 43.3, '2016': 85.8, '2017': 93.7},
                        {product: 'Milk Tea', '2015': 83.1, '2016': 73.4, '2017': 55.1},
                        {product: 'Cheese Cocoa', '2015': 86.4, '2016': 65.2, '2017': 82.5},
                        {product: 'Walnut Brownie', '2015': 72.4, '2016': 53.9, '2017': 39.1}
                    ]
                },
                xAxis: {type: 'category'},
                yAxis: {},
                // Declare several bar series, each will be mapped
                // to a column of dataset.source by default.
                series: [
                    {type: 'bar',color:"#00C9FF"},
                    {type: 'bar'},
                ]
            };
            // option.dataset.dimensions=['product', '2015', '2016', '2018'];
            // option.dataset.source[0]={product: 'Matcha Latte', '2015': 49.3, '2016': 85.8, '2017': 93.7};

    //   const option = {
    //              title:{
    //                 left: 'center',
    //                 text: '2013-2019热度趋势',
    //              },
    //              tooltip: {
    //                 // trigger: 'axis',
    //                 // axisPointer: {            // 坐标轴指示器，坐标轴触发有效
    //                 //     type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
    //                 // },
    //                 //  formatter: `<b>年份</b>:{b}<br/>
    //                 //              <b>论文占比</b>:{c}<br/>
    //                 //              `
    //                 // formatter(params){
                
    //                 //   return `<b>年份</b>:${params.name}<br/>
    //                 //              <b>论文占比</b>:${params.data}<br/>
    //                 //              <b>论文数目</b>`
    //                 // }
    //             },
    //              xAxis: {
    //                 type: 'category',
                    
    //                 // axisTick: {
    //                 //     alignWithLabel: true
    //                 // }
    //             },
    //             yAxis: {
    //                 // type: 'value',
    //                 // boundaryGap: [0, '100%']
    //             },
    //             dataset: {
    //                dimensions:[],
    //                 source:[],
    //             },
    //             series: [
    //                 {type: 'bar'},
    //                 {type: 'bar'},
    //             ]   
    //   };
  
    //   //option.series[0].data[1].name='12312312';
    //   //在这一段地方书写东西来改变上面data里的值。
        const search = this.$route.params.search
        const compare = this.$route.params.compare
        option.dataset.dimensions=['year',search,compare]
        option.dataset.source[0]={
                    'year':'2013',
                    [search]:820,
                    [compare]:230,
                } 
      option.dataset.source[0]={
          'year':'2013',
          [search]:820,
          [compare]:230,
      }
      option.dataset.source[1]={
          'year':'2014',
          [search]:120,
          [compare]:603,
      }
      option.dataset.source[2]={
          'year':'2015',
          [search]:500,
          [compare]:500,
      }
      option.dataset.source[3]={
          'year':'2016',
          [search]:480,
          [compare]:1230,
      }
      option.dataset.source[4]={
          'year':'2017',
          [search]:1000,
          [compare]:250,
      }
      option.dataset.source[5]={
          'year':'2018',
          [search]:1500,
          [compare]:603,
      }
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