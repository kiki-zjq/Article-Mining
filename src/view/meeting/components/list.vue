<template>
    <div>
        <el-table
            :data="tableData"
            stripe
            style="width: 100%">

            <el-table-column
            prop="pid"
            label=" "
            width="60">
            </el-table-column>
            
            <el-table-column
            prop="paperTitle"
            label="论文题目"
            width="500">
            </el-table-column>
            
            <el-table-column
            prop="metTitle"
            label="会议来源"
            width="500">
            </el-table-column>
            
            <el-table-column
            prop="year"
            label="发表时间"
            width="180"
            align="center">
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
            :hide-on-single-page="hide"
            layout="prev, pager, next"
            :page-size="10"
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
        //  hide:true
        // tableData:[]
      }
    },
    computed:{
        hide:function(){
            if(this.total>10){
                return true
            }else{
                return false
            }
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