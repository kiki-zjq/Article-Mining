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
        name:'Java SE',
        value:'2000',
        children:[
            {
                name:'JVM',  //children里面内容介绍的链接https://blog.csdn.net/TZ845195485/article/details/93238857?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158591779319724843358393%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158591779319724843358393&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-all_SOOPENSEARCH-1
                value:'600',
				children:[
                    {
                        name:'总体架构',
                        value:'150',
                    },
                    {
                        name:'类加载器的介绍',
                        value:'150',
						children:[
						    {
							      name:'启动类加载器',
							      value:'40',
                            },
							{
							      name:'扩展类加载器',
							      value:'60',
                            },
			       		   {
							      name:'应用程序类加载器',
							      value:'30',
                            },
				           {
							      name:'用户自定义类加载器',
							      value:'70',
                            },
                                 ]
                    },
					{
                        name:'Execution Engine',
                        value:'30',
                    },
	                {
                        name:'运行时数据区',
                        value:'150',
						children:[
						    {
							      name:'程序计数器',
							      value:'100',
                            },
							{
							      name:'本地方法栈',
							      value:'100',
                            },
			       		   {
							      name:'虚拟机栈',
							      value:'130',
                            },
                                 ]
                    },
                    {
                        name:'堆',
                        value:'150',
						children:[
						    {
							      name:'概述',
							      value:'50',
                            },
							{
							      name:'内存内部结构',
							      value:'100',
                            },
			       		   {
							      name:'养老区和永久代',
							      value:'80',
                            },
							{
							      name:'jdk1.7和1.8堆中结构区别',  //详细介绍https://blog.csdn.net/yjph83/article/details/84795856?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158600594419195162527033%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158600594419195162527033&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-all_SOOPENSEARCH-4
							      value:'100',
                            },
                                 ]
                    },
					{
                        name:'方法区',
                        value:'150',
                    },
                    {
                        name:'堆内存调优简介',
                        value:'150',
                    },
					{
                        name:' 四大垃圾算法GC',
                        value:'150',
						children:[
						    {
							      name:'引用计数法',
							      value:'40',
                            },
							{
							      name:'复制算法',
							      value:'60',
                            },
			       		   {
							      name:'标记清除',
							      value:'30',
                            },			       		
							{
							      name:'标记整理算法',
							      value:'70',
                            },
                                 ]
                    },
                ],
            },
            {
                name:'开发工具',
                value:'400',
                children:[
                    {
                        name:'Eclipse',
                        value:'100',
                    },
                    {
                        name:'IDEA',
                        value:'150',
                    },
                ],
            },
            {
                name:'数据结构', //附chidren展开的链接https://blog.csdn.net/weixin_43774841/article/details/93366381?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158600643619725211937932%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158600643619725211937932&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-all_SOOPENSEARCH-1
                value:'700',
                children:[
				    {
                        name:'栈',
                        value:'120',
                    },
					{
                        name:'队列',
                        value:'120',
                    },
                    {
                        name:'数组',
                        value:'160',
                    },
                    {
                        name:'链表',
                        value:'150',
                    },
					{
                        name:'红黑树',
                        value:'200',
                    },
                ]
            },
            {
                name:'基本语法',
                value:'1000',
                children:[				    
				    {
                        name:'流程控制',
                        value:'200',
                    },
                    {
                        name:'关键字',        //关键字包含了原有的数据类型这一项
                        value:'120',
                    },

                    {
                        name:'运算符',
                        value:'100'
                    },
                    {
                        name:'标识符',
                        value:'100',
                    },
					{
                        name:'注释',
                        value:'150',
                    },
                ]

            },
            {
                name:'面向对象',//children链接https://blog.csdn.net/weixin_38689154/article/details/78159273?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158600658719724843318468%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158600658719724843318468&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-all_SOOPENSEARCH-1
                value:'1000',
                children:[
                    {
                        name:'对象与类',
                        value:'200',
                    },
				    {
                        name:'封装',
                        value:'200',
                    },
                    {
                        name:'继承',
                        value:'200',
                    },
                    {
                        name:'多态',
                        value:'100',
                    },
                    {
                        name:'接口',
                        value:'200',
                    },
					{
                        name:'内部类',
                        value:'100',
                    },				
				    {
                        name:'Object类',
                        value:'50',
                    },
					{
                        name:'包',
                        value:'50',
                    },
                ],
            },
			{
                name:'IO流',
                value:'400',
				children:[
                         {
                        name:'文件',
                        value:'100',
                    },
				    {
                        name:'字节流',
                        value:'200',
                    },
                    {
                        name:'字符流',
                        value:'200',
                    },
                    {
                        name:'装饰器 ',
                        value:'100',
                    },
                    {
                        name:'序列化和反序列化',
                        value:'100',
                    },
					{
                        name:'随机访问文件',
                        value:'100',
                    },
                ],
            },
            {
                name:'多线程',//附chidren展开的链接https://blog.csdn.net/weixin_38689154/article/details/78162026?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158600737819726869021079%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158600737819726869021079&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-all_SOOPENSEARCH-1
                value:'600',
				children:[
                         {
                        name:'概述',
                        value:'100',
                    },
				    {
                        name:'多线程创建',
                        value:'200',
                    },
                    {
                        name:'多线程同步',
                        value:'200',
                    },
                    {
                        name:'多线程死锁',
                        value:'100',
                    },
                    {
                        name:'多线程通信',
                        value:'100',
                    },
					{
                        name:'多线程停止',
                        value:'100',
                    },
                ],
            },
            {
                name:'网络编程',//附chidren展开的链接https://blog.csdn.net/weixin_38689154/article/details/78165040?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158600770819724845058737%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158600770819724845058737&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-all_SOOPENSEARCH-1
                value:'300',
				children:[
                         {
                        name:'网络模型概述',
                        value:'200',
                    },
				    {
                        name:'TCP和UDP协议',
                        value:'300',
                    },
                    {
                        name:'网络编程其他',
                        value:'100',
                    },
                ],
            },
        ]

    },
    //------------------------------为了便于阅读，每个大类之间，写个注释分割开
    {
        name:'Database',
        value:'1000',
        children:[
            {
                name:'Mysql',
                value:'500'
            },
            {
                name:'Redis',
                value:'600',
                

            },
            {
                name:'MongoDB',
                value:'400'
            },
        ]
    },
	//--------------------
{
        name:'JavaWeb',//附链接
        value:'1000',
        children:[
            {
                name:'Tomcat',
                value:'100',
            },
            {
                name:'Servlet',
                value:'180',
            },
			{
                name:'Requeset',
                value:'100',
            },
			{
                name:'Responset',
                value:'100',
            },
			{
                name:'Cookie and Session',
                value:'100',
            },
			{
                name:'JSP',
                value:'250',
            }
        ]
    },
    //--------------------
    {
        name:'Java 常用框架',//附链接https://blog.csdn.net/guorui_java/article/details/104018528?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158597340519725222444953%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158597340519725222444953&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-all_SOOPENSEARCH-3
        value:'1200',
        children:[
            {
                name:'SSH',
                value:'600',
                children:[
                    {
                        name:'Struts',
                        value:'600',
                    },
					{
                        name:'Spring',
                        value:'600',
                    },
					{
                        name:'Hibernate',
                        value:'600',
                    }
                ]
            },
            {
                name:'SSM',
                value:'600',
                children:[
                    {
                        name:'spring',
                        value:'600',
                    },
					{
                        name:'SpringMVC',
                        value:'600',
                    },
					{
                        name:'mybatis',
                        value:'600',
                    }
					
                ]
            },
			{
                name:'Springboot',
                value:'600',
                
            }
        ]
    },
    //-------------------
    {
        name:'其他',
        value:'1000',
        children:[
            {
                name:'开发相关 Git',
                value:'700'
            },
            {
                name:'机器学习 Machine Learning',
                value:'400'
            },
            {
                name:'Elastic Search',
                value:'500'
            }
        ]
    }
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