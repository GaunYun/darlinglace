	var zutaten=new Array(50);
	   var gerichte = new Array(20); 
	   var cart=new Array(10);
	   var cart_nummer;
	   var gewaehltes_datum;
	   var gewaehlter_wochentag;
	   var index_nummer;
	   var ingredients;
	   var lingerie_selection;
	   var pics =[]
	   var sizes
	   var gesamtbewertung;
	   var bewertungen;
	   var colors;
	   var groessentabelle_uebersicht;
	   var groessentabelle_detailliert;
	   var resize;
	   	var bh_zaehler;
		var panty_zaehler;
		var pricesforaddlpanty;
	   /*
   
   
   
   i,0,0: Name
   i,1,var: Filter: 1) Vegan, 2) Vegetarisch, 3) Gluten-frei, 4) Laktosefrei, 5) Nussfrei, 6) Ei-frei
   i,2,var:Zutaten*/
   
   
   
   function datum_auswahl(ausgewaehlter_tag,index_,ausgewaehlter_wochentag) 	
{
		index_nummer=index_;

		
		gewaehltes_datum=ausgewaehlter_tag;
		gewaehlter_wochentag=ausgewaehlter_wochentag;
		

}




 function verfuegbarkeits_check()
 {
	


	 if ((parseInt(lingerie_selection[0].gerichte_uebrig)-parseInt(lingerie_selection[0].warenkorb_menge))<=10)
		 return (parseInt(lingerie_selection[0].gerichte_uebrig)-parseInt(lingerie_selection[0].warenkorb_menge))+" Gerichte übrig";
	 else
		 return "";
		 
	 
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
 
 
 function check_selected_options()
 {
 	i=0;
 	
 	 if(bh_zaehler==0)
		max=0;
 	else
		max=1;
 	while(i<=max)
 	{
	 	if(document.getElementsByClassName("bra_size_select")[i].selectedIndex==0)
	 	{
	 		document.getElementsByClassName("bra_size_select")[i].style.backgroundColor="red";
	 		document.getElementsByClassName("bra_size_select")[i].style.color="#ffffff";
	 	}
	 	
	 	i=i+1;
	 }
	if(max==1)
	{
		 if(document.getElementsByClassName("bra_size_select")[0].selectedIndex=="0" || document.getElementsByClassName("bra_size_select")[1].selectedIndex=="0")
		 	return "not ok"
		 else
		 	return "ok"
	}
	else
	{
		 if(document.getElementsByClassName("bra_size_select")[0].selectedIndex=="0")
		 	return "not ok"
		 else
		 	return "ok"		
		
	}
 		
 	
 }
 
 
 function reset_bra_size_select(i)
 {
	document.getElementsByClassName("bra_size_select")[i].style.backgroundColor="#ffffff";
	document.getElementsByClassName("bra_size_select")[i].style.color="#4d4d4d"; 	
	

		
		

 }
 
 function add_panties()
 {
 	if(document.getElementsByClassName("bra_size")[3].style.display=="block")
 	{
 		
 		 document.getElementsByClassName("bra_size")[3].style.display="none";
 		document.getElementsByClassName("add_panties")[0].innerHTML="Zweiten Slip hinzufügen";
 		document.getElementsByClassName("add_panties")[3].selectedIndex=0;
 	}	
 	else
 	{
 		document.getElementsByClassName("bra_size")[3].style.display="block";
 		document.getElementsByClassName("add_panties")[0].innerHTML="Zweiten Slip entfernen";
 		
 	}
 	
 }
 

 
 
   function alert_sizing()
 {	 
	


	ratio_=0.8


	check_sizing("80B","M")


	slider.setValue(80);


 }


function check_sizing(size,bralette_size)
{
	i=0

	document.getElementsByClassName("button_main_sizing_calc")[0].style.pointerEvents = 'none';
	document.getElementsByClassName("button_main_sizing_calc")[0].style.opacity = '0.4';

	while(i<=sizes.length-1)
	{

		if(sizes[i].type=="BH")
			if("Deine BH-Größe ist "+size=="Deine BH-Größe ist "+sizes[i].size)
			{
				
				document.getElementsByClassName("button_main_sizing_calc")[0].style.pointerEvents = 'auto';
				document.getElementsByClassName("button_main_sizing_calc")[0].style.opacity = '1.0';
				break;
			}
			else
			{
				
				if("Deine Bralette-Größe ist "+bralette_size=="Deine Bralette-Größe ist "+sizes[i].size)
				{

					document.getElementsByClassName("button_main_sizing_calc")[0].style.pointerEvents = 'auto';
					document.getElementsByClassName("button_main_sizing_calc")[0].style.opacity = '1.0';
					break;		
				}
				else
				{
					document.getElementsByClassName("button_main_sizing_calc")[0].style.pointerEvents = 'none';
					document.getElementsByClassName("button_main_sizing_calc")[0].style.opacity = '0.4';
				}
			}
				

		i=i+1;
	}
	
	
}

$('#myModal').on('shown.bs.modal', function () {
    

  alert_sizing();

});

 	
   
function add_cart()
{

	if(check_selected_options()=="ok")
	{

		//button_logo(0,"add_to_cart_text","add_to_cart_logo","button_cart")


	 	windowwidth=window.innerWidth;
 	windowheight=window.innerHeight;

 	if(bh_zaehler==0)
 	{
 		slip_groesse=document.getElementsByClassName("bra_size_select")[0].value
 		bh_groesse=""
 	}
 	else
 	{
 		slip_groesse=document.getElementsByClassName("bra_size_select")[1].value
 		bh_groesse=document.getElementsByClassName("bra_size_select")[0].value	
 	}

	slip_groesse_2=""
	if(document.getElementsByClassName("bra_size")[2].innerHTML=="")
	{
		slip_groesse_2=""
	}
	else
	{
		if(document.getElementsByClassName("bra_size")[3].style.display=="")
		{
			slip_groesse_2=""
		}
		else
		{
		 	if(bh_groesse!="")
		 	{
		 		
		 		if(document.getElementsByClassName("pricesforaddlpanty")[0].innerHTML!="[]")
		 		{ 			
				 	if(document.getElementsByClassName("bra_size_select")[2].selectedIndex>0)
				 		slip_groesse_2=document.getElementsByClassName("bra_size_select")[2].value
				 	else
				 		slip_groesse_2=""
			 	}
			 }
		}
	}




				
 		$.ajax({
		type: "GET",
		url: "/big_data_cart_put/",
		dataType: "json",
		data: { "stylecode": lingerie_selection[0].stylecode,"colorcode": lingerie_selection[0].colorcode, "putincart":"yes","windowheight":windowheight,"windowwidth":windowwidth},
		success: function(data) {		

				$.ajax({
					type: "GET",
					url: "/add/",
					dataType: "json",
					data: { "add_or_erase":"add","gerichtname": lingerie_selection[0].name,"stylecode": lingerie_selection[0].stylecode,"colorcode": lingerie_selection[0].colorcode,"bh_groesse": bh_groesse,"slip_groesse": slip_groesse,"regular_price":lingerie_selection[0].priceregular,"subscription_price":lingerie_selection[0].pricesubscription,"slip_groesse_2":slip_groesse_2,"productgroup":lingerie_selection[0].productgroup   },
					success: function(data) {



							    fbq('track', 'AddToCart', {
							      content_name: lingerie_selection[0].name, 
							      content_category: lingerie_selection[0].stylegroup,
							      content_ids: [lingerie_selection[0].stylecode+"_"+lingerie_selection[0].colorcode],
							      content_type: lingerie_selection[0].stylegroup,
							      value: lingerie_selection[0].pricesubscription,
							      currency: 'EUR' 
							    });  


						if(data=="nicht genuegend warenmenge")
							alert_userdata("SET NICHT VERFÜGBAR","Da war jemand anderes wohl schneller. Leider ist diese Größe von dem Set vergriffen")
						else
							if(data=="maximum warenmenge")
								alert_userdata("MAXIMALE ANZAHL ","Du kannst maximal 10 Sets in dieser Größe bestellen.")						
							else
							{
								
							
								
												document.getElementsByClassName("warenkorb_daten")[0].innerHTML=data;
												cart=JSON.parse(document.getElementsByClassName("warenkorb_daten")[0].innerHTML);
												warenkorb_ermitteln()
												insert_cart_content_in_header();
												show_dropdown(0);
		
								
							}
					}
				});
			}
		})
	}


}






function groessentabelle()
{
			$.ajax({
			type: "GET",
			url: "/account_page/groessentabelle_uebersicht/",
			dataType: "json",
			data: {'asd':'asd'  },
			success: function(data) {
						groessentabelle_uebersicht=data;
					$.ajax({
					type: "GET",
					url: "/account_page/groessentabelle_detailliert/",
					dataType: "json",
					data: {'':''  },
					success: function(data) {

							groessentabelle_detailliert=data;
							table_loaded="true"
							
							//set_new_ratios_1(0.49,100)

							
					}
					})
				
			}
			})
}

 
 


function update_produktionsmenge()
{
	i=0;
	while(i<=cart.length-1)
	{
		if(cart[i].datum==gewaehltes_datum)
			document.getElementsByClassName("box_zusatz_produktionsmenge")[0].innerHTML=verfuegbarkeits_check()
		i=i+1;
	}
	
	
	j=0;

	while(j<=lingerie_selection.length-1)
	{




			i=0;
			status=1;
			
			while(i<=cart.length-1)
			{

				if(cart[i].datum==gewaehltes_datum)
					if(lingerie_selection[j].name==cart[i].linkzugericht) 
						status=0;			
				i=i+1;
			}
			

			

			if(status==1)
			{
				
				document.getElementById("cart_image").style.display="none";
				document.getElementById("erase_from_cart").style.display="none";
				document.getElementsByClassName("box_zusatz_produktionsmenge")[0].innerHTML=verfuegbarkeits_check()
				add_cart_button_reset()
				cart_nummer=-1;
				
			}

		
	
		j=j+1;
	}	
	
}





function add_cart_button_reset()
{
	if(verfuegbarkeits_check()=="0 Gerichte übrig" || document.getElementById("cart_image").innerHTML=="10 Mal im Warenkorb")
	{
		document.getElementById("add_to_cart").style.backgroundColor="#E47272";
		document.getElementById("add_to_cart").style.pointerEvents = "none";
	}
	else
	{
		document.getElementById("add_to_cart").style.backgroundColor="#E47272";
		document.getElementById("add_to_cart").style.pointerEvents = "auto";
	}
}


//	

 function warenkorb_ermitteln()
 {

	cart=JSON.parse(document.getElementsByClassName("warenkorb_daten")[0].innerHTML)	
	
	 
	 	 var i=0;
	 cart_gesamt=0;
	 cart_nummer=-1;
	 
	
	anzahl=0
	 while (i<=cart.length-1)
	 {
		 if (parseInt(cart[i].anzahl)>0)
			cart_gesamt=cart_gesamt+parseInt(cart[i].anzahl);
		i=i+1;
	 }
	

		

	if (cart_gesamt!=0)
	{

		document.getElementsByClassName("cart_text")[0].innerHTML=cart_gesamt;

		document.getElementsByClassName("cart")[0].style.backgroundImage="url('/static/Cart-open.png')";
		
	}
	else
	{
		document.getElementsByClassName("cart_text")[0].innerHTML=" ";
		document.getElementsByClassName("cart")[0].style.backgroundImage="url('/static/Cart-closed.png')";

		
	}

 }
 
 












function replace_dot_comma(zahl)
{
	
	
	var zahl_=	zahl.toFixed(2);
	zahl_ = zahl_.toString();
	return zahl_.replace(".", ",");
	
	
	
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
			//s(t),o(t),u(t)
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
      var currentRating = parseInt(data);
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

	
	
	
function zurueck_button(index)
{
	window.location= "/"+index;
	
	
}


function pic_change(i)
{


	 	windowwidth=window.innerWidth;
 	windowheight=window.innerHeight;


		 		$.ajax({
		type: "GET",
		url: "/big_data_picture_clicked/",
		dataType: "json",
		data: { "stylecode": lingerie_selection[0].stylecode,"colorcode": lingerie_selection[0].colorcode, "pictureclicked":pics[i].toString(),"windowheight":windowheight,"windowwidth":windowwidth},
		success: function(data) {


			
				document.getElementsByClassName("bild-laden")[0].src=pics[i]
				j=0;
				while(j<=pics.length-1)
				{
			
					if(j==0 || j==4 || j==8)
						document.getElementsByClassName("small_pictures_huelle_1")[j/4].style.backgroundColor="";
					if(j==1 || j==5 || j==9)	
						document.getElementsByClassName("small_pictures_huelle_2")[(j-1)/4*2].style.backgroundColor="";
					if(j==2 || j==6 || j==10)
						document.getElementsByClassName("small_pictures_huelle_2")[(j-2)/4*2+1].style.backgroundColor="";
					if(j==3 || j==7 || j==11)
						document.getElementsByClassName("small_pictures_huelle_3")[(j-3)/4].style.backgroundColor="";
			
					j=j+1;
				}
				
			
				if(i==0 || i==4 || i==8)
					document.getElementsByClassName("small_pictures_huelle_1")[i/4].style.backgroundColor="#E47272";
				if(i==1 || i==5 || i==9)	
					document.getElementsByClassName("small_pictures_huelle_2")[(i-1)/4*2].style.backgroundColor="#E47272";
				if(i==2 || i==6 || i==10)
					document.getElementsByClassName("small_pictures_huelle_2")[(i-2)/4*2+1].style.backgroundColor="#E47272";
				if(i==3 || i==7 || i==11)
					document.getElementsByClassName("small_pictures_huelle_3")[(i-3)/4].style.backgroundColor="#E47272";
				if(window.innerWidth>=568)
					$('#ex1').zoom();
		
	 		}
 	})
}

window.onresize = function(event) {
	if(resize!=window.innerWidth)
	{
		resize=window.innerWidth
		initial_setup("yes");
		
	}
};
   
   
   
   function initial_setup(resize_)
   {

   	
   		var maxim= document.getElementsByClassName("image-box");
	var small_pics= document.getElementsByClassName("images_small");

	
	
	
	

			var arr1 = lingerie_selection[0].pic.split(",");
			

		for (i = 0; i < arr1.length; i++) {
			pics[i]=arr1[i].split(",");
		}  
		i=0;

		

		if(window.innerWidth>=568)
		{
			box="<img class='bild-laden' src='"+pics[0]+"'></img>"
			document.getElementsByClassName("image-box")[0].innerHTML =box;
			
			$('#ex1').zoom();
		}
		else
		{

			box="<div class='swiper-container'><div class='swiper-wrapper'>"
			i=0;
			while(i<=pics.length-1)
			{
				box=box+"<div class='swiper-slide'><img class='bild-laden' src='"+pics[i]+"'></img></div>"
				i=i+1;
			}

			
			box=box+"</div><div class='swiper-pagination'></div></div>"
			document.getElementsByClassName("image-box")[0].innerHTML =box;
			 var swiper = new Swiper('.swiper-container', {
		        pagination: '.swiper-pagination',
		        paginationClickable: true,
		       touchMoveStopPropagation:false 
		       
		    });
		}
			
		

		box="<br>"
		i=0;
		while(i<=pics.length-1)
		{
			if(i==0 || i==4 || i==8)
				box=box+"<div class='small_pictures_huelle_1'><img  class='small_pictures' src='"+pics[i]+"' onclick='pic_change("+i+")'></img></div>"
			if(i==1 || i==5 || i==9)
				box=box+"<div class='small_pictures_huelle_2'><img  class='small_pictures' src='"+pics[i]+"' onclick='pic_change("+i+")'></img></div>"				
			if(i==2 || i==6 || i==10)
				box=box+"<div class='small_pictures_huelle_2'><img  class='small_pictures' src='"+pics[i]+"' onclick='pic_change("+i+")'></img></div>"
				
			if(i==3 || i==7 || i==11)
				box=box+"<div class='small_pictures_huelle_3'><img  class='small_pictures' src='"+pics[i]+"' onclick='pic_change("+i+")'></img></div>"
				
			
				
				
			i=i+1;
		}
		

			
		if(resize_=="no")
		{			
			
			i=0
			bh_zaehler=0;
			panty_zaehler=0;
			while(i<=sizes.length-1)
			{
	
				if(sizes[i].type=="BH")
					bh_zaehler=bh_zaehler+1;
	
				if(sizes[i].type=="panties")
					panty_zaehler=panty_zaehler+1;
				i=i+1;
			}
		
			document.getElementsByClassName("bra_size_select")[0].innerHTML="<option>BH Größe</option>"
			document.getElementsByClassName("bra_size_select")[1].innerHTML="<option>Slip	 Größe</option>"
			document.getElementsByClassName("bra_size_select")[2].innerHTML="<option>Zweiter Slip Größe</option>"
			i=0;

			while(i<=sizes.length-1)
			{
	
				if(sizes[i].type=="BH")
					document.getElementsByClassName("bra_size_select")[0].innerHTML=document.getElementsByClassName("bra_size_select")[0].innerHTML+"<option value='"+sizes[i].size+"'>"+sizes[i].size+"</option>"
	
				if(sizes[i].type=="panties")
				{
					document.getElementsByClassName("bra_size_select")[1].innerHTML=document.getElementsByClassName("bra_size_select")[1].innerHTML+"<option value='"+sizes[i].size+"'>"+sizes[i].size+"</option>"
					
					
					if(document.getElementsByClassName("pricesforaddlpanty")[0].innerHTML!="[]")
					
						document.getElementsByClassName("bra_size_select")[2].innerHTML=document.getElementsByClassName("bra_size_select")[2].innerHTML+"<option value='"+sizes[i].size+"'>"+sizes[i].size+" (+ "+replace_dot_comma(pricesforaddlpanty[0].priceregular)+" €)</option>"
					else
						document.getElementsByClassName("bra_size")[2].innerHTML=""	
					
					

				}
				
				i=i+1;
			}
		}

	if(sizes[0].stylecode=="geschenkkarte")
	{
		document.getElementsByClassName("bra_size")[0].innerHTML=""
		document.getElementsByClassName("bra_size")[1].innerHTML=""
		document.getElementsByClassName("bra_size")[2].innerHTML=""	
		document.getElementsByClassName("ueberschrift_sizing")[0].innerHTML=""	
			
		
	}
	else
	{

		if (document.getElementsByClassName("bra_size_select")[0].innerHTML=="<option>BH Größe</option>")
		{
			document.getElementsByClassName("bra_size")[0].innerHTML=""
			document.getElementsByClassName("bra_size")[2].innerHTML=""
		}
	}
	
	small_pics[0].innerHTML=box
	

	document.getElementsByClassName("small_pictures_huelle_1")[0].style.backgroundColor="#E47272";
	
	document.getElementsByClassName("button_detail")[0].style.borderRight="0.5px solid #e6e6e6 ";

	if(document.getElementsByClassName("gesamtbewertung")[0].innerHTML!="[]")
	{
		
		document.getElementsByClassName("bewertungsblock")[0].style.display="block"
		document.getElementsByClassName("anzahl_bewertungen")[0].style.display="block"
		document.getElementsByClassName("anzahl_bewertungen_detailliert")[0].style.display="block"
		document.getElementsByClassName("anzahl_bewertungen")[0].innerHTML ="("+gesamtbewertung[0].gesamtbewertunganzahl+" Bewertungen)"
		document.getElementsByClassName("anzahl_bewertungen_detailliert")[0].innerHTML ="("+gesamtbewertung[0].gesamtbewertunganzahl+" Bewertungen)"

		document.getElementsByClassName("stacked_bar_bewertungen")[0].style.width=parseInt(gesamtbewertung[0].fuenfsternbewertunganzahl)/parseInt(gesamtbewertung[0].gesamtbewertunganzahl)*100+"%"
		document.getElementsByClassName("bewertung_anzahl")[0].innerHTML =gesamtbewertung[0].fuenfsternbewertunganzahl
		
		document.getElementsByClassName("stacked_bar_bewertungen")[1].style.width=parseInt(gesamtbewertung[0].viersternbewertunganzahl)/parseInt(gesamtbewertung[0].gesamtbewertunganzahl)*100+"%"
		document.getElementsByClassName("bewertung_anzahl")[1].innerHTML=gesamtbewertung[0].viersternbewertunganzahl
		
		document.getElementsByClassName("stacked_bar_bewertungen")[2].style.width=parseInt(gesamtbewertung[0].dreisternbewertunganzahl)/parseInt(gesamtbewertung[0].gesamtbewertunganzahl)*100+"%"
		document.getElementsByClassName("bewertung_anzahl")[2].innerHTML=gesamtbewertung[0].dreisternbewertunganzahl
		
		document.getElementsByClassName("stacked_bar_bewertungen")[3].style.width=parseInt(gesamtbewertung[0].zweisternbewertunganzahl)/parseInt(gesamtbewertung[0].gesamtbewertunganzahl)*100+"%"
		document.getElementsByClassName("bewertung_anzahl")[3].innerHTML=gesamtbewertung[0].zweisternbewertunganzahl
		
		document.getElementsByClassName("stacked_bar_bewertungen")[4].style.width=parseInt(gesamtbewertung[0].einsternbewertunganzahl)/parseInt(gesamtbewertung[0].gesamtbewertunganzahl)*100+"%"
		document.getElementsByClassName("bewertung_anzahl")[4].innerHTML=gesamtbewertung[0].einsternbewertunganzahl
		
	}

	
	var inhalt=lingerie_selection[0].name;
	document.getElementsByClassName("header_beschreibung")[0].innerHTML=inhalt;

	if(document.getElementsByClassName("VIP")[0].innerHTML=="Regular")
		document.getElementById("preis").innerHTML="<div class='price_subscription'>VIP: € "+replace_dot_comma(lingerie_selection[0].pricesubscription)+"</div><div class='price_regular'>Regulär: € "+replace_dot_comma(lingerie_selection[0].priceregular)+"</div>"
	else
		document.getElementById("preis").innerHTML="<div class='price_subscription'>VIP: € "+replace_dot_comma(lingerie_selection[0].pricesubscription)+"</div>"	
	
	document.getElementById("subtitle").innerHTML=lingerie_selection[0].descriptionshort;
	

	
	var i=0;


	if(lingerie_selection[0].wishlist=="yes")
		document.getElementsByClassName("wishlist_text")[0].innerHTML="Von der Wunschliste nehmen"
	else
		document.getElementsByClassName("wishlist_text")[0].innerHTML="Auf die Wunschliste nehmen"	
	
	if(resize_=="no")
		beschreibung_abrufen();
	warenkorb_ermitteln();
	
	getcolors();
	

   }
   
   
   
 window.onload=function datum_abrufen()
 {

	initial_setup("yes");
 }
 
 
 function getcolors()
 {
 	i=0;
 	box=""
	while(i<=colors.length-1)
	{

		if(colors[i].detaildatabase==lingerie_selection[0].name)
		{
			marker=i;
			box=box+"<div class='colors_huelle'><img src='"+colors[i].pic+"' class='colors' onclick='farbe_click("+i+")'></img></div>"
			i=colors.length;
			j=0;
			while(j<=colors.length-1)
			{
				if(marker!=j)
					box=box+"<div class='colors_huelle'><img src='"+colors[j].pic+"' class='colors' onclick='farbe_click("+j+")'></img></div>"
				j=j+1;
			}
		}
		i=i+1;
	} 	

	document.getElementsByClassName("color_auswahl")[0].innerHTML=box;
	if(box!="")
		document.getElementsByClassName("farbe_headline")[0].style.display="BLOCK"
	document.getElementsByClassName("colors_huelle")[0].style.backgroundColor="#E47272";
	
 }
 
 function farbe_click(id)
 {
 	windowwidth=window.innerWidth;
 	windowheight=window.innerHeight;
 		$.ajax({
		type: "GET",
		url: "/big_data_farbe_click/",
		dataType: "json",
		data: { "stylecode": lingerie_selection[0].stylecode,"colorcode": lingerie_selection[0].colorcode, "farbe":colors[id].colorcode,"windowheight":windowheight,"windowwidth":windowwidth},
		success: function(data) {

				window.location= "/overview/"+url_lingerie+"/"+colors[id].detaildatabase;

 		}
 	})
 }
 
 function bewertung_abrufen()
 {



				 addRatingWidget(buildShopItem(parseInt(gesamtbewertung[0].gesamtbewertung)/parseInt(gesamtbewertung[0].gesamtbewertunganzahl),0),parseInt(gesamtbewertung[0].gesamtbewertung)/parseInt(gesamtbewertung[0].gesamtbewertunganzahl));
			 addRatingWidget(buildShopItem(parseInt(gesamtbewertung[0].gesamtbewertung)/parseInt(gesamtbewertung[0].gesamtbewertunganzahl),1),parseInt(gesamtbewertung[0].gesamtbewertung)/parseInt(gesamtbewertung[0].gesamtbewertunganzahl));
 	if(bewertungen.length-1>=0)
 	{


			 
			 
		i=0;
		box=""

		while(i<=bewertungen.length-1)
		{

			box=box+"<div class='horizontale_linie'></div><div style='float:left;'><div class='bewertung_name'>Von "+bewertungen[i].namebewerter+"</div><div class='bewertung_datum'>am "+bewertungen[i].bewertungsdatum+"</div></div><br><div class='shop'></div><div class='bewertung_headline'>"+bewertungen[i].bewertungsheadline+"</div><div class='bewertung_text'>"+bewertungen[i].bewertungstext+"</div>"
			i=i+1;
		}
		
		document.getElementsByClassName("bewertungen")[0].innerHTML=box;
		
		i=0;
		while(i<=bewertungen.length-1)
		{
			addRatingWidget(buildShopItem(parseInt(bewertungen[i].bewertung),i+2),parseInt(bewertungen[i].bewertung)); 
			i=i+1;
		}	
	}
	else
		document.getElementsByClassName("bewertungsblock")[0].style.display="none";
	


 }
 

 
 
 function beschreibung_abrufen()
 {
	 var text="<br><br><br>"+lingerie_selection[0].description
	
	 



	 

	 document.getElementById("gerichte_info_box").innerHTML="<div style='margin-left:10px;margin-right:10px;'>"+text+"</div>";
	 
	var maxim= document.getElementsByClassName("button_detail");
	maxim[0].style.borderBottom="1.5px solid #E47272";
	maxim[1].style.borderBottom="0.5px solid #e6e6e6";

	

	
	 
 }
 
 
  function details_abrufen()
 {
	var text="<br><br><br>"+lingerie_selection[0].details

	 
	 document.getElementById("gerichte_info_box").innerHTML="<div style='margin-left:10px;margin-right:10px;'>"+text+"</div>";
	 
	 	var maxim= document.getElementsByClassName("button_detail");
	maxim[1].style.borderBottom="1.5px solid #E47272";
	maxim[0].style.borderBottom="0.5px solid #e6e6e6";

	 
 }
   
   
  function bewertungen_ansehen()
  {
  	window.location.href="#Kundenbewertungen"


 }  

 
 

  function daten_ermitteln()
 {

	 lingerie_selection=JSON.parse(document.getElementsByClassName("lingerie_offerings_daten")[0].innerHTML)
	 pricesforaddlpanty=JSON.parse(document.getElementsByClassName("pricesforaddlpanty")[0].innerHTML)
	 colors=JSON.parse(document.getElementsByClassName("colors")[0].innerHTML)

	 
	sizes=JSON.parse(document.getElementsByClassName("sizes")[0].innerHTML)

	if(document.getElementsByClassName("gesamtbewertung")[0].innerHTML!="")
		gesamtbewertung=JSON.parse(document.getElementsByClassName("gesamtbewertung")[0].innerHTML)


	bewertungen=JSON.parse(document.getElementsByClassName("bewertungen_detail")[0].innerHTML)



	var convert = function(convert){
		return $("<span />", { html: convert }).text();
		//return document.createElement("span").innerText;
	};
	



	
	 	windowwidth=window.innerWidth;
 	windowheight=window.innerHeight;

 		$.ajax({
		type: "GET",
		url: "/big_data_initial_input_detailed_page/",
		dataType: "json",
		data: { "stylecode": lingerie_selection[0].stylecode,"colorcode": lingerie_selection[0].colorcode,"windowheight":windowheight,"windowwidth":windowwidth},
		success: function(data) {		

		
				}
		})
	 


 }

		$(document).ready(function(){

			
			

		});






 function wishlist_abrufen(i) {

	if(lingerie_selection[0].wishlist=="yes")
		status="no"
	else
		status="yes"

	$.ajax({
		type: "GET",
		url: "/new_value_for_wishlist/",
		dataType: "json",
		data: { "stylecode": lingerie_selection[0].stylecode,"colorcode": lingerie_selection[0].colorcode,"status":status,"productgroup": lingerie_selection[0].productgroup },
		success: function(data2) {
		alert(status)
			if(status=="yes")
			{
					fbq('track', 'AddToWishlist', {
							      content_name: lingerie_selection[0].name, 
							      content_category: lingerie_selection[0].stylegroup,
							      content_ids: [lingerie_selection[0].stylecode+"_"+lingerie_selection[0].colorcode],
							      content_category: lingerie_selection[0].stylegroup,
							      value: lingerie_selection[0].pricesubscription,
							      currency: 'EUR' 
							    });
							alert("ASD")
			}  	
	 	windowwidth=window.innerWidth;
 	windowheight=window.innerHeight;

		
		 		$.ajax({
				type: "GET",
				url: "/big_data_wishlist_put/",
				dataType: "json",
				data: { "stylecode": lingerie_selection[0].stylecode,"colorcode": lingerie_selection[0].colorcode, "putinwishlist":lingerie_selection[0].wishlist,"windowheight":windowheight,"windowwidth":windowwidth},
				success: function(data) {			
							lingerie_selection[0].wishlist=status;
				
				
							if(lingerie_selection[0].wishlist=="yes")
								document.getElementsByClassName("wishlist_text")[0].innerHTML="Von Wunschliste nehmen"
							else
								document.getElementsByClassName("wishlist_text")[0].innerHTML="Zur Wunschliste hinzufügen"	
							
				
								
							document.getElementsByClassName("wishlist")[0].innerHTML=data2;
							load_wishlist()
							insert_wishlist_content_in_header();
							show_dropdown(1)
					}
				})

			


		}
	});
	

}


 
 
 
 
