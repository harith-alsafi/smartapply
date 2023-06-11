from src.logic.User import User
from src.logic.JobInfo import JobInfo
from src.education.Education import Education
from typing import List
from src.skills.Skill import Skill

DOCTYPE:str = """
<!DOCTYPE html>
"""

SCRIPT:str = """
<script>
    $(document).ready(function()
{
	
	$("html").niceScroll({
		
		cursorcolor:"#212b37",
		cursorborder:"5px solid #212b37",
		cursorborderradius:"0",
		scrollspeed:65
	})

	$("ul, div").filter("#scrolls").niceScroll({
		
		cursorcolor:"#ff4359",
		cursorborder:"2px solid #ff4359",
		cursorborderradius:"0",
		scrollspeed:65
	})
	
});
</script>

"""

HEAD:str = """
<head>
    <meta charset="UTF-8" />
    <meta name="" content="" />
    <title>cv</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700&display=swap" />
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" />
    <link rel="stylesheet" href="css/normalize.css" />
    <link rel="stylesheet" href="css/project03.css" />
    <!--[if it IE 9]>
    <script src="js/tools/html5shiv.min.js"></script>
    <[endif]-->
</head>
"""

def get_style(image_url:str):
    return f"""
    <style>
@charset "UTF-8";

body {
  padding: 0;
  margin: 0;
  background-color: #f2f2f2;
}

* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

.margin {
  width: 699px;
  margin: 0 auto;
}

.cv-base {
  width: 800px;
  height: 1052px;
  margin: 45px auto;
  background-color: transparent;
  position: relative;
}

.cv-base .back {
  z-index: 1;
  width: 100%;
  height: 100%;
  transform: rotate(4deg);
  background-color: #ff4359;
  position: absolute;
  overflow: hidden;
  top: 0;
}


.cv-base .front {
  z-index: 2;
  width: 100%;
  height: 100%;
  background-color: white;
  position: relative;
  overflow: hidden;
}

.cv-base .front header {
  width: 100%;
  height: 200px;
  padding-bottom: 5px;
  margin-bottom: 5px;
  background-color: transparent;
  position: relative;
  overflow: hidden;
}

.cv-base .front header .head-top {
  width: 100%;
  height: 68px;
  z-index: 1;
  -webkit-transform: rotate(1deg);
  -moz-transform: rotate(1deg);
  -ms-transform: rotate(1deg);
  -o-transform: rotate(1deg);
  transform: rotate(1deg);
  background-color: #ff4359;
  position: absolute;
  overflow: hidden;
  top: -16px;
}


.cv-base .front header .head-right {
  width: 497px;
  height: 373px;
  z-index: 3;
  -webkit-transform: rotate(22deg);
  -moz-transform: rotate(22deg);
  -ms-transform: rotate(22deg);
  -o-transform: rotate(22deg);
  transform: rotate(22deg);
  -webkit-box-shadow: 0 1px 12px -4px #292929;
  -moz-box-shadow: 0 1px 12px -4px #292929;
  box-shadow: 0 1px 12px -4px #292929;
  background-color: #292929;
  position: absolute;
  overflow: hidden;
  top: -288px;
  right: -98px;
}


.cv-base .front header .head-bottom {
  z-index: 2;
  width: 100%;
  height: 214px;
  padding: 3px 0 0 0;
  background-color: transparent;
  position: absolute;
  overflow: hidden;
  top: 5px;
}

.cv-base .front header .head-bottom .image-left {
  float: left;
  width: 130px;
  height: 130px;
  margin-right: 44px;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
  border-radius: 50%;
  background-color: #292929;
  background-image: url("{image_url}");
  background-repeat: no-repeat;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  background-size: cover;
  overflow: hidden;
  margin-top: 45px;
}

.cv-base .front header .head-bottom .words-right {
  float: left;
  height: 201px;
  padding: 66px 0 0 0;
  background-color: transparent;
}

.cv-base .front header .head-bottom .words-right h3 {
  padding: 12px 40px 9px 46px;
  margin: 0 0 0 0;
  position: relative;
  border-radius: 100px;
  display: inline-block;
  background-color: #292929;
  text-transform: uppercase;
  letter-spacing: 1px;
  text-align: center;
  font-family: "Poppins", sans-serif;
  font-weight: 600;
  font-size: 25px;
  color: #efefef;
}

.cv-base .front header .head-bottom .words-right p {
  padding: 7px 0 0 3px;
  margin: 0;
  text-transform: capitalize;
  text-align: center;
  font-family: "Poppins", sans-serif;
  font-size: 19px;
  color: #292929;
}

.cv-base .front header .head-bottom .words-right h3:before {
  content: "";
  width: 50px;
  height: 17px;
  background-color: #292929;
  position: absolute;
  bottom: -16px;
  right: 0;
}

.cv-base .front header .head-bottom .words-right h3:after {
  content: "";
  width: 23px;
  height: 17px;
  background-color: #292929;
  position: absolute;
  bottom: -16px;
  right: -27px;
}


.cv-base .front header .head-bottom .aesthetic01:before {
  content: "";
  width: 54px;
  height: 17px;
  background-color: #ff4359;
  position: absolute;
  top: 54px;
  left: 52px;
}

.cv-base .front header .head-bottom .aesthetic01:after {
  content: "";
  width: 54px;
  height: 17px;
  background-color: #ff4359;
  position: absolute;
  top: 70px;
  left: 29px;
}

.cv-base .front header .head-bottom .aesthetic02:before {
  content: "";
  width: 51px;
  height: 17px;
  background-color: #ff4359;
  position: absolute;
  top: 140px;
  left: 269px;
}

.cv-base .front header .head-bottom .aesthetic02:after {
  content: "";
  width: 26px;
  height: 17px;
  background-color: #ff4359;
  position: absolute;
  top: 140px;
  left: 237px;
}

.cv-base .front header .head-bottom .aesthetic03:before {
  content: "";
  width: 84px;
  height: 21px;
  background-color: #ff4359;
  position: absolute;
  top: 181px;
  left: 222px;
}

.cv-base section {
  width: 100%;
  height: 657.7px;
  background-color: transparent;
  overflow: visible;
}

.cv-base section aside {
  float: left;
  width: 242px;
  height: 650.7px;
  margin-right: 20px;
  background-color: transparent;
  border-right: 1px solid #d8d8d8;
  overflow: visible;
}

.cv-base section aside .aside-parts {
  width: 100%;
  padding-right: 10px;
  margin-bottom: 5px;
  background-color: transparent;
  overflow: visible;
}

.cv-base section aside .aside-parts h3 {
  padding: 0 0 8px 0;
  margin: 0;
  text-align: center;
  text-transform: uppercase;
  font-family: "Poppins", sans-serif;
  font-weight: 600;
  font-size: 20px;
  color: #292929;
}

.cv-base section aside .aside-parts ul {
  width: 100%;
  padding: 0;
  margin: 0;
  list-style-type: none;
  overflow: visible;
  display: contents;
}

.cv-base section aside .aside-parts ul li {
  width: 100%;
  /* margin-bottom: 10px; */
  display: contents;
  visibility: visible;
}

.cv-base section aside .aside-parts ul li h3 {
  color: #ff4359;
}

.cv-base section aside .aside-parts ul li p {
  padding: 0;
  margin: 0;
  font-family: "Poppins", sans-serif;
  color: #777;
  display: contents;
  visibility: visible;
}

.cv-base section aside #aside01 ul {
  height: 124px;
}

.cv-base section aside #aside01 ul li p {
  line-height: 19px;
  font-size: 12px;
}

.cv-base section aside #aside02 {
  margin-bottom: 0;
}

.cv-base section aside #aside02 ul {
  height: 326.7px;
  padding-right: 8px;
}

.cv-base section aside #aside02 ul li h3 {
  padding: 0 0 3px 0;
  text-align: left;
  font-size: 15px;
}

.cv-base section aside #aside02 ul li p:first-of-type {
  padding: 0 0 3px 0;
  font-size: 13px;
}

.cv-base section aside #aside02 ul li p:last-of-type {
  line-height: 19px;
  font-size: 12px;
}

.cv-base section aside #aside02 ul #education01 {
  display: list-item;
}

.cv-base section aside #aside02 ul #education02 {
  display: list-item;
}

.cv-base section aside #aside02 ul #education03 {
  display: none;
}

.cv-base section aside #aside02 ul #education04 {
  display: none;
}

.cv-base section aside #aside02 ul #education05 {
  display: none;
}

.cv-base section aside #aside02 ul #education06 {
  display: none;
}

.cv-base section aside #aside02 ul #education07 {
  display: none;
}

.cv-base section aside #aside02 ul #education08 {
  display: none;
}

.cv-base section aside #aside02 ul #education09 {
  display: none;
}

.cv-base section aside #aside02 ul #education10 {
  display: none;
}

.cv-base section aside #aside02 ul #education11 {
  display: none;
}

.cv-base section aside #aside02 ul #education12 {
  display: none;
}

.cv-base section aside #aside02 ul #education13 {
  display: none;
}

.cv-base section aside #aside02 ul #education14 {
  display: none;
}

.cv-base section aside #aside02 ul #education15 {
  display: none;
}

.cv-base section aside #aside02 ul #education16 {
  display: none;
}

.cv-base section aside #aside02 ul #education17 {
  display: none;
}

.cv-base section aside #aside02 ul #education18 {
  display: none;
}

.cv-base section aside #aside02 ul #education19 {
  display: none;
}

.cv-base section aside #aside02 ul #education20 {
  display: none;
}

.cv-base section aside #aside02 ul #education21 {
  display: none;
}

.cv-base section aside #aside02 ul #education22 {
  display: none;
}

.cv-base section aside #aside02 ul #education23 {
  display: none;
}

.cv-base section aside #aside02 ul #education24 {
  display: none;
}

.cv-base section aside #aside02 ul #education25 {
  display: none;
}

.cv-base section aside #aside02 ul #education26 {
  display: none;
}

.cv-base section aside #aside02 ul #education27 {
  display: none;
}

.cv-base section aside #aside02 ul #education28 {
  display: none;
}

.cv-base section aside #aside02 ul #education29 {
  display: none;
}

.cv-base section aside #aside02 ul #education30 {
  display: none;
}

.cv-base section aside #aside02 ul #education31 {
  display: none;
}

.cv-base section aside #aside02 ul #education32 {
  display: none;
}

.cv-base section aside #aside02 ul #education33 {
  display: none;
}


.cv-base section article {
  float: right;
  width: 435px;
  height: 521.7px;
  background-color: transparent;
  overflow: hidden;
}

.cv-base section article .article-parts {
  width: 100%;
  margin-bottom: 18px;
  background-color: transparent;
  overflow: hidden;
}

.cv-base section article .article-parts h3 {
  padding: 0 0 10px 0;
  margin: 0;
  text-align: center;
  text-transform: uppercase;
  font-family: "Poppins", sans-serif;
  font-weight: 600;
  font-size: 20px;
  color: #292929;
}

.cv-base section article .article-parts ul {
  padding: 0;
  margin: 0;
  list-style-type: none;
  display: contents;
  visibility: visible;
}


.cv-base section article #article01 .groups {
  width: 100%;
  height: 74px;
  padding-right: 10px;
  overflow: hidden;
}

.cv-base section article #article01 .groups .lines {
  width: 100%;
  margin-bottom: 15px;
  background-color: transparent;
  overflow: hidden;
}

.cv-base section article #article01 .groups .lines:last-child {
  margin-bottom: 0;
}

.cv-base section article #article01 .groups .lines ul li {
  float: left;
  width: 135px;
  margin-right: 10px;
  background-color: transparent;
  overflow: hidden;
}

.cv-base section article #article01 .groups .lines ul li:last-child {
  margin-right: 0;
}

.cv-base section article #article01 .groups .lines ul li .icons {
  float: left;
  width: 18px;
  padding-right: 0;
  overflow: hidden;
}

.cv-base section article #article01 .groups .lines ul li .icons i {
  font-size: 14px;
  color: #ff4359;
}


.cv-base section article #article01 .groups .lines ul li .words {
  float: right;
  width: 108px;
  padding-top: 3px;
  overflow: hidden;
}

.cv-base section article #article01 .groups .lines ul li .words p {
  padding: 0;
  margin: 0;
  text-transform: uppercase;
  font-family: "Poppins", sans-serif;
  font-size: 13px;
  color: #777;
}

.cv-base section article #article01 .groups #line01 {
  display: inline-block;
}

.cv-base section article #article01 .groups #line02 {
  display: inline-block;
}

.cv-base section article #article01 .groups #line03 {
  display: none;
}

.cv-base section article #article01 .groups #line04 {
  display: none;
}

.cv-base section article #article01 .groups #line05 {
  display: none;
}

.cv-base section article #article01 .groups #line06 {
  display: none;
}


.cv-base section article #article01 .groups #line01 ul li:first-child {
  display: list-item;
}

.cv-base section article #article01 .groups #line01 ul li:nth-child(2) {
  display: list-item;
}

.cv-base section article #article01 .groups #line01 ul li:last-child {
  display: list-item;
}

/*End Line01*/
/********************/
/*Line02*/
.cv-base section article #article01 .groups #line02 ul li:first-child {
  display: list-item;
}

.cv-base section article #article01 .groups #line02 ul li:nth-child(2) {
  display: list-item;
}

.cv-base section article #article01 .groups #line02 ul li:last-child {
  display: list-item;
}

/*End Line02*/
/********************/
/*Line03*/
.cv-base section article #article01 .groups #line03 ul li:first-child {
  display: none;
}

.cv-base section article #article01 .groups #line03 ul li:nth-child(2) {
  display: none;
}

.cv-base section article #article01 .groups #line03 ul li:last-child {
  display: none;
}

/*End Line03*/
/********************/
/*Line04*/
.cv-base section article #article01 .groups #line04 ul li:first-child {
  display: none;
}

.cv-base section article #article01 .groups #line04 ul li:nth-child(2) {
  display: none;
}

.cv-base section article #article01 .groups #line04 ul li:last-child {
  display: none;
}

/*End Line04*/
/********************/
/*Line05*/
.cv-base section article #article01 .groups #line05 ul li:first-child {
  display: none;
}

.cv-base section article #article01 .groups #line05 ul li:nth-child(2) {
  display: none;
}

.cv-base section article #article01 .groups #line05 ul li:last-child {
  display: none;
}

/*End Line05*/
/********************/
/*Line06*/
.cv-base section article #article01 .groups #line06 ul li:first-child {
  display: none;
}

.cv-base section article #article01 .groups #line06 ul li:nth-child(2) {
  display: none;
}

.cv-base section article #article01 .groups #line06 ul li:last-child {
  display: none;
}


.cv-base section article #article02 {
  margin-bottom: 0;
}

.cv-base section article #article02 ul {
  height: 367px;
  padding-right: 10px;
  overflow: hidden;
}

.cv-base section article #article02 ul li {
  width: 100%;
  margin-bottom: 10px;
  overflow: hidden;
}

.cv-base section article #article02 ul li h3 {
  padding: 0 0 3px 0;
  text-align: left;
  font-size: 15px;
  color: #ff4359;
}

.cv-base section article #article02 ul li p:first-of-type {
  padding: 0 0 3px 0;
  margin: 0 0 0 0;
  font-family: "Poppins", sans-serif;
  font-size: 13px;
  color: #777;
}

.cv-base section article #article02 ul li p:last-of-type {
  padding: 0;
  margin: 0;
  font-family: "Poppins", sans-serif;
  line-height: 19px;
  font-size: 12px;
  color: #777;
}


.cv-base section article #article02 ul #experience01 {
  display: list-item;
}

.cv-base section article #article02 ul #experience02 {
  display: list-item;
}

.cv-base section article #article02 ul #experience03 {
  display: list-item;
}

.cv-base section article #article02 ul #experience04 {
  display: none;
}

.cv-base section article #article02 ul #experience05 {
  display: none;
}

.cv-base section article #article02 ul #experience06 {
  display: none;
}

.cv-base section article #article02 ul #experience07 {
  display: none;
}

.cv-base section article #article02 ul #experience08 {
  display: none;
}

.cv-base section article #article02 ul #experience09 {
  display: none;
}

.cv-base section article #article02 ul #experience10 {
  display: none;
}

.cv-base section article #article02 ul #experience11 {
  display: none;
}

.cv-base section article #article02 ul #experience12 {
  display: none;
}

.cv-base section article #article02 ul #experience13 {
  display: none;
}

.cv-base section article #article02 ul #experience14 {
  display: none;
}

.cv-base section article #article02 ul #experience15 {
  display: none;
}

.cv-base section article #article02 ul #experience16 {
  display: none;
}

.cv-base section article #article02 ul #experience17 {
  display: none;
}

.cv-base section article #article02 ul #experience18 {
  display: none;
}

.cv-base section article #article02 ul #experience19 {
  display: none;
}

.cv-base section article #article02 ul #experience20 {
  display: none;
}

.cv-base section article #article02 ul #experience21 {
  display: none;
}

.cv-base section article #article02 ul #experience22 {
  display: none;
}

.cv-base section article #article02 ul #experience23 {
  display: none;
}

.cv-base section article #article02 ul #experience24 {
  display: none;
}

.cv-base section article #article02 ul #experience25 {
  display: none;
}

.cv-base section article #article02 ul #experience26 {
  display: none;
}

.cv-base section article #article02 ul #experience27 {
  display: none;
}

.cv-base section article #article02 ul #experience28 {
  display: none;
}

.cv-base section article #article02 ul #experience29 {
  display: none;
}

.cv-base section article #article02 ul #experience30 {
  display: none;
}

.cv-base section article #article02 ul #experience31 {
  display: none;
}

.cv-base section article #article02 ul #experience32 {
  display: none;
}

.cv-base section article #article02 ul #experience33 {
  display: none;
}

.cv-base .loop {
  width: 100%;
  height: 142px;
  z-index: 1;
  -webkit-transform: rotate(-16deg);
  -moz-transform: rotate(-16deg);
  -ms-transform: rotate(-16deg);
  -o-transform: rotate(-16deg);
  transform: rotate(-16deg);
  background-color: #ff4359;
  position: absolute;
  bottom: -106px;
  left: 55px;
}

.cv-base .front footer {
  width: 100%;
  height: 190px;
  background-color: transparent;
  position: absolute;
  overflow: hidden;
  z-index: 2;
}

.cv-base .front footer .foot-back {
  width: 86%;
  height: 195px;
  z-index: 1;
  -webkit-transform: rotate(7deg);
  -moz-transform: rotate(7deg);
  -ms-transform: rotate(7deg);
  -o-transform: rotate(7deg);
  transform: rotate(7deg);
  background-color: #292929;
  position: absolute;
  overflow: hidden;
  bottom: -98px;
  left: -43px;
}

.cv-base .front footer .foot-front {
  width: 345px;
  height: 178px;
  z-index: 2;
  -webkit-transform: rotate(28deg);
  -moz-transform: rotate(28deg);
  -ms-transform: rotate(28deg);
  -o-transform: rotate(28deg);
  transform: rotate(28deg);
  background-color: #292929;
  position: absolute;
  overflow: hidden;
  bottom: -193px;
  right: -133px;
}

.cv-base .front footer .foot-words {
  z-index: 3;
  width: 639px;
  height: 115px;
  padding: 8px 0 0 49px;
  background-color: transparent;
  position: absolute;
  overflow: hidden;
  top: 75px;
  margin-left: -20px;
  left: 0;
}

.cv-base .front footer .foot-words h3 {
  padding: 0 0 13px 0;
  margin: 0;
  text-transform: uppercase;
  font-family: "Poppins", sans-serif;
  font-weight: 600;
  font-size: 20px;
  color: #efefef;
}

.cv-base .front footer .foot-words ul {
  padding: 0;
  margin: 0;
  list-style-type: none;
}

.cv-base .front footer .foot-words ul li {
  float: left;
  width: 182px;
  margin-bottom: 14px;
  background-color: transparent;
  overflow: hidden;
}

.cv-base .front footer .foot-words ul li .icons {
  float: left;
  width: 20px;
  overflow: hidden;
}

.cv-base .front footer .foot-words ul li .icons i {
  font-size: 16px;
  color: #ff4359;
}


.cv-base .front footer .foot-words ul li .words {
  float: right;
  width: 156px;
  overflow: hidden;
}

.cv-base .front footer .foot-words ul li .words p {
  width: 149px;
  padding: 0;
  margin: 0;
  overflow: hidden;
  font-family: "Poppins", sans-serif;
  font-size: 13px;
  color: #efefef;
}


.cv-base .back, .cv-base .front, .cv-base .front footer .foot-back {
  -webkit-box-shadow: 0 0 12px -4px #000;
  -moz-box-shadow: 0 0 12px -4px #000;
  box-shadow: 0 0 12px -4px #000;
}

.cv-base .front header .head-bottom .words-right h3:before, .cv-base .front header .head-bottom .words-right h3:after, .cv-base .front header .head-bottom .aesthetic01:before, .cv-base .front header .head-bottom .aesthetic01:after, .cv-base .front header .head-bottom .aesthetic02:before, .cv-base .front header .head-bottom .aesthetic02:after, .cv-base .front header .head-bottom .aesthetic03:before {
  -webkit-border-radius: 100px;
  -moz-border-radius: 100px;
  border-radius: 100px;
}
</style>
    """

