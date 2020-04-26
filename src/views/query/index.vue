<template>
    <div class='dashbord'>
        <el-row class='search-bar query-bar'>
            <el-col :span='24'>
                <!-- <span style='background:#2da8ff;width:5px;height:15px;display:inline-block'></span> -->
                <span style='color:#2da8ff;margin-left:5px'>算法查询</span>
                <el-button type="primary" style="background-color:#2DA8FF;border:#2DA8FF" icon="el-icon-search" @click='search'>搜索</el-button>
                <el-input v-model="searchWords" placeholder="请输入算法名称查询"></el-input>
            </el-col>
        </el-row>

        <el-row class='cloud-place'>
            <el-col :span='24'>
                <span style='background:#2da8ff'>&nbsp;</span>
                <span style='color:#2da8ff;margin-left:5px'>算法映射</span>

                <!-- <div class='select-place'>
                    <span style='font-size:14px'>算法领域：</span>
                    <el-select v-model='domain' clearable placeholder="请选择">
                        <el-option
                            v-for="domain in domains"
                            :key="domain.value"
                            :label="domain.label"
                            :value="domain.value">
                        </el-option>
                    </el-select>

                    <span style='margin-left:5px;font-size:14px'>  选择年份：</span>
                    <el-select v-model='year' clearable placeholder="请选择">
                        <el-option
                            v-for="year in years"
                            :key="year.value"
                            :label="year.label"
                            :value="year.value">
                        </el-option>
                    </el-select>
                </div> -->
                <SelectBar />
                <div class='pie-place' style='text-align:center;padding:20px'>
                    <div class="wrapper" style="width:600px;transform:translate(50%,0%)">
                        <PieChart width='600px'/>
                    </div>
                </div>
            </el-col>
        </el-row>

        <el-row class="analyse-part">
            <el-col :span='13' class='analyse-left'>
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

<style lang="scss">
    .dashbord {
        background-color: #f0f3f4;
        width:100%;
        padding:20px;
        .search-bar{
            margin-left:-20px;
        }
    }

    .search-bar{
        box-sizing: border-box;
        padding:10px;
        background: #fff;
        margin: 0 -20px 0 0;
        font-size:18px;
        width:100%;
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

    .cloud-place{
        width:100%;
        box-sizing: border-box;
        padding:10px;
        margin: 20px 0;
        background: #fff;
        min-height:400px;
        font-size:18px;
        
        .el-col {
            padding: 0 20px;
        }
        .select-place{
            padding-top:10px;
        }
        .el-input__inner{
            height:30px;
            line-height:30px;
        }
        .el-input__icon{
            line-height:30px;
        }
    }

    .analyse-part{
        min-height: 400px;
        background-color: #fff;
        .analyse-left{
            padding:20px;
            box-sizing: border-box;
            box-shadow: inset -30px 0px #f0f3f4;
            min-height: 400px;
        }
        .analyse-right{
            padding:20px;
            box-sizing: border-box;
            // box-shadow: inset 20px 0px #f0f3f4;
            min-height: 400px;
        }
    }

</style>