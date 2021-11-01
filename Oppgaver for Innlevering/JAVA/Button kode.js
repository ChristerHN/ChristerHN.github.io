function displayRandomImages() 
{
  
   var imageArray = [
   { 
     
     src: "https://cdn.discordapp.com/attachments/622836043262984231/903217957457526784/unknown.png",
  
     width: "280",
     height: "200"
   }, 
   {
     src: "https://akamai.vgc.no/drfront3/images/01250db4e36eea251995e95091574cd8.jpg",
     width: "320",
     height: "195"
   }, 
   {
     src: "https://cdn.discordapp.com/attachments/654801600761823244/902127531577188363/ekspressen_norled.jpg",
     width: "320",
     height: "195"
   },
   {
     src: "https://cdn.discordapp.com/attachments/654801600761823244/880750527913287680/20210827_113855.jpg",
     width: "350",
     height: "250"
    } ];
    
   
    var arrayLength = imageArray.length;
    var newArray = [];
    for (var i = 0; i < arrayLength; i++) {
        newArray[i] = new Image();
        newArray[i].src = imageArray[i].src;
        newArray[i].width = imageArray[i].width;
        newArray[i].height = imageArray[i].height;
    }
  
  function getRandomNum(min, max) 
  {
      
      imgNo = Math.floor(Math.random() * (max - min + 1)) + min;
      return newArray[imgNo];
  }  


  var newImage = getRandomNum(0, newArray.length - 1);

  var images = document.getElementsByTagName('img');
  var l = images.length;
  for (var p = 0; p < l; p++) {
     images[0].parentNode.removeChild(images[0]);
  }

  document.body.appendChild(newImage);
}