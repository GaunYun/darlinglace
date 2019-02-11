var bewertungsdetails;
var gerichtdetails;


function profil_hauptseite()
{
	
	window.location.href="/hello/account_page/";
}

function bewertungen_bearbeiten_hauptseite()
{

	document.getElementsByClassName("button_abbrechen")[0].style.pointerEvents = "none";
	document.getElementsByClassName("bewertung_speichern_button")[0].style.pointerEvents = "none";
	
	
	window.location.href="/hello/account_page/bewertungen_bearbeiten/";
}


function test() 
{
	"use strict";
	function t(t,i,n,e)
	{
		function r(t,i)
		{
			for(var n=0;n<t.length;n++)
			{
				var e=t[n];i(e,n)
			}
		}
		
		function a(t)
		{
			s(t),o(t),u(t)
		}
		
		function s(t)
		{
			t.addEventListener("mouseover",function(i)
			{
				r(f,function(i,n)
				{
					n<=parseInt(t.getAttribute("data-index"))?i.classList.add("is-active"):i.classList.remove("is-active")
				})
			})
		}
		
		function o(t)
		{
			t.addEventListener("mouseout",function(t)
			{
				-1===f.indexOf(t.relatedTarget)&&c(null,!1)
			})
		}
		
		function u(t)
		{
			t.addEventListener("click",function(i)
			{
				i.preventDefault(),c(parseInt(t.getAttribute("data-index"))+1,!0)
			})
		}
		
		function c(t,a)
		{
			t&&0>t||t>n||(void 0===a&&(a=!0),i=t||i,r(f,function(t,n)
			{
				i>n?t.classList.add("is-active"):t.classList.remove("is-active")
			}
			),e&&a&&e(d()))
		}
		
		function d()
		{
			return i
		}
		
		var f=[];
		
		return function()
		{
			if(!t)throw Error("No element supplied.");
			if(!n)throw Error("No max rating supplied.");
			if(i||(i=0),0>i||i>n)throw Error("Current rating is out of bounds.");
			for(var e=0;n>e;e++)
			{
				var r=document.createElement("li");r.classList.add("c-rating__item"),r.setAttribute("data-index",e),i>e&&r.classList.add("is-active"),t.appendChild(r),f.push(r),a(r)
			}
		}(),
		{
			setRating:c,getRating:d
		}
	}
	window.rating=t
};


    function addRatingWidget(shopItem, data) {
    	
      var ratingElement = shopItem.querySelector('.c-rating');
      var currentRating = data;
      var maxRating = 5;
      var callback = function(rating) {  };
      
      var r = rating(ratingElement, currentRating, maxRating, callback);
    }
	
	    function buildShopItem(data,index) {
      var shopItem = document.createElement('div');

      var html ='<ul class="c-rating"></ul>' 



      shopItem.innerHTML = html;
      document.getElementsByClassName("shop")[index].appendChild(shopItem);

      return shopItem;
    }
	
	
  function button_logo(index,text_area,logo_area,button_)
 {
	 
	 if (index==0)
	 {
		document.getElementsByClassName(""+text_area+"")[0].style.display="none";
		document.getElementsByClassName(""+logo_area+"")[0].style.display="block";

		document.getElementsByClassName(""+button_+"")[0].style.pointerEvents = 'none';
		

		
	 }
	 else
	 {
		document.getElementsByClassName(""+text_area+"")[0].style.display="block";
		document.getElementsByClassName(""+logo_area+"")[0].style.display="none";	
		document.getElementsByClassName(""+button_+"")[0].style.pointerEvents = 'auto';
		
		 
	 }
	 
 }


function bewertungen_aufrufen(daten,daten_2)
{
	

	bestellungen=JSON.parse(document.getElementsByClassName("bestellungen_daten")[0].innerHTML)
	bestelldetails=JSON.parse(document.getElementsByClassName("bestelldetails_daten")[0].innerHTML)
	
	box_1="<img style='margin-Top:10px;width:250px;height:250px;float:left;'/>"
	box_2="<div class='links'></div><br><div style='font-size:14px;font-style:italic;line-height:20px;'></div><br><br><div style='font-size:14px;'>Zugestellt am </div><br>"
	box_2=box_2+"<div style='font-size:14px;'>Deine Bewertung</div><div class='shop'></div>";
	
	

	

	
	
	document.getElementsByClassName("spalte_text_1")[0].innerHTML=box_1;
	document.getElementsByClassName("spalte_text_2")[0].innerHTML=box_2;

	//	document.getElementById("bewertungsdetails_textarea").value=bestelldetails[0].bewertungstext;


      for (var i = 0; i < 1; i++) {

        addRatingWidget(buildShopItem(2,0),2);

      }
			

	
}




function bewertung_bearbeiten(index,index_1)
{
	
	window.location.href="/hello/account_page/bewertungen_bearbeiten/"+bestellungen[index][2]+"/"+gericht_name[index][index_1]+"/";
}

function bewertung_speichern()
{
	
	button_logo(0,"bewertung_speichern_button_text","bewertung_speichern_button_logo","bewertung_speichern_button")
	document.getElementsByClassName("button_abbrechen")[0].style.pointerEvents = "none";
	
	$.ajax({
		type: "POST",
		url: "/hello/account_page/bewertung_speichern/",
		dataType: "json",
		data: { "bestellnummer":bestelldetails[0].bestellnummer,"gerichtname":bestelldetails[0].linkzugericht,"bewertung": bestelldetails[0].bewertung,"bewertungstext": document.getElementById("bewertungsdetails_textarea").value},
		success: function(data) {
			button_logo(1,"bewertung_speichern_button_text","bewertung_speichern_button_logo","bewertung_speichern_button")
			document.getElementsByClassName("button_abbrechen")[0].style.pointerEvents = "auto";
			window.location.href="/hello/account_page/bewertungen_bearbeiten/";
			

		}

	});
}



	


    // BUILD SHOP ITEM


    // ADD RATING WIDGET





