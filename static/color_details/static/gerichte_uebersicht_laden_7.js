	var filter=new Array(5);
	var scroll_position_absolute;
   var gerichte = new Array(50);
	var cart=new Array(10);
	var cart_gesamt;
	var gewaehltes_datum;
	var auswahl_tag_final;
	var text_;
	var timeout_index;
	var warteliste_plz;
	var submit_plz_input;
	var gewaehlter_wochentag;
	var lingerie_selection;
	var ausgewaehlter_tag_;
		var gerichte_gruppen=new Array(4);
	var kalender
	var links;
	var filter;
	var colors;
   /* 
   
   
   
   
   i,0,0: Name
   i,1,var: Filter: 1) Vegan, 2) Vegetarisch, 3) Gluten-frei, 4) Laktosefrei, 5) Nussfrei, 6) Ei-frei*/
   
 window.onload=function datum_abrufen()
 {

	document.getElementById("eingabe1").value="";
	document.getElementsByClassName("filter_leer")[0].style.display="none";
	var jetzt = new Date();
	var Tag = jetzt.getDate();
	var Jahresmonat = jetzt.getMonth();
	var Monat = new Array("Januar", "Februar", "März", "April", "Mai", "Juni","Juli", "August", "September", "Oktober", "November", "Dezember");

	
	for (var i=0; i<=5; i++) 
	{
		filter[i]=new Array;
	}
	can_click="true";
	text_="";
	
	   
	 
 }
 





 
 

 
 
 
 
 
 
 function overlay() {
	
	
		var submit_plz_input=document.getElementById("eingabe1").value;
		if(isNaN(submit_plz_input) ==true || submit_plz_input.length<5)
		{
			document.getElementById("plz_fehler").innerHTML="Bitte eine fünfstellige PLZ angeben";
		}
		else
		{
			
			el = document.getElementById("overlay");
			
			el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
			document.getElementById("x-mask").style.opacity="0.4";
			document.getElementById("x-mask_2").style.opacity="0.4";
			
			document.getElementById("plz_fehler").innerHTML="";
			
		}


	
	
	


}


 function wishlist_abrufen(i) {

	if(lingerie_selection[i].wishlist=="yes")
		status="no"
	else
		status="yes"

	$.ajax({
		type: "GET",
		url: "/hello/new_value_for_wishlist/",
		dataType: "json",
		data: { "stylecode": lingerie_selection[i].stylecode,"colorcode": lingerie_selection[i].colorcode,"status":status },
		success: function(data2) {


		 		windowwidth=window.innerWidth;
		 	windowheight=window.innerHeight;

		 		$.ajax({
				type: "GET",
				url: "/hello/big_data_wishlist_click_main_page/",
				dataType: "json",
				data: { "windowheight":windowheight,"windowwidth":windowwidth,"stylecode":lingerie_selection[i].stylecode,"colorcode":lingerie_selection[i].colorcode,"position":lingerie_selection[i].position,"putinwishlist":status},
				success: function(data) {			

								lingerie_selection[i].wishlist=status;

								if(status=="yes")
									wishlist_abrufen_markieren(i)
								else
									wishlist_abrufen_entmarkieren(i)

								document.getElementsByClassName("wishlist")[0].innerHTML=data2;
								load_wishlist()
								
								insert_wishlist_content_in_header();
								show_dropdown(1)
					
								if(url_lingerie=="")
								{
					
						 	  			$.ajax({
									type: "GET",
									url: "/hello/content_abrufen/",
									dataType: "json",
									data: { "name":"","group1":"Wunschliste","group2":"","group3":"","color": "","size":"",'filter_style':"",'filter_color':"",'filter_size':"",'filter_padding':"",'filter_feature':""},
									success: function(data) {	
					
						
										document.getElementsByClassName("lingerie_data")[0].innerHTML=data
										
										lingerie_selection_laden();
										
									}
									})
								}
						}
				})
				
			


		}
	});
	

}






	
 
 function validate(evt) {
  var theEvent = evt || window.event;
  var key = theEvent.keyCode || theEvent.which;
  key = String.fromCharCode( key );
  var regex = /[0-9]|\./;
  if( !regex.test(key) && theEvent.keyCode!=8) {
    theEvent.returnValue = false;
    if(theEvent.preventDefault) theEvent.preventDefault();
  }
}

 
 
 
 
 
 
 
function mouse_effect_in(clicked_id) 
{


	var maxim= document.getElementsByClassName("box_zusatz_2");

	if(verfuegbarkeits_check(gericht_id_suchen_id(clicked_id))=="0 Gerichte übrig" || document.getElementsByClassName("anzahl_warenkorb")[clicked_id].innerHTML=="10 X IM WARENKORB")
	{

		maxim[clicked_id].style.backgroundColor="#4E4E4E";
		maxim[clicked_id].style.color="#ffffff";
	}
	else
	{
		
		maxim[clicked_id].style.backgroundColor="#e65c00";
		maxim[clicked_id].style.color="#ffffff";
	}
		
		


 }
 
 



 
 
 
 
 

 
 
 





 

 
 
  function overlay() {
	
	
		var submit_plz_input=document.getElementById("eingabe1").value;
		if(isNaN(submit_plz_input) ==true || submit_plz_input.length<5)
		{
			document.getElementById("plz_fehler").innerHTML="Bitte eine fünfstellige PLZ angeben";
		}
		else
		{
			
			el = document.getElementById("overlay");

			el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
			document.getElementById("x-mask").style.opacity="0.4";
			document.getElementById("x-mask_2").style.opacity="0.4";
			document.getElementById("plz_fehler").innerHTML="";
			
		}

}




 

 
 function replace_dot_comma(zahl)
{
	zahl=zahl.toFixed(2)
	zahl=zahl.toString()
	return zahl.replace(".", ",");
}


 
 function filter_click(id)
 {


		
	i=0
	style_selectedIndex=document.getElementsByClassName("style_selection")[0].selectedIndex
	color_selectedIndex=document.getElementsByClassName("color_selection")[0].selectedIndex
	padding_selectedIndex=document.getElementsByClassName("padding_selection")[0].selectedIndex
	feature_selectedIndex=document.getElementsByClassName("feature_selection")[0].selectedIndex
	sizes_selectedIndex=document.getElementsByClassName("sizing_selection")[0].selectedIndex
	
	if(style_selectedIndex!=0 || color_selectedIndex!=0 || padding_selectedIndex!=0 || feature_selectedIndex!=0 || sizes_selectedIndex!=0)
		document.getElementsByClassName("filter_aufheben")[0].style.display="block";
	while(i<=4)
	{
		if(i==0)
			if(style_selectedIndex!=0)
				filter_style=document.getElementsByClassName("style_selection")[0].options[style_selectedIndex].innerHTML
			else
				filter_style=""
				
		if(i==1)
			if(color_selectedIndex!=0)
				filter_color=document.getElementsByClassName("color_selection")[0].options[color_selectedIndex].innerHTML
			else
				filter_color=""

		if(i==2)
			if(padding_selectedIndex!=0)
				filter_padding=document.getElementsByClassName("padding_selection")[0].options[padding_selectedIndex].innerHTML
			else
				filter_padding=""			
		if(i==3)
			if(feature_selectedIndex!=0)
				filter_feature=document.getElementsByClassName("feature_selection")[0].options[feature_selectedIndex].innerHTML
			else
				filter_feature=""	
		if(i==4)
			if(sizes_selectedIndex!=0)
				filter_sizes=document.getElementsByClassName("sizing_selection")[0].options[sizes_selectedIndex].innerHTML
			else
				filter_sizes=""	
		i=i+1	
	}
	
	

 		document.getElementsByClassName("background_loading_products")[0].style.opacity="0.2"
 		document.getElementsByClassName("container_gerichte")[0].style.pointerEvents="none"
	
		if(url_lingerie=="Mein Showroom")
			url_lingerie_=url_lingerie
		else
			url_lingerie_="lingerie"

 	  			$.ajax({
			type: "GET",
			url: "/hello/content_abrufen/",
			dataType: "json",
			data: { "name":"","group1":url_lingerie_,"group2":"","group3":"","color": "","size":"",'filter_style':filter_style,'filter_color':filter_color,'filter_size':filter_sizes,'filter_padding':filter_padding,'filter_feature':filter_feature},
			success: function(data) {	


				lingerie_selection=JSON.parse(data)
					
					$.ajax({
							type: "GET",
							url: "/hello/filter_abrufen/",
							dataType: "json",
							data: { "group1":url_lingerie_,'filter_style':filter_style,'filter_color':filter_color,'filter_size':filter_sizes,'filter_padding':filter_padding,'filter_feature':filter_feature,'click_last':id},
							success: function(data) {	
							
							
		
					 		windowwidth=window.innerWidth;
					 	windowheight=window.innerHeight;
					
					 		$.ajax({
							type: "GET",
							url: "/hello/big_data_filter_click_main_page/",
							dataType: "json",
							data: { "windowheight":windowheight,"windowwidth":windowwidth,"filter":filter_style+"_"+filter_color+"_"+filter_sizes+"_"+filter_padding+"_"+filter_feature},
							success: function(data2) {	
				
				
									
													filter=data
					
													
													lingerie_laden()
					
													document.getElementsByClassName("style_selection")[0].selectedIndex=style_selectedIndex;
													document.getElementsByClassName("color_selection")[0].selectedIndex=color_selectedIndex;
													document.getElementsByClassName("padding_selection")[0].selectedIndex=padding_selectedIndex;
													document.getElementsByClassName("feature_selection")[0].selectedIndex=feature_selectedIndex;
													document.getElementsByClassName("sizing_selection")[0].selectedIndex=sizes_selectedIndex;

											 		document.getElementsByClassName("background_loading_products")[0].style.opacity="1.0"
											 		document.getElementsByClassName("container_gerichte")[0].style.pointerEvents="auto"
										}
							})
							
													
													
							
									}
							})
			
					}
			})
 }

 
 function search_field_sidebar_uebersicht()
 {
 	document.getElementsByClassName("filter_feld")[0].style.width="90%";
 	document.getElementsByClassName("schliessen_searchbox_uebersicht")[0].style.display="block";
 		
 }

 
 
 function leave_search_overview()
{

	if(document.getElementsByClassName("filter_feld")[0].value =="" && document.getElementsByClassName("filter_feld")[0].style.width=="90%")
	{
		
		document.getElementsByClassName("filter_feld")[0].style.width="200px";
		document.getElementsByClassName("schliessen_searchbox_uebersicht")[0].style.display="none";
		schliessen_searchbox_uebersicht();
	}
} 

