<template>
    <div class="display">
        <h1 class="title">论文信息呈现页</h1>
        <p style="font-weight:bold">论文名称：<span style="font-weight:normal">{{data.paperTitle}}</span></p>
        <span style="margin-right:20px;font-weight:bold">会议名称：<span style="font-weight:normal">{{data.metTitle}}</span></span>
        <p class='abstract'>年份：<span style="font-weight:normal">{{data.year}}</span></p>
        <p class='abstract'>涉及算法：<span style="font-weight:normal">{{data.algorithm}}</span></p>
        <p class='abstract' >摘要：<span class="abstract-info">{{data.paperAbstract}}</span></p>
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
        text-align: left;
        margin: 20px 20px 0 20px;
        padding-right:20px;
        float:left;
        width:95%;
        word-wrap: break-word;
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
            float: left;
            width: 100%;
            font-weight:normal;
        }
</style>