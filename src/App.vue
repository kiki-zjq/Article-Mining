<template>
  <div id="app">
      <TopBar />
      <SideBar class="menu" />
      <div class='view'>
        <router-view/>
      </div>
<<<<<<< HEAD
      <!-- <FootPart /> -->
=======
>>>>>>> 1407ff8d6ffabdb6d9f16968993e83a9ff9152e5
       
  </div>
</template>

<script>
import SideBar from './layout/menu.vue'
import TopBar from './layout/header.vue'
<<<<<<< HEAD
import FootPart from './layout/footer.vue'
=======
>>>>>>> 1407ff8d6ffabdb6d9f16968993e83a9ff9152e5

export default {
  name: 'App',
  data(){
    return{

    }
  },


  components:{
    SideBar,
<<<<<<< HEAD
    TopBar,
    FootPart
=======
    TopBar
>>>>>>> 1407ff8d6ffabdb6d9f16968993e83a9ff9152e5
  },
};


</script>

<style>
body{
  padding: 0;
  margin: 0;
  background-color: #f0f3f4;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 0px;
  text-align: center;
  position: relative;
  /* background-color: #FBFCFE; */
  box-sizing: border-box;
  min-height:100px;
  width:100vw;
  background-color: #f0f3f4;
}

.view{
  box-sizing: border-box;
  background-color: #f0f3f4;
  /* background-color: yellow;
  min-height:100vh; */
  /* border:10px black solid; */
  width:85%;
  position: relative;
  top:60px;
  left:13%;
  min-height:800px;
  padding:1px;
}
</style>
