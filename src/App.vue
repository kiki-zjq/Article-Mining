<template>
  <div id="app">
      <SideBar/>
      <TopBar/>
      <div class='view'>
        <router-view/>
      </div>
  </div>
</template>

<script>
import SideBar from './layout/sideBar.vue'
import TopBar from './layout/topBar.vue'

export default {
  name: 'app',
  components: {
    SideBar,
    TopBar,
  }
}
</script>

<style lang="scss">
body{
  background-color:#f0f3f4;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  /* margin-top: 60px; */
  margin-left:-20px;
  box-sizing:border-box;
  min-height:100px;
  width:100vw;
  position: relative;
  top:80px;
  background-color: #f0f3f4;
  //background-color: green;
  border:#f0f3f4;
}
.view{
  background-color: #f0f3f4;
  //background-color: yellow;
  // min-height:100vh;
  width:85%;
  position: relative;
  top:0px;
  left:220px;
}
</style>
