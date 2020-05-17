<template>
    <div class='dashbord'>
        <el-row class='search-bar' :gutter="40">
            <el-col :span='24'>
                <span style='background:#2da8ff'>&nbsp;</span>
                <span style='color:#2da8ff;margin-left:5px'>算法查询</span>
                <el-button type="primary"  style="background-color:#2DA8FF;border:#2DA8FF" icon="el-icon-search" @click='search'>搜索</el-button>
                <el-input v-model="searchWords" placeholder="请输入算法名称查询"></el-input>
            </el-col>
        </el-row>

        <el-row class='charts-place' :gutter="20">
            <el-col :span="12">
                <div class='chart-title-left'>在相关会议中的占比</div>
                <CirclePieChart  
                    v-loading="loading1"
                    class='Left-Chart' 
                    :data='circleData'
                    id='conferenceDistribute' 
                    @clickPie='clickPie'>
                </CirclePieChart>
            </el-col>
            <el-col :span="12">
                <div class='chart-title-right'>相关算法云图</div>
                <word-cloud-chart
                    v-loading="loading2"
                    :data='cloudData' 
                    class='Right-Chart' 
                    id='wordCloud' 
                    height='350px' 
                    @clickCloud='clickCloud'>
                </word-cloud-chart >
            </el-col>
            <el-col :span="12">
               <div class='chart-title-left'>该算法的热度趋势</div>
                <LineChart 
                    v-loading="loading3"
                    :data='lineData' 
                    class='Left-Chart' 
                    id='recentYear' 
                    @clickLine='clickLine'>
                </LineChart>
            </el-col>
            <el-col :span="12">
               <div class='chart-title-right'>在相关会议中的占比</div>
                <CombineChart class='Right-Chart' id='realApply' ></CombineChart>
            </el-col>
        </el-row>


                        
    </div>
</template>


<script>
import CirclePieChart from './components/CirclePieChart';
import LineChart from './components/LineChart';
import PieChart from './components/PieChart';
import WordCloudChart from './components/WordCloudChart';
import CombineChart from './components/CombineChart';
import {fetchCloudChart,fetchPieChart,fetchBarChart} from '@/request/api'
// import {getMeetPercent} from '@/api/searchMeeting.js';

export default {
    data(){
        return{
            searchWords:'',
            cloudData:[],
            formData:{},
            circleData:[],
            lineData:[],
            CirclePieChartData:[],
            loading2:true,
            loading1:true,
            loading3:true,
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
        getPiedata(){
            fetchPieChart().then((res)=>{
                    this.loading1=false;
                    this.circleData=[
                        {value: res.data.percentAAAI, name: 'AAAI'},
                        {value: res.data.percentACM, name: 'ACM'},
                        {value: res.data.percentMK, name: 'MK'},
                        {value: res.data.percentMIT, name: 'MIT'},
                        {value: res.data.percentACL, name: 'ACL'}
                    ]
                    this.getBarData();
                })
        },
        getBarData(){
            fetchBarChart().then((res)=>{
                    this.loading3=false;
                    this.lineData = [
                        res.data.heat2014,res.data.heat2015,res.data.heat2016,
                        res.data.heat2017,res.data.heat2018,res.data.heat2019
                    ]
                    this.getCloudData();
                })
        },
        getCloudData(){
            fetchCloudChart().then((res)=>{
                    this.loading2=false;
                    // this.cloudData=function(){
                    //     return [...res.data.mapList]
                    // }
                    // let cloudData = []
                    // res.data.mapList.forEach((data)=>{
                    //     if (data.value>10)
                    //         cloudData.push(data)
                    // })
                    this.cloudData = res.data.mapList
    
                    
                })
        },
        _getAllData() {
                
                
                
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
        },
        clickLine(params){
            const searchWords = this.$route.params.search
            const year = params.name;
            this.$router.push(
                `/algorithm/yearcount/${searchWords}/${year}`,
            );
        },
        clickCloud(params){
            const searchWords = this.$route.params.search
            const compareWords = params.name
            console.log(params.name)
            this.$router.push(
                `/algorithm/comparecount/${searchWords}/${compareWords}`,
            );
        },
    },
    created(){
            this.getPiedata()
    },
    components:{
        CirclePieChart,
        LineChart,
        PieChart,
        WordCloudChart,
        CombineChart
    }
}
</script>


<style scoped>
    
    .dashbord {
        background-color: #f0f3f4;
       text-align: left;
        width:100%;
        padding:20px;
        padding-top:0;
        margin-top:20px;
        
    }
    .dashbord .search-bar{
            margin-left:0
        }

    .search-bar{
        box-shadow: inset 20px 0px #f0f3f4;
        box-sizing: border-box;
        padding:10px;
        background: #fff;
        margin: 0 -20px 0 0px;

        width:100%;
        font-size:18px;
    }

    .search-bar .el-col {
            line-height:40px;
            padding: 0 20px;
        }
    .search-bar .el-input{
            width:20%;
            float:right;
            margin-right:10px;
        }
    .search-bar .el-button{
            float:right;
        }

    .charts-place{
        width: 100%;
        margin: 0 -20px 0 0;
        font-size:18px;
    }

    .charts-place .el-col{
            margin:10px 0 0 0;
        }
    .charts-place .chart-title-left{
            background: #fff;
            padding:5px 20px;
            box-sizing:border-box;
            color:#2da8ff;
            font-weight:bold;
        }
    .charts-place .chart-title-right{
            background: #fff;
            padding:5px 40px;
            box-sizing:border-box;
            color:#2da8ff;
            font-weight:bold;
        }
    .charts-place .Left-Chart{
            background: #fff;
            padding:20px;
            box-sizing: border-box;
        }
    .charts-place .Right-Chart{
            background: #fff;
            padding:20px 20px 20px 40px;
            box-sizing: border-box;
        }
</style>