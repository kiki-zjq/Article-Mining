<template>
    <div class='dashbord'>
        <el-row class='search-bar'>
            <el-col :span='24'>
                <span style='background:#2da8ff'>&nbsp;</span>
                <span style='color:#2da8ff;margin-left:5px'>会议查询</span>
            </el-col>
        </el-row>

        <el-row class='conference-place'>
            <el-col :span='6'>
                <div class='blockItem' v-on:click='title="HICSS"'>
                    <conference-block title="HICSS" theme='blue'></conference-block>
                </div>
            </el-col>

            <el-col :span='6'>
                <div class='blockItem' v-on:click='title="RECYSC"'>
                    <conference-block title="RECYSC" theme='red' start='2016'></conference-block>
                </div>
            </el-col>

            <el-col :span='6'>
                <div class='blockItem' v-on:click='title="ECIR"'>
                    <conference-block title="ECIR" theme='cyan' start='2017'></conference-block>
                </div>
            </el-col>

            <el-col :span='6'>
                <div class='blockItem' v-on:click='title="IEEE"'>
                    <conference-block title="IEEE" theme='orange' start='2018'></conference-block>
                </div>
            </el-col>
        </el-row>

        <el-row class='disp-place'>
            <el-col class='disp-left' :span='12'>
                    <div class='title'>{{title}}</div>
                    <div class='intro-place'>{{introduction}}</div>
            </el-col>
            <el-col class='disp-right' :span='12'>
                <scatter-chart></scatter-chart>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import ConferenceBlock from './components/conferenceBlock.vue'
import ScatterChart from './components/ScatterChart.vue'
export default {
    data(){
        return{
            title:'',
        }
    },
    components:{
        ConferenceBlock,
        ScatterChart,
    },
    computed:{
        introduction(){
            let template = '';
            if(this.title=='HICSS'){
                template ="我们过了江，进了车站。我买票，他忙着照看行李。行李太多，得向脚夫11行些小费才可过去。他便又忙着和他们讲价钱。我那时真是聪明过分，总觉他说话不大漂亮，非自己插嘴不可，但他终于讲定了价钱；就送我上车。他给我拣定了靠车门的一张椅子；我将他给我做的紫毛大衣铺好座位。他嘱我路上小心，夜里要警醒些，不要受凉。又嘱托茶房好好照应我。我心里暗笑他的迂；他们只认得钱，托他们只是白托！而且我这样大年纪的人，难道还不能料理自己么？我现在想想，我那时真是太聪明了。";
            }
            if(this.title=='RECYSC'){
                template='到南京时，有朋友约去游逛，勾留7了一日；第二日上午便须渡江到浦口，下午上车北去。父亲因为事忙，本已说定不送我，叫旅馆里一个熟识的茶房8陪我同去。他再三嘱咐茶房，甚是仔细。但他终于不放心，怕茶房不妥帖9；颇踌躇10了一会。其实我那年已二十岁，北京已来往过两三次，是没有什么要紧的了。他踌躇了一会，终于决定还是自己送我去。我再三劝他不必去；他只说：“不要紧，他们去不好！”';
            }
            if(this.title=='ECIR'){
                template='我说道：“爸爸，你走吧。”他望车外看了看，说：“我买几个橘子去。你就在此地，不要走动。”我看那边月台的栅栏外有几个卖东西的等着顾客。走到那边月台，须穿过铁道，须跳下去又爬上去。父亲是一个胖子，走过去自然要费事些。我本来要去的，他不肯，只好让他去。我看见他戴着黑布小帽，穿着黑布大马褂12，深青布棉袍，蹒跚13地走到铁道边，慢慢探身下去，尚不大难。可是他穿过铁道，要爬上那边月台，就不容易了。他用两手攀着上面，两脚再向上缩；他肥胖的身子向左微倾，显出努力的样子。这时我看见他的背影，我的泪很快地流下来了。我赶紧拭干了泪。怕他看见，也怕别人看见。我再向外看时，他已抱了朱红的橘子往回走了。过铁道时，他先将橘子散放在地上，自己慢慢爬下，再抱起橘子走。到这边时，我赶紧去搀他。他和我走到车上，将橘子一股脑儿放在我的皮大衣上。于是扑扑衣上的泥土，心里很轻松似的。过一会儿说：“我走了，到那边来信！”我望着他走出去。他走了几步，回过头看见我，说：“进去吧，里边没人。”等他的背影混入来来往往的人里，再找不着了，我便进来坐下，我的眼泪又来了。';
            }
            if(this.title=='IEEE'){
                template='电气和电子工程师协会（IEEE，全称是Institute of Electrical and Electronics Engineers）是一个美国的电子技术与信息科学工程师的协会，是世界上最大的非营利性专业技术学会，其会员人数超过40万人，遍布160多个国家。IEEE致力于电气、电子、计算机工程和与科学有关的领域的开发和研究，在航空航天、信息技术、电力及消费性电子产品等领域 [1]  已制定了900多个行业标准，现已发展成为具有较大影响力的国际学术组织。国内已有北京、上海、西安、武汉、郑州、济南等地的55所高校成立IEEE学生分会。 [2-3] 2019年5月30日，IEEE发表声明，将针对美国出口管制条例的增加名单作出回应。 [4]  6月3日，恢复华为审核资格。 [5] 2019年9月6日，电气与电子工程师协会（IEEE）年度媒体交流会在北京举行。IEEE高级会员、中科院自动化研究所副研究员、中国人工智能学会理事董晶博士分享了智能图像识别技术的发展趋势，以及如何通过AI技术遏制图像内容篡改问题。';
            }
            return template;
        }
    }

}
</script>

<style lang="scss">
    .dashbord {
        background-color: #f0f3f4;
    }
    .search-bar{
        padding:10px;
        background: #fff;
        margin: 0 -20px 0 -20px;
        font-size:18px;
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

    .conference-place {
        margin: 20px -40px 0 -40px;
        .el-col {
                padding: 0 20px;
                .blockItem {
                border-radius: 20px;
                height: 200px;
                background: #fff;
                }
            }
        }
    
    .disp-place{
        margin: 20px -20px 0 -20px;
        .el-col{
            padding: 0 20px;
            background: #fff;
            height: 600px;
        }
        .disp-left{
            box-shadow: inset -30px 0px #f0f3f4;
        }
        .disp-right{
            padding:20px;
        }
        .title{
            margin-left:-20px;
            padding-top:20px;
            text-align: center;
            font-size:20px;
            font-weight:bold;
        }
    }
    .intro-place{
        font-size:14px;
        padding:20px 30px 0 0;
    }
</style>