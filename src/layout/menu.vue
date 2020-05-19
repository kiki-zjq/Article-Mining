<template>
      
<div>
    <!-- <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
        <el-radio-button :label="false">展开</el-radio-button>
        <el-radio-button :label="true">收起</el-radio-button>
    </el-radio-group> -->
    <div class='icon-title'></div>
    <el-menu 
        :default-active="active"
        class="el-menu-vertical-demo" 
        :collapse="isCollapse"
        text-color="#B5B6BD"
        background-color='#3A3F51'
        active-text-color="#4F94D4">
    <!-- <el-submenu index="1">
        <template slot="title">
        <i class="el-icon-location"></i>
        <span slot="title">导航一</span>
        </template>
        <el-menu-item-group>
        <span slot="title">分组一</span>
        <el-menu-item index="1-1">选项1</el-menu-item>
        <el-menu-item index="1-2">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
        <el-menu-item index="1-3">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="1-4">
        <span slot="title">选项4</span>
        <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
    </el-submenu> -->

    <el-menu-item index="1" @click='handleClick(1)'>
        <i class="el-icon-menu"></i>
        <span slot="title">导航一</span>
    </el-menu-item>

    <el-menu-item index="2" @click='handleClick(2)'>
        <i class="el-icon-menu"></i>
        <span slot="title">算法</span>
    </el-menu-item>


    <!-- <el-menu-item index="3" @click='handleClick(3)'>
        <i class="el-icon-document"></i>
        <span slot="title">会议一</span>
    </el-menu-item> -->


    <el-menu-item index="4" @click='handleClick(4)'>
        <i class="el-icon-setting"></i>
        <span slot="title">会议</span>
    </el-menu-item>

    <el-menu-item index="5" @click='handleClick(5)'>
        <i class="el-icon-setting"></i>
        <span slot="title">查询</span>
    </el-menu-item>
    
    
    </el-menu>
</div>
</template>

<script>
let active='1';
export default {
    data(){
        return{
            active,
        }
    },
    methods: {
       handleClick(index){
        switch(index){
          case 1:this.$router.push('/');break;
          case 2:this.$router.push('/algorithm');break;
          case 3:this.$router.push('/meet');break;
          case 4:this.$router.push('/meeting');break;
          case 5:this.$router.push('/query');break;
        }

      }
    },
    watch:{
    $route(to,from){
        // alert(to.path)
        switch(to.path){
        case '/':
            this.active='1';return;
        case '/algorithm':
            this.active='2';return;
        case '/meet':
            this.active='3';return;
        case '/meeting':
            this.active='4';break;
        case '/query':
            this.active ='5';break;
        
            }
            
        }
  },
  mounted(){
      
      switch(this.$route.path){
        case '/':
            this.active='1';return;
        case '/algorithm':
            this.active='2';return;
        case '/meet':
            this.active='3';return;
        case '/meeting':
            this.active='4';break;
        case '/query':
            this.active ='5';break;
        
            }
        
        }
}
</script>

<style scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 12%;
    min-height: 100vh;
    background: #3A3F51;
    position: fixed;
    top:50px;
    border:#3A3F51;
    z-index: 9;
    text-align: left;
    border-right: black 1px solid;
    box-sizing: border-box;
  }

</style>