function schliessen_searchbox_uebersicht()
{

 	  			$.ajax({
			type: "GET",
			url: "/hello/content_abrufen/",
			dataType: "json",
			data: { "name":"","group1":"lingerie","group2":"","group3":"","color": "","size":"",'filter_style':"",'filter_color':"",'filter_size':"",'filter_padding':"",'filter_feature':""},
			success: function(data) {	

				lingerie_selection=JSON.parse(data)
				lingerie_laden()
				document.getElementsByClassName("filter_feld")[0].value="";
				leave_search_overview();
			}
			});
				
}

function full_text_search_uebersicht()
{

			 $.ajax({
			type: "GET",
			url: "/hello/full_text_search/",
			dataType: "json",
			data: { "search_item": document.getElementsByClassName("filter_feld")[0].value  },
			success: function(data) {
					lingerie_selection=data

					document.getElementsByClassName("main_uebersicht")[0].innerHTML =show_lingerie_details()

				
			},
			error:function() {

					

				
			}
			
			})
	
}
 
 
 
 function lingerie_laden()
 {

	document.getElementsByClassName("cart")[0].style.backgroundImage="url('/static/Cart-open.PNG')";

	



		 i=0;
		 box=""

	i=0;
	
	while(i<=links.length-1)
	{

		if(links[i].name==url_lingerie)
			 box=box+"<img src='"+links[i].pictureoverallsrc+"'  class='overall_picture'><div class='picture_subtitle' ><p style='margin-top:0px;'><p style='font-weight:bold;'>"+links[i].headlineoverall+"</p><p class='picture_subsubtitle'>"+links[i].subtitleoverall+"</p></p></div></img>"		
		
		i=i+1;	
	}
		
	if(url_lingerie!="Wunschliste" && url_lingerie!="Geschenkkarten")
	{
		
		if(url_lingerie!="Mein Showroom")
		{
		 	box=box+"<div class='filter_uebersicht'>"
		 	box=box+"<input class='filter_feld' name='search' placeholder='Suchen..' onfocus='search_field_sidebar_uebersicht()' onblur='leave_search_overview()' oninput='full_text_search_uebersicht()'></input><img class='schliessen_searchbox_uebersicht' src='/static/x.png' width='15' onclick='schliessen_searchbox_uebersicht();' height='15'/></img>"
		 	box=box+"</div>"
		}
		 				
		box=box+"<div class='main_uebersicht'>"
		box=box+"<div ><div class='filter_headline'>Filtern nach:</div>"
		box=box+"<div style='float:left'><select class='style_selection'  onchange='filter_click(0)'>";
		i=0;
		box=box+"<option>Stil-Auswahl</option>";
		while(i<=filter.length-1)
		{

			if(filter[i].group=="Styles")
				if(filter[i].show=="true")
					box=box+"<option>"+filter[i].name+"</option>"
				else
					box=box+"<option disabled='true'>"+filter[i].name+"</option>"
				
			
			i=i+1
		}
		
		


		 
		 box=box+"</select>"


		box=box+"<select class='color_selection'  onchange='filter_click(1)'>";
		  

		box=box+"<option>Farb-Auswahl</option>";
		i=0
		while(i<=filter.length-1)
		{

			if(filter[i].group=="Color")
				if(filter[i].show=="true")
					box=box+"<option>"+filter[i].name+"</option>"
				else
					box=box+"<option disabled='true'>"+filter[i].name+"</option>"
			
			i=i+1
		}
		 
		 
		 box=box+"</select>"
		 

		if(url_lingerie!="Slips") 
		{
			box=box+"<select class='feature_selection'  onchange='filter_click(3)'>";
			  
			i=0;
			box=box+"<option>Feature-Auswahl</option>";
			while(i<=filter.length-1)
			{
	
				if(filter[i].group=="Feature")
					if(filter[i].show=="true")
						box=box+"<option>"+filter[i].name+"</option>"
					else
						box=box+"<option disabled='true'>"+filter[i].name+"</option>"
					
				
				i=i+1
			}
			 
			 
			 box=box+"</select>"
		}
		
		
		if(url_lingerie!="Slips") 
		{
		 
			box=box+"<select class='padding_selection' onchange='filter_click(2)'>";
			  
	
			box=box+"<option>Padding-Auswahl</option>";
			i=0
			while(i<=filter.length-1)
			{
	
				if(filter[i].group=="Padding")
					if(filter[i].show=="true")
						box=box+"<option>"+filter[i].name+"</option>"
					else
						box=box+"<option disabled='true'>"+filter[i].name+"</option>"
				
				i=i+1
			}
	
			 
			 
			 box=box+"</select>"
		}
		 
		 		 

		box=box+"<select class='sizing_selection'  onchange='filter_click(4)'>";
		  
		i=0;
		box=box+"<option>Größen-Auswahl</option>";
		while(i<=filter.length-1)
		{

			if(filter[i].group=="Sizes")
				if(filter[i].show=="true")
					box=box+"<option>"+filter[i].name+"</option>"
				else
					box=box+"<option disabled='true'>"+filter[i].name+"</option>"
				
			
			i=i+1
		}
		 
		 box=box+"</select></div>"
		 
		 box=box+"<div class='filter_aufheben'  onclick='filter_aufheben()'>Filter aufheben</div></div><br><br><br>"
		 
		}
		else
			box=box+"<div class='main_uebersicht'></div>"

		box=box+"<div class='background_loading_products'>"+show_lingerie_details()+"</div>";

			document.getElementsByClassName("container_gerichte")[0].innerHTML=box+"</div>"
			

 }
 
 
 window.onresize=function(event){

 	document.getElementsByClassName("background_loading_products")[0].innerHTML =show_lingerie_details()

 }
 
 function filter_aufheben()
 {
 	document.getElementsByClassName("style_selection")[0].selectedIndex=0;
	document.getElementsByClassName("color_selection")[0].selectedIndex=0;
	if(url_lingerie!="Slips") 
	{
		document.getElementsByClassName("padding_selection")[0].selectedIndex=0;
		document.getElementsByClassName("feature_selection")[0].selectedIndex=0;
	}
	document.getElementsByClassName("sizing_selection")[0].selectedIndex=0;
	 filter_click(0)
	 document.getElementsByClassName("filter_aufheben")[0].style.display="none";
	 
	 
	 
 }
 
 
 
 function show_lingerie_details()
 {

 			 	 		 i=0;
		 zaehler=0;
		 box="";
	array_elemente=0;
	  var pics =[]
		while (i<=lingerie_selection.length-1)
		{
					if(lingerie_selection[i].wishlist=="yes")
						herz="herz_paleo.png"
					else
						herz="herz_grau.png"
					
					
					var arr1 = lingerie_selection[i].pic.split(",");
						
	
					for (j = 0; j < arr1.length; j++) {
						pics[j]=arr1[j].split(",");
					}  
					
					
					j=0;
					box_color=""
					zaehler_2=0;
								
					while(j<=colors.length-1)
					{
						
						
							if(colors[j].name==lingerie_selection[i].name)
							{

								marker=j;
								box_color=box_color+"<div class='colors_huelle'><img src='"+colors[j].pic+"' class='colors' onclick='farbe_click("+j+","+i+")'></img></div>"
								zaehler_2=zaehler_2+1;
		
								
								j=colors.length;
								k=0;
								while(k<=colors.length-1)
								{


									if(marker!=k && colors[k].style==lingerie_selection[i].stylecode)
									{
										box_color=box_color+"<div class='colors_huelle'><img src='"+colors[k].pic+"' class='colors' onclick='farbe_click("+k+","+i+")'></img></div>"
										zaehler_2=zaehler_2+1;
									}
									k=k+1;
								}
							}
							j=j+1;

					} 	
					if(zaehler_2==1)
						box_color="";
					
					
					if(zaehler==0)
						box=box+"<div class='block'>\r";
					box=box+"<div class='box_1'><div class='box_1_herz'></div><div ><div ><img class='image_box' src='"+pics[0]+"' onclick='detail_page("+i+")'><img class='herz' src='/static/"+herz+"' onclick='wishlist_abrufen("+i+")' onmouseenter='wishlist_abrufen_markieren("+i+")' onmouseleave='wishlist_abrufen_entmarkieren("+i+")'></img></img></div></div><div class='box_erste_ebene'><div class='gericht_auswahl_text' >"+lingerie_selection[i].name+"</div>"
					
					
					if(document.getElementsByClassName("VIP")[0].innerHTML=="regular")
						box=box+"<div class='price_subscription'>€ "+replace_dot_comma(lingerie_selection[i].pricesubscription)+" VIP</div></div><div class='box_zweite_ebene'><div class='short_description'>"+lingerie_selection[i].descriptionshort+" </div><div class='price_regular'>€ "+replace_dot_comma(lingerie_selection[i].priceregular)+" Reg</div></div><div class='box_dritte_ebene'><div class='color_auswahl'>"+box_color+"</div>	</div></div>\r";
					else
						box=box+"<div class='price_subscription'>€ "+replace_dot_comma(lingerie_selection[i].pricesubscription)+" VIP</div></div><div class='box_zweite_ebene'><div class='short_description'>"+lingerie_selection[i].descriptionshort+" </div></div><div class='box_dritte_ebene'><div class='color_auswahl'>"+box_color+"</div>	</div></div>\r";
			
					
					zaehler=zaehler+1;

					if(window.innerWidth<=420)
					{
						if(zaehler>=2)
						{
							box=box+"<span class='stretch'></span></div>\r"
							zaehler=0;
						}
					}
					else
					{
						if(window.innerWidth>=421 && window.innerWidth<=1199)
						{
							if(zaehler>=3)
							{
								box=box+"<span class='stretch'></span></div>\r"
								zaehler=0;
							}
						}		

						else
						{
							if(window.innerWidth>=1200)
							{
								
								if(zaehler>=4)
								{
									box=box+"<span class='stretch'></span></div>\r"
									zaehler=0;
								}
							}	
						}
					}
					
						

//<div class='groessen'>Größen: "+lingerie_selection[i].sizerange+" </div>					

		i=i+1;
	}	

	return box;
	

 }
 
 
  function farbe_click(color_id,lingerie_id)
 {
	windowwidth=window.innerWidth;
 	windowheight=window.innerHeight;

 		$.ajax({
		type: "GET",
		url: "/hello/big_data_color_click_main_page/",
		dataType: "json",
		data: { "windowheight":windowheight,"windowwidth":windowwidth,"stylecode":lingerie_selection[lingerie_id].stylecode,"colorcode":lingerie_selection[lingerie_id].colorcode,"farbe":colors[color_id].colorcode,"position":lingerie_selection[lingerie_id].position},
		success: function(data) {		
				window.location= "/hello/overview/"+url_lingerie+"/"+colors[color_id].name;
		
				}
		})


 
 }
 
 function detail_page(i)
 {
 		windowwidth=window.innerWidth;
 	windowheight=window.innerHeight;

 		$.ajax({
		type: "GET",
		url: "/hello/big_data_picture_click_main_page/",
		dataType: "json",
		data: { "windowheight":windowheight,"windowwidth":windowwidth,"stylecode":lingerie_selection[i].stylecode,"colorcode":lingerie_selection[i].colorcode,"position":lingerie_selection[i].position},
		success: function(data) {	


 				window.location.href=lingerie_selection[i].name;
 		}
 		})
 }
 
 function wishlist_abrufen_markieren(i)
 {
 	document.getElementsByClassName("herz")[i].src='/static/herz_paleo.png'
 	
 }
  function wishlist_abrufen_entmarkieren(i)
 {
 	if(lingerie_selection[i].wishlist=="no")
 		document.getElementsByClassName("herz")[i].src='/static/herz_grau.png'
 	
 }
 

 


		



 

