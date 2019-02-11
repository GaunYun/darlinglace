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
	var gerichte_menu;
	var ausgewaehlter_tag_;
		var gerichte_gruppen=new Array(4);
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
 

   
   
   
function filter_(clicked_id)
{
	

	var maxim= document.getElementsByClassName("box");
	var filter_var=document.getElementsByClassName("filter");
	

	if(filter_var[clicked_id].style.backgroundColor=="")
	{

		filter_var[clicked_id].style.backgroundColor="#e6e6e6";
		filter[clicked_id]=1;
	}
	else
	{
		filter_var[clicked_id].style.backgroundColor="";
		filter[clicked_id]=0;
	}
	

	gerichte_gruppen[0][1]=0;
	gerichte_gruppen[1][1]=0;
	gerichte_gruppen[2][1]=0;
	gerichte_gruppen[3][1]=0;
	gerichte_gruppen[4][1]=0;
	
	
	
		
	j=0;
	i=0;
	var nicht_zeigen=0;
	

	
	o=-1;
	var k=0;

	while(k<=4)
	{
		
		i=0;
		var nicht_zeigen=-1;

		while(i<=gerichte_menu.length-1)	
		{

			j=0;

			if(gerichte_gruppen[k][0]==gerichte_menu[i].artdesgerichtes && gewaehltes_datum==gerichte_menu[i].datum)
			{
				o=o+1;
				var nicht_zeigen=0;
				while(j<=5)
				{
					if (filter[j]==1 && gerichte_menu[i].vegan=="false")
						nicht_zeigen=1;
					if (filter[j]==1 && gerichte_menu[i].vegetarian=="false")
						nicht_zeigen=1;
					if (filter[j]==1 && gerichte_menu[i].glutenfree=="false")
						nicht_zeigen=1;
					if (filter[j]==1 && gerichte_menu[i].dairyfree=="false")
						nicht_zeigen=1;
					if (filter[j]==1 && gerichte_menu[i].nutfree=="false")
						nicht_zeigen=1;
					if (filter[j]==1 && gerichte_menu[i].eggfree=="false")
						nicht_zeigen=1;
					

					j=j+1;
				}
				
				if(nicht_zeigen==1)
				{
					
					maxim[o].style.display="none";
				
				}
				else
				{
					maxim[o].style.display="block";		
					gerichte_gruppen[k][1]=1;
				}
				
			}
			

			

			i=i+1;
		}
		
		if(nicht_zeigen ==-1)
				gerichte_gruppen[k][1]=1;

		k=k+1;
	}

	
	k=0;

	while(k<=4)	
	{

		if(gerichte_gruppen[k][1]==0)
		{
			document.getElementsByClassName("filter_leer")[k].style.display="block";
			
			document.getElementsByClassName("font_festlegen")[k+1].style.marginTop="100px";
		}
		else
		{
			document.getElementsByClassName("filter_leer")[k].style.display="none";
			document.getElementsByClassName("font_festlegen")[k+1].style.marginTop=gerichte_gruppen[k+1][2]+"px";
		}
		
		k=k+1;
	}
	



}







