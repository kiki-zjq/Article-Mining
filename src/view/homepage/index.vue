<template>
    <div class="homepage-block">
        <el-row class='total-look' >
            <el-col :span='5' >
                <span style="color:#40C9C6;font-size:20px;font-weight:bold">15,036</span>
                <i  style='float:right;font-size:54px;color:#40C9C6;margin-top:10px;' class="el-icon-document"></i>
                <br />
                <span style="font-size:16px">论文数量</span>
                
            </el-col>

            <el-col :span='5' :offset="1">
                <span style="color:#36A3F7;font-size:20px;font-weight:bold">108</span>
                 <i  style='float:right;font-size:54px;color:#36A3F7;margin-top:10px;' class="el-icon-monitor"></i>
                <br />
                <span style="font-size:16px">算法数量</span>
            </el-col>
            
            <el-col :span='5' :offset="1">
                <span style="color:#F4516C;font-size:20px;font-weight:bold">5</span>
                <i  style='float:right;font-size:54px;color:#F4516C;margin-top:10px;' class="el-icon-menu"></i>
                <br />
                <span style="font-size:16px">会议数量</span>
            </el-col>
            
            <el-col :span='5' :offset="1">
                <span style="color:#34BFA3;font-size:20px;font-weight:bold">5 <span style='font-size:16px'>年</span></span>
                <i  style='float:right;font-size:54px;color:#34BFA3;margin-top:10px;' class="el-icon-date"></i>
                <br />
                <span style="font-size:16px">年份跨度</span>
            </el-col>

        </el-row>
        
        <el-row class='intro'>
            <el-col :span='13'>
                <div>
                    <h3 class='main-title'>网站介绍</h3>
                    <p style='text-indent:2em;'>AMS Stack是一个采用数据挖掘技术开发的，可以连接算法，会议和应用场景的网站。AMS Stack不仅可以提供算法，会议和场景的基本信息，并且能够深入分析算法和会议的热度趋势变化，评估会议质量和影响力，根据应用场景推荐合适的算法，甚至把算法，会议和场景联系起来，向用户展示全方位的信息等。</p>
                </div>
            </el-col>
            <el-col :span='9' :offset='1' style='background-color: #f0f3f4;box-shadow: 0 0 0 #e2e2e2;'>
                <div style='width:100%;margin:-40px auto'>
                <img src='./logo.png' width='120%'/>
                </div>
            </el-col>
        </el-row>  

        <el-row class='enter'>
            <el-col :span='7'>
                <div class='wrapper' @click='handleClick(1)' @mouseenter='handleHover(1)'>
                    <img src='./alg.png' width='100%'/>
                    <div class='inner'>算法页面</div>
                </div>
            </el-col>

            <el-col :span='7' :offset='1'>
                <div class='wrapper' @click='handleClick(2)' @mouseenter='handleHover(2)'>
                    <img src='./meet.png' width='100%' @click='handleClick(2)'/>
                    <div class='inner'>会议页面</div>
                </div>
            </el-col>

            <el-col :span='7' :offset='1'>
                <div class='wrapper' @click='handleClick(3)' @mouseenter='handleHover(3)'>
                    <img src='./query.png' width='100%' @click='handleClick(3)'/>
                    <div class='inner'>查询页面</div>
                </div>
            </el-col>

        </el-row>  

        <el-row class='module-intro'>
            <el-col :span='13'>
                <h3 class='main-title'>{{title}}</h3>
                <p style='text-indent:2em'>{{description}}</p>
            </el-col>

            <el-col :span='9' :offset='1'>
                <PieCharts />
            </el-col>
        </el-row> 


    </div>
</template>

<script>
import IntroCard from './components/IntroCard';
import PieCharts from './components/PieChart'
export default {
    components:{
        IntroCard,
        PieCharts
    },
     data(){
            return{
                title:'算法界面',
                description:'算法查询版块包括近五年来算法热度趋势分析；与该算法类似的其他算法介绍；该算法在相关会议的情况以及算法对应的论文列表等。',
            }
        },
    methods:{
       
        handleClick(val){
            switch(val){
                case 1:this.$router.push('/algorithm');break;
                case 2:this.$router.push('/meeting');break;
                case 3:this.$router.push('/query');break;
            }
        },
        handleHover(val){
            switch(val){
                case 1: 
                    this.description='算法查询版块包括近五年来算法热度趋势分析；与该算法类似的其他算法介绍；该算法在相关会议的情况以及算法对应的论文列表等。';
                    this.title='算法界面';
                    break;
                case 2: 
                    this.description='会议查询版块包括5个顶会的基本介绍；五个顶会在论文发布量，论文的平均引用量和论文下载量三个方面的可视化比较；每个会议的论文情况；会议的算法云图以及在该会议中某个算法的分析。';
                    this.title='会议界面';
                    break;
                case 3: 
                    this.description='通过搜索框搜索场景，场景查询版块包括该场景映射的所有算法的分析和比较，为用户推荐合适的算法。';
                    this.title='查询界面';
                    break;
            }
        }
    }
}
</script>

<style scoped>
.homepage-block{
    background-color: #f0f3f4;
    width:100%;
    padding:20px 0 20px;
    box-sizing: border-box;
    text-align: left;
    margin-left:20px;
}
.total-look{
    box-sizing: border-box;
    padding:10px;
    margin: 0 -20px 20px 0;
    font-size:18px;
    width:100%;
}
.total-look .el-col {
    background: #fff;
    height:108px;
    line-height:40px;
    padding:  20px;
    text-align: left;
    box-shadow: 0 0 10px #e2e2e2;
}
.intro{
    box-sizing: border-box;
    padding:10px;
    margin: 0 -20px 20px 0;
    font-size:18px;
    width:100%;
}

.intro .el-col {
    background: #fff;
    height:400px;
    line-height:40px;
    padding:  20px;
    text-align: left;
    box-shadow: 0 0 10px #e2e2e2;
}

.intro .el-col .main-title{
    margin-left:5px;
    width:fit-content;
    display: inline-block;
    padding:2px 12px 4px;
    border-bottom: 4px #4F94D4 solid;
}

.enter{
    box-sizing: border-box;
    padding:10px;
    margin: 0 -20px 40px 0;
    font-size:18px;
    width:100%;
}

.enter .el-col {
    
    height:300px;
    line-height:40px;
    /* padding:  20px; */
    text-align: left;
    /* box-shadow: 0 0 10px #e2e2e2; */

}

.enter .el-col .wrapper:hover{
    transform: translateY(15px);
    cursor: pointer;
    
}
.enter .el-col .wrapper{
    
    transition: transform 0.5s;
    position: relative;
}

.enter .el-col .wrapper .inner{
    position: relative;
    background:rgba(255,255,255,0.7);
    border-radius:10px;
    box-shadow: 0 0 10px #e2e2e2; 
    top:-200px;
    border:1px black solid;
    padding:3px 10px;
    z-index:10;
    width:100px;
    text-align: center;
    margin:20px auto;
}
.enter .el-col img{
    opacity: 0.8;
    
}


.module-intro{
    box-sizing: border-box;
    padding:10px;
    margin: 0 -20px 20px 0;
    font-size:18px;
    width:100%;
}

.module-intro .el-col {
    background: #fff;
    height:400px;
    line-height:40px;
    padding:  20px;
    text-align: left;
    box-shadow: 0 0 10px #e2e2e2;
}

.module-intro .el-col .main-title{
    margin-left:5px;
    width:fit-content;
    display: inline-block;
    padding:2px 12px 4px;
    border-bottom: 4px #4F94D4 solid;
}

</style>