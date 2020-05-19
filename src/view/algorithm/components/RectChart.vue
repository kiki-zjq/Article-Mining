<template>
  <div :id="id" :class="className" :style="{ height:height,width:width }" />
</template>


<script>
import echarts from 'echarts'
// import resize from '@/mixins/resize'
// import setup from '@/echarts/setup'
require('echarts/theme/macarons') // echarts theme

export default {
  props: {
    className: {
      type: String,
      default: "chart"
    },
    id: {
      type: String,
      default: "TreeChart"
    },
    width: {
      type: String,
      default: "100%"
    },
    height: {
      type: String,
      default: "500px"
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
  methods: {
      
    initChart() {

        let callback = function(param){
            if(param.data && !param.data.children){
                console.log(param)
                this.$emit('clickCloud',param.data)
            }
            
      }
      callback = callback.bind(this)

      this.chart = echarts.init(document.getElementById(this.id),'setup');
      const option = {
            series: [{
                type: 'treemap',
                leafDepth: 1,
                visibleMin: 300,
                roam:'false',
                label:{
                  normal:{
                      fontSize:16,
                  }  
                },
                data: [
    {
        
            
                name:'A-C',  
                value:'200',
				children:[
                    {
                        name:'A',
                        value:'100',
						children:[
						    {
							      name:'AdaBoost algorithm',
							      value:'10',
                            },
							{
							      name:'ANNs',
							      value:'30',
                            },
			       		   {
							      name:'approximation algorithm',
							      value:'122',
                            },
				           {
							      name:'Artificial Neural Networks',
							      value:'40',
                            },
                            {
                                name:'association rules',
							    value:'20',
                            }
                        ]
                    },
					{
                        name:'B',
                        value:'40',
                        children:[
                            {
                                name:'Back Propagation',
							    value:'4',
                            },
                            {
                                name:'backward algorithm',
							    value:'2',
                            },
                            {
                                name:'Batch Gradient Descent',
							    value:'1',
                            },
                            {
                                name:'Baum-Welch algorithm',
							    value:'2',
                            },
                            {
                                name:'BFGS algorithm',
							    value:'4',
                            },
                            {
                                name:'boosting method',
							    value:'2',
                            },
                            {
                                name:'boosting tree',
							    value:'1',
                            }
                        ]
                    },
                    {
                        name:'C',
                        value:'40',
                        children:[
                            {
                                name:'C 4.5',
							    value:'10',
                            },
                            {
                                name:'CART',
							    value:'10',
                            },
                            {
                                name:'classification algorithm',
							    value:'30',
                            },
                            {
                                name:'clustering algorithm',
							    value:'90',
                            },
                            {
                                name:'conditional random field',
							    value:'30',
                            },
                            {
                                name:'Convolutional Network',
							    value:'90',
                            },
                            {
                                name:'CRF',
							    value:'40',
                            },
                            {
                                name:'cross validation',
							    value:'20',
                            }
                        ]
                    },
                ]
	               

    },
    //------------------------------为了便于阅读，每个大类之间，写个注释分割开
    {
        name:'D-E',
        value:'600',
        children:[
            {
                name:'D',
                value:'200',
                children:[
                    {
                        name:'DBN',
                        value:'20',
                    },
                     {
                        name:'DBSCAN',
                        value:'20',
                    },
                     {
                        name:'decision tree',
                        value:'70',
                    },
                    {
                        name:'deep learning',
                        value:'150',
                    },
                    {
                        name:'DFP',
                        value:'10',
                    },
                    {
                        name:'dimensionality reduction algorithm',
                        value:'10',
                    },
                    {
                        name:'DT',
                        value:'60',
                    },
                    {
                        name:'dual algorithm',
                        value:'30',
                    }
                ],
            },
            {
                name:'E',
                value:'100',
                children:[
                     {
                        name:'EM',
                        value:'150',
                    },
                     {
                        name:'EM algorithm',
                        value:'90',
                    }
                ]
            },
        ]
    },
	//--------------------
{
        name:'F-I',//附链接
        value:'200',
        children:[
            {
                name:'F',
                value:'100',
                children:[
                    {
                        name:'forward stagewise',
                        value:'10',
                    }
                ]
            },
            {
                name:'G',
                value:'200',
                 children:[
                    {
                        name:'Gaussian mixture model',
                        value:'20',
                    },
                    {
                        name:'GBDT',
                        value:'10',
                    },
                    {
                        name:'GBM',
                        value:'10',
                    },
                    {
                        name:'GEM',
                        value:'10',
                    },
                    {
                        name:'GMM',
                        value:'30',
                    },
                    {
                        name:'gradient boosting algorithm',
                        value:'10',
                    },
                    {
                        name:'GSP',
                        value:'10'
                    }
                ]
            },
            {
                name:'H',
                value:'200',
                 children:[
                    {
                        name:'hidden Markov model',
                        value:'40',
                    },
                    {
                        name:'hierarchical clustering algorithm',
                        value:'10',
                    },
                    {
                        name:'HITS',
                        value:'15',
                    },
                    {
                        name:'HMM',
                        value:'50',
                    },
                    {
                        name:'HNN',
                        value:'15',
                    },
                ]
            },
            {
                name:'I',
                value:'100',
                children:[
                    {
                        name:'ID3',
                        value:'10',
                    },
                    
                ]
            },
			
        ]
    },
    //--------------------
    {
        name:'K-M',//附链接https://blog.csdn.net/guorui_java/article/details/104018528?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158597340519725222444953%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158597340519725222444953&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-all_SOOPENSEARCH-3
        value:'800',
        children:[
            {
                name:'K',
                value:'100',
                children:[
                    {
                        name:'kernel methods',
                        value:'56',
                    },
                    {
                        name:'Kernel PCA',
                        value:'10',
                    },
                    {
                        name:'K-Means',
                        value:'20',
                    },
                    {
                        name:'k-nearest neighbor',
                        value:'20',
                    },
                    {
                        name:'kNN',
                        value:'20',
                    },
                    {
                        name:'K-NN',
                        value:'20',
                    },
                ]
            },
            {
                name:'L',
                value:'150',
                 children:[
                    {
                        name:'LDA',
                        value:'66',
                    },
                    {
                        name:'linear regression',
                        value:'105',
                    },
                    {
                        name:'LLE',
                        value:'10',
                    },
                    {
                        name:'linear support vector machine',
                        value:'10',
                    },
                    {
                        name:'logistic regression',
                        value:'93',
                    },
                ]
            },
            {
                name:'M',
                value:'130',
                 children:[
                    {
                        name:'Markov random field',
                        value:'40',
                    },
                    {
                        name:'Mart',
                        value:'10',
                    },
                    {
                        name:'maximum margin method',
                        value:'15',
                    },
                    {
                        name:'MDS',
                        value:'10',
                    },
                    {
                        name:'Mini-Batch Gradient Descent',
                        value:'10',
                    },
                    {
                        name:'MRF',
                        value:'32',
                    },
                    {
                        name:'Multi-Dimensional Scaling',
                        value:'10',
                    },
                ]
            },
			
        ]
    },
    //-------------------
    {
        name:'N-R',
        value:'600',
       children:[
            {
                name:'N',
                value:'100',
                children:[
                    {
                        name:'Newton method',
                        value:'20',
                    },
                    {
                        name:'non-linear support vector machine',
                        value:'10',
                    },
                ]
            },
            {
                name:'P',
                value:'150',
                 children:[
                    {
                        name:'PageRank',
                        value:'30',
                    },
                    {
                        name:'PCA',
                        value:'105',
                    },
                    {
                        name:'perceptron algorithm',
                        value:'10',
                    },
                    {
                        name:'PLS',
                        value:'10',
                    },
                    {
                        name:'PLSA',
                        value:'10',
                    },
                    {
                        name:'Principal Component Analysis',
                        value:'40',
                    }
                ]
            },
            {
                name:'R',
                value:'200',
                 children:[
                            {
                                name:'random forest',
                                value:'40',
                            },
                            {
                                name:'RBF',
                                value:'10',
                            },
                            {
                                name:'RBN',
                                value:'15',
                            },
                            {
                                name:'regularization',
                                value:'200',
                            },
                            {
                                name:'reinforcement learning',
                                value:'300',
                            },
                            {
                                name:'Restricted Boltzmann Machine',
                                value:'30',
                            },

                        ]
                    },
                    
                ]
            },
            {
                name:'S-W',
                value:'300',
                children:[
                    {
                        name:'S',
                        value:'150',
                        children:[
                            {
                                name:'Self-Organizing Map',
                                value:'20',
                            },
                            {
                                name:'semi-supervised learning',
                                value:'150',
                            },
                            {
                                name:'sequential minimal optimization',
                                value:'10',
                            },
                            {
                                name:'semi-supervised learning',
                                value:'100',
                            },
                            {
                                name:'SGD',
                                value:'120',
                            },
                            {
                                name:'SMO',
                                value:'10',
                            },
                            {
                                name:'SOM',
                                value:'10',
                            },
                            {
                                name:'SOM',
                                value:'10',
                            },
                            {
                                name:'steepest descent',
                                value:'10',
                            },
                            {
                                name:'Stochastic Gradient Descent',
                                value:'60',
                            },
                            {
                                name:'supervised learning',
                                value:'200',
                            },
                            {
                                name:'support vector machines',
                                value:'50',
                            },
                            {
                                name:'SVM',
                                value:'150',
                            },
                        ]
                    },
                    {
                        name:'T-V',
                        value:'90',
                        children:[
                            {
                            name:'t-SNE',
                            value:'30',
                            },
                            {
                                name:'unsupervised learning',
                            value:'100',
                            },
                            {
                                name:'Viterbi algorithm',
                            value:'30',
                            }
                        ]
                    },
                ]
            },
            

],

                    levels: [
                        {   color:['#FF4F4F', '#EFBB36','#39A7F5','#FC58C8','#67C23A'],
                            itemStyle: {
                                borderColor: 'white',
                                borderWidth: 4,
                                gapWidth: 4
                            }
                        },
                        {
                            colorSaturation: [0.75, 0.5],
                            itemStyle: {
                                //borderColorSaturation: 0.9,
                                borderColor:'white',
                                gapWidth: 2,
                                borderWidth: 4
                            }
                        },
                        {
                            colorSaturation: [0.75, 0.5],
                            itemStyle: {
                                //borderColorSaturation: 0.9,
                                borderColor:'white',
                                gapWidth: 1,
                                borderWidth: 4
                            }
                        },
                        {
                            colorSaturation: [0.75, 0.5],
                            itemStyle: {
                                //borderColorSaturation: 0.9,
                                borderColor:'white',
                                gapWidth: 1,
                                borderWidth: 4
                            }
                        }
                    ]



            }]
        };
  
      //option.series[0].data[1].name='12312312';
      //在这一段地方书写东西来改变上面data里的值。
      
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