def get_full(style:str, cv_body:str)->str:
    return f"""
    {DOCTYPE}
    {style}
    {SCRIPT}
    <html>
        {HEAD}
        <body>
        <div class="cv-base">
            <div class="front">
                {cv_body}
            </div>
		</div>
        <script src="js/tools/jquery-3.4.1.min.js"					></script>
		<script src="js/tools/jquery.nicescroll.min.js"				></script>
		<script src="js/features.js"								></script>
		<script src="js/add-edit/add-namejob.js"					></script>
		<script src="js/add-edit/add-about.js"						></script>
		<script src="js/add-edit/add-education.js"					></script>
		<script src="js/add-edit/add-skills.js"						></script>
		<script src="js/add-edit/add-experience.js"					></script>
		<script src="js/add-edit/add-contact.js"	
        </body>
    </html>
    """

def get_header(name:str, position:str):
    return f"""
    <header>
    <div class="head-top"></div>
    <div class="head-right"></div>
    <div class="head-bottom">
        <div class="margin">
            <div class="image-left"></div>
            <div class="words-right">
                <h3 title="">{name}</h3>
                <p>{position}</p>
            </div>
        </div>
        <!-- <div class="aesthetic01"></div> -->
        <!-- <div class="aesthetic02"></div> -->
        <!-- <div class="aesthetic03"></div> -->
    </div>
    </header>
    """

