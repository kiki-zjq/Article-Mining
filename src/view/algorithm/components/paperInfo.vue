<template>
    <div class="display">
        <h1 class="title">论文信息呈现页</h1>
        <h2>论文名称：{{data.title}}</h2>
        <span style="margin-right:20px;font-weight:bold">会议名称：{{data.src}}</span>
        <span class='abstract'>年份：{{data.time}}</span>
        <p class='abstract'>涉及算法：{{data.src}}</p>
        <span class='abstract' >摘要：<span class="abstract-info">12312312啊实打实打算就肯定会喀什的距离喀什觉得奥斯卡大奖拉克斯基的啦扣税的拉伸</span></span>
    </div>
</template>

<script>
export default {
    props:{
        data:Object
    }
}
</script>

<style  scoped>

    .display {
        margin: 20px 20px 0 20px;
    }
     .display .title {
            width: fit-content;
            display: inline-block;
            padding: 2px 12px 4px;
            border-bottom: 4px #2DA8FF solid;
        }

    .display .abstract {
            font-weight: bold;
        }
     .display .abstract-info{
            text-indent: 2em;
            float:left;
        }
</style>