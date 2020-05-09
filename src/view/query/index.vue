<template>
    <div class='dashbord'>
        <el-row class='search-bar query-bar'>
            <el-col :span='24'>
                <!-- <span style='background:#2da8ff;width:5px;height:15px;display:inline-block'></span> -->
                <span style="background-color:#2da8ff">&nbsp;</span><span style='color:#2da8ff;margin-left:6px'>算法查询</span>
                <el-button type="primary" style="background-color:#2DA8FF;border:#2DA8FF" icon="el-icon-search" @click='search'>搜索</el-button>
                <el-input v-model="searchWords" placeholder="请输入算法名称查询"></el-input>
            </el-col>
        </el-row>

        <el-row class='cloud-place'>
            <el-col :span='24'>
                <span style='background:#2da8ff'>&nbsp;</span>
                <span style='color:#2da8ff;margin-left:5px'>算法映射</span>

    
                <SelectBar />
                <div class='pie-place' style='text-align:center;padding:20px'>
                    <div class="wrapper" style="width:600px;transform:translate(50%,0%)">
                        <PieChart width='600px'/>
                    </div>
                </div>
            </el-col>
        </el-row>

       
        <el-row class="analyse-part">
            <el-col :span='12' class='analyse-left'>
                <span style='color:#2da8ff;margin-left:5px'>算法分析</span>

            </el-col>
    
            <el-col :span='10' class='analyse-right'>
                <span style='color:#2da8ff;margin-left:5px'>2015-2019热门算法变化</span>
                <Form />
            </el-col>

        </el-row>
    </div>
</template>

<script>
import SelectBar from './components/SelectBar'
import PieChart from './components/PieChart'
import Form from './components/Form'
export default {
    data() {
    return {
        }
    },
    components: {
        SelectBar,
        PieChart,
        Form
    },

    methods: {

       
    }
}
</script>

<style scoped>
    .dashbord {
        background-color: #f0f3f4;
        width:100%;
        padding:20px 0 20px 20px;
        box-sizing: border-box;
    }

    .dashbord .search-bar{
            margin-left:-20px;
        }
    .search-bar{
        box-sizing: border-box;
        padding:10px;
        background: #fff;
        margin: 0 -20px 0 0;
        font-size:18px;
        width:100%;
    }
    .search-bar .el-col {
            line-height:40px;
            padding: 0 20px;
            text-align: left;
        }
    .search-bar .el-input{
            width:20%;
            float:right;
            margin-right:10px;
        }
    .search-bar .el-button{
            float:right;
        }

    .cloud-place{
        width:100%;
        box-sizing: border-box;
        padding:20px;
        padding-left:30px;
        margin: 20px 0 20px -20px;
        background: #fff;
        min-height:400px;
        font-size:18px;
        text-align:left;
    }


        .cloud-place .select-place{
            padding-top:10px;
        }
        .cloud-place .el-input__inner{
            height:30px;
            line-height:30px;
        }
        .cloud-place .el-input__icon{
            line-height:30px;
        }

    .analyse-part{
        box-sizing: border-box;
        min-height: 400px;
        background-color: #fff;
        width:100%;
        margin-left:-20px;
        text-align:left;
    }
     .analyse-part .analyse-left{
            padding:20px;
            box-sizing: border-box;
            box-shadow: inset -30px 0px #f0f3f4;
            min-height: 400px;
        }
         .analyse-part .analyse-right{
            padding:20px;
            box-sizing: border-box;
            /* // box-shadow: inset 20px 0px #f0f3f4; */
            min-height: 400px;
        }

</style>