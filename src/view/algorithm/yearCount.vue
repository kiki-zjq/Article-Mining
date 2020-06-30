<template>
    <div class='dashboard'>
        <el-row class='title-bar'>
            <el-col :span='24'>
                <!-- <span style='background:#2da8ff;width:5px;height:15px;display:inline-block'></span> -->
                <span style='color:#2da8ff;margin-left:5px'>会议情况分析</span>
                <el-button 
                    type="primary" 
                    style="background-color:#2DA8FF;border:#2DA8FF"  
                    @click='search'>
                    返回上一级
                </el-button>
            </el-col>
        </el-row>

        <el-row class='count-bar'>
            <el-col :span='11' class='count-left'>
                <!-- <div class='title'>{{title}}</div>
                <div class='intro-place'>{{introduction}}</div> -->
                <LineChart 
                    v-loading="loading3"
                    :data='lineData' 
                    class='Left-Chart' 
                    id='recentYear' 
                    @clickLine='clickLine'>
                </LineChart>
            </el-col>
            <el-col :span='12' offset="1" class='count-middle'>
                <CirclePieChart :data='circleData' :width='600' height="380px" @clickPie='clickPie'/>
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
                <List :tableData="listData" @pageChange='pageChange' @check='check'/>
            
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
import CirclePieChart from './components/CirclePieChart';
import LineChart from './components/LineChart';
import PaperInfo from './components/paperInfo';
import {fetchPieChart,fetchBarChart,fetchPaper} from '@/request/api'
export default {
    data(){
        return{
            listData:[],
            drawer:false,
            direction:'rtl',
            paperInfo:{},
            circleData:[],
            loading3:true,
            loading1:true,
            totalData:[],
        }
    },
    mounted(){
        const value = this.$route.params.year
        fetchPaper(value).then((res)=>{
            console.log("Paper info:")
            console.log(res)
            this.totalData = res.data
            //this.listData = res.data
            this.total = res.data.length
            this.listData = res.data.slice(0,10)

        })
        fetchPieChart(value).then((res)=>{
                    this.loading1=false;
                    this.circleData=[
                         {value: 14, name: 'AAAI'},
                        {value: 8, name: 'ACM'},
                        {value: 5, name: 'MK'},
                        {value: 3, name: 'MIT'},
                        {value: 2, name: 'ACL'}
                    ]
                })
        fetchBarChart(value).then((res)=>{
                    this.loading3=false;
                    this.lineData = [
                        res.data.heat2014,res.data.heat2015,res.data.heat2016,
                        res.data.heat2017,res.data.heat2018,res.data.heat2019
                    ]
                    // this.getCloudData();
                })
    },
    components:{
        List,
        CirclePieChart,
        PaperInfo,
        LineChart
    },
    methods:{
        clickPie(params){
            console.log(params)
        },
        clickLine(params){
            const searchWords = this.$route.params.search
            const year = params.name;
            this.$router.push(
                `/algorithm/yearcount/${searchWords}/${year}`,
            );
            this.$router.go(0)
        },
        search(){
            const searchWords = this.$route.params.search
            console.log(searchWords)
            this.$router.push(
                `/algorithm/${searchWords}`,
            );
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
    .dashbord {
        background-color: #f0f3f4;
        width:100%;
        padding:20px;
        margin-left:20px;
        
    }
    .dashbord .title-bar{
            margin-left:0;
            text-align:left;
        }

    .title-bar{
        box-sizing: border-box;
        padding:10px;
        background: #fff;
        margin: 0 -20px 0 0;
        font-size:18px;
        width:100%;
        text-align:left;
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
            height: 400px;
        }
    .count-bar .count-left{
            /* box-shadow: inset -30px 0px #f0f3f4; */
            padding-top: 30px;
        }
    .count-bar .count-middle{
            padding-top:30px;
        }
    .count-bar .count-right{
            /* box-shadow: inset 30px 0px #f0f3f4; */
        }

    .list-place{
        margin: 20px 0;
    }
    .list-place .el-col{
            padding: 0 20px;
            background: #fff;
            min-height: 700px;
        }
</style>