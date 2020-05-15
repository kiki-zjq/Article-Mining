<template>
    <div class='document-block'>
        
        <div class='title'>
            Documentation
        </div>
        <el-divider></el-divider>

        <div class='sub-title'>
            Introduction
        </div>
        <p style="margin-left:2em;">
            This file provide a sample way for multiple cores CPU. It could automatically load the file and calculate the sample and
store them in h5 format file.
        </p>
        <el-divider></el-divider>
        <!-------------------------------------------------------------------------------------->
        <div class='sub-title'>
            Module List
        </div>
        <p><span class="module-name">heapq</span> -- Elementary package provided by python3.x to implement the data structure of heap and relevant methods.</p>
        <p><span class="module-name">multiprocessing</span> -- Elementary package provided by python 3.x to support the multi-core feature.</p>
        <p><span class="module-name">math</span> -- Elementary math package supporting some calculation including pow, log, exp and so on.</p>
        <p><span class="module-name">random </span> -- Used to generate random number, including seed(used to set random seed), uniform and randint.</p>
        <p><span class="module-name">numpy </span> -- Used in sample_int_expj to store and process probability data.</p>
        <p><span class="module-name">time </span> -- Used to record time.</p>
        <p><span class="module-name">sys </span> -- Used exit function to exit while error happens.</p>
        <p><span class="module-name">pandas </span> -- Used to read tsv data and generate data list.</p>
        <p><span class="module-name">h5py  </span> -- Used to store the data in h5 format.</p>
        <p><span class="module-name">os </span> -- Elementary process of operating system.</p>

        <el-divider></el-divider>
        <!-------------------------------------------------------------------------------------->
        <div class='sub-title'>
            Function Details
        </div>

        <div class='code-block'>
            <span class="function-name">check_args(n, size, prob)</span>
            <span class="function-description">-- Check whether size is less than n and whether n is equal to the length of prob.</span>
            <br />
            <p>@param n: The number of all the zones in a tissue.</p>
            <p>@param size: The number of how many zones we want to sampled out.</p>
            <p>@param prob: The probabilities for every zone in a numpy(float32) format.</p>
        </div>

        <div class='code-block'>
            <span class="function-name">sample_int_expj(n, size, prob)</span>
            <span class="function-description">-- Sampling will be performed according to the weight of each member of the population.</span>
            <br />
            <p>@param n: The number of all the zones in a tissue.</p>
            <p>@param size: The number of how many zones we want to sampled out.</p>
            <p>@param prob: The probabilities for every zone in a numpy(float32) format.</p>
            <p>@return List including the weighted sample position.</p>
        </div>

        <div class='code-block'>
            <span class="function-name">reading_file(count_file_path, intersect_file_path)</span>
            <span class="function-description">-- Reading data from peak_file_path and intersect_file_path, and format them in specific format.</span>
            <br />
            <p>@param count_file_path: The path for counting file</p>
            <p>@param intersect_file_path: The path for intersect path</p>
            <p>@return Count File Data, Intersect File Data, Intersect Dictionary Data</p>
            
        </div>

        <div class='code-block'>
            <span class="function-name">run(bg_path, bg_intersect_path, peak_path, peak_intersect_path, cell_number, fragment_number=1000, frag_num_var=1,max_threshold=2000, min_threshold=500, signal2noise=0.5, core_number=1)</span>
            
            <br />
            <p>@param bg_path: background counting file path</p>
            <p>@param bg_intersect_path: background intersect file path</p>
            <p>@param peak_path: peak counting file path</p>
            <p>@param peak_intersect_path: peak intersect file path</p>
            <p>@param cell_number: How many cells you wnat to sample from a tissue</p>
            <p>@param fragment_number: The average value of fragment number for one cell. Default value is 1000</p>
            <p>@param frag_num_var: The variance for fragment number's value. Default value is 1</p>
            <p>@param max_threshold: The maximum threshold for fragment number. Default value is 2000</p>
            <p>@param min_threshold: The minimum threshold for fragment number. Default value is 500</p>
            <p>@param signal2noise: The signal to noise ratio. Default value is 0.5</p>
            <p>@param core_number: The CPU core number you want to use. Default value is 1</p>
        </div>

        <div class='code-block'>
            <span class="function-name">first_sample(data, intersect_data, dictionary, size, order, t="normal")</span>
            <span class="function-description">-- Read data, process data, pass them into sample_int_expjs and return results.</span>
            <br />
            <p>@param data: Counting Data. Generated by reading_file().</p>
            <p>@param intersect_data: Intersect Data. Generated by reading_file().</p>
            <p>@param dictionary: Intersect Data Dictionary. Generated by reading_file().</p>
            <p>@param size: The number of zones you want to sample from all the zones.</p>
            <p>@param order: The order of this cell</p>
            <p>@param t: The type of this sample, e.g. Peak Data, Background Data, etc. Default Value is normal.</p>
        </div>

        <div class='code-block'>
            <span class="function-name">second_sample(data, dictionary, sample_name, order, t="normal")</span>
            <span class="function-description">-- Read data, process data, conduct the second step sample, return the result.</span>
            <br />
            <p>@param data: Intersect Data. Passed by first_sample</p>
            <p>@param dictionary: Intersect Dictionary Data. Passed by fisrt_sample.</p>
            <p>@param sample_name: The sample name for all the sampled zones.</p>
            <p>@param order: The order of this cell</p>
            <p>@param t: The type of this sample, e.g. Peak Data, Background Data, etc. Default Value is normal.</p>
        </div>


    <div class='code-block'>
            <span class="function-name">multi_core_function(peak_data, peak_intersect_data, peak_dictionary, peak_round_1, peak_round_2, bg_data,
        bg_intersect_data, bg_dictionary, bg_round_1, bg_round_2, order)</span>
            <span class="function-description">-- Used to group all the four sample functions in one function in order to pass them to one CPU CORE.</span>
            <br />
            <p>@param peak_data: peak counting data reading from reading_file()</p>
            <p>@param peak_intersect_data: peak intersect data reading from reading_file()</p>
            <p>@param peak_dictionary: peak intersect dictionary data reading from reading_file().</p>
            <p>@param peak_round_1: The number of first round to sample the peak data</p>
            <p>@param peak_round_2: The number of second round to sample the peak data</p>
            <p>@param bg_data: background counting data reading from reading_file()</p>

            <p>@param bg_intersect_data: background intersect data reading from reading_file()</p>
            <p>@param bg_dictionary: background intersect dictionary data reading from reading_file()</p>
            <p>@param bg_round_1: The number of first round to sample the background data</p>
            <p>@param bg_round_2: The number of second round to sample the background data</p>
            <p>@param order: The order of this cell</p>
        </div>



        <el-divider></el-divider>
        <!-------------------------------------------------------------------------------------->
        <div class='sub-title'>
            Experimental Results
        </div>
        <div class="table" style="margin:10px auto;width:90%;">
            <el-table
                :data="tableData"
                stripe
                style="width: 100%">
                <el-table-column
                prop="core"
                label="Number of cores"
                width="230">
                </el-table-column>
                <el-table-column
                prop="total"
                label="Total number"
                width="230">
                </el-table-column>
                <el-table-column
                prop="sample"
                label="Sampling size"
                width="230">
                </el-table-column>
                <el-table-column
                prop="time"
                label="time">
                </el-table-column>
            </el-table>
        </div>

    </div>    
