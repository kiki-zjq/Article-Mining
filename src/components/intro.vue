<template>
    <div class="intro-page">
        <div style="width:80%;margin:auto;">
            <span class="main-title">{{Title}}</span><br/>
            <span class="intro">{{Intro}}</span>
        </div>
    </div>
</template>

<script>
export default {
    props:{
        Title:{
            style:String,
            default:'Homepage',
        },
        Intro:{
            style:String,
            default:'It is a sub-title',
        }
    },
    computed:{
        Title:function(){
            return this.$store.state.Page
        },
        Intro:function(){
            return this.$store.state.Intro
        }
    }
}
</script>


<style scoped>
    .intro-page{
       
        position:relative;
        width:100%;
        height:460px;
        background-color: #404040;
        text-align: center;
        color:white;
    }
    .main-title{
        font-weight: 600;
        font-size:80px;
        display: block;
        padding: 150px 0 20px;
    }
    .intro{
        font-size:18px;
        font-weight:300;
    }
</style>