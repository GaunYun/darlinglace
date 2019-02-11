	var filter=new Array(5);
	var scroll_position_absolute;
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
	var kalender
	var links;
	var filter;
	var colors;
   
   
   
   
   
   
 window.onload=function datum_abrufen()
 {





	
	for (var i=0; i<=5; i++) 
	{
		filter[i]=new Array;
	}
	can_click="true";
	text_="";
	
	   
	 
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
	if(url_lingerie!="Slips")
		padding_selectedIndex=document.getElementsByClassName("padding_selection")[0].selectedIndex
	else
		padding_selectedIndex=0
		
	sizes_selectedIndex=document.getElementsByClassName("sizing_selection")[0].selectedIndex
	
	

	if(style_selectedIndex!=0 || color_selectedIndex!=0 || padding_selectedIndex!=0 || sizes_selectedIndex!=0)
		document.getElementsByClassName("filter_aufheben")[0].style.display="block";
	else
		id=-1;

	while(i<=3)
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
		if(url_lingerie!="Slips")
		{
			if(i==2)
				if(padding_selectedIndex!=0)
					filter_padding=document.getElementsByClassName("padding_selection")[0].options[padding_selectedIndex].innerHTML
				else
					filter_padding=""		
		}
		else
			filter_padding=""
		if(i==3)
			if(sizes_selectedIndex!=0)
				filter_sizes=document.getElementsByClassName("sizing_selection")[0].options[sizes_selectedIndex].innerHTML
			else
				filter_sizes=""	
		i=i+1	
	}
	
	

 	
	
		if(url_lingerie=="Dein Showroom")
			url_lingerie_=url_lingerie
		else
			if(url_lingerie=="Slips")
				url_lingerie_="panties"
			else
				url_lingerie_="lingerie"
			windowwidth=window.innerWidth;
			windowheight=window.innerHeight;
			
			document.getElementsByClassName("background_loading_products")[0].style.opacity="0.4"
 			document.getElementsByClassName("container_gerichte")[0].style.pointerEvents="none"			
  			$.ajax({
  				timeout:15000,
	 			error: function(){	
	 					document.getElementsByClassName("background_loading_products")[0].style.opacity="1"
 						document.getElementsByClassName("container_gerichte")[0].style.pointerEvents="auto"	},
			type: "GET",
			url: "/content_abrufen/",
			dataType: "json",
			data: {"windowheight":windowheight,"windowwidth":windowwidth, "name":"","group1":url_lingerie_,"group2":"","group3":"","color": "","size":"",'filter_style':filter_style,'filter_color':filter_color,'filter_size':filter_sizes,'filter_padding':filter_padding},
			success: function(data) {	
			
				feedback=JSON.parse(data)
	
				lingerie_selection=JSON.parse(feedback[0].lingerieselection)
				filter=JSON.parse(feedback[0].filter)
					
				lingerie_laden()
				if(id==-1)
					document.getElementsByClassName("filter_aufheben")[0].style.display="none";
				select_filter()

		 		document.getElementsByClassName("background_loading_products")[0].style.opacity="1.0"
		 		document.getElementsByClassName("container_gerichte")[0].style.pointerEvents="auto"

			}
		})
 }
 
 
 function select_filter()
 {
 		i=0;
 		document.getElementsByClassName("style_selection")[0].selectedIndex=0;
 		document.getElementsByClassName("color_selection")[0].selectedIndex=0;
 		if(url_lingerie!="Slips")
 			document.getElementsByClassName("padding_selection")[0].selectedIndex=0;
 		document.getElementsByClassName("sizing_selection")[0].selectedIndex=0;
 		
 		document.getElementsByClassName("filter_aufheben")[0].style.display="none";
 		zaehler_style=1;
 		zaehler_padding=1;
 		zaehler_color=1;
 		zaehler_sizes=1;

 		while(i<=filter.length-1)
		{

			if(filter[i].group=="Styles")
			{
				if(filter[i].selected=="true")	
				{
					document.getElementsByClassName("filter_aufheben")[0].style.display="block";
					document.getElementsByClassName("style_selection")[0].selectedIndex=zaehler_style
				}
				zaehler_style=zaehler_style+1
			}

			if(filter[i].group=="Color")
			{
				if(filter[i].selected=="true")	
				{
					document.getElementsByClassName("filter_aufheben")[0].style.display="block";
					document.getElementsByClassName("color_selection")[0].selectedIndex=zaehler_color
				}
				zaehler_color=zaehler_color+1
			}
			
			if(filter[i].group=="Padding")
			{
				if(filter[i].selected=="true")	
				{
					document.getElementsByClassName("filter_aufheben")[0].style.display="block";
					document.getElementsByClassName("padding_selection")[0].selectedIndex=zaehler_padding
				}
				zaehler_padding=zaehler_padding+1
			}
			
			if(filter[i].group=="Sizes")
			{
				if(filter[i].selected=="true")	
				{
					document.getElementsByClassName("filter_aufheben")[0].style.display="block";
					document.getElementsByClassName("sizing_selection")[0].selectedIndex=zaehler_sizes
				}
				zaehler_sizes=zaehler_sizes+1
			}
			

						
			i=i+1
						
						
			}

	
 	
 	
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
			url: "/content_abrufen/",
			dataType: "json",
			data: { "name":"","group1":"lingerie","group2":"","group3":"","color": "","size":"",'filter_style':"",'filter_color':"",'filter_size':"",'filter_padding':""},
			success: function(data) {	

				feedback=JSON.parse(data)
	
				lingerie_selection=JSON.parse(feedback[0].lingerieselection)
				filter=JSON.parse(feedback[0].filter)
				lingerie_laden()
				document.getElementsByClassName("filter_feld")[0].value="";
				leave_search_overview();
				document.getElementsByClassName("filter_aufheben")[0].style.display="none";
			}
			});
				
}