function replaceAll(str, find, replace) {
  return str.replace(new RegExp(find, 'g'), replace);
}


function test(data)
{
	//data_2=data.replace("&#39;","")
	
	data=replaceAll(data,"&quot;",'"');


	var text = '{ "employees" : [' +
'{ "firstName":"John" , "lastName":"Doe" },' +
'{ "firstName":"Anna" , "lastName":"Smith" },' +
'{ "firstName":"Peter" , "lastName":"Jones" } ]}';



	a=JSON.parse(data);


}


function lingerie_selection_laden()
{

	if(document.getElementsByClassName("lingerie_data")[0].innerHTML!="Quiz")
	{
		if(document.getElementsByClassName("lingerie_data")[0].innerHTML!="")
			lingerie_selection=JSON.parse(document.getElementsByClassName("lingerie_data")[0].innerHTML)
		if(document.getElementsByClassName("filter")[0].innerHTML!="")
			filter=JSON.parse(document.getElementsByClassName("filter")[0].innerHTML)

		if(document.getElementsByClassName("colors")[0].innerHTML!="")
			colors=JSON.parse(document.getElementsByClassName("colors")[0].innerHTML)
		if(document.getElementsByClassName("lingerie_data")[0].innerHTML!="")
			lingerie_laden();

	}
	else
		quiz_laden();

	
}


function initialize()
{
	document.getElementsByClassName("filter_aufheben")[0].style.display="none";
	windowwidth=window.innerWidth;
 	windowheight=window.innerHeight;
 	

 		$.ajax({
		type: "GET",
		url: "/hello/big_data_initial_input_main_page/",
		dataType: "json",
		data: { "windowheight":windowheight,"windowwidth":windowwidth},
		success: function(data) {		

		
				}
		})
	 
	
}






 
 
 
 
