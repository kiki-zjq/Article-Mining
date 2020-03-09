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

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  /* margin-top: 60px; */
  margin-left:-20px;
  height:100vh;
  width:100vw;
  background-color: gray;
  border:gray;
}
.view{
  height:100vh;
  width:100vw;
  position: fixed;
  top:50px;
  left:200px;
}
</style>