function full_text_search_uebersicht()
{

			 $.ajax({
			type: "GET",
			url: "/full_text_search/",
			dataType: "json",
			data: { "search_item": document.getElementsByClassName("filter_feld")[0].value  },
			success: function(data) {
					lingerie_selection=data

					document.getElementsByClassName("background_loading_products")[0].innerHTML =show_lingerie_details()
					update_wishlist_on_lingerie()
					document.getElementsByClassName("filter_boxes")[0].style.opacity="0.4"
		 			document.getElementsByClassName("filter_boxes")[0].style.pointerEvents="none"		
					

				
			}
			})
	
}


function update_wishlist_on_lingerie()
{
 		 j=0;
		while (j<=lingerie_selection.length-1)
		{	
	 		 i=0;
	 		 markieren="false"
			while (i<=wishlist.length-1)
			{	
			
				if(wishlist[i].stylecode==lingerie_selection[j].stylecode && wishlist[i].colorcode==lingerie_selection[j].colorcode)
					markieren="true"
				i=i+1;
			}
			
			if(markieren=="true")
			{
				wishlist_abrufen_markieren(j)
			}
			else
			{
				wishlist_abrufen_entmarkieren(j)
			}
			
			j=j+1
		}				
}





function showroom_bearbeiten()
{
	
	quiz_laden();
}
 
 
 
