<template>
    <div class='select-place'>
        <span style='font-size:14px'>算法领域：</span>
            <el-select v-model='domain' clearable placeholder="请选择">
                <el-option
                    v-for="domain in domains"
                    :key="domain.value"
                    :label="domain.label"
                    :value="domain.value">
                </el-option>
            </el-select>

        <span style='margin-left:5px;font-size:14px'>  选择年份：</span>
            <el-select v-model='year' clearable placeholder="请选择">
                <el-option
                    v-for="year in years"
                    :key="year.value"
                    :label="year.label"
                    :value="year.value">
                </el-option>
            </el-select>
    </div>
</template>

<script>
export default {
    data() {
        return {
            domain:'',
            domains: [{
                value: '算法1',
                label: '算法1'
                }, {
                value: '算法2',
                label: '算法2'
                }, {
                value: '算法3',
                label: '算法3'
                }],
            year:'',
            years: [{
                value: '2019',
                label: '2019'
                }, {
                value: '2018',
                label: '2018'
                }, {
                value: '2017',
                label: '2017'
                }],
            }
    },
}
</script>


<style scoped>
    .select-place{
        padding-top:10px;
        }
    .select-place .el-input__inner{
                height:30px;
                line-height:30px;
            }
    .select-place .el-input__icon{
                line-height:30px;
            }
</style>