</template>

<script>
  export default {
    data() {
      return {
        tableData: [
            {
                core: '1',
                total: '10k',
                sample: '2k',
                time:'602min 12s',
            },
            {
                core: '4',
                total: '10k',
                sample: '2k',
                time:'151min 05s',
            },
            {
                core: '8',
                total: '10k',
                sample: '2k',
                time:'78min 48s',
            }
        ]
      }
    }
  }
</script>


<style scoped>
.document-block{
    box-sizing: border-box;
    text-align:left;
    padding:20px;
    font-size:14px;
}
.title{
    font-weight: bold;
    font-size:20px;
    padding-left:40px;
}
.code-block{
    width:90%;
    padding:10px 20px;
    margin:10px auto 1.5em;
    background-color: #F6F8FA;
    /* min-height:300px; */
    border-radius: 20px;
    font-size:14px;
}
.code-block .function-name{
    font-weight: bold;
    font-size: 14px;
}
.code-block .function-description{
    font-style: italic;
    font-size: 14px;
}

.document-block .sub-title{
        color:white;
        margin-top:2%;
        margin-bottom: 2%;
        padding-left:2em;
        padding-right:2em;
        font-weight: bold;
        font-size:16px;
        width:fit-content;
        background-color:rgb(0,100,164);
        height:2em;
        line-height:2em;
        border-radius:20px;
    }
.module-name{
    font-weight: bold;
    margin-left:2em;
}
</style>