function get_mein_showroom_results()
{
	
	document.getElementById("mein_showroom").style.display="block"
		document.getElementById("brustform").innerHTML
		
		document.getElementsByClassName("brustform_picture")[parseInt(document.getElementById("brustform").innerHTML)].style.display="block"
	if(document.getElementById("cupproblem").innerHTML==0)
		document.getElementById("quiz_results_passform_probleme_1_subtext").innerHTML="Zu groß"
	if(document.getElementById("cupproblem").innerHTML==1)
		document.getElementById("quiz_results_passform_probleme_1_subtext").innerHTML="Zu klein"
	if(document.getElementById("cupproblem").innerHTML==2)
	{
		document.getElementById("quiz_results_passform_probleme_1").style.display="none"	
		document.getElementsByClassName("vertical_line_passform_probleme")[0].style.display="none"		
		
	}



	if(document.getElementById("bandproblem").innerHTML==0)
		document.getElementById("quiz_results_passform_probleme_2_subtext").innerHTML="Zu locker"
	if(document.getElementById("bandproblem").innerHTML==1)
		document.getElementById("quiz_results_passform_probleme_2_subtext").innerHTML="Zu eng"
	if(document.getElementById("bandproblem").innerHTML==2)
	{
		document.getElementById("quiz_results_passform_probleme_2").style.display="none"		
		document.getElementsByClassName("vertical_line_passform_probleme")[1].style.display="none"		
		
	}		
		
	if(document.getElementById("strapproblem").innerHTML==0)
		document.getElementById("quiz_results_passform_probleme_3_subtext").innerHTML="Schneiden ein"
	if(document.getElementById("strapproblem").innerHTML==1)
		document.getElementById("quiz_results_passform_probleme_3_subtext").innerHTML="Rutschen"
	if(document.getElementById("strapproblem").innerHTML==2)
		document.getElementById("quiz_results_passform_probleme_3").style.display="none"	
		

	if(document.getElementById("recommendedsizetext").innerHTML==0)
		document.getElementById("quiz_results_right_subtext").innerHTML="Du trägst die richtige Größe."	
	if(document.getElementById("recommendedsizetext").innerHTML==1)
		document.getElementById("quiz_results_right_subtext").innerHTML="Versuche unsere BHs in einer größeren Cupgröße, um Dir etwas mehr Platz zu geben."		

	if(document.getElementById("recommendedsizetext").innerHTML==2)
		document.getElementById("quiz_results_right_subtext").innerHTML="Versuche unsere BHs in einer kleineren Cupgröße, damit die Cups optimal anliegen."		
	if(document.getElementById("recommendedsizetext").innerHTML==3)
		document.getElementById("quiz_results_right_subtext").innerHTML="Versuche unsere BHs in der nächstgrößeren Bandweite, damit das Band weniger einengt. Mit steigender Bandweite werden auch die Cups größer, daher empfehlen wir Dir bei der Cupgröße einen Buchstaben kleiner zu wählen."	
	if(document.getElementById("recommendedsizetext").innerHTML==4)
		document.getElementById("quiz_results_right_subtext").innerHTML="Versuche unsere BHs in der nächstgrößeren Bandweite, damit das Band weniger einengt. Mit steigender Bandweite werden auch die Cups größer, daher geben Dir Cups mit dem gleichen Buchstaben mehr Platz."			
	if(document.getElementById("recommendedsizetext").innerHTML==5)
		document.getElementById("quiz_results_right_subtext").innerHTML="Versuche unsere BHs in einer kleineren Bandweite, damit das Band optimal anliegt und auf dem letzten Haken geschlossen werden kann. Bei einer kleineren Bandweite fallen auch die Cups kleiner aus."
	
	if(document.getElementById("recommendedsizetext").innerHTML==6)
		document.getElementById("quiz_results_right_subtext").innerHTML="Versuche unsere BHs in einer kleineren Bandweite, damit das Band optimal anliegt und auf dem letzten Haken geschlossen werden kann. Da bei einer kleineren Bandweite die Cups kleiner ausfallen, solltest Du einen größeren Buchstaben bei der Cupgröße wählen."	
	document.getElementById("quiz_results_right_headline_subtext").innerHTML	="Deine Größe bei Darling Lace ist "+document.getElementById("recommendedbandsize").innerHTML+document.getElementById("recommendedcupsize").innerHTML
	
	document.getElementsByClassName("passform_probleme")[0].innerHTML="DEINE PASSFORM PROBLEME MIT "+document.getElementById("currentbandsize").innerHTML+document.getElementById("currentcupsize").innerHTML
	
		
}
 
 
 function lingerie_laden()
 {



	



		 i=0;
		 box=""

	i=0;
	
	

					
	while(i<=links.length-1)
	{

		if(links[i].name==url_lingerie)
		{
			if(url_lingerie=="Mein Showroom")
			 	get_mein_showroom_results()
			 else
			 {
			 	box=box+"<div class='box_overall_picture'><img src='"+links[i].pictureoverallsrc+"' class='overall_picture'><div class='picture_subtitle' ><div class='picture_subtitle_headline'>"+links[i].headlineoverall+"</div><p class='picture_subsubtitle'>"+links[i].subtitleoverall+"</p></div></img></div>"
			 document.getElementById("sub_header_product_page").innerHTML=	links[i].group3;
			 }
		}		
		
		i=i+1;	
	}
	
	
	if(url_lingerie!="Wunschliste" && url_lingerie!="Geschenkkarten")
	{
		

		 	
		if(url_lingerie!="Mein Showroom")
		{		 	
			box=box+"<div class='filter_uebersicht'>"
			box=box+"<img class='schliessen_searchbox_uebersicht' src='/static/x.png' width='15' onclick='schliessen_searchbox_uebersicht();' height='15'/></img><input class='filter_feld' name='search' placeholder='Suchen...' onfocus='search_field_sidebar_uebersicht()' onblur='leave_search_overview()' oninput='full_text_search_uebersicht()'></input>"
		}

	 	box=box+"</div>"
		 				
		box=box+"<div class='main_uebersicht'>"
		
		

		box=box+"<div ><br><br>"
		if(url_lingerie!="Mein Showroom")
			box=box+"<div class='filter_boxes'>"
		else
			box=box+"<div class='filter_boxes' style='display:none'>"
		box=box+"<select class='style_selection'  onchange='filter_click(0)'>";
		i=0;
		box=box+"<option>Stil</option>";
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
		  

		box=box+"<option>Farbe</option>";
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
		 
			box=box+"<select class='padding_selection' onchange='filter_click(2)'>";
			  
	
			box=box+"<option>Fütterung</option>";
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
		box=box+"<option>Größen</option>";
		if(url_lingerie!="Slips")
			anpassung=5
		else
			anpassung=1
		while(i<=filter.length-anpassung)
		{

			if(filter[i].group=="Sizes")
				if(filter[i].show=="true")
					box=box+"<option>"+filter[i].name+"</option>"
				else
					box=box+"<option disabled='true'>"+filter[i].name+"</option>"
				
			
			i=i+1
		}
		 
		 box=box+"</select>"

		 box=box+"<div class='box_filter'><div class='filter_aufheben'  onclick='filter_aufheben()'>Filter aufheben</div></div></div></div>"
		 
	}
	else
		box=box+"<div class='main_uebersicht' style='marginBottom:100px;margin-top:30px;'></div><br><br><br><br><br>"

	box=box+"<div class='background_loading_products'>"+show_lingerie_details()+"</div>";

	document.getElementsByClassName("container_gerichte")[0].innerHTML=box+"</div>"
	update_wishlist_on_lingerie()
	if(document.getElementById("filter_style").innerHTML!="")
		document.getElementsByClassName("style_selection")[0].value=document.getElementById("filter_style").innerHTML
	if(document.getElementById("filter_color").innerHTML!="")
		document.getElementsByClassName("color_selection")[0].value=document.getElementById("filter_color").innerHTML
		
	if(document.getElementById("filter_padding").innerHTML!="")
		document.getElementsByClassName("padding_selection")[0].value=document.getElementById("filter_padding").innerHTML
	if(document.getElementById("filter_size").innerHTML!="")
		document.getElementsByClassName("sizing_selection")[0].value=document.getElementById("filter_size").innerHTML
		
		
		i=0;
		while (i<=lingerie_selection.length-1)
		{
			
			pre_load_heart_images(i)
			
			i=i+1;
		}

 }

 function filter_aufheben()
 {
 	document.getElementsByClassName("style_selection")[0].selectedIndex=0;
	document.getElementsByClassName("color_selection")[0].selectedIndex=0;
	if(url_lingerie!="Slips") 
	{
		document.getElementsByClassName("padding_selection")[0].selectedIndex=0;
	}
	document.getElementsByClassName("sizing_selection")[0].selectedIndex=0;
	 filter_click(-1)
	 document.getElementsByClassName("filter_aufheben")[0].style.display="none";

 }
 
 
 
 function show_lingerie_details()
 {

 			 	 		 i=0;
		 zaehler=0;
		 box="";
	array_elemente=0;
		while (i<=lingerie_selection.length-1)
		{
			if(lingerie_selection[i].pic!="")
			{
				pictures_lingerie=JSON.parse(lingerie_selection[i].pic)
				picture=pictures_lingerie[0].link
			}
			else
			
				picture=""
			


					
					j=0;
					box_color=""
					zaehler_2=0;
								
					while(j<=colors.length-1)
					{
						
						
							if(colors[j].stylegroupcode==lingerie_selection[i].stylegroupcode)
							{

								marker=j;
								box_color=box_color+"<div class='colors_huelle'><img src='"+colors[j].pic+"' class='colors' onclick='farbe_click("+j+","+i+")'></img></div>"
								zaehler_2=zaehler_2+1;
		
								
								j=colors.length;
								k=0;
								while(k<=colors.length-1)
								{


									if(marker!=k && colors[k].stylegroupcode==lingerie_selection[i].stylegroupcode)
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
					{
						box=box+"<div class='block'>\r";
						zaehler_boxes=0
					}


		
				
					if(window.innerWidth>=320 && window.innerWidth<=499)		
					{
						if(zaehler_boxes==0)
							box=box+"<div class='box_1' style='padding-left:10px'>"
						if(zaehler_boxes==1)
							box=box+"<div class='box_1' style='padding-right:10px'>"
								
						zaehler_boxes=zaehler_boxes+1;
						
						if(zaehler_boxes>1)
							zaehler_boxes=0
					}		
					
					
					if(window.innerWidth>=500 && window.innerWidth<=1199)		
					{
						if(zaehler_boxes==0)
							box=box+"<div class='box_1' style='padding-left:10px'>"
						if(zaehler_boxes==1)
							box=box+"<div class='box_1'  style='padding-left:5px;padding-right:5px;'>"
						if(zaehler_boxes==2)
							box=box+"<div class='box_1' style='padding-right:10px'>"
								
						zaehler_boxes=zaehler_boxes+1;
						
						if(zaehler_boxes>2)
							zaehler_boxes=0
					}	
					
					if(window.innerWidth>=1200)		

						box=box+"<div class='box_1' >"


					link="https://www.darlinglace.com/Produktauswahl/"+lingerie_selection[i].link+"/"+lingerie_selection[i].name;
					link=encodeURI(link)
					box=box+"<img class='image_box' src='"+picture+"' onclick='detail_page("+i+")'><img class='herz' src='/static/herz_grey.png' onclick='wishlist_abrufen("+i+",0)' onmouseenter='wishlist_abrufen_markieren("+i+")' onmouseleave='wishlist_abrufen_entmarkieren("+i+")'></img><div class='rotating_loader' onclick='detail_page("+i+")' style='cursor:pointer'><button style='background-color:transparent;' >	<i class='fa fa-circle-o-notch fa-spin fa-2x' id='button_cart_id_logo' style='display:none;color:#b51d36;'></i></button></div></img><div class='box_erste_ebene'><div class='gericht_auswahl_text' ><h2><a href="+link+">"+lingerie_selection[i].name+"</a></h2></div>"
					
					if(lingerie_selection[i].productgroup!="geschenkkarten")
					{
						if(url_lingerie=="Slips")
							price=replace_dot_comma(lingerie_selection[i].pricesubscription)
						else
							price="19,95"
						if(document.getElementsByClassName("VIP")[0].innerHTML=="Regular")
							box=box+"<div class='price_subscription'>"+price+" € VIP</div></div><div class='box_zweite_ebene'><div class='short_description' ><h2 style='font-weight:300'>"+lingerie_selection[i].descriptionshort+"</h2></div><div class='price_regular'>"+replace_dot_comma(lingerie_selection[i].priceregular)+" €</div></div><div class='box_dritte_ebene'><div class='color_auswahl'>"+box_color+"</div>	</div></div>\r";
						else
							box=box+"<div class='price_subscription'>"+price+" € VIP</div></div><div class='box_zweite_ebene'><div class='short_description'><h2 style='font-weight:300'>"+lingerie_selection[i].descriptionshort+"</h2></div></div><div class='box_dritte_ebene'><div class='color_auswahl'>"+box_color+"</div>	</div></div>\r";
					}
					else
							box=box+"<div class='price_subscription'> "+replace_dot_comma(lingerie_selection[i].pricesubscription)+" €</div></div><div class='box_zweite_ebene'><div class='short_description'><h2 style='font-weight:300'>"+lingerie_selection[i].descriptionshort+"</h2></div></div><div class='box_dritte_ebene'><div class='color_auswahl'>"+box_color+"</div>	</div></div>\r";						
				
					
					zaehler=zaehler+1;

					if(window.innerWidth<=499)
					{
						if(zaehler>=2)
						{
							box=box+"<span class='stretch'></span></div>\r"
							zaehler=0;
						}
					}
					else
					{
						if(window.innerWidth>=500 && window.innerWidth<=1199)
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
	
	if(window.innerWidth>=421 && window.innerWidth<=1199)
	{
		if(zaehler==1)
		{
			box=box+"<div class='box_1'></div>"
			box=box+"<div class='box_1'></div>"
			box=box+"<span class='stretch'></span></div>\r"
		}
		if(zaehler==2)
		{
			box=box+"<div class='box_1'></div>"
			box=box+"<span class='stretch'></span></div>\r"
		}
	}
	
	if(window.innerWidth>=1200)
	{
		if(zaehler==1)
		{
			box=box+"<div class='box_1'></div>"
			box=box+"<div class='box_1'></div>"
			box=box+"<div class='box_1'></div>"
			box=box+"<span class='stretch'></span></div>\r"
		}
		if(zaehler==2)
		{
			box=box+"<div class='box_1'></div>"
			box=box+"<div class='box_1'></div>"
			box=box+"<span class='stretch'></span></div>\r"
		}
		if(zaehler==3)
		{
			box=box+"<div class='box_1'></div>"
			box=box+"<span class='stretch'></span></div>\r"
		}	
	}
	return box;
	

 }
 

 
  function farbe_click(color_id,lingerie_id)
 {
	windowwidth=window.innerWidth;
 	windowheight=window.innerHeight;

 		$.ajax({
		type: "GET",
		url: "/big_data_color_click_main_page/",
		dataType: "json",
		data: { "windowheight":windowheight,"windowwidth":windowwidth,"stylecode":lingerie_selection[lingerie_id].stylecode,"colorcode":lingerie_selection[lingerie_id].colorcode,"farbe":colors[color_id].colorcode,"position":lingerie_selection[lingerie_id].position},
		success: function(data) {		
				window.location= "/Produktauswahl/"+lingerie_selection[lingerie_id].link+"/"+colors[color_id].name;
		
				}
		})


 
 }
 
 function detail_page(i)
 {
	windowwidth=window.innerWidth;
 	windowheight=window.innerHeight;
	window.location= "/Produktauswahl/"+lingerie_selection[i].link+"/"+lingerie_selection[i].name;
 }
 
 
 function pre_load_heart_images(i)
 {
 	
  
 }
 
 function wishlist_abrufen_markieren(i)
 {
 	document.getElementsByClassName("herz")[i].src='/static/herz_color.png'

 	
 }
  function wishlist_abrufen_entmarkieren(i)
 {

 	if(check_whether_wishlist_markiert(i)=="no")
 		document.getElementsByClassName("herz")[i].src='/static/herz_grey.png'
 	
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
		else
			lingerie_selection=""

		if(document.getElementsByClassName("filter")[0].innerHTML!="")
			filter=JSON.parse(document.getElementsByClassName("filter")[0].innerHTML)
		else
			filter=""

		if(document.getElementsByClassName("colors")[0].innerHTML!="")
			colors=JSON.parse(document.getElementsByClassName("colors")[0].innerHTML)
		else
			colors=""
		if(document.getElementsByClassName("lingerie_data")[0].innerHTML!="")
			lingerie_laden();

	}
	else
		quiz_laden();

	
}


function initialize()
{
	if(url_lingerie!="Wunschliste" && url_lingerie!="Geschenkkarten")
	{
		document.getElementsByClassName("filter_aufheben")[0].style.display="none";
		windowwidth=window.innerWidth;
 		windowheight=window.innerHeight;
 	}
 	
 	select_filter()
 	
 	
 	
 	


	 
	
}






 
 
 
 

