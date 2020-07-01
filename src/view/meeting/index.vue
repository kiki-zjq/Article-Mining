<template>
    <div class='dashbord'>
        <el-row class='search-bar'>
            <el-col :span='24'>
                <span style='background:#2da8ff'>&nbsp;</span>
                <span style='color:#2da8ff;margin-left:5px'>会议查询</span>
            </el-col>
        </el-row>

        <el-row class='conference-place'>
            <!-- <el-col :span='15'>
            <el-carousel :interval="2500" type="card" height="250px" autoplay=true>

                <el-carousel-item >
                    <div class='blockItem' v-on:click='title="AAAI"'>
                        <conference-block title="AAAI" theme='blue'></conference-block>
                    </div>
                </el-carousel-item>
                
                <el-carousel-item>
                    <div class='blockItem' v-on:click='title="ACM"'>
                        <conference-block title="ACM" theme='red' start='2016'></conference-block>
                    </div>
                </el-carousel-item>
                
                <el-carousel-item>
                    <div class='blockItem' v-on:click='title="MK"'>
                        <conference-block title="MK" theme='cyan' start='2017'></conference-block>
                    </div>
                </el-carousel-item>
                
                <el-carousel-item>
                    <div class='blockItem' v-on:click='title="MIT"'>
                        <conference-block title="MIT" theme='orange' start='2018'></conference-block>
                    </div>
                </el-carousel-item>
                
                <el-carousel-item>
                    <div class='blockItem' v-on:click='title="MK"'>
                        <conference-block title="MK" theme='cyan' start='2017'></conference-block>
                    </div>
                </el-carousel-item>
            </el-carousel>
            </el-col> -->
            
                <div class='blockItem' @click='handleClick(1)' @mouseenter='handleHover(1)'>
                    <conference-block title="AAAI" theme='blue'></conference-block>
                </div>
            
                <div class='blockItem'  @click='handleClick(2)' @mouseenter='handleHover(2)'>
                    <conference-block title="ACM" theme='red' start='2016'></conference-block>
                </div>
            
                <div class='blockItem'  @click='handleClick(3)' @mouseenter='handleHover(3)'>
                    <conference-block title="MK" theme='cyan' start='2017'></conference-block>
                </div>
           
                <div class='blockItem'  @click='handleClick(4)' @mouseenter='handleHover(4)'>
                    <conference-block title="MIT" theme='orange' start='2018'></conference-block>
                </div>

                <div class='blockItem'  @click='handleClick(5)' @mouseenter='handleHover(5)'>
                    <conference-block title="ACL" theme='red' start='2016'></conference-block>
                </div>
        </el-row>

        <el-row class='disp-place'>
            <el-col class='disp-left' :span='12'>
                    <div class='title'>{{title}}</div>
                    <div class='intro-place'>{{introduction}}</div>
            </el-col>
            <el-col class='disp-right' :span='12'>
                <!-- <scatter-chart></scatter-chart> -->
                <RadarChart/>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import ConferenceBlock from './components/conferenceBlock.vue'
// import ScatterChart from './components/ScatterChart.vue'
import RadarChart from './components/radarChart.vue'
export default {
    data(){
        return{
            title:'',
        }
    },
    components:{
        ConferenceBlock,
        // ScatterChart,
        RadarChart,
    },
    methods:{
        handleHover(val){
            switch (val) {
                case 1:
                    this.title = 'AAAI';
                    break;
            
                case 2:
                    this.title = 'ACM';
                    break;
                case 3:
                    this.title = 'MK';
                    break;

                case 4:
                    this.title = 'MIT';
                    break;

                case 5:
                    this.title = 'ACL';
                    break;
            }
        },
        handleClick(val){
            switch (val) {
                case 1:
                    this.title = 'MK';
                    break;
            
                case 2:
                    this.title = 'ACM';
                    break;
                case 3:
                    this.title = 'MK';
                    break;

                case 4:
                    this.title = 'MIT';
                    break;

                case 5:
                    this.title = 'ACL';
                    break;
            }
        }
    },
    computed:{
        introduction(){
            let template = '';
            if(this.title=='AAAI'){
                template ="AAAI（American Association for Artificial Intelligence）成立于1979年,是一个非盈利性科学学会，致力于促进对思想和智能行为及其在机器中的体现机制的科学理解;旨在促进人工智能研究和负责任地使用。 和提高公众对人工智能的理解。";
            }
            if(this.title=='ACM'){
                template='ACM(Associine for Computer Mair coolinghinery):计算机协会。它是一个国际性的科技教育组织，创立于1947年，是世界上第一个科学性及教育性计算机学会，总部设在美国纽约。ACM致力于提高信息技术在科学、艺术等各行各业的应用水平。从成立之初ACM就开始为会员的信息、思想和发现提供交流平台';
            }
            if(this.title=='MK'){
                template='自1984年以来，摩根·考夫曼（Morgan Kaufmann）便将专家的知识带入了计算机界。我们的目标是为研究与开发专业人员，商业领袖和信息技术经理，日常从业人员以及学术界提供优质的印刷和数字内容。Morgan Kaufmann经常重新定义计算机科学教育和技术参考的轨迹，以帮助专业人士保持领先地位并激发未来的创新。';
            }
            if(this.title=='MIT'){
                template='麻省理工学院出版社成立于1962年，是世界上最大，最杰出的大学出版社之一，也是科学，技术，艺术，社会科学和设计交叉领域的领先书籍和期刊出版商。 麻省理工学院出版社的书籍和期刊以其大胆的知识，学术水平，跨学科重点和独特的设计而著称。';
            }
            if(this.title=='ACL'){
                template = '麻省理工学院出版社成立于1962年，是世界上最大，最杰出的大学出版社之一，也是科学，技术，艺术，社会科学和设计交叉领域的领先书籍和期刊出版商。 麻省理工学院出版社的书籍和期刊以其大胆的知识，学术水平，跨学科重点和独特的设计而著称。'
            }
            return template;
        }
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
    .search-bar{
        /* padding:10px;
        background: #fff;
        margin: 0 -20px 0 -20px;
        font-size:18px; */
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

    .conference-place {
        width:100%;
        box-sizing: border-box;
        padding:10px;
        margin: 20px 0;
        /* background-color: white; */
        /* min-height:400px; */
       
        font-size:18px;
        text-align:left;
        overflow-x: auto;
        overflow-y: hidden;
         white-space: nowrap;
        }

        .conference-place .el-col {
                padding: 0 20px;
            }

        .conference-place .el-col .blockItem {
                border-radius: 20px;
                height: 200px;
                position: relative;
                }
        .conference-place div{
            transition: transform 0.5s;
        }
        .conference-place div:hover{
                    transform: translateY(30px);
                    cursor: pointer;
                    
                }
    ::-webkit-scrollbar{
        display: none;
    }
    .conference-place div{
        display: inline-block;
        margin-right:30px;
    }

    .disp-place{
        margin: 20px 0;
    }
    .disp-place .el-col{
            padding: 0 20px;
            background: #fff;
            height: 600px;
        }
    .disp-place .disp-left{
            box-shadow: inset -30px 0px #f0f3f4;
        }
    .disp-place .disp-right{
            padding:20px;
        }
    .disp-place .title{
            margin-left:-20px;
            padding-top:20px;
            text-align: center;
            font-size:20px;
            font-weight:bold;
        }
    .intro-place{
        font-size:14px;
        padding:20px 30px 0 0;
    }
</style>