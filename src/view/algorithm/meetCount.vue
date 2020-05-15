<template>
    <div class='dashboard'>
        <el-row class='title-bar'>
            <el-col :span='24'>
                <!-- <span style='background:#2da8ff;width:5px;height:15px;display:inline-block'></span> -->
                <span style='color:#2da8ff;margin-left:5px'>会议情况分析</span>
                <el-button 
                    type="primary" 
                    style="background-color:#2DA8FF;border:#2DA8FF" 
                    icon="el-icon-search" 
                    @click='search'>
                    直接前往该会议
                </el-button>
            </el-col>
        </el-row>

        <el-row class='count-bar'>
            <el-col :span='8' class='count-left'>
                <div class='title'>{{title}}</div>
                <div class='intro-place'>{{introduction}}</div>
            </el-col>
            <el-col :span='12' class='count-middle'>
                <LineChart :data='lineData' :width='600' height="380px" @clickLine='clickLine'/>
            </el-col>
            <el-col :span='4' class='count-right'>

            </el-col>
        </el-row>

        <el-row class='title-bar' style='margin-top:20px'>
            <el-col :span='24'>
                <span style='color:#2da8ff;margin-left:5px'>论文列表</span>
                <el-button 
                    type="primary" 
                    style="background-color:#2DA8FF;border:#2DA8FF" 
                    icon="el-icon-search" 
                    @click='test'>
                    直接前往该会议
                </el-button>
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
import LineChart from './components/LineChart';
import PaperInfo from './components/paperInfo'
import {fetchBarChart} from '@/request/api'
export default {
    data(){
        return{
            lineData:[],
            listData:[],
            drawer:false,
            direction:'rtl',
            paperInfo:{},
        }
    },
    mounted(){
        this.listData =[{
            index:'1',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        }, {
         index:'1',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        }, {
          index:'1',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        }, {
          index:'1',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        },{
            index:'1',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        }, {
         index:'1',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        }, {
          index:'1',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        }, {
          index:'1',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        },{
          index:'1',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        },{
          index:'1',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        },{
          index:'1',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        },]
        fetchBarChart().then((res)=>{
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
        LineChart,
        PaperInfo,
    },
    methods:{
        clickLine(params){
            console.log(params)
        },
        check(params){
            console.log(params)
            this.drawer='true'
            this.paperInfo = params
        },
        pageChange(){
            this.listData =[{
            index:'1',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
            }, {
            index:'1',
                title: '这个是第二页',
                src: '王小虎',
                time: '2016-05-02'
            }, {
            index:'1',
                title: '这个是第二页',
                src: '王小虎',
                time: '2016-05-02'
            }, {
            index:'1',
                title: '这个是第二页',
                src: '王小虎',
                time: '2016-05-02'
            },{
                index:'1',
                title: '这个是第二页',
                src: '王小虎',
                time: '2016-05-02'
            }, {
            index:'1',
                title: '这个是第二页',
                src: '王小虎',
                time: '2016-05-02'
            }, {
            index:'1',
                title: '这个是第二页',
                src: '王小虎',
                time: '2016-05-02'
            }, {
            index:'1',
                title: '这个是第二页',
                src: '王小虎',
                time: '2016-05-02'
            },{
            index:'1',
                title: '这个是第二页',
                src: '王小虎',
                time: '2016-05-02'
            },{
            index:'1',
                title: '这个是第二页',
                src: '王小虎',
                time: '2016-05-02'
            },{
            index:'1',
                title: '这个是第二页',
                src: '王小虎',
                time: '2016-05-02'
            },]
        }
    }
}
</script>
<style scoped>
    .dashbord {
        background-color: #f0f3f4;
        width:100%;
        padding:20px;
        padding-top:40px;
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
            box-shadow: inset -30px 0px #f0f3f4;
        }
    .count-bar .count-middle{
            padding-top:30px;
        }
    .count-bar .count-right{
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
</style>