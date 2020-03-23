<template>
    <div>
        <el-table
            :data="tableData"
            stripe
            style="width: 100%">

            <el-table-column
            prop="index"
            label=" "
            width="60">
            </el-table-column>
            
            <el-table-column
            prop="title"
            label="论文题目"
            width="200">
            </el-table-column>
            
            <el-table-column
            prop="src"
            label="会议来源"
            width="150">
            </el-table-column>
            
            <el-table-column
            prop="time"
            label="发表时间"
            width="150">
            </el-table-column>
            
        
        </el-table>
    </div>
</template>

<script>
  export default {
    props:{
        tableData:Array,
    },
    data() {
      return {
        // tableData:[]
      }
    },
    methods:{
        
    }
  }
</script>