function datum_auswahl(ausgewaehlter_tag, akt_datum) 	
{

	ausgewaehlter_tag_=ausgewaehlter_tag
			
		if (ausgewaehlter_tag>5 || ausgewaehlter_tag<0)
			window.location.href="/hello/0/";
		var arr1 = akt_datum.split(";");
		var arr2 = [];
		for (i = 0; i < arr1.length; i++) {
			arr2[i]=arr1[i].split(",");
		}  

		datum_output=arr2;

		var maxim= document.getElementsByClassName("datum_auswahl");

		var Wochentag = new Array("MO", "DI", "MI","DO", "FR", "SA", "SO");
		var Monat = new Array("Januar", "Februar", "März", "April",
		"Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember");
		
		var Wochentag_ausfuehrlich = new Array("Montag", "Dienstag", "Mittwoch","Donnerstag", "Freitag", "Samstag","Sonntag");
		


		var j=0;
		var nummer=0;
		auswahl_tag=0;
		
		
		while (nummer<=5)
		{
			
			if (datum_output[j][5]==1)
			{
				maxim[j].innerHTML="<div class='box_datum'><a class='box_datum_css_haupt' href='/hello/"+nummer+"/' ><font size='0.5' color='#4E4E4E'>"+Wochentag[datum_output[j][2]]+"</font><br>"+datum_output[j][1]+"</a></div>";
				if (j==0)
					document.getElementById("aktuelles_Datum").innerHTML="Heute, <br>" + datum_output[j][1] + ". " + Monat[datum_output[j][3]] + " "+datum_output[j][4];
				else
					if (auswahl_tag==1)
						document.getElementById("aktuelles_Datum").innerHTML="Morgen, <br>" + datum_output[j][1] + ". " + Monat[datum_output[j][3]] + " "+datum_output[j][4];
					else
						document.getElementById("aktuelles_Datum").innerHTML=Wochentag_ausfuehrlich[datum_output[j][2]]+", <br>" + datum_output[j][1] + ". " + Monat[datum_output[j][3]] + " "+datum_output[j][4];
						
				auswahl_tag_final=nummer;	
				
				gewaehltes_datum=datum_output[j][1] + ". " + Monat[datum_output[j][3]] + " "+datum_output[j][4];
				gewaehlter_wochentag=Wochentag_ausfuehrlich[datum_output[j][2]]
				
				nummer=nummer+1
			}
			else
			{
				if (datum_output[j][0]=="Wochenende")
				{
					if(datum_output[j][0]=="Wochenende" && datum_output[j+1][0]=="Wochenende")
					{
						
						
						maxim[j].innerHTML="<div class='box_datum'><div class='box_datum_css_wochenende'><font size='0.5' color='#4E4E4E'>Geschlossen</font><br><font color='#4E4E4E'>"+datum_output[j][1]+"-"+datum_output[j+1][1]+"</div></div>";
						j=j+1

					}
					else
						maxim[j].innerHTML="<div class='box_datum'><div class='box_datum_css_wochenende'><font size='0.5' color='#4E4E4E'>Geschlossen</font><br><font color='#4E4E4E'>"+datum_output[j][6]+"-"+datum_output[j][1]+"</div></div>";						
				}	
				else
				{
					maxim[j].innerHTML="<div class='box_datum'><a class='box_datum_css' href='/hello/"+nummer+"/' ><font size='1.5' color='#4E4E4E'>"+Wochentag[datum_output[j][2]]+"</font><br>"+datum_output[j][1]+"</a></div>";
					nummer=nummer+1
				}
			}
			
			j=j+1;

		}

}

 


 
 
 
 function arrow_laden_filter(id) 
{

	var maxim= document.getElementsByClassName("arrow_filter");
	if (id==0)
	{
		variable = "/static/arrow_up.png";	
		maxim[0].src=variable;

	}
	else
	{
		variable = "/static/arrow_down.png";	
		maxim[0].src=variable;

		
	}
		
	
 }
 
  function arrow_laden_plz(id) 
{
	var maxim= document.getElementsByClassName("arrow_plz");
	if (id==0)
	{
		variable = "/static/arrow_up.png";	
		maxim[0].src=variable;

	}
	else
	{
		variable = "/static/arrow_down.png";	
		maxim[0].src=variable;

		
	}
		
	
 }
 
 
   function arrow_laden_datum(id) 
{

	var maxim= document.getElementsByClassName("arrow_plz");
	if (id==0)
	{
		variable = "/static/arrow_up.png";	
		maxim[1].src=variable;

	}
	else
	{
		variable = "/static/arrow_down.png";	
		maxim[1].src=variable;

		
	}
		
	
 }
 
 
    function arrow_laden_rubrikfilter(id) 
{

	var maxim= document.getElementsByClassName("arrow_rubrikfilter");
	if (id==0)
	{
		variable = "/static/arrow_up.png";	
		maxim[0].src=variable;

	}
	else
	{
		variable = "/static/arrow_down.png";	
		maxim[0].src=variable;

		
	}
		
	
 }
 
 
 
 
 
 
 
 function submit_zip()
 
 {
	 

		var submit_plz_input=document.getElementById("eingabe1").value;
		if(isNaN(submit_plz_input) ==true || submit_plz_input.length<5)
		{
			document.getElementById("plz_fehler").innerHTML="Bitte eine fünfstellige PLZ angeben";
		}
		else
		{
			
				document.getElementById("plz_fehler").innerHTML="";

			
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



 function warteliste_click() {
	 

	$.ajax({
		type: "POST",
		url: "/hello/auf_warteliste_setzen/",
		dataType: "json",
		data: { "item": warteliste_plz+","+document.getElementsByClassName("email-eingabe")[0].value },
		success: function(data) {
			
			warteliste_click_schliessen()
			window.location.href="/hello/0/";


		}
	});

}



 function warteliste_click_schliessen() {

	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "hidden") ? "visible" : "hidden";
	document.getElementById("x-mask").style.opacity="1.0";
	document.getElementById("x-mask_2").style.opacity="1.0";
	enableScroll();
}

 function warteliste_click_schliessen_2() {
	enableScroll();
	window.location.href="/hello/0/";
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
 
 
 function alert_click_schliessen() {

	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "hidden") ? "visible" : "hidden";
	document.getElementById("x-mask").style.opacity="1.0";

			document.getElementById("x-mask_2").style.opacity="1.0";
	enableScroll();
}


 
 
 
 
 
  function alert_userdata(content1,content2)
 {	 

	el = document.getElementById("overlay");
	box=""
	box=box+"<br><b>"+content1+"</b><img class='schliessen_alert' src='/static/x.png' width='15' onclick='alert_click_schliessen();' height='15'/></img><br><br>";
	box=box+"<p style='margin-left:20px;margin-right:20px;'>"+content2+"</p><br>";

	
	document.getElementById("alert_address").innerHTML=box

	disableScroll();

	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";

			document.getElementById("x-mask").style.opacity="0.4";
			document.getElementById("x-mask_2").style.opacity="0.4";

 }
 
 
 
 function warenkorb_und_gerichte_abrufen(text1,text2,clicked_id)
 {

 			$.ajax({
			type: "POST",
			url: "/hello/warenkorb_abrufen/",
			dataType: "json",
			data: {  },
			success: function(data) {

				document.getElementsByClassName("warenkorb_daten")[0].innerHTML=data;
				cart=JSON.parse(document.getElementsByClassName("warenkorb_daten")[0].innerHTML);
				$.ajax({
							type: "POST",
							url: "/hello/gerichte_abrufen/",
							dataType: "json",
							data: { "bestellnummer":"", "auswahl_tag":auswahl_tag_final, "gerichtname":"" },
							success: function(data) {
								

								gerichte_menu=JSON.parse(data);
								warenkorb_aufsetzen();
			
								update_produktionsmenge();

		
								mouse_effect_out(clicked_id) 

								document.getElementsByClassName("delete_button")[clicked_id].style.pointerEvents = "auto";
								document.getElementsByClassName("box_zusatz_2")[clicked_id].style.pointerEvents = "auto";
								if(text1!="")
									alert_userdata(text1,text2)
								
							}
						});
			}
			})
 	
 	
 }
 
 function add_cart(clicked_id)
{
	if(verfuegbarkeits_check(gericht_id_suchen_id(clicked_id))!="0 Gerichte übrig" &&  document.getElementsByClassName("anzahl_warenkorb")[clicked_id].innerHTML != "10 X IM WARENKORB")
	{
		document.getElementsByClassName("delete_button")[clicked_id].style.pointerEvents = "none";
		document.getElementsByClassName("box_zusatz_2")[clicked_id].style.pointerEvents = "none";

		$.ajax({
			type: "POST",
			url: "/hello/add/",
			dataType: "json",
			data: { "add_or_erase":"add","gerichtname": gerichte_menu[gericht_id_suchen_id(clicked_id)].name, "datum":gewaehltes_datum, "auswahl_tag_final":auswahl_tag_final,"gewaehlter_wochentag":gewaehlter_wochentag,"anzahl":"" },
			success: function(data) {
	

				if(data=="nicht genuegend warenmenge")
					warenkorb_und_gerichte_abrufen("GERICHTE NICHT VERFÜGBAR","Da war jemand anderes wohl schneller. Leider sind von diesem Gericht keine weiteren verfügbar.",clicked_id)
				else
					if(data=="nicht genuegend fahrer")
						warenkorb_und_gerichte_abrufen("BESTELLUNG FÜR HEUTE NICHT MEHR MÖGLICH","Leider sind für heute keine Fahrer mehr verfügbar. Schau dir doch unsere tollen Gerichte für die nächsten Tage an.",clicked_id)

					else
						warenkorb_und_gerichte_abrufen("","",clicked_id)	

			}
		});
	}
}






function erase_cart(clicked_id)
{
		
		document.getElementsByClassName("delete_button")[clicked_id].style.pointerEvents = "none";
		document.getElementsByClassName("box_zusatz_2")[clicked_id].style.pointerEvents = "none";
		
		$.ajax({
			type: "POST",
			url: "/hello/add/",
			dataType: "json",
			data: { "add_or_erase":"erase","gerichtname": gerichte_menu[gericht_id_suchen_id(clicked_id)].name, "datum":gewaehltes_datum, "auswahl_tag_final":auswahl_tag_final,"gewaehlter_wochentag":gewaehlter_wochentag },
			success: function(data) {	


				if(data=="nicht genuegend warenmenge")
					warenkorb_und_gerichte_abrufen("GERICHTE NICHT VERFÜGBAR","Da war jemand anderes wohl schneller. Leider sind von diesem Gericht keine weiteren verfügbar.",clicked_id)
				else
					if(data=="nicht genuegend fahrer")
						warenkorb_und_gerichte_abrufen("BESTELLUNG FÜR HEUTE NICHT MEHR MÖGLICH","Leider sind für heute keine Fahrer mehr verfügbar. Schau dir doch unsere tollen Gerichte für die nächsten Tage an.",clicked_id)

					else
						warenkorb_und_gerichte_abrufen("","",clicked_id)	
			}
		});

	
		
}		

function update_produktionsmenge()
{
	i=0;
	while(i<=cart.length-1)
	{
		if(cart[i].datum==gewaehltes_datum)
			document.getElementsByClassName("box_zusatz_produktionsmenge")[gericht_id_suchen(cart[i].linkzugericht)].innerHTML=verfuegbarkeits_check(gericht_id_suchen_id(gericht_id_suchen(cart[i].linkzugericht)))
		i=i+1;
	}
	
	
	j=0;
	while(j<=gerichte_menu.length-1)
	{
		document.getElementsByClassName("box_zusatz_produktionsmenge")[gericht_id_suchen(gerichte_menu[j].name)].innerHTML=verfuegbarkeits_check(j)

		if(document.getElementsByClassName("anzahl_warenkorb")[gericht_id_suchen(gerichte_menu[j].name)].innerHTML!="")
		{

			
			i=0;
			status=1;

			while(i<=cart.length-1)
			{

				
				if(cart[i].datum==gewaehltes_datum)
					if(document.getElementsByClassName("gericht_auswahl_text")[gericht_id_suchen(gerichte_menu[j].name)].innerHTML==cart[i].linkzugericht) 
						status=0;			
				i=i+1;
			}


			if(status==1)
			{
				
					
					if(document.getElementsByClassName("box_zusatz_produktionsmenge")[gericht_id_suchen(gerichte_menu[j].name)].innerHTML!="0 Gerichte übrig")
					{
						document.getElementsByClassName("anzahl_warenkorb")[gericht_id_suchen(gerichte_menu[j].name)].innerHTML="";
						document.getElementsByClassName("cart_image")[gericht_id_suchen(gerichte_menu[j].name)].style.opacity="0";
						document.getElementsByClassName("delete_button")[gericht_id_suchen(gerichte_menu[j].name)].style.display="none";					
						document.getElementsByClassName("bild-laden")[gericht_id_suchen(gerichte_menu[j].name)].style.opacity="1.0";	
						document.getElementsByClassName("box_zusatz_2")[gericht_id_suchen(gerichte_menu[j].name)].style.backgroundColor="#ffffff";	
						document.getElementsByClassName("box_zusatz_2")[gericht_id_suchen(gerichte_menu[j].name)].style.color="#4E4E4E";
					

					
					}
					else
					{
						document.getElementsByClassName("anzahl_warenkorb")[gericht_id_suchen(gerichte_menu[j].name)].innerHTML="AUSVERKAUFT";
						document.getElementsByClassName("cart_image")[gericht_id_suchen(gerichte_menu[j].name)].style.backgroundColor="#4E4E4E";
						document.getElementsByClassName("cart_image")[gericht_id_suchen(gerichte_menu[j].name)].style.opacity="0.5";
						
						document.getElementsByClassName("delete_button")[gericht_id_suchen(gerichte_menu[j].name)].style.display="none";					
						document.getElementsByClassName("bild-laden")[gericht_id_suchen(gerichte_menu[j].name)].style.opacity="0.2";	
						
						document.getElementsByClassName("box_zusatz_2")[gericht_id_suchen(gerichte_menu[j].name)].style.backgroundColor="#4E4E4E";
						document.getElementsByClassName("box_zusatz_2")[gericht_id_suchen(gerichte_menu[j].name)].style.color="#ffffff";
						
					}
					



				
				
			}
			
			

		}
		else
					if(document.getElementsByClassName("box_zusatz_produktionsmenge")[gericht_id_suchen(gerichte_menu[j].name)].innerHTML!="0 Gerichte übrig")
					{
						document.getElementsByClassName("anzahl_warenkorb")[gericht_id_suchen(gerichte_menu[j].name)].innerHTML="";
						document.getElementsByClassName("cart_image")[gericht_id_suchen(gerichte_menu[j].name)].style.opacity="0";
						document.getElementsByClassName("delete_button")[gericht_id_suchen(gerichte_menu[j].name)].style.display="none";					
						document.getElementsByClassName("bild-laden")[gericht_id_suchen(gerichte_menu[j].name)].style.opacity="1.0";	
						document.getElementsByClassName("box_zusatz_2")[gericht_id_suchen(gerichte_menu[j].name)].style.backgroundColor="#ffffff";	
						document.getElementsByClassName("box_zusatz_2")[gericht_id_suchen(gerichte_menu[j].name)].style.color="#4E4E4E";
					

					
					}
					else
					{
						document.getElementsByClassName("anzahl_warenkorb")[gericht_id_suchen(gerichte_menu[j].name)].innerHTML="AUSVERKAUFT";
						document.getElementsByClassName("cart_image")[gericht_id_suchen(gerichte_menu[j].name)].style.backgroundColor="#4E4E4E";
						document.getElementsByClassName("cart_image")[gericht_id_suchen(gerichte_menu[j].name)].style.opacity="0.5";
						
						document.getElementsByClassName("delete_button")[gericht_id_suchen(gerichte_menu[j].name)].style.display="none";					
						document.getElementsByClassName("bild-laden")[gericht_id_suchen(gerichte_menu[j].name)].style.opacity="0.2";	
						
						document.getElementsByClassName("box_zusatz_2")[gericht_id_suchen(gerichte_menu[j].name)].style.backgroundColor="#4E4E4E";
						document.getElementsByClassName("box_zusatz_2")[gericht_id_suchen(gerichte_menu[j].name)].style.color="#ffffff";
						
					}

	
		j=j+1;
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


 function change_plz()
 {
	 submit_plz_input=document.getElementById("eingabe1").value;
	if(isNaN(submit_plz_input) ==true || submit_plz_input.length<5)
	{
		document.getElementById("plz_fehler").innerHTML="Bitte eine fünfstellige PLZ angeben";
	}
	else
	{

		$.ajax({
			type: "POST",
			url: "/hello/change_plz/",
			dataType: "json",
			data: { "item": submit_plz_input },
			success: function(data) {
				
				warteliste_plz=submit_plz_input
				if (data=="ok")
				{
					document.getElementById("gewaehlte_plz").innerHTML=submit_plz_input;

				}
				else
				{
					el = document.getElementById("overlay");
					box=""
					box=box+"<br><b>WARTELISTE</b><img class='schliessen_warteliste' src='/static/x.png' width='15' onclick='warteliste_click_schliessen_2();' height='15'/></img><br><br>";
					box=box+"<p>Leider sind wir in deinem Postleitzahl-Bereich noch nicht verfügbar. Setze Dich doch auf die Warteliste, damit du informiert wirst, wann wir bei Dir verfügbar sind!</p><br>";
					box=box+"<input class='email-eingabe' type='text' style='width:150px;height:25px;font-size:14px;color:#000000;'  placeholder='E-Mail Adresse' />";
					box=box+"<button onclick='warteliste_click()' class='button_warteliste' style='margin-left:10px'>Auf die Warteliste</button>";

					
					
					document.getElementById("alert_address").innerHTML=box

					disableScroll();
				
					el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";


	

					document.getElementById("x-mask").style.opacity="0.4";
					document.getElementById("x-mask_2").style.opacity="0.4";

				}
					

			}
		});
	}
	 
	 
	 
 }


 
 function check_plz()
 {
	 var submit_plz_input=document.getElementsByClassName("plz_eingabe")[0].value;
	if(isNaN(submit_plz_input) ==true || submit_plz_input.length<5)
	{
		document.getElementById("plz_fehler").innerHTML="Bitte eine fünfstellige PLZ angeben";
	}
	else
	{
		
		$.ajax({
			type: "POST",
			url: "/hello/check_plz/",
			dataType: "json",
			data: { "item": document.getElementsByClassName("plz_eingabe")[0].value },
			success: function(data) {
				warteliste_plz=document.getElementsByClassName("plz_eingabe")[0].value
				if (data=="ok")
				{
					document.getElementById("gewaehlte_plz").innerHTML=document.getElementsByClassName("plz_eingabe")[0].value
					warteliste_click_schliessen();
				}
				else
				{
					
										
					el = document.getElementById("overlay");
					box=""
					box=box+"<br><b>WARTELISTE</b><img class='schliessen_warteliste' src='/static/x.png' width='15' onclick='warteliste_click_schliessen_2();' height='15'/></img><br><br>";
					box=box+"<p>Leider sind wir in deinem Postleitzahl-Bereich noch nicht verfügbar. Setze Dich doch auf die Warteliste, damit du informiert wirst, wann wir bei Dir verfügbar sind!</p><br>";
					box=box+"<input class='email-eingabe' type='text' style='width:150px;height:25px;font-size:14px;color:#000000;'  placeholder='E-Mail Adresse' />";
					box=box+"<button onclick='warteliste_click()' class='button_warteliste' style='margin-left:10px'>Auf die Warteliste</button>";
					
					
					
					document.getElementById("alert_address").innerHTML=box

					disableScroll();
				
					el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
					document.getElementById("x-mask").style.opacity="0.4";
					document.getElementById("x-mask_2").style.opacity="0.4";

				}

			}
		});
	}
	 
	 
	 
 }
 
 function plz_ermitteln(plz)
 {
	 
	 
	 if (plz=="")
	 {
		 
		el = document.getElementById("overlay");
		box=""
		box=box+"<br><b>POSTLEITZAHL EINGEBEN</b><br><br>";
		box=box+"<p>Damit wir überprüfen können, ob wir schon bei Dir verfügbar sind, gib bitte Deine PLZ ein:</p><br>";
		box=box+"<input class='plz_eingabe' type='text' style='width:80px;height:25px;font-size:14px;color:#000000;'  placeholder='PLZ' onclick='input_plz_text()' onblur='input_plz_text_blur()' onkeypress='validate(event)' maxlength='5'/>";
		box=box+"<button style='margin-left:10px;' class='button_warteliste' onclick='check_plz()'>Überprüfen</button><p id='plz_fehler' style='font-size:10px;color:#C80000  ' ></p>";

		document.getElementById("alert_address").innerHTML=box

		disableScroll();
	
		el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
		document.getElementById("x-mask").style.opacity="0.4";
		document.getElementById("x-mask_2").style.opacity="0.4";
	 }
	 else
		 document.getElementById("gewaehlte_plz").innerHTML=plz
		 
	 
	 
 }
 
 

 
 function replace_dot_comma(zahl)
{

	zahl=zahl.toString()
	return zahl.replace(".", ",");
}



 
 function gericht_id_suchen(name)
 {
	 

	

	
	 j=0;
	 o=-1;
	 var k=0;
	 while(k<=4)
	 {
		 var j=0;
		 while (j<=gerichte_menu.length-1)
		 {

			 if(gerichte_menu[j].artdesgerichtes==gerichte_gruppen[k][0] && gerichte_menu[j].datum==gewaehltes_datum)
			 {
				 
				 o=o+1;
				 if (gerichte_menu[j].name==name)
					 return o
			 }
			 
			 j=j+1;
			 
		 }
		 k=k+1;
	 }
	 
	 
 }
 
 
  function gericht_id_suchen_id(index)
 {
	 
	
	 

	
	 j=0;
	 o=-1;
	 var k=0;
	 while(k<=4)
	 {
		 var j=0;
		 while (j<=gerichte_menu.length-1)
		 {
			 if(gerichte_menu[j].artdesgerichtes==gerichte_gruppen[k][0] && gerichte_menu[j].datum==gewaehltes_datum)
			 {
				 o=o+1;
				 if (o==index)
					 return j
			 }
			 
			 j=j+1;
			 
		 }
		 k=k+1;
	 }
	 
	 
 }
 

 
  function warenkorb_aufsetzen()
 {

	
	cart=JSON.parse(document.getElementsByClassName("warenkorb_daten")[0].innerHTML);	
	
	 i=0;
	 cart_gesamt=0;
	 

	 
	 while (i<=cart.length-1)
	 {
		 
		 if(gewaehltes_datum==cart[i].datum)
		 {

			
			if (cart[i].anzahl>0)
			{
				
						 
				
				document.getElementsByClassName("anzahl_warenkorb")[gericht_id_suchen(cart[i].linkzugericht)].innerHTML=cart[i].anzahl+" X IM WARENKORB";
				document.getElementsByClassName("cart_image")[gericht_id_suchen(cart[i].linkzugericht)].style.opacity="0.5";
				document.getElementsByClassName("delete_button")[gericht_id_suchen(cart[i].linkzugericht)].style.display="block";
				document.getElementsByClassName("cart_image")[gericht_id_suchen(cart[i].linkzugericht)].style.backgroundColor="";
				
				document.getElementsByClassName("bild-laden")[gericht_id_suchen(cart[i].linkzugericht)].style.opacity="0.2";
				

				document.getElementsByClassName("box_zusatz_produktionsmenge")[gericht_id_suchen(cart[i].linkzugericht)].innerHTML=verfuegbarkeits_check(gericht_id_suchen_id(gericht_id_suchen(cart[i].linkzugericht)))
				
				if(document.getElementsByClassName("box_zusatz_produktionsmenge")[gericht_id_suchen(cart[i].linkzugericht)].innerHTML=="0 Gerichte übrig" || document.getElementsByClassName("anzahl_warenkorb")[gericht_id_suchen(cart[i].linkzugericht)].innerHTML=="10 X IM WARENKORB")
				{

					document.getElementsByClassName("box_zusatz_2")[gericht_id_suchen(cart[i].linkzugericht)].style.backgroundColor="#4E4E4E";
					document.getElementsByClassName("box_zusatz_2")[gericht_id_suchen(cart[i].linkzugericht)].style.color="#ffffff";
					
				}
				else
				{
					document.getElementsByClassName("box_zusatz_2")[gericht_id_suchen(cart[i].linkzugericht)].style.backgroundColor="#ffffff";	
					document.getElementsByClassName("box_zusatz_2")[gericht_id_suchen(cart[i].linkzugericht)].style.color="#4E4E4E";
				}
				
			}
			else
			{

					document.getElementsByClassName("anzahl_warenkorb")[gericht_id_suchen(cart[i].linkzugericht)].innerHTML="";
					document.getElementsByClassName("cart_image")[gericht_id_suchen(cart[i].linkzugericht)].style.opacity="0";
					document.getElementsByClassName("delete_button")[gericht_id_suchen(cart[i].linkzugericht)].style.display="none";					
					document.getElementsByClassName("bild-laden")[gericht_id_suchen(cart[i].linkzugericht)].style.opacity="1.0";
					
					document.getElementsByClassName("box_zusatz_produktionsmenge")[gericht_id_suchen(cart[i].linkzugericht)].innerHTML=verfuegbarkeits_check(gericht_id_suchen_id(gericht_id_suchen(cart[i].linkzugericht)))

			
			
			
			}
		 }


		 
		 if (parseInt(cart[i].anzahl)>0)
			cart_gesamt=cart_gesamt+parseInt(cart[i].anzahl);
		i=i+1;
	 }
	 
	 
	 


	if (cart_gesamt!=0)
	{	
		document.getElementsByClassName("cart_text")[0].innerHTML=cart_gesamt;
		document.getElementsByClassName("cart")[0].style.backgroundImage="url('/static/Cart-open.PNG')";

	}
	else
	{
		document.getElementsByClassName("cart_text")[0].innerHTML=" ";
		document.getElementsByClassName("cart")[0].style.backgroundImage="url('/static/Cart.PNG')";

	}
 }
 
 
 function gerichte_filterkriterien_laden(index)
 {
	 
	 var variable=""
	 
	if(gerichte_menu[index].vegan=="true")
	{
		variable = variable+ "<img src='/static/vegan.PNG'  width='15' height='15'></img>";		
	}
	
	if(gerichte_menu[index].vegetarian=="true")
	{
		variable = variable+ "<img src='/static/vegetarian.png'  width='15' height='15'></img>";		
	}
	
	if(gerichte_menu[index].glutenfree==="true")
	{
		variable = variable+ "<img src='/static/gluten-free.png'  width='15' height='15'></img>";		
	}
	if(gerichte_menu[index].dairyfree==="true")
	{
		variable = variable+ "<img src='/static/dairy-free.png'  width='15' height='15'></img>";		
	}
	
	if(gerichte_menu[index].nutfree==="true")
	{
		variable = variable+ "<img src='/static/nut-free.png'  width='15' height='15'></img>";		
	}
	
	if(gerichte_menu[index].eggfree==="true")
	{
		variable = variable+ "<img src='/static/egg-free.png'  width='15' height='15'></img>";		
	}
	
	return variable;
	 
	 
 }
 
 
 function fahrer_kapa_anzeigen(daten_,nummer,plz)
{
	if(daten_=="nicht ok")
	{
		
		new_nummer=parseInt(nummer)+1
		el = document.getElementById("overlay");
		box=""
		box=box+"<br><b>FÜR HEUTE KEINE BESTELLUNG MEHR MÖGLICH</b><br><br>";
		box=box+"<p>Am liebsten würden wir heute noch mehr Emnschen mit unserem Essen glücklich machen, aber leider haben unsere Köche schon Feierabend. :)</p><br>";

		box=box+"<button onclick='neuen_tag_waehlen("+new_nummer+")' class='button_warteliste' style='margin-left:10px'>Nächsten Tag wählen</button>";
		document.getElementById("alert_address").innerHTML=box

		disableScroll();
	
		el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
			document.getElementById("x-mask").style.opacity="0.4";
		document.getElementById("x-mask_2").style.opacity="0.4";
		
		
	}
	else
		plz_ermitteln(plz);
	
	

		

}


function neuen_tag_waehlen(new_nummer)
{
	window.location.href="/hello/"+new_nummer+"/";
	
}
 
 
 
 

 
 
 function gerichte_laden()
 {
	  
	 
	var box=new Array(4);
	

	
	gerichte_gruppen[0]=new Array;
	gerichte_gruppen[1]=new Array;
	gerichte_gruppen[2]=new Array;
	gerichte_gruppen[3]=new Array;
	gerichte_gruppen[4]=new Array;
	

	
	gerichte_gruppen[0][0]="Apero/ Vorspeise";
	gerichte_gruppen[0][1]=0;
	
	gerichte_gruppen[1][0]="Hauptgerichte";
	gerichte_gruppen[1][1]=0;
	
	gerichte_gruppen[2][0]="Kindergerichte";
	gerichte_gruppen[2][1]=0;
	
	gerichte_gruppen[3][0]="Desserts";
	gerichte_gruppen[3][1]=0;
	
	gerichte_gruppen[4][0]="Getränke";
	gerichte_gruppen[4][1]=0;
	
	
	
	array_elemente=0;
	 
	 k=0;
	 while(k<=4)	 
	 {
		 box[k]="<div class='filter_leer'><br><br>Keine Gerichte sind bei den gewählten Filtern verfügbar.</div>";
		 i=0;
		while (i<=gerichte_menu.length-1)
		{
			
			
			if (gerichte_menu[i].artdesgerichtes==gerichte_gruppen[k][0] && gewaehltes_datum == gerichte_menu[i].datum)
			{

				if (gerichte_menu[i].gerichte_uebrig==0 )
				{
					cart_image_style="opacity:0.5;background-Color:#4E4E4E;border-radius: 5px;'"
					bild_laden_style="opacity:0.2;";
					ausverkauft="AUSVERKAUFT";
					add_cart_style="background-color:#4E4E4E;color:#ffffff;";
					
					
				}
				else
				{
					ausverkauft="";
					cart_image_style="opacity:0;border-radius: 5px;";
					bild_laden_style="opacity:1.0;";
					add_cart_style="display:block;color:#4E4E4E;";
					
				}
				
				


				
				if(gerichte_gruppen[k][1]==0 || gerichte_gruppen[k][1]==4 || gerichte_gruppen[k][1]==8 || gerichte_gruppen[k][1]==12 || gerichte_gruppen[k][1]==16 || gerichte_gruppen[k][1]==20 || gerichte_gruppen[k][1]==24 )
					box[k]=box[k]+"<div class='box' ><div class='box_1'><a href='"+gerichte_menu[i].name+"'><div class='image-box'><div class='bild-laden' style='"+bild_laden_style+"'><img src='"+gerichte_menu[i].picture_link_small+"'	width='100%' style='border-radius: 5px;'></img></div><h2 class='cart_image' style='"+cart_image_style+"'><div class='anzahl_warenkorb'>"+ausverkauft+"</div></h2></div></a><div class='gericht_auswahl_text' >"+gerichte_menu[i].name+"</div><div class='box_zusatz'>€ "+replace_dot_comma(gerichte_menu[i].preis)+"<div id='"+array_elemente+"' class='box_zusatz_2' value='+' onmouseenter='mouse_effect_in("+array_elemente+")' onmouseout='mouse_effect_out("+array_elemente+")' onclick='add_cart("+array_elemente+")' style='"+add_cart_style+"'>+</div><div id='delete_button_"+array_elemente+"' class='delete_button' value='-' onmouseover='mouse_effect_in_delete("+array_elemente+")' onmouseout='mouse_effect_out_delete("+array_elemente+")' onclick='erase_cart("+array_elemente+")'>-</div></div><div class='box_zusatz_produktionsmenge'>"+verfuegbarkeits_check(i)+"</div></div></div>";
				if(gerichte_gruppen[k][1]==1 || gerichte_gruppen[k][1]==2 || gerichte_gruppen[k][1]==5 || gerichte_gruppen[k][1]==6 || gerichte_gruppen[k][1]==9 || gerichte_gruppen[k][1]==10 || gerichte_gruppen[k][1]==13 || gerichte_gruppen[k][1]==14 || gerichte_gruppen[k][1]==17 || gerichte_gruppen[k][1]==18 || gerichte_gruppen[k][1]==21 || gerichte_gruppen[k][1]==22 || gerichte_gruppen[k][1]==25 || gerichte_gruppen[k][1]==26)
					box[k]=box[k]+"<div class='box'><div class='box_2-3'><a href='"+gerichte_menu[i].name+"'><div class='image-box'><div class='bild-laden' style='"+bild_laden_style+"'><img src='"+gerichte_menu[i].picture_link_small+"'	width='100%' style='border-radius: 5px;' ></img></div><h2 class='cart_image' style='"+cart_image_style+"'><div class='anzahl_warenkorb'>"+ausverkauft+"</div></h2></div></a><div class='gericht_auswahl_text'>"+gerichte_menu[i].name+"</div><div class='box_zusatz'>€ "+replace_dot_comma(gerichte_menu[i].preis)+"<div id='"+array_elemente+"' class='box_zusatz_2' value='+' onmouseenter='mouse_effect_in("+array_elemente+")' onmouseout='mouse_effect_out("+array_elemente+")' onclick='add_cart("+array_elemente+")' style='"+add_cart_style+"'>+</div><div id='delete_button_"+array_elemente+"' class='delete_button' value='-' onmouseover='mouse_effect_in_delete("+array_elemente+")' onmouseout='mouse_effect_out_delete("+array_elemente+")' onclick='erase_cart("+array_elemente+")'>-</div></div><div class='box_zusatz_produktionsmenge'>"+verfuegbarkeits_check(i)+"</div></div></div>";
				if(gerichte_gruppen[k][1]==3 || gerichte_gruppen[k][1]==7 || gerichte_gruppen[k][1]==11 || gerichte_gruppen[k][1]==15 || gerichte_gruppen[k][1]==19 || gerichte_gruppen[k][1]==23 || gerichte_gruppen[k][1]==27 )
					box[k]=box[k]+"<div class='box'><div class='box_4'><a href='"+gerichte_menu[i].name+"'><div class='image-box'><div class='bild-laden' style='"+bild_laden_style+"'><img src='"+gerichte_menu[i].picture_link_small+"'	width='100%' style='border-radius: 5px;'></img></div><h2 class='cart_image' style='"+cart_image_style+"'><div class='anzahl_warenkorb'>"+ausverkauft+"</div></h2></div></a><div class='gericht_auswahl_text'>"+gerichte_menu[i].name+"</div><div class='box_zusatz'>€ "+replace_dot_comma(gerichte_menu[i].preis)+"<div id='"+array_elemente+"' class='box_zusatz_2' value='+' onmouseenter='mouse_effect_in("+array_elemente+")' onmouseout='mouse_effect_out("+array_elemente+")' onclick='add_cart("+array_elemente+")' style='"+add_cart_style+"'>+</div><div id='delete_button_"+array_elemente+"' class='delete_button' value='-' onmouseover='mouse_effect_in_delete("+array_elemente+")' onmouseout='mouse_effect_out_delete("+array_elemente+")' onclick='erase_cart("+array_elemente+")'>-</div></div><div class='box_zusatz_produktionsmenge'>"+verfuegbarkeits_check(i)+"</div></div></div>";;
				gerichte_gruppen[k][1]=gerichte_gruppen[k][1]+1;
				array_elemente=array_elemente+1;

					
			}	
			i=i+1;
		}
		document.getElementsByClassName("container_gerichte")[k].innerHTML=box[k];
		document.getElementsByClassName("container_gerichte")[k].style.marginTop="-70px";

		
		
		
		if(k<4)
		{
			document.getElementsByClassName("font_festlegen")[k+1].style.marginTop=Math.ceil(gerichte_gruppen[k][1]/4)*400+100	+"px";
			gerichte_gruppen[k+1][2]=Math.ceil(gerichte_gruppen[k][1]/4)*400+100;
		}

		
		k=k+1;
		
	 }

 }
 
 function verfuegbarkeits_check(i)
 {
	

	 if ((parseInt(gerichte_menu[i].gerichte_uebrig)-parseInt(gerichte_menu[i].warenkorb_menge))<=10)
		 return (parseInt(gerichte_menu[i].gerichte_uebrig)-parseInt(gerichte_menu[i].warenkorb_menge))+" Gerichte übrig";
	 else
		 return "";
		 
	 
 }



 
function mouse_effect_out(clicked_id) 
{

	var maxim= document.getElementsByClassName("box_zusatz_2");

	if(verfuegbarkeits_check(gericht_id_suchen_id(clicked_id))!="0 Gerichte übrig" && document.getElementsByClassName("anzahl_warenkorb")[clicked_id].innerHTML!="10 X IM WARENKORB")
	{

		maxim[clicked_id].style.backgroundColor="#ffffff";
		maxim[clicked_id].style.color="#4E4E4E";
	}
	else
	{
		maxim[clicked_id].style.backgroundColor="#4E4E4E";
		maxim[clicked_id].style.color="#ffffff";
	}

 }
 

 
 
 function filter_function() {
	if (document.getElementById("filter_dropdown").style.display=="block")
	{
		document.getElementById("myDropdown").style.display = "none";
		document.getElementById("myDropdown_").style.display = "none";
		document.getElementById("filter_dropdown").style.display = "none";
		document.getElementById("rubrikfilter_dropdown").style.display = "none";
		
		
		arrow_laden_plz(0);
		arrow_laden_datum(0);
		arrow_laden_filter(0);
		arrow_laden_rubrikfilter(0);
		
	}
	else
	{
		document.getElementById("filter_dropdown").style.display = "block";
		document.getElementById("myDropdown_").style.display = "none";
		document.getElementById("myDropdown").style.display = "none";
		document.getElementById("rubrikfilter_dropdown").style.display = "none";
		
		arrow_laden_plz(0);
		arrow_laden_datum(0);
		arrow_laden_filter(1);
		arrow_laden_rubrikfilter(0);
		
	}
} 

 

 
 
function myFunction() {
	if (document.getElementById("myDropdown").style.display=="block")
	{
		document.getElementById("myDropdown").style.display = "none";
		document.getElementById("myDropdown_").style.display = "none";
		document.getElementById("filter_dropdown").style.display = "none";
		document.getElementById("rubrikfilter_dropdown").style.display = "none";
		arrow_laden_plz(0);
		arrow_laden_datum(0);
		arrow_laden_filter(0);
		arrow_laden_rubrikfilter(0);
	}
	else
	{
		document.getElementById("myDropdown").style.display = "block";
		document.getElementById("myDropdown_").style.display = "none";
		document.getElementById("filter_dropdown").style.display = "none";
		document.getElementById("rubrikfilter_dropdown").style.display = "none";
		arrow_laden_plz(0);
		arrow_laden_datum(1);
		arrow_laden_filter(0);
		arrow_laden_rubrikfilter(0);
		
	}
}



function myFunction_() {
	
	if (document.getElementById("myDropdown_").style.display=="block")
	{
		document.getElementById("myDropdown_").style.display = "none";
		document.getElementById("myDropdown").style.display = "none";
		document.getElementById("filter_dropdown").style.display = "none";
		document.getElementById("rubrikfilter_dropdown").style.display = "none";

		arrow_laden_plz(0);
		arrow_laden_datum(0);
		arrow_laden_filter(0);
		arrow_laden_rubrikfilter(0);
		

	}
	else
	{
		
		document.getElementById("myDropdown_").style.display = "block";
		document.getElementById("myDropdown").style.display = "none";
		document.getElementById("filter_dropdown").style.display = "none";
		document.getElementById("rubrikfilter_dropdown").style.display = "none";

		arrow_laden_plz(1);
		arrow_laden_datum(0);
		arrow_laden_filter(0);
		arrow_laden_rubrikfilter(0);
	}	
}


function rubrikfilter_function() {
	
	if (document.getElementById("rubrikfilter_dropdown").style.display=="block")
	{
		document.getElementById("myDropdown_").style.display = "none";
		document.getElementById("myDropdown").style.display = "none";
		document.getElementById("filter_dropdown").style.display = "none";
		document.getElementById("rubrikfilter_dropdown").style.display = "none";

		arrow_laden_plz(0);
		arrow_laden_datum(0);
		arrow_laden_filter(0);
		arrow_laden_rubrikfilter(0);
		

	}
	else
	{
		
		document.getElementById("myDropdown_").style.display = "none";
		document.getElementById("myDropdown").style.display = "none";
		document.getElementById("filter_dropdown").style.display = "none";
		document.getElementById("rubrikfilter_dropdown").style.display = "block";
		
		arrow_laden_rubrikfilter(1);
		arrow_laden_plz(0);
		arrow_laden_datum(0);
		arrow_laden_filter(0);
	}	
}



function rubrikfilterfilter_(id)
{

	if (id==0)
		window.location.hash="#Vorspeisen"
	if (id==1)
		window.location.href="#Hauptgerichte"
	if (id==2)
		window.location.href="#Kindergerichte"
	if (id==3)
		window.location.href="#Desserts"
	if (id==4)
		window.location.href="#Getränke"


	window.scrollTo(0,document.body.scrollTop-80);
	rubrikfilter_function()
	
	
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


function gerichte_menu_laden()
{


	gerichte_menu=JSON.parse(document.getElementsByClassName("menu_daten")[0].innerHTML)

	
}





 
 
 
 
