<template>
    <div class='dashboard'>
        <el-row class='title-bar'>
            <el-col :span='24'>
                <!-- <span style='background:#2da8ff;width:5px;height:15px;display:inline-block'></span> -->
                <span style='color:#2da8ff;margin-left:5px'>会议情况分析:<span style="font-weight:bold;color:orange">{{meetName}}</span></span>
                <!-- <el-button 
                    type="primary" 
                    style="background-color:#2DA8FF;border:#2DA8FF" 
                    icon="el-icon-search" 
                    @click='search'>
                    直接前往该会议
                </el-button> -->
            </el-col>
        </el-row>

        <el-row class='count-bar'>
            <el-col :span='12' class='count-left'>
                <div class='chart-title-left'>会议涉及算法</div>
                <word-cloud-chart
                    v-loading="loading2"
                    :data='cloudData' 
                    class='Right-Chart' 
                    id='wordCloud' 
                    
                    @clickCloud='clickCloud'>
                </word-cloud-chart >
            </el-col>
            <el-col :span='12' class='count-middle'>
                <div class='chart-title-left'>会议主要算法</div>
                <CirclePieChart  
                    v-loading="loading1"
                    class='Left-Chart' 
                    :data='circleData'
                    id='conferenceDistribute' 
                    >
                </CirclePieChart>
                <!-- <LineChart :data='lineData' :width='600' height="380px" @clickLine='clickLine'/> -->
            </el-col>

        </el-row>

        <el-row class='title-bar' style='margin-top:20px'>
            <el-col :span='24'>
                <span style='color:#2da8ff;margin-left:5px'>论文列表</span>
                <!-- <el-button 
                    type="primary" 
                    style="background-color:#2DA8FF;border:#2DA8FF" 
                    icon="el-icon-search" 
                    @click='test'>
                    直接前往该会议
                </el-button> -->
            </el-col>
        </el-row>

        <el-row class='list-place'>
            <el-col :span='24'>
                <List :tableData="listData" :total="total" @pageChange='pageChange' @check='check'/>
                
            </el-col>
        </el-row>

        <el-drawer
            title="论文呈现页"
            :with-header="false"
            :visible.sync="drawer"
            :direction="direction"
            :before-close="handleClose">
            <PaperInfo :data='paperInfo'/>
        </el-drawer>
    
    
    
    </div>
</template>
<script>
import List from './components/list.vue'
// import LineChart from './components/LineChart';
import PaperInfo from './components/paperInfo.vue'
import CirclePieChart from './components/PieChart.vue'
import WordCloudChart from './components/WordCloudChart';
import {fetchCloudChart,fetchPieChart,CircleBarChart,fetchPaper} from '@/request/api'
export default {

    data(){
        return{
            lineData:[],
            listData:[],
            drawer:false,
            direction:'rtl',
            paperInfo:{},
            meetName:'',
            totalData:[],
            total:0,
            loading1:true,
            loading2:true,
            cloudData:[],
            circleData:[],
}
    },
    mounted(){
        this.meetName = this.$route.params.search.split("=")[1];
        
        fetchPaper(this.meetName).then((res)=>{
            console.log("Paper info:")
            console.log(res)
            this.totalData = res.data
            //this.listData = res.data
            this.total = res.data.length
            this.listData = res.data.slice(0,10)

        })
        fetchCloudChart(this.meetName).then((res)=>{
                    this.loading2=false;
                    this.cloudData = res.data.mapList

                    
                })
        fetchPieChart(this.meetName).then((res)=>{
            this.loading1=false;
                    this.circleData=[
                        {value: res.data.percentAAAI, name: 'AAAI'},
                        {value: res.data.percentACM, name: 'ACM'},
                        {value: res.data.percentMK, name: 'MK'},
                        {value: res.data.percentMIT, name: 'MIT'},
                        {value: res.data.percentACL, name: 'ACL'}
                    ]
        })

        fetchBarChart(this.meetName).then((res)=>{
                    console.log(res.data.mapList)
                    // this.cloudData=function(){
                    //     return [...res.data.mapList]
                    // 
                    this.lineData = [
                        res.data.heat2014,res.data.heat2015,res.data.heat2016,
                        res.data.heat2017,res.data.heat2018,res.data.heat2019
                    ]
                })
    },
    components:{
        List,
        WordCloudChart,
        PaperInfo,
        CirclePieChart
    },
    methods:{
        clickCloud(params){
        
            const searchWords = params.name
            console.log(params.name)
            this.$router.push(
                `/algorithm/${searchWords}`,
            );
        },
        clickLine(params){
            console.log(params)
        },
        check(params){
            console.log(params)
            this.drawer='true'
            this.paperInfo = params
        },
        pageChange(val){
           this.listData = this.totalData.slice(10*val-10,10*val)
        }
    }
}
</script>
<style scoped>
    .dashboard {
        background-color: #f0f3f4;
        width:100%;
        padding:20px 0 20px 20px;
        box-sizing: border-box;
        text-align:left;
    }
    .dashboard .title-bar{
            margin-left:0
        }

    .title-bar{
        margin-left:0px;
        box-sizing: border-box;
        padding:10px;
        background: #fff;
        margin: 0 -20px 0 0;
        font-size:18px;
        width:100%;
    }
    .title-bar .el-col {
            line-height:40px;
            padding: 0 20px;
        }
    .title-bar .el-input{
            width:20%;
            float:right;
            margin-right:10px;
        }
    .title-bar .el-button{
            float:right;
        }

    .count-bar{
        margin-top:20px;
    }
    .count-bar .el-col{
            padding: 0 20px;
            background: #fff;
            height: 500px;
        }
    .count-left{
            box-shadow: inset -30px 0px #f0f3f4;
        }
        .count-middle{
            padding-top:30px;
        }
        .count-right{
            box-shadow: inset 30px 0px #f0f3f4;
        }

    .list-place{
        margin: 20px 0;
    }
    .list-place .el-col{
            padding: 0 20px;
            background: #fff;
            min-height: 700px;
        }

     .Right-Chart{
            background: #fff;
            padding:20px;
            box-sizing: border-box;
        }
        .chart-title-left{
             background: #fff;
            padding:10px 10px;
            box-sizing:border-box;
            color:#2da8ff;
            font-weight:bold;
        }
</style>