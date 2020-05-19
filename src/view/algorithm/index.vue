<template>
    <div class='dashbord'>
        <el-row class='search-bar-index'>
            <el-col :span='24'>
                <!-- <span style='background:#2da8ff;width:5px;height:15px;display:inline-block'></span> -->
                <span style="background-color:#2da8ff">&nbsp;</span><span style='color:#2da8ff;margin-left:5px'>算法查询</span>
                <!-- <el-button type="primary" style="background-color:#2DA8FF;border:#2DA8FF" icon="el-icon-search" @click='search'>搜索</el-button>
                <el-input v-model="searchWords" placeholder="请输入算法名称查询"></el-input> -->
            </el-col>
        </el-row>

        <el-row class='cloud-place'>
            <el-col :span='24'>
                <span style='background:#2da8ff'>&nbsp;</span>
                <span style='color:#2da8ff;margin-left:5px'>矩形树图</span>

               
                <!-- <SelectBar /> -->
                <div class='cloud-place'>
                    <!-- <word-cloud-chart
                        v-loading="loading1"
                        ref="wordCloud"
                        :data="cloudData"
                        @clickCloud='searchCloud'
                    ></word-cloud-chart> -->
                    <RectTree @clickCloud='searchCloud'/>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import WordCloudChart from './components/WordCloudChart'
import SelectBar from './components/SelectBar'
import {fetchCloudChart} from '@/request/api'
import RectTree from './components/RectChart'
export default {
    data() {
    return {
        loading1:true,
      searchWords: '',
      domain:'',
      domains: [{
          value: '算法1',
          label: '算法1'
        }, {
          value: '算法2',
          label: '算法2'
        }, {
          value: '算法3',
          label: '算法3'
        }],
      year:'',
      years: [{
          value: '2019',
          label: '2019'
        }, {
          value: '2018',
          label: '2018'
        }, {
          value: '2017',
          label: '2017'
        }],
      cloudData:[],
        }
    },
    components: {
        WordCloudChart,
        SelectBar,
        RectTree,
    },
    created() {
        this._getAllData()
    },
    methods: {
        _getAllData() {
           
            fetchCloudChart().then((res)=>{
                console.log(res.data.mapList)
                // this.cloudData=function(){
                //     return [...res.data.mapList]
                // }
                this.cloudData = res.data.mapList
                this.loading1=false;
            })
        },
        search(){
            const searchWords = this.searchWords;
            this.$router.push(
                `/search=${searchWords}`,
            );
        },
        searchCloud(params){
            const searchWords = params.name;
            this.$router.push(
                `/algorithm/${searchWords}`,
            );
        },
    }
}
</script>

<style scoped>
    .dashbord {
        text-align: left;
        background-color: #f0f3f4;
        width:100%;
        padding:20px 0 20px 20px;
        box-sizing: border-box;
    }

    .dashbord .search-bar-index{
            margin-left:0px;
            background: #fff;
        }
    .search-bar-index{
        box-sizing: border-box;
        padding:10px;
        background: #fff;
        margin: 0 -20px 0 0;
        font-size:18px;
        width:100%;
    }

    .search-bar-index .el-col {
            line-height:40px;
            padding: 0 20px;
            text-align: left;
        }
    .search-bar-index .el-input{
            width:20%;
            float:right;
            margin-right:10px;
        }
    .search-bar-index .el-button{
            float:right;
        }


    .cloud-place{
        width:100%;
        box-sizing: border-box;
        padding:10px;
        margin: 20px 0;
        background: #fff;
        min-height:500px;
        font-size:18px;
        
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

</style>