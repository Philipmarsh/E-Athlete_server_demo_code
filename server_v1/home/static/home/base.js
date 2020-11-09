let mainNav = document.getElementById('js-menu');
let navBarToggle = document.getElementById('js-navbar-toggle');
navBarToggle.addEventListener('click', function () {
    mainNav.classList.toggle('active');
}) ;

 var prevScrollpos = window.pageYOffset;


 console.log(top);
 window.onscroll = function() {
   var currentScrollPos = window.pageYOffset;
   var difference = prevScrollpos - currentScrollPos;
   var top = document.getElementById("full-navbar").style.top;
   var topNum = parseInt(top);
   if(top == "") topNum = 0;
   top = (topNum + difference) + "px";
  
   if((topNum + difference) <=0 && (topNum + difference) >=-80){
   	document.getElementById("full-navbar").style.top = top;
   }

   else if((topNum + difference) > 0 ){
     document.getElementById("full-navbar").style.top = "0px";
   }
   else{
     document.getElementById("full-navbar").style.top = "-80px";
   }
  prevScrollpos = currentScrollPos;
 }
