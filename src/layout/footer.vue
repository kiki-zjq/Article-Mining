<template>
    <div class='footer'>
        
            <div class="contact-section-header">
                <h2>Contact me...</h2>
                
            </div>
                <div class="contact-links">
                    <a
                    href="#"
                    target="_blank"
                    class="btn contact-details"
                    ><i class="fa fa-facebook-square fa-2x"></i> <span class='contact-way'>Facebook</span></a>


                    <a
                    id="profile-link"
                    href="#"
                    target="_blank"
                    class="btn contact-details"
                    ><i class="fa fa-github fa-2x"></i> <span class='contact-way'>GitHub</span></a>

                    <a
                        href="#"
                        target="_blank"
                        class="btn contact-details"
                    ><i class="fa fa-twitter fa-2x"></i> <span class='contact-way'>Twitter</span></a>

                    <a 
                        href="#" 
                        class="btn contact-details"
                    ><i class="fa fa-at fa-2x"></i> <span class='contact-way'>Send a mail</span></a>

                    <a 
                        href="#" 
                        class="btn contact-details"
                    ><i class="fa fa-phone-square fa-2x"></i> <span class='contact-way'>Call me</span></a>

                </div>
            <el-divider></el-divider>
            <div class="copyright">
                <i class="fa fa-copyright fa-1x" aria-hidden="true"></i><span class='team-name'>SCAN-ATAC GPU Simulator</span>
            </div>
    </div>
</template>
<script>
import "font-awesome/css/font-awesome.css"
export default {
    

}
</script>
<style scoped>
@import "font-awesome/css/font-awesome.css";
.fa {
    z-index:100;
    color:white!important;
    margin-left:40px;
}
.footer{
        box-sizing: border-box;
        padding:20px;
        color:white;
        background-color: rgb(0,100,164);
        width:100%;
        height:40vh;
        position: relative;        
    }
.footer a {
    display: inline-block;
    color:white;
    text-decoration: none;
    transition: transform 0.5s;
    /* text-decoration: none; */
    /* font-size:px; */
}
a:hover{
    transform: translateY(12px);
    
}
.contact-way{
    font-size:24px;
    line-height:40px;
}
.contact-links{
    margin-bottom: 5em;
}
.contact-section-header > h2 {
  font-size: 2rem;
  color:white;
}
.copyright{
    text-align: right;
}
.team-name{
    margin-left:4px;
    margin-right:3em;
    font-size:16px;
    line-height:40px;
}

</style>