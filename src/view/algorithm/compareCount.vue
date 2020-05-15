<template>
    <div class='dashboard'>
        <el-row class='title-bar'>
            <el-col :span='24'>
                <!-- <span style='background:#2da8ff;width:5px;height:15px;display:inline-block'></span> -->
                <span style='color:#2da8ff;margin-left:5px'>
                    <b>{{search}}</b>与<b>{{compare}}</b>对比
                    </span>
                <el-button 
                    type="primary" 
                    style="background-color:#2DA8FF;border:#2DA8FF" 
                    icon="el-icon-search" 
                    @click='searchCompare'>
                    直接前往{{compare}}算法
                </el-button>
            </el-col>
        </el-row>

        <el-row class='count-bar'>
            <el-col :span='8' class='count-left'>
                <div class='title'>{{title}}</div>
                <div class='intro-place'>{{introduction}}</div>
            </el-col>
            <el-col :span='12' class='count-middle'>
                <CompareBar :width='600' height="380px" @clickLine='clickLine'/>
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
import CompareBar from './components/CompareBar';
import PaperInfo from './components/paperInfo'
export default {
    components:{
        List,
        CompareBar,
        PaperInfo,
    },
    data(){
        return{
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
         index:'2',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        }, {
          index:'3',
            title: '宇宙无敌第一论文',
            src: '王小虎',
            time: '2016-05-02'
        }, {
          index:'4',
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
    },
    computed:{
        search:function(){
            return this.$route.params.search
        },
        compare:function(){
            return this.$route.params.compare
        },
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
        searchCompare(){
            const searchWords = this.$route.params.compare;
            this.$router.push(
                `/algorithm/${searchWords}`,
            );
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
        text-align: left;
    }
    .dashbord .title-bar{
            margin-left:0;
            text-align: left;
        }

    .title-bar{
        box-sizing: border-box;
        padding:10px;
        background: #fff;
        margin: 0 -20px 0 0;
        font-size:18px;
        width:100%;
        text-align: left;
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