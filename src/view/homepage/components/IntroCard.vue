<template>
    <div class='card'>

    </div>
</template>

<script>
export default {
    props:{
      title: {
        type: String,
        default: ''
      },
    }
}
</script>

<style scoped>
.card{
    width:100%;
    height:100%;
    background-color: red;
}
</style>