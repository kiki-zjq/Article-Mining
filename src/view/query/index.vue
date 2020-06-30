<template>
    <div class='dashbord'>
        <el-row class='search-bar query-bar'>
            <el-col :span='24'>
                <!-- <span style='background:#2da8ff;width:5px;height:15px;display:inline-block'></span> -->
                <span style="background-color:#2da8ff">&nbsp;</span><span style='color:#2da8ff;margin-left:5px'>算法查询</span>
        

                <el-button type="primary" style="background-color:#2DA8FF;border:#2DA8FF" icon="el-icon-search" @click='search'>搜索</el-button>
                <el-input v-model="searchWords" placeholder="请输入算法名称查询"></el-input>
            </el-col>
        </el-row>

        <!-- <el-row class='cloud-place' >
            <el-col :span='11'>
                <span style='background:#2da8ff;margin-left:-10px'>&nbsp;</span><span style='color:#2da8ff;margin-left:5px'>算法比例</span>

    
                <SelectBar />
                <div class='pie-place' style='text-align:center;padding:20px'>
                    
                </div>
            </el-col>

            <el-col :span='11' :offset='1'>
                <div>
                    <span style='background:#2da8ff;margin-left:-10px'>&nbsp;</span><span style='color:#2da8ff;margin-left:5px'>过滤器</span>
                </div>
            </el-col>
        </el-row> -->

        <el-row class='count-bar'>
            <el-col :span='12' class='count-left'>
                 <span style='background:#2da8ff;margin-left:-30px;'>&nbsp;</span><span style='color:#2da8ff;margin-left:5px'>算法比例</span>
                <CirclePieChart  
                    style="margin-top:20px"
                    v-loading="loading1"
                    class='Left-Chart' 
                    :data='circleData'
                    id='conferenceDistribute' 
                    @clickPie='clickPie'>
                </CirclePieChart>

            </el-col>
            <el-col :span='11' :offset='1' class='count-middle'>
                 <span style='background:#2da8ff;margin-left:0px;'>&nbsp;</span><span style='color:#2da8ff;margin-left:5px'>过滤器</span>
                <div style="margin-top:20px">
                    <i style='color:#A0A3A4'>通过修改过滤器设置，可以更改搜索的范围以及结果</i><br/><br/>
                    <span style='color:#2da8ff;margin-right:5px'>修改搜索年份:</span>
                    <el-select v-model='yearStart' clearable placeholder="请选择起始年份">
                        <el-option
                            v-for="year in years1"
                            :key="year.value"
                            :label="year.label"
                            :value="year.value">
                        </el-option>
                    </el-select>
                    <span style='color:#2da8ff;margin:0 10px'>至</span>
                    <el-select v-model='yearEnd' clearable placeholder="请选择结束年份">
                        <el-option
                            v-for="year in years2"
                            :key="year.value"
                            :label="year.label"
                            :value="year.value">
                        </el-option>
                    </el-select>
                    <br/><br/>
                    <span style='color:#2da8ff;margin-right:10px;float:left'>修改会议范围:</span>
                    <el-checkbox-group style='float:left' v-model="checkList">
                        <el-checkbox label="AAAI"></el-checkbox>
                        <el-checkbox label="ACM"></el-checkbox>
                        <el-checkbox label="MK"></el-checkbox>
                        <el-checkbox label="MIT"></el-checkbox>
                        <el-checkbox label="ACL"></el-checkbox>
                </el-checkbox-group>

                <br /><br />
                 <el-button type="primary" style="float:right;background-color:#2DA8FF;border:#2DA8FF" @click='filter'>开始过滤</el-button>

                </div>
            
            </el-col>
            <!-- <el-col :span='4' class='count-right'>

            </el-col> -->
        </el-row>
       
        <el-row class="analyse-part">
            <!-- <el-col :span='12' class='analyse-left'>
                <span style="background-color:#2da8ff">&nbsp;</span><span style='color:#2da8ff;margin-left:5px'>算法分析</span>

            </el-col> -->
    
            <el-col :span='24' class='analyse-right'>
                <span style="background-color:#2da8ff">&nbsp;</span><span style='color:#2da8ff;margin-left:5px'>论文列表</span>
                <Form :tableData="listData" :total="total" @pageChange='pageChange' @check='check'/>
            </el-col>

        </el-row>
    </div>
