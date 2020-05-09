<template>
    <div class="simulator-block">
        <div class='title'>
            Simulator
        </div>
        <el-divider></el-divider>


        <div class='sub-title'>
            Illustration
        </div>
        
        <div class="simulator-pic">
            <img src='./simulator.png' />
        </div>
   
        <el-divider></el-divider>
   
   
        <div class='sub-title'>
            Pre-processing        
        </div>

        <div class='pre-processing'>
            <p>The input for preprocessing is the <b>bam files</b> and the <b>narrow peaks</b> 
                called using the ENCODE ATAC-seq pipeline (MACS2) for each cell type in the cell group.</p>
            <p>SCAN-ATAC_Preprocessing.ipynb is the Jupyter Notebook for preprocessing the bam files. 
                It will output fragments with read coverage and reads overlapping with the fragments. </p>
            <br />
            <p>The python script could be executed as follows:</p>
            <i style="padding-left:2em;color:#b4b4b4">Make sure to have pysam==0.15.4, pandas==1.0.3, and matplotlib==3.1.1 installed</i>
            <div class='code-block'>
                <p>python SCAN-ATAC_Preprocessing.py \</p>
                <p>-c &lt;comma separated file prefixes for each cell type> \</p>
                <p>-i &lt;directory containig the peak files with prefix and .narrowPeak suffix> \</p>
                <p>-j &lt;directory containing the bam files with prefix and .bam suffix> \</p>
                <p>-e &lt;custom configuration for bp length separating between foreground and background fragments> \</p>
                <p>-b &lt;bp length for background fragment size> \</p>
                <p>-o &lt;output directory></p>
            </div>
            <p>The output files are:</p>
            <p><b>*.peak_counts.bed</b> - fragment with read coverage</p>
            <p><b>*.peak_intersect.bed</b> - reads in the previous fragments</p>
            
        </div>
        <el-divider></el-divider>

        <div class='sub-title'>
            Simulator        
        </div>

        <div class='simulator'>
            <p>Follow the example in run.sh to simulate one cell type.</p>
            <p><b>1. To compile with Intel C++ compiler:</b></p>
            <p style='margin-left:3em;'>make weighted_sampling</p>
            <p style='margin-left:3em;'>make uniform_sampling</p>
            <br/>

            <p><b>2. Sample fragments without replacement:</b></p>
            <p>./weighted_sampling -f NKcell.peak_counts.bed -b bg_counts.bed -of</p>
            <p>NKcell.foreground.sampled.bed -ob NKcell.background.sampled.bed -n 2000 -nv 0.5 -c 10000 </p>
            <p><b>-s</b> 0.6 -min 1000 -max 20000</p>
            <p><b>-f</b> specifies foreground fragments</p>
            <p><b>-b</b> specifies background fragments</p>
            <p><b>-of</b> foreground output name</p>
            <p><b>-ob</b> background output name</p>
            <p><b>-n</b> number of fragments sampled (or the mean of the log-normal distribution of peak number) </p>
            <p><b>-nv</b> variance of fragments sampled for the log-normal distribution of peak number</p>
            <p><b>-c</b> specifies the number of cells sampled for single-cell</p>
            <p><b>-s</b> signal to noise ratio</p>
            <p><b>-min</b> minimum fragments in a cell (only for the log-normal distribution mode)</p>
            <p><b>-max</b> maximum fragments in a cell (only for the log-normal distribution mode)</p>
            <br/>

            <p><b>3. Sample reads:</b></p>
            <p>./uniform_sampling NKcell.peak_intersect.bed NKcell.foreground.sampled.bed NKcells.background.bed</p>
            <p>./uniform_sampling bg_intersect.expanded.bed NKcell.background.sampled.bed NKcells.foreground.bed</p>
            <p>cat NKcells.background.bed NKcells.foreground.bed > NKcells.bed</p>


            <p>The script uniform_sampling takes the fragments sampled and finds the reads. It collects 
                the mapping in a dictionary, then outputs a reads for each dictionary entry. The samples 
                repeat for foreground and background, and the results should then be combined for all cells of that cell type. </p>
        </div>

        <el-divider></el-divider>

    </div>
</template>

<style scoped>
.simulator-block{
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

.simulator-block .simulator-pic{
    text-align: center
}
.simulator-block .sub-title{
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

.code-block{
    width:90%;
    padding:10px 20px;
    margin:10px auto 1.5em;
    background-color: #F6F8FA;
    /* min-height:300px; */
    border-radius: 20px;
    font-size:14px;

    /* background-color: black;
    color:#EBDBB2; */
}

.pre-processing p{
    margin-left:2em;
}

.simulator p{
    margin-left:2em;
}
</style>