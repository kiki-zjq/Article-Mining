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
<<<<<<< HEAD
            width="500">
=======
            width="600">
>>>>>>> 1407ff8d6ffabdb6d9f16968993e83a9ff9152e5
            </el-table-column>
            
            <el-table-column
            prop="src"
            label="会议来源"
            width="300">
            </el-table-column>
            
            <el-table-column
            prop="time"
            label="发表时间"
            width="300">
            </el-table-column>
            
            <el-table-column
            label=" ">
                <template slot-scope="scope">
                    <el-button 
                        @click="handleClick(scope.row)" 
                        type="primary" 
                        style="background-color:#2DA8FF;border:#2DA8FF" 
                        icon="el-icon-search" 
                        size="small">
                        查询
                    </el-button>
                </template>
            </el-table-column>
        
        </el-table>
        <el-pagination
            layout="prev, pager, next"
            @current-change="handleCurrentChange"
            :total="total">
        </el-pagination>
    </div>
</template>

<script>
  export default {
    props:{
        tableData:Array,
        total:{
            type:Number,
            default:100,
        }
    },
    data() {
      return {
        // tableData:[]
      }
    },
    methods:{
        handleCurrentChange(val){
            this.$emit('pageChange',val)
        },
        handleClick(params){
            this.$emit('check',params)
        }
    }
  }
</script>