</template>

<script>
import SelectBar from './components/SelectBar'
import CirclePieChart from './components/CirclePieChart';
import Form from './components/Form'
import {fetchBarChart,fetchPieChart,fetchPaper} from '@/request/api'
export default {
    data() {
    return {
        checkList:['AAAI','ACM','MK','MIT','ACL'],
        searchWords:'',
        total:0,
        yearStart:'',
        yearEnd:'',
            lineData:[],
            listData:[],
            drawer:false,
            direction:'rtl',
            paperInfo:{},
            circleData:[],
            loading2:true,
            totalData:[],
             years2: [{
                value: '2016',
                label: '2016'
                }, {
                value: '2017',
                label: '2017'
                }, {
                value: '2018',
                label: '2018'
                }, {
                value: '2019',
                label: '2019'
                }],
             years1: [{
                value: '2015',
                label: '2015'
                }, {
                value: '2016',
                label: '2016'
                }, {
                value: '2017',
                label: '2017'
                }, {
                value: '2018',
                label: '2018'
                }, {
                value: '2019',
                label: '2019'
                }],
            
        }
    },
    components: {
        SelectBar,
        CirclePieChart,
        Form
    },
     mounted(){
       
    },
    methods: {

        filter(){
            if(this.total==0&&this.searchWords==''){
                this.$notify({
                title: '失败',
                message: '请先进行搜索',
                type: 'warning'
                });
            }else if(this.total==0&&this.searchWords!=''){
                this.search()
            }else{
                this.$notify({
                title: '成功',
                message: '已开始过滤',
                type: 'success'
                });
            }


        },
        search(){
             this.$notify({
          title: '成功',
          message: '已开始查询',
          type: 'success'
        });

            fetchPaper().then((res)=>{
            console.log("Paper info:")
            console.log(res)
            this.totalData = res.data
            //this.listData = res.data
            this.total = res.data.length
            this.listData = res.data.slice(0,10)

         })
          fetchPieChart().then((res)=>{
                    this.loading1=false;
                    this.circleData=[
                        {value: res.data.percentAAAI, name: 'AAAI'},
                        {value: res.data.percentACM, name: 'ACM'},
                        {value: res.data.percentMK, name: 'MK'},
                        {value: res.data.percentMIT, name: 'MIT'},
                        {value: res.data.percentACL, name: 'ACL'}
                    ]
                    //this.getBarData();
                })
        },
        goback(){
            const searchWords = this.$route.params.search
            console.log(searchWords)
            this.$router.push(
                `/algorithm/${searchWords}`,
            );
        },
       
    }
}
</script>

<style scoped>
    .dashbord {
        background-color: #f0f3f4;
        width:100%;
        padding:20px 0 20px 20px;
        box-sizing: border-box;
        text-align:left;
    }

    .dashbord .search-bar{
            margin-left:0px;
        }
    .search-bar{
        margin-left:0px;
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
        
        margin: 20px 0;
        background: #fff;
        min-height:400px;
        font-size:18px;
        text-align:left;
    }


    .cloud-place .el-col {
            padding: 0 20px;
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
        margin-left:0;
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

            .count-bar{
        margin-top:20px;
    }
    .count-bar .el-col{
            padding: 0 20px;
            background: #fff;
            height: 400px;
            margin-bottom: 40px;
        }
    .count-bar .count-left{
            /* box-shadow: inset -30px 0px #f0f3f4; */
            padding-top: 30px;
            padding-left:60px;
        }
    .count-bar .count-middle{
            padding-top:30px;
        }
    .count-bar .count-right{
            /* box-shadow: inset 30px 0px #f0f3f4; */
        }
</style>