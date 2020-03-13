<template>
    <div class='dashbord'>
        <el-row class='search-bar'>
            <el-col :span='24'>
                <span style='background:#2da8ff'>&nbsp;</span>
                <span style='color:#2da8ff;margin-left:5px'>算法查询</span>
                <el-button type="primary"  style="background-color:#2DA8FF;border:#2DA8FF" icon="el-icon-search" @click='search'>搜索</el-button>
                <el-input v-model="searchWords" placeholder="请输入算法名称查询"></el-input>
            </el-col>
        </el-row>

        <el-row class='charts-place'>
            <el-col :span="12">
                <div class='chart-title-left'>在相关会议中的占比</div>
                <CirclePieChart  class='Left-Chart' id='conferenceDistribute' @clickPie='clickPie'></CirclePieChart>
            </el-col>
            <el-col :span="12">
                <div class='chart-title-right'>相关算法云图</div>
                <word-cloud-chart 
                    :data='cloudData' 
                    class='Right-Chart' 
                    id='wordCloud' 
                    height='350px' 
                    @clickCloud='searchCloud'>
                </word-cloud-chart >
            </el-col>
            <el-col :span="12">
               <div class='chart-title-left'>该算法的热度趋势</div>
               <LineChart class='Left-Chart' id='recentYear'></LineChart>
            </el-col>
            <el-col :span="12">
               <div class='chart-title-right'>在相关会议中的占比</div>
                <PieChart class='Right-Chart' id='realApply' ></PieChart>
            </el-col>
        </el-row>


                        
    </div>
</template>


<script>
import CirclePieChart from './components/CirclePieChart';
import LineChart from './components/LineChart';
import PieChart from './components/PieChart';
import WordCloudChart from './components/WordCloudChart';

// import {getMeetPercent} from '@/api/searchMeeting.js';

export default {
    data(){
        return{
            searchWords:'',
            cloudData:[],
            formData:{},
            CirclePieChartData:[],
        }
    },
    computed:{
        searchAlgorithm(){
            const searchWords = this.$route.params.search.split('=')[1];
            return searchWords;
        }
    },
    methods:{
        search(){
            const searchWords = this.searchWords;
            this.$router.push(
                `search=${searchWords}`,
            );
            
        },
        _getAllData() {
            // this.$http
            //     .all([getMeetPercent()])
            //     .then(
            //     this.$http.spread((meetData) => {
            //         this.formData = meetData.data;
            //         console.log(this.formData)
            //         this.CirclePieChartData=[
            //                 {value:this.formData.percentAAAI,name:'AAAI'},
            //                 {value:this.formData.percentMeet1,name:'Meet1'},
            //                 {value:this.formData.percentMeet2,name:'Meet2'},
            //                 {value:this.formData.percentMeet3,name:'Meet3'},
            //                 {value:this.formData.percentMeet4,name:'Meet4'},

            //             ]
            //         console.log(this.CirclePieChartData)
            //         })
            //     )
            },
        searchCloud(params){
            const searchWords = params.name;
            this.$router.push(
                `/algorithm/search=${searchWords}`,
            );
        },
        clickPie(params){
            const searchWords = this.$route.params.search
            const meeting = params.name;
            this.$router.push(
                `/algorithm/meetingcount/${searchWords}/${meeting}`,
            );
        }
    },
    created(){
       this.cloudData=[
                {
                name: "穷举法",
                value: 9898,
                year:2019,
                //在wordcloudchart.vue中的param.data属性里有name value 和 year
                },
                {
                name: "K-means",
                value: 1991
                },
                {
                name: "K-means",
                value: 9386
                },
                {
                name: "匈牙利算法",
                value: 7500
                },
                {
                name: "回溯法",
                value: 7500
                },
                {
                name: "Bellman算法",
                value: 6500
                },
                {
                name: "Vector-Direction",
                value: 6500
                },
                {
                name: "拉格朗日对数法",
                value: 6000
                },
                {
                name: "SVM向量机",
                value: 4500
                },
                {
                name: "匈牙利算法",
                value: 3800
                },
                {
                name: "朴素贝叶斯",
                value: 3000
                },
                {
                name: "协同过滤",
                value: 2500
                },
                {
                name: "推荐算法",
                value: 2300
                },
                {
                name: "匈牙利算法",
                value: 2000
                },
                {
                name: "协同过滤",
                value: 1900
                },
                {
                name: "自然语言处理",
                value: 1800
                },
                {
                name: "推荐算法",
                value: 1700
                },
                {
                name: "数据挖掘",
                value: 1600
                },
               
            ];
            this._getAllData()
            // alert('1');
            // this.$http.all([getMeetPercent(),getCardsData()])
            // .then(this.$http.spread((meetData,cardsData)=>{
            //             console.log(meetData);
            //             console.log(cardsData)
            //             alert('2')
            //         }
            //     )
            // )
    },
    components:{
        CirclePieChart,
        LineChart,
        PieChart,
        WordCloudChart,
    }
}
</script>


<style lang="scss">
    @mixin shadow {
    box-shadow: 0 0 10px #e2e2e2;
    }
    .dashbord {
         background-color: #f0f3f4;
        // background-color: red;
        width:100%;
        padding:20px;
        padding-top:0;
        margin-top:-20px;
        .search-bar{
            margin-left:0
        }
    }

    .search-bar{
        box-sizing: border-box;
        padding:10px;
        background: #fff;
        margin: 0 -20px 0 0;

        width:100%;
        font-size:18px;
        .el-col {
            line-height:40px;
            padding: 0 20px;
        }
        .el-input{
            width:20%;
            float:right;
            margin-right:10px;
        }
        .el-button{
            float:right;
        }
    }

    .charts-place{
        width: 100%;
        margin: 0 -20px 0 0;
        font-size:18px;
        .el-col{
            margin:10px 0 0 0;
        }
        .chart-title-left{
            background: #fff;
            box-shadow: inset -20px 0px #f0f3f4;
            padding:5px 20px;
            box-sizing:border-box;
            color:#2da8ff;
            font-weight:bold;
        }
        .chart-title-right{
            background: #fff;
            box-shadow: inset 20px 0px #f0f3f4;
            padding:5px 40px;
            box-sizing:border-box;
            color:#2da8ff;
            font-weight:bold;
        }
        .Left-Chart{
            background: #fff;
            padding:20px;
            box-sizing: border-box;
            box-shadow: inset -20px 0px #f0f3f4;
        }
        .Right-Chart{
            background: #fff;
            padding:20px 20px 20px 40px;
            box-sizing: border-box;
            box-shadow: inset 20px 0px #f0f3f4;
        }
    }
</style>