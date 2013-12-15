var url = window.location.href.toLowerCase(); 
//alert(url);
if (url.indexOf("www.google.com.hk") >= 0 || url.indexOf("www.google.com") >= 0 || url.indexOf("/search") >= 0) 
{ 
    var all = document.querySelectorAll("*");  //origin 
    //var all = document.getElementById("search").getElementsByTagName("a");       //updated
    for (var i = 0; i < all.length; i ++) 
    { 
        all[i].onmousedown = null; 
		all[i].setAttribute("onmousedown", " ");
		/*
		all[i].onmousedown = function(){
			alert("nowamagic");	
		}
		*/
    }
}