def get_section(body:str):
    return f"""
    <section>
    <div class="margin">
    {body}
    </div>
    </section>
    """

def get_education(index:int, education:Education):
    return f"""
    <li id="education0{index}">
        <h3>{education.major}</h3>
        <p>{education.skills} * {education.date_range}</p>
        <p>{education.details}</p>
    </li>
    """

def get_skill(skill:Skill):
    return f"""
    <li>
        <div class="icons">
            <i class="fas fa-star"></i>
        </div>
        <div class="words">
            <p>{skill.title}</p>
        </div>
    </li>
    """

def get_skills(skills:List[str]):
    if len(skills) > 6:
        skills = skills[0:6]
    else:
        missing = 6-len(skills)
        
        


def get_footer(location:str, email:str, phone:str, facebook:str, twitter:str, google:str):
    return f"""
    <div class="loop"></div>
    <footer>
        <div class="foot-back"></div>
        <div class="foot-front"></div>
        <div class="foot-words">
            <h3>contact me</h3>
            <ul>
                <li id="contact01">
                    <div class="icons">
                        <i class="fas fa-map-marker-alt"></i>
                    </div>
                    <div class="words">
                        <p title="">{location}</p>
                    </div>
                </li>
                <li id="contact02">
                    <div class="icons">
                        <i class="fas fa-envelope"></i>
                    </div>
                    <div class="words">
                        <p maxlength="10">{email}</p>
                    </div>
                </li>
                <li id="contact03">
                    <div class="icons">
                        <i class="fas fa-phone"></i>
                    </div>
                    <div class="words">
                        <p>{phone}</p>
                    </div>
                </li>
                <li id="contact04">
                    <div class="icons">
                        <i class="fab fa-facebook-f"></i>
                    </div>
                    <div class="words">
                        <p>/{facebook}</p>
                    </div>
                </li>
                <li id="contact05">
                    <div class="icons">
                        <i class="fab fa-twitter"></i>
                    </div>
                    <div class="words">
                        <p>{twitter}</p>
                    </div>
                </li>
                <li id="contact06">
                    <div class="icons">
                        <i class="fab fa-google-plus-g"></i>
                    </div>
                    <div class="words">
                        <p>{google}</p>
                    </div>
                </li>
            </ul>
        </div>
    </footer>
    """