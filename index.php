<!DOCTYPE html>
<html>
  <head>
  
<link rel="icon" href="images/switch_up.png" type="image/icon">

    <title>SwitchMap</title>
    <meta name="viewport" content="initial-scale=1.0">
    <script src="https://code.jquery.com/jquery-latest.min.js"></script>
    <meta charset="utf-8">
    <style>
      #map {
        height: 100%;
      }/*เซ็ต Google map เต็มจอ */
     
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }/*เซ็ต Google map เต็มจอ */
    </style>
    
  </head>
  <script> 
        setTimeout(function() {
        location.reload();
        }, 500000);
  </script>
  
  <body>
    <?php //id = "map" ?>
    <div id="map"></div>
    
    <script>

      
      var maps;//กำหนด ตัวแปร "map"
      var position = {lat: 20.046556 , lng: 99.894151};//กำหนดตัวแปร"position"ที่ตั้งที่จะแสดง
      /*
      var path = [
        {lat:20.047994,lng:99.895254},
        {lat:20.046356,lng:99.892844},
        
        ];
      */
     


      function initMap() {
        maps = new google.maps.Map(document.getElementById('map'), {
          center: position,//แสดงตรงกลาง ตำแหน่งตัวแปรposition
          zoom: 17,//zoom= 1:World,5:Landmass/Continent,10:City,15:Streets,20:Buildings
          mapTypeId:google.maps.MapTypeId.SATELLITE, //ชนิดMap => 1.ROADMAP,2.SATELLITE,3.HYBRID,4.TERRAIN
          
          
        });
        
      var marker,info;//สร้างตัวแปร marker,info
      $.getJSON("switchesdata.php",function(jsonObj){//สร้างfunction getJSONดึงข้อมูลจากไฟล์ , callback function
          $.each(jsonObj,function(i,item){//loopข้อมูล
            if(item.status == 1){
              icon = "images/switch_up.png"
            }else if(item.status == 0){
              icon = "images/switch_down.png"
            }
            marker = new google.maps.Marker({//สร้าง marker ขึ้นมา
            position: new google.maps.LatLng(item.lat,item.lng),//mark ที่ตำแหน่งไหน จาก lat,lng column
            map: maps,//แสดง marker ที่ maps
            icon: icon,//icon switches
            animation: google.maps.Animation.DROP
          });
       
            info = new google.maps.InfoWindow({
            maxWidth: 270,
        

             });//หมุดตัวนี้มีคำอธิบายอะไรบ้าง ทำการสร้างobject
            
            google.maps.event.addListener(marker,"click",(function(marker,i){//สร้าง eventให้กับ marker,click,สร้าง callback function loopข้อมูลแต่ละชุด
            //google.maps.event.addListener(flightPath,"mouseover",)
            var detail = item.detail ;
            var lat = item.lat;
            var lng = item.lng;
            console.log(detail);
            console.log(item.lat);
            console.log(item.lng)                
              return function(){
                /*if (marker.getAnimation() !== null){
                  marker.setAnimation(null);
                }else{
                  marker.setAnimation(google.maps.Animation.BOUNCE)
                  setTimeout(function(){ marker.setAnimation(null); }, 750);
                }
                */

              if(item.status == 1){
                let detail0 = item.detail[0].toString();
                let detail1 = item.detail[1].toString();
                let detail2 = item.detail[2].toString();
                let detail3 = item.detail[3].toString();
                let detail4 = item.detail[4].toString();
                let detail5 = item.detail[5].toString();
                let detail6 = item.detail[6].toString();
              
                let detail = detail0.concat("\n",detail1,"\n",detail2,"\n",detail3,"\n",detail4,"\n",detail5,"\n",detail6,"\n");
                info.setContent(detail);//แสดง key=detail
                info.open(maps,marker);//แสดงที่ตัวmap,marker
              }else if(item.status == 0){
                info.setContent(item.detail[1]+" Status:Down ");//แสดง key=detail
                info.open(maps,marker);//แสดงที่ตัวmap,marker
              }
             
             }
            })(marker,i));
      });
    });



   
    
var flightPath;//สร้างตัวแปร flighPath,infointerface

  $.getJSON("interfacesdata.php",function(jsonObj){//สร้างfunction getJSONดึงข้อมูลจากไฟล์ , callback function
      $.each(jsonObj,function(i,item){//loopข้อมูล
        var path = item.path;
        flightPath = new google.maps.Polyline({//สร้าง Polyline ขึ้นมา
        //position: new google.maps.LatLng(item.path[0],item.path[1]),//mark ที่ตำแหน่งไหน จาก lat,lng column
        path:path,
        strokeColor: '#ed1c24',
        strokeOpacity:1,
        strokeWeight:6,  
      });

        flightPath.setMap(maps);

        
        google.maps.event.addListener(flightPath,"click",(function(flightPath,i){//สร้าง eventให้กับ flighPath,mouseover,สร้าง callback function loopข้อมูลแต่ละชุด
        
        var int = item.int ;
        var path = item.path;
        
        console.log(int[1]);
        console.log(path[0]);
        console.log(path[1]);
        path[0]= 0
        path[1]= 1
        console.log(path[0]);
        console.log(path[1]);
            
          return function(){
            let int0 = item.int[0].toString();
            let int1 = item.int[1].toString();
            let int = int0.concat("\n",int1);
            
            info.setContent(int);//แสดง key=int
            info.open(maps,flightPath);//แสดงที่ตัวmap,flighPath
            
            
           
              
           

            
         }
        })(flightPath,i));
  });
});



      }// สร้างฟังก์ชั่นในการสร้างMapไปแสดงใน"div id="map""
    </script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script><?php //Jquery?>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAwE8AonEc5Nk-qoEzb3VEsYNotmv8h_L0&callback=initMap"<?php //พอทำการใช้งาน"API Key"ใช้ฟังก์ชั่น"InitMap"?>
    async defer></script><?php //API Key ?>
  </body>
</html>