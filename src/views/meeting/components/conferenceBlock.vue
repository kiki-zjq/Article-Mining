<template>
    <section :class="theme" :style="{ height:height,width:width }">
      <div class="title">
        {{title}}
        <div class='search' style='float:right'>
          <el-button icon="el-icon-search" circle @click='search'></el-button>
        </div>
      </div>
      <div class='number'>
        <p>论文数</p>
        <div class='article-number'>{{number}}</div>
      </div>
      <div class='time'>
        <p>时间</p>
        <br/>
          <div>
            <span style='font-size:14px;font-weight:bold'>{{start}}年</span>
            至 
            <span style='font-size:14px;font-weight:bold'>{{end}}年</span>
          </div>
      </div>
    </section>
</template>

<script>
export default {
    data(){
      return{
        number:0,
      }
    },
    props:{
      title: {
        type: String,
        default: ''
      },
      theme:{
        type: String,
        default:''
      },
      width: {
        type: String,
        default: "100%"
      },
      height: {
        type: String,
        default: "400px"
      },
      start: {
        type: String,
        default: "2015"
      },
      end: {
        type: String,
        default: "2019"
      },
    },
    mounted(){
      this.init();
    },
    methods:{
      init(){
        this.number=500;//日后改成请求获取
      },
      search(){
        alert(this.title);
      }
    },
}
</script>

<style  lang="scss" scoped>
section {
  color:white;
  padding:20px;
  box-sizing:border-box;
  position: relative;
  margin-bottom: 15px;
  border-radius: 20px;
  background: #fff;
  overflow: hidden;
  &::before {
    content: "";
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    width: 6px;
    height: 100%;
  }
}
.blue{
    background:blue;
    background-image: linear-gradient(#3498db, #2c3e50);
}
.red{
    background:red;
    background-image: linear-gradient(#F15F79, #B24592);
}
.cyan{
    background:cyan;
    background-image: linear-gradient(#92FE9D, #00C9FF);
}
.orange{
    background:orange;
    background-image: linear-gradient(#f0cb35, #C02425);
}
.title{
  height:50%;
  font-size:24px;
  font-weight: bold;
  color:white;
}
.article-number{
  margin-top:10px;
  font-size:30px;
  font-weight: bold;
  color:white;
}
.number{
  width:40%;
  float:left;
  border-right:white 2px solid;
}
.time{
  margin-left:20px;
  float:left;
 }
.content {
  margin-left: 6px;
  padding: 15px 20px;
}
</style>