var bestellungen;
var gericht_name;
var passform;
var bestelldetails;
var bestellungsindex;
var zaehler;

function profil_hauptseite()
{
	
	window.location.href="/hello/account_page/";
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


    function addRatingWidget(shopItem, data,id) {

      var ratingElement = shopItem.querySelector('.c-rating');

      var currentRating = data;
      var maxRating = 5;
      var callback = function(rating) {
		bewertung[id]=rating

	
	 };
      
      var r = rating(ratingElement, currentRating, maxRating, callback);
    }
	
	    function buildShopItem(data,index) {
      var shopItem = document.createElement('div');

      var html ='<ul class="c-rating"></ul>' 



      shopItem.innerHTML = html;
      document.getElementsByClassName("shop")[index].appendChild(shopItem);

      return shopItem;
    }
	


function bewertungen_aufrufen()
{

	

	bestellungen=JSON.parse(document.getElementsByClassName("bestellungen_daten")[0].innerHTML)
	bestelldetails=JSON.parse(document.getElementsByClassName("bestelldetails_daten")[0].innerHTML)

	
	i=0;
	block=""
	passform=[]
	bewertung=[]
	zaehler=0;
	while (i<=bestelldetails.length-1)
	{
		block=block+document.getElementsByClassName("zusammenfassung")[0].innerHTML;
		i=i+1;
	}
	document.getElementsByClassName("zusammenfassung")[0].innerHTML=block
	
	i=0;

	while (i<=bestellungen.length-1)
	{
		
		
		j=0;
		
		while (j<=bestelldetails.length-1)
		{
			
			
			if(bestelldetails[j].bestellnummer==bestellungen[i].bestellnummer)
			{
				passform.push(bestelldetails[j].passform)
				bewertung.push(bestelldetails[j].bewertung)
				
				bestellungsindex=i
				b=bestelldetails[j].passform

				zaehler=zaehler+1;
				document.getElementsByClassName("block_1_style")[j].innerHTML =bestelldetails[j].style
				
				document.getElementsByClassName("block_1_bh_groesse")[j].innerHTML =bestelldetails[j].bhgroesse

				document.getElementsByClassName("block_1_slip_groesse")[j].innerHTML =bestelldetails[j].slipgroesse
				document.getElementsByClassName("block_1_style_beschreibung")[j].innerHTML =bestelldetails[j].subtitle

				document.getElementsByClassName("order_picture")[j].src=bestelldetails[j].picture_link_small
				

				document.getElementsByClassName("passform_inhalt")[j].innerHTML="<div class='little_cube' id='"+parseInt(j*3)+"' onclick='passform_click(this.id)'><br>Zu klein</div><div class='little_cube' id='"+parseInt(j*3+1)+"' onclick='passform_click(this.id)'><br>Passt genau</div><div class='little_cube' id='"+parseInt(j*3+2)+"' onclick='passform_click(this.id)'><br>Zu groß</div>"
				document.getElementsByClassName("bewertungsdetails")[j].innerHTML ="<b>Details zu deiner Bewertung</b><br><br><input type='text' class='headline_input' onkeyup='change()' placeholder='Überschrift' id='"+parseInt(j)+"' value='"+bestelldetails[j].bewertungsheadline+"'></input><br><br><textarea name='html_elemente' cols='50' rows='15' maxlength='300' class='textarea_bewertung'  id='"+parseInt(j)+"' onkeyup='change()' placeholder='Details Deiner Bewertung' >"+bestelldetails[j].bewertungstext+"</textarea>";
				if(bestelldetails[j].passform!="")
					document.getElementsByClassName("little_cube")[parseInt(j*3)+parseInt(bestelldetails[j].passform)-1].style.backgroundColor="#DB7093"

				
				
			}
			j=j+1;
		}
		
			
		i=i+1
	}
	

      for (var i = 0; i <=bestelldetails.length-1; i++) {

        addRatingWidget(buildShopItem(bestelldetails[i].bewertung,i),bestelldetails[i].bewertung,i);

      }
				
	
	
}


function change()
{
	i=0;

	while (i<=bestellungen.length-1)
	{
		
		
		j=0;
		
		while (j<=bestelldetails.length-1)
		{
			if(bestelldetails[j].bestellnummer==bestellungen[i].bestellnummer)
			{

				if(document.getElementsByClassName("headline_input")[j].value!="")
					document.getElementsByClassName("headline_input")[j].style.border="1px solid #e6e6e6";
			
				if(document.getElementsByClassName("textarea_bewertung")[j].value!="")
					document.getElementsByClassName("textarea_bewertung")[j].style.border="1px solid #e6e6e6";
			}
			j=j+1;
		}
		i=i+1;
	}
		
		
}

function replace_dot_comma(zahl)
{

	var zahl_=	zahl.toFixed(2);
	zahl_ = zahl_.toString();
	return zahl_.replace(".", ",");
}

function check_if_completed_form()
{
	i=0;
	feedback="true";
	
	while (i<=bestellungen.length-1)
	{
		j=0;
		while (j<=bestelldetails.length-1)
		{
			
			if(bestelldetails[j].bestellnummer==bestellungen[i].bestellnummer)
			{
				
				if(document.getElementsByClassName("headline_input")[j].value=="")
				{
					document.getElementsByClassName("headline_input")[j].style.border="1px solid red";
					feedback="false";
				}

				if(document.getElementsByClassName("textarea_bewertung")[j].value=="")
				{
					document.getElementsByClassName("textarea_bewertung")[j].style.border="1px solid red";
					feedback="false";
				}			
				
				if(bewertung[j]=="")
				{
					document.getElementsByClassName("bewertung_headline")[j].style.color="red";
					feedback="false";
				}			


				if(passform[j]=="")
				{
					document.getElementsByClassName("passform_headline")[j].style.color="red";
					feedback="false";
				}	
			}		
			j=j+1
		}		
		i=i+1;
	}		
	
	return feedback;

}




function bestellungen_bearbeiten()
{
	
	window.location.href="/hello/account_page/bestellungen_bearbeiten/";

}

function bewertung_bearbeiten(index,index_1)
{
	
	window.location.href="/hello/account_page/bewertungen_bearbeiten/"+bestellungen[index].bestellnummer+"/"+bestelldetails[index_1].linkzugericht+"/";
}


function passform_click(id)
{
	
	j=0;
	passform_=0
	while (j<=bestelldetails.length-1)
	{

		if(id==j*3)
			passform_=1
		else
			if(id==j*3+1)
				passform_=2
			else		
				if(id==j*3+2)
					passform_=3
		if(passform_!=0)
		{

			document.getElementsByClassName("little_cube")[parseInt(j*3)].style.backgroundColor=""
	
			document.getElementsByClassName("little_cube")[parseInt(j*3+1)].style.backgroundColor=""
			document.getElementsByClassName("little_cube")[parseInt(j*3+2)].style.backgroundColor=""
			break;
		}
		j=j+1
		
	}
	
	document.getElementsByClassName("little_cube")[id].style.backgroundColor="#DB7093";


	document.getElementsByClassName("passform_headline")[Math.floor(id/3)].style.color="#000000";
	passform[j]=passform_



}


function save_bewertungen()
{
	zaehler_=0
	

	if(check_if_completed_form()=="true")
	{
		i=0;

		while (i<=bestellungen.length-1)
		{

			
			j=0;
			while (j<=bestelldetails.length-1)
			{

				if(bestelldetails[j].bestellnummer==bestellungen[i].bestellnummer)
				{
		
					i_alt=i
					j_alt=j

					$.ajax({
					type: "POST",
					url: "/hello/account_page/bewertung_speichern/",
					dataType: "json",
					data: { "bestellnummer":bestellungen[i].bestellnummer,"style":bestelldetails[j].style,"stylecode":bestelldetails[j].stylecode,"color":bestelldetails[j].color,"bewertungsheadline":document.getElementsByClassName("headline_input")[j].value,"bewertungstext":document.getElementsByClassName("textarea_bewertung")[j].value,"bewertung":bewertung[j],"passform":passform[j]},
					success: function(data) {

							i=i_alt
							j=j_alt
							zaehler_=zaehler_+1
								if(zaehler==zaehler_)
		bestellungen_bearbeiten()

					}
					})
				}
				j=j+1;
			}
			i=i+1;
		}

	}


}



	


    // BUILD SHOP ITEM


    // ADD RATING WIDGET





