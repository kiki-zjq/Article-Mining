<template>
    <div class='download-block'>
        <div class='title'>
            Installation
        </div>
        <el-divider></el-divider>

        <div class='sub-title'>
            Installation Guide
       </div>

        


        <div class="guide-block">
           <p style="font-weight:bold;">Install:</p>
            <ol>
                <li>pip install numpy</li>
                <li>pip install h5py</li>
                <li>pip install pandas</li>
                <li>pip install SASample</li>
            </ol>
        </div>

        <el-divider></el-divider>

        
        <div class='sub-title'>
            Source code download
        </div>
        <i style="padding-left:2em;color:#b4b4b4">(Click to download)</i>
        <p class="downloader"><a href="./static/code/SASample.py" download="SASample.py">SASample</a></p>
        <p class="downloader"><a href="./static/code/SASample_functions.py" download="SASample_functions.py">SASample_function</a></p>
        <el-divider></el-divider>
        
        <div class='sub-title'>
            Using Directions
       </div>

       <p class="function-name">SASample</p>
       <div class="guide-block">
           <p style="font-weight:bold;">Using Directions:</p>
            <ol>
                <li>Initialize a SASample Class<br/><b>E.g. sample = SASample(bg_path, bg_intersect_path, peak_path, peak_intersect_path)</b></li>
                <li>Set proper parameter for this Class, like signal2noise, fragment_number, saving_path, etc. Or just use the default value.<br/><b>E.g. sample.set_cores(5)</b></li>
                <li>Use run method to start sample process <br/><b>E.g. sample.run()</b></li>
            </ol>
       </div>

        <br />
        <p class="function-name">SASample_function</p>
        

        <div class="guide-block">
           <p style="font-weight:bold;">Using Directions:</p>
            <div style="margin-left:2em">
                Simply use the run() method to start sample process.<br/>
                Please notice that the data paths are required.<br/>
                Some other parameters is optional. If you want to change them, please change them in run() method.<br/>
                Or they will run by deafult value.
            </div>

        </div>


    </div>    
</template>

<style scoped>
.download-block{
    box-sizing: border-box;
    text-align:left;
    padding:20px;
    font-size:14px;
}
.download-block .sub-title{
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
.downloader a{
    text-decoration: none;
    margin-left: 1em;

}
.title{
    font-weight: bold;
    font-size:20px;
    padding-left:40px;
}
.function-name{
    width:fit-content;
    display: inline-block;
    font-weight:bold;
    font-size:16px;
    padding-bottom: 4px;
    margin-left:1em;
    border-bottom: 2px rgb(0,100,164) solid;
}

.guide-block{

    width:90%;
    padding:10px 20px;
    margin:0px auto 1.5em;
    background-color: #F6F8FA;
    /* min-height:300px; */
    border-radius: 20px;
    font-size:14px;

}
</style>