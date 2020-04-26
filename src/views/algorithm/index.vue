<template>
    <div class='dashbord'>
        <el-row class='search-bar-index'>
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
                <span style='color:#2da8ff;margin-left:5px'>算法云图</span>

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
                <div class='cloud-place'>
                    <word-cloud-chart
                        v-loading="loading1"
                        ref="wordCloud"
                        :data="cloudData"
                        @clickCloud='searchCloud'
                    ></word-cloud-chart>
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
            // this.cloudData=[
            //     {
            //     name: "穷举法",
            //     value: 9898,
            //     year:2019,
            //     //在wordcloudchart.vue中的param.data属性里有name value 和 year
            //     },
            //     {
            //     name: "K-means",
            //     value: 1991
            //     },
            //     {
            //     name: "K-means",
            //     value: 9386
            //     },
            //     {
            //     name: "匈牙利算法",
            //     value: 7500
            //     },
            //     {
            //     name: "回溯法",
            //     value: 7500
            //     },
            //     {
            //     name: "Bellman算法",
            //     value: 6500
            //     },
            //     {
            //     name: "Vector-Direction",
            //     value: 6500
            //     },
            //     {
            //     name: "拉格朗日对数法",
            //     value: 6000
            //     },
            //     {
            //     name: "SVM向量机",
            //     value: 4500
            //     },
            //     {
            //     name: "匈牙利算法",
            //     value: 3800
            //     },
            //     {
            //     name: "朴素贝叶斯",
            //     value: 3000
            //     },
            //     {
            //     name: "协同过滤",
            //     value: 2500
            //     },
            //     {
            //     name: "推荐算法",
            //     value: 2300
            //     },
            //     {
            //     name: "匈牙利算法",
            //     value: 2000
            //     },
            //     {
            //     name: "协同过滤",
            //     value: 1900
            //     },
            //     {
            //     name: "自然语言处理",
            //     value: 1800
            //     },
            //     {
            //     name: "推荐算法",
            //     value: 1700
            //     },
            //     {
            //     name: "数据挖掘",
            //     value: 1600
            //     },
            //     {
            //     name: "郝人定",
            //     value: 1500
            //     },
            //     {
            //     name: "史胜天",
            //     value: 1200
            //     },
            //     {
            //     name: "王全会",
            //     value: 1100
            //     },
            //     {
            //     name: "郝继斐",
            //     value: 900
            //     },
            //     {
            //     name: "含哥又懂了",
            //     value: 800
            //     },
            // ]
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

<style lang="scss">
    .dashbord {
        background-color: #f0f3f4;
        width:100%;
        padding:20px;
        .search-bar-index{
            margin-left:0
        }
    }

    .search-bar-index{
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
        min-height:500px;
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

</style>