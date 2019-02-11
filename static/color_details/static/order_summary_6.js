
var gerichte;
var bestellung;
var height;
var fahrer_kapazitaet;
var gerichte;
var aenderung;
var min_height;
var rebates;





function change()
{
	
	document.getElementsByClassName("button_uebernehmen")[0].style.display="block";
	check_fields()
}


function change_lingerie()
{

	document.getElementsByClassName("button_uebernehmen")[0].style.display="block";

	j=0;
	item="";

	zaehler=-1;

	

	while(j<=bestelldetails.length-1)
	{


		item=item+bestelldetails[j].style+",";
		item=item+bestelldetails[j].stylecode+",";
		item=item+bestelldetails[j].color+",";
		item=item+bestelldetails[j].bhgroesse+",";
		item=item+bestelldetails[j].slipgroesse+",";
		item=item+parseInt(document.getElementsByClassName("select_anzahl")[j].selectedIndex+1)+",";
		item=item+bestelldetails[j].preis+",";
		zaehler=zaehler+1;
		j=j+1;
	}
	
	$.ajax({
			type: "GET",
			url: "/hello/get_rebates/",
			dataType: "json",
			data: { "bestellnummer":bestellung[0].bestellnummer,"item":  item,"item-length":  zaehler,"aenderung":"yes"},
			success: function(data) {

				rebates=JSON.parse(data)

				bestellung_block()
				
			}
			
	})
	
	
}


function status_anzeigen(j)
{

	if(bestelldetails[j].status=="Bestellt")
		return ""
	else
		return bestelldetails[j].status;
	
}




function bestellte_lingerie_anzeigen()
{
	aenderung=0;

	
	box="";
	datum="";
	var j=0;
	height=0;


	while(j<=bestelldetails.length-1)
	{

			box=box+"<div style='float:left;width:100%;margin-bottom:10px;'>"
			box=box+"<img src='"+bestelldetails[j].picture_link_small+"' style='height:100px;float:left;'/>"
			box=box+"<div style='margin-left:10px;float:left;'/><b>"+bestelldetails[j].style+"</b></div>"

			box=box+"<div class='anzahl_anzeigen' style='float:right;'>Anzahl: "+bestelldetails[j].anzahl+"</div>"

			box=box+"<div class='anzahl_bearbeiten' style='display:none;float:right'><select class='select_anzahl' style='width:40px;' onchange='change_lingerie()' >"



			min_1=parseInt(bestelldetails[j].freiemenge)+parseInt(bestelldetails[j].anzahl)


			w=1;
			while(w<=Math.min(min_1,10))
			{
				box=box+"<option>"+w+"</option>";
				w=w+1;
			}
			
					
					
			box=box+"</select></div>"
					
			
			box=box+"<br><div class='details_order'>"+bestelldetails[j].bhgroesse+"</div> <br>"
			box=box+"<div class='details_order'>"+bestelldetails[j].slipgroesse+"</div><br><br>"
			box=box+"<div class='details_order'>"+replace_dot_comma(parseFloat(bestelldetails[j].preis)*bestelldetails[j].anzahl)+" EUR</div> </div>";


		
		j=j+1;
	}
	box=box+"</div><br><br>"


	document.getElementsByClassName ("lingerie_i")[0].innerHTML=box;
	

	j=0;
	zaehler=0;
	
	
	while(j<=bestelldetails.length-1)
	{
			document.getElementsByClassName("select_anzahl")[j].selectedIndex=bestelldetails[j].anzahl-1;
			
		j=j+1;
	}

	if(window.innerWidth>=768)	
	{
		min_height=Math.max(document.getElementsByClassName("lingerie_with_border")[0].clientHeight,document.getElementsByClassName("lingerie_with_border")[1].clientHeight,350)
		
		if(document.getElementsByClassName("lingerie_with_border")[0].clientHeight<min_height)
			document.getElementsByClassName("lingerie_with_border")[0].style.height=min_height+"px"
		if(document.getElementsByClassName("lingerie_with_border")[1].clientHeight<min_height)
			document.getElementsByClassName("lingerie_with_border")[1].style.height=min_height+"px"
	
		document.getElementsByClassName("lingerie_wo_border")[0].style.height=min_height+"px"	
	}

}


function bestellung_bearbeiten()
{


	
	var j=0;

			while(j<=bestelldetails.length-1)
			{

							if(bestelldetails[j].status=="Bestellt")
							{
								

								document.getElementsByClassName("anzahl_anzeigen")[j].style.display="none";
								document.getElementsByClassName("anzahl_bearbeiten")[j].style.display="block";
								status=1;
								
								
							}
							zaehler=zaehler+1;
							
						

				j=j+1;
			}
			
			
			if (status==1)
			{
				document.getElementsByClassName("button_abbrechen")[0].style.display="block";
				document.getElementsByClassName("button_bearbeiten")[0].style.display="none";
				document.getElementsByClassName("adresse_anzeigen")[0].style.display="none";
				document.getElementsByClassName("adresse_anzeigen")[1].style.display="none";
				if(bestellung[0].unternehmensdetails!="")
					document.getElementsByClassName("adresse_anzeigen")[2].style.display="none";
				document.getElementsByClassName("adresse_bearbeiten")[0].style.display="block";

				document.getElementsByClassName("plz_stadt_anzeigen")[0].style.display="none";	
				document.getElementsByClassName("lieferhinweise_anzeigen")[0].style.display="none";
				document.getElementsByClassName("lieferhinweise_bearbeiten")[0].style.display="block";	
				document.getElementsByClassName("unternehmensdetails_anzeigen")[0].style.display="none";

			}

	
}

 function alert_click_schliessen1() {
	$('#alert_box_rechnungsbetrag').modal('hide');
	$('#alert_box_reload').modal('hide');
}




function bearbeitungsblock_hinzufuegen()
{
	var block="";
	j=0;
	while(j<=bestelldetails.length-1)
	{
		if(status_anzeigen(j)=="")
		{
			
			block=block+"<div  class='button_uebernehmen' style='margin-top:25px;margin-Bottom:25px;display:none' onclick='bestellung_bearbeiten_uebernehmen()' onmouseenter='button_bearbeiten_onmouseenter()' onmouseout='button_bearbeiten_onmouseleave()'>Übernehmen</div>"
			block=block+"<div  class='button_bearbeiten' style='margin-top:25px;margin-Bottom:25px;' onclick='bestellung_bearbeiten()' onmouseenter='button_bearbeiten_onmouseenter()' onmouseout='button_bearbeiten_onmouseleave()'>Bearbeiten</div>";
			block=block+"<div class='button_abbrechen' style='margin-top:25px;margin-Bottom:25px;display:none;max-width:100px;float:right;margin-right:10px;' onclick='bestellung_bearbeiten_abbrechen()' onmouseenter='button_bearbeiten_onmouseenter()' onmouseout='button_bearbeiten_onmouseleave()'>Abbrechen</div>"
			break;
		}
		j=j+1;
	}
	block=block+"<div  class='button_zurueck' style='margin-top:25px;margin-Bottom:25px;max-width:100px;float:right;margin-right:10px;' onclick='bestellung_bearbeiten_hauptseite()' onmouseenter='button_bearbeiten_onmouseenter()' onmouseout='button_bearbeiten_onmouseleave()'>Zurück</div>"

	block=block+"<br><br><br>";
	
	document.getElementsByClassName("bearbeitunsblock_hinzufuegen")[0].innerHTML=block;
}

function check_fields()
{
	check="true"

	if(document.getElementsByClassName("vorname_input")[0].value=="")
	{
		document.getElementsByClassName("vorname_input")[0].style.border="1px solid red";	
		check="false"
	}
	else
		document.getElementsByClassName("vorname_input")[0].style.border="1px solid #e6e6e6";	

	if(document.getElementsByClassName("nachname_input")[0].value=="")
	{
		document.getElementsByClassName("nachname_input")[0].style.border="1px solid red";		
		check="false"
	}
	else
		document.getElementsByClassName("nachname_input")[0].style.border="1px solid #e6e6e6";	

	if(document.getElementsByClassName("adresse_input")[0].value=="")
	{
		document.getElementsByClassName("adresse_input")[0].style.border="1px solid red";	
		check="false"
	}	
	else
		document.getElementsByClassName("adresse_input")[0].style.border="1px solid #e6e6e6";		
				
	if(document.getElementsByClassName("plz_input")[0].value=="")
	{
		document.getElementsByClassName("plz_input")[0].style.border="1px solid red";	
		check="false"
	}
	else
		document.getElementsByClassName("plz_input")[0].style.border="1px solid #e6e6e6";	
	
	if(document.getElementsByClassName("stadt_input")[0].value=="")
	{
		document.getElementsByClassName("stadt_input")[0].style.border="1px solid red";	
		check="false"
	}
	else
		document.getElementsByClassName("stadt_input")[0].style.border="1px solid #e6e6e6";	
		
	return check
}

function bestellung_bearbeiten_uebernehmen()
{
	
	if(check_fields()=="true")

		initMap(document.getElementsByClassName("adresse_input")[0].value,document.getElementsByClassName("plz_input")[0].value,document.getElementsByClassName("stadt_input")[0].value);
	else
		alert_userdata_2("ADRESSDETAILS ANGEBEN","Bitte alle Adressfelder ausfüllen!")
	


	
}

function alert_rechnungsbetrag()
{

	j=0;
	item="";

	zaehler=-1;

	

	while(j<=bestelldetails.length-1)
	{


		item=item+bestelldetails[j].style+",";
		item=item+bestelldetails[j].stylecode+",";
		item=item+bestelldetails[j].color+",";
		item=item+bestelldetails[j].bhgroesse+",";
		item=item+bestelldetails[j].slipgroesse+",";
		item=item+parseInt(document.getElementsByClassName("select_anzahl")[j].selectedIndex+1)+",";
		item=item+bestelldetails[j].preis+",";
		zaehler=zaehler+1;
		j=j+1;
	}

	
	$.ajax({
			type: "GET",
			url: "/hello/change_order_check/",
			dataType: "json",
			data: { "bestellnummer":bestellung[0].bestellnummer,"item":  item,"item-length":  zaehler,'unternehmensdetails':document.getElementsByClassName("unternehmensdetails_input")[0].value,'stadt':document.getElementsByClassName("stadt_input")[0].value,'adresse':document.getElementsByClassName("adresse_input")[0].value,'plz':document.getElementsByClassName("plz_input")[0].value,'lieferdetails':document.getElementById("lieferdetails_textarea").value,'bestellungspreis':parseFloat(bestellung[0].bestellungspreis)+aenderung},
			success: function(data) {

				if (data=="nicht genuegend Warenmenge")
					alert_userdata("ZUSÄTZLICHE MENGEN NICHT VERFÜGBAR","Da war ein anderer Kunde schneller. Zusätzliche Mengen sind von dem Set nicht mehr verfügbar. Diese Seite wird neu geladen.")
				else
				{
					if (data=="nicht genuegend Fahrer")
						alert_userdata("ZUSTELLZEIT NICHT MEHR VERFÜGBAR","Da war ein anderer Kunde schneller. Leider ist Deine gewünschte Zustellzeit ist nicht mehr verfügbar.")
					else
					{
						
							$.ajax({
							type: "GET",
							url: "/hello/get_rebates/",
							dataType: "json",
							data: { "bestellnummer":bestellung[0].bestellnummer,"item":  item,"item-length":  zaehler,"aenderung":"ja"},
							success: function(data) {
								
								rebates=JSON.parse(data)
						

								
										if (rebates[0].aenderung_rechnungsbetrag>0)
											alert_userdata_2("HÖHERER RECHNUNGSBETRAG","Die Änderung Deiner Bestellung führt zu einem höheren Rechnungsbetrag. Bitte bestätige, dass wir Deine Kreditkarte um "+replace_dot_comma(parseFloat(rebates[0].aenderung_rechnungsbetrag))+" EUR belasten dürfen.","<div  class='button_rechnungsbetrag_abbrechen'  onclick='alert_click_schliessen1()' >Abbrechen</div>\r<div  class='button_rechnungsbetrag_akzeptieren'  onclick='alert_rechnungsbetrag_akzeptieren()' >Akzeptieren</div>\r<span class='stretch'></span>\r</div>\r")
										else
											alert_userdata_2("GERINGERER RECHNUNGSBETRAG","Die Änderung Deiner Bestellung führt zu einem geringeren Rechnungsbetrag. Bitte bestätige, dass wir Dir "+replace_dot_comma(parseFloat(-rebates[0].aenderung_rechnungsbetrag))+" EUR gutschreiben werden.","<div  class='button_rechnungsbetrag_abbrechen'  onclick='alert_click_schliessen1()' >Abbrechen</div>\r<div  class='button_rechnungsbetrag_akzeptieren'  onclick='alert_rechnungsbetrag_akzeptieren()' >Akzeptieren</div>\r<span class='stretch'></span>\r</div>\r")
											

							}
					})
		
						
					}
				}	
			}
	});
} 


  function button_logo(index,text_area,button_)
 {

	 
	 if (index==0)
	 {

		document.getElementsByClassName(""+button_+"")[0].innerHTML="";

		document.getElementsByClassName(""+button_+"")[0].style.background="url('/static/ajax-loader.gif')";
		document.getElementsByClassName(""+button_+"")[0].style.backgroundsSize="15px 15px";
		document.getElementsByClassName(""+button_+"")[0].style.backgroundPosition="absolute";
		document.getElementsByClassName(""+button_+"")[0].style.backgroundColor="#ff761a";
		document.getElementsByClassName(""+button_+"")[0].style.backgroundPosition="center center";



		document.getElementsByClassName(""+button_+"")[0].style.backgroundRepeat="no-repeat";


		document.getElementsByClassName(""+button_+"")[0].style.pointerEvents = 'none';

		

		

		
	 }
	 else
	 {
		document.getElementsByClassName(""+button_+"")[0].innerHTML=text_area;
		document.getElementsByClassName(""+button_+"")[0].style.background="";

		document.getElementsByClassName(""+button_+"")[0].style.pointerEvents = 'atuo';	 
	 }
 }
 


 
 
  function alert_userdata_2(content1,content2,footer)
 {	 
	document.getElementById("alert_box_rechnungsbetrag_headline").innerHTML=content1;
	document.getElementById("alert_box_rechnungsbetrag_body").innerHTML=content2;
	document.getElementById("alert_box_rechnungsbetrag_footer").innerHTML=footer;
	$('#alert_box_rechnungsbetrag').modal('show');
	

 }
 

 


function alert_rechnungsbetrag_akzeptieren()
{

	//button_logo(0,"Akzeptieren","button_rechnungsbetrag_akzeptieren")

	bestellung_bestaetigen();
	$('#alert_box_rechnungsbetrag').modal('hide');
	
	
	
}



function adresse_ok()
{

	if (rebates[0].aenderung_rechnungsbetrag>0 || rebates[0].aenderung_rechnungsbetrag<0)
		alert_rechnungsbetrag();
	else
		bestellung_bestaetigen();
}



 function input_on_change(element,element2)
{
	element.style.border="1px solid #e6e6e6 ";	
	element2.style.color="#4E4E4E";
}
 
 
 
function bestellung_bestaetigen()
{		

	j=0;
	item="";

	zaehler=-1;

	

	while(j<=bestelldetails.length-1)
	{


		item=item+bestelldetails[j].style+",";
		item=item+bestelldetails[j].stylecode+",";
		item=item+bestelldetails[j].color+",";
		item=item+bestelldetails[j].bhgroesse+",";
		item=item+bestelldetails[j].slipgroesse+",";
		item=item+parseInt(document.getElementsByClassName("select_anzahl")[j].selectedIndex+1)+",";
		item=item+bestelldetails[j].preis+",";
		zaehler=zaehler+1;
		j=j+1;
	}


	$.ajax({
			type: "POST",
			url: "/hello/change_order/",
			dataType: "json",
			data: { "aenderung":"","bestellnummer":bestellung[0].bestellnummer,"item":  item,"item-length":  zaehler,'unternehmensdetails':document.getElementsByClassName("unternehmensdetails_input")[0].value,'nachname':document.getElementsByClassName("nachname_input")[0].value,'vorname':document.getElementsByClassName("vorname_input")[0].value,'stadt':document.getElementsByClassName("stadt_input")[0].value,'adresse':document.getElementsByClassName("adresse_input")[0].value,'plz':document.getElementsByClassName("plz_input")[0].value,'lieferdetails':document.getElementById("lieferdetails_textarea").value,'bestellungspreis':parseFloat(bestellung[0].bestellungspreis)+aenderung},
			success: function(data) {

				if (data=="nicht genuegend Warenmenge")
				{
					alert_click_schliessen1();
					alert_userdata("ZUSÄTZLICHE MENGEN NICHT VERFÜGBAR","Da war ein anderer Kunde schneller. Zusätzliche Mengen sind von dem Gericht nicht mehr verfügbar. Diese Seite wird neu geladen.")
				}
				else
				{

						$.ajax({
								type: "POST",
								url: "/hello/bestelldetails_abrufen/",
								dataType: "json",
								data: { "bestellnummer":bestellung[0].bestellnummer},
								success: function(data) {
									document.getElementsByClassName("bestelldetails_daten")[0].innerHTML=data;
									bestelldetails=JSON.parse(document.getElementsByClassName("bestelldetails_daten")[0].innerHTML)	
											
												
												$.ajax({
														type: "POST",
														url: "/hello/bestellung_abrufen/",
														dataType: "json",
														data: { "bestellnummer":bestellung[0].bestellnummer},
														success: function(data) {
															
															alert_click_schliessen1();
															document.getElementsByClassName("bestellung_daten")[0].innerHTML=data;															
															bestellung=JSON.parse(document.getElementsByClassName("bestellung_daten")[0].innerHTML)	


															$.ajax({
																	type: "GET",
																	url: "/hello/get_rebates/",
																	dataType: "json",
																	data: { "bestellnummer":bestellung[0].bestellnummer,"item":  item,"item-length":  zaehler,"aenderung":""},
																	success: function(data) {
																		rebates=JSON.parse(data)
															
															
															
																		document.getElementsByClassName("button_uebernehmen")[0].style.display="none";
																		
																		document.getElementsByClassName("button_abbrechen")[0].style.display="none";
																		
																		document.getElementsByClassName("button_bearbeiten")[0].style.display="block";
																		
			
																		
																		lieferuebersicht();
																		
																		bestellung_block();
																		
																		initialize()
																		bestellte_lingerie_anzeigen();
																		
																	}
																	
															})
															
															
												
															

														}
												});
									
												
												
									
		
									
						
									

								}
						});
					}
				}
			
		});	

	


}



function bestellung_bearbeiten_abbrechen()
{
	document.getElementsByClassName("button_uebernehmen")[0].style.display="none";
	document.getElementsByClassName("button_abbrechen")[0].style.display="none";
	document.getElementsByClassName("button_bearbeiten")[0].style.display="block";

	lieferuebersicht();
	bestellung_block();
	bestellte_lingerie_anzeigen();	
	
}
function bestellung_aufrufen()
{
	
	bestellung=JSON.parse(document.getElementsByClassName("bestellung_daten")[0].innerHTML)
	rebates=JSON.parse(document.getElementsByClassName("rebates")[0].innerHTML)



	lingerieselection=JSON.parse(document.getElementsByClassName("lingerie_daten")[0].innerHTML)
		
	bestelldetails=JSON.parse(document.getElementsByClassName("bestelldetails_daten")[0].innerHTML)	

}

function profil_hauptseite()
{
	
	window.location.href="/hello/account_page/";
}


function bestellung_bearbeiten_hauptseite()
{
	
	window.location.href="/hello/account_page/bestellungen_ansehen/";
}



function bestellung_block()
{
	

	var maxim= document.getElementsByClassName("zahlung");

	preis_=	replace_dot_comma(parseFloat(bestellung[0].bestellungspreis));
	

	
	rabatt=parseFloat(bestellung[0].rabatt);
	var gesamt=parseFloat(bestellung[0].bestellungspreis)+parseFloat(bestellung[0].lieferkosten)+rabatt+aenderung-bestellung[0].braforfreevalue-bestellung[0].storecredit;

	preis_=	replace_dot_comma(parseFloat(bestellung[0].bestellungspreis));
	rabatt_=	replace_dot_comma(parseFloat(bestellung[0].rabatt));
	preis_gesamt=	replace_dot_comma(gesamt);
	lieferung=replace_dot_comma(parseFloat(bestellung[0].lieferkosten))


	var uebersicht="<div style='width:50%;float:left;'>Bestellung:</div><div style='float:right;width:50%;text-align:right;'>"+replace_dot_comma(rebates[0].bestellung)+" EUR</div><br>";
	if (rebates[0].aenderung!=0)
		uebersicht=uebersicht+"<div style='float:left;color:red;'>Bestelländerung:</div><div style='float:right;color:red;'>"+replace_dot_comma(parseFloat(rebates[0].aenderung))+" EUR</div><br>";

	uebersicht=uebersicht+"<div style='width:50%;float:left;'>Lieferung:</div><div style='float:right;width:50%;text-align:right;'>KOSTENLOS</div><br>";
	
	if(rebates[0].braforfreevalue!=0)
		uebersicht=uebersicht+"<div style='width:50%;float:left;'>Sets umsonst (VIP):</div><div style='float:right;width:50%;text-align:right;'>-"+replace_dot_comma(parseFloat(rebates[0].braforfreevalue))+" EUR</div><br>";
	if(rebates[0].storecredit!=0)
		uebersicht=uebersicht+"<div style='width:50%;float:left;'>VIP Guthaben:</div><div style='float:right;width:50%;text-align:right;'>-"+replace_dot_comma(parseFloat(rebates[0].storecredit))+" EUR</div><br>";



	if(rebates[0].coupon!=0)
		uebersicht=uebersicht+"<div style='float:left;'>Rabatt:</div><div style='float:right;'>-"+replace_dot_comma(parseFloat(rebates[0].coupon))+" EUR</div><br>";	


	if(rebates[0].credit!=0)
		uebersicht=uebersicht+"<div style='float:left;'>Freundschaftswerbung:</div><div style='float:right;'>-"+replace_dot_comma(parseFloat(rebates[0].credit))+" EUR</div><br>";	
		
		
	uebersicht=uebersicht+"<div style='border-bottom:1px solid #e6e6e6 ;'></div>";
	

	if (rebates[0].aenderung!=0)
		uebersicht=uebersicht+"<div style='float:left;font-weight: bold;color:red;'>Gesamt:</div><div style='float:right;font-weight: bold;color:red;'>"+replace_dot_comma(rebates[0].gesamtpreis)+" EUR</div><br><br>";
	else
		uebersicht=uebersicht+"<div style='float:left;font-weight: bold;'>Gesamt:</div><div style='float:right;font-weight: bold;'>"+replace_dot_comma(rebates[0].gesamtpreis)+" EUR</div><br><br>";
	
	if (bestellung[0].zahlungsoption=="0")
		uebersicht=uebersicht+"<div style='line-Height:18px'>Zahlung per Kreditkarte: ****-****-****-"+bestellung[0].kartennummer+"</div>";

	
	maxim[0].innerHTML=uebersicht+"</div>";
	




	
	
}

function bestellnummer_abrufen()
{
	
	document.getElementsByClassName("bestellnummer")[0].innerHTML="Bestellnummer: "+bestellung[0].bestellnummer.toUpperCase();
	document.getElementsByClassName("headline_text")[0].innerHTML="Bestelldatum: "+bestellung[0].datum;
	
	//.toUpperCase();
}


function lieferuebersicht()
{
	
	var maxim= document.getElementsByClassName("lieferung_i");
	uebersicht="<b>Lieferadresse:</b><br>";

		

	
	uebersicht=uebersicht+"<br><div class='adresse_bearbeiten' style='display:none;float:left;margin-bottom:10px;width:100%;'><input type='text' placeholder='Vorname'  class='vorname_input' value='"+bestellung[0].vorname+"' style='width:40%;float:left;' onkeypress='change()' onkeyup='change()'></input><input type='text' placeholder='Nachname' class='nachname_input'  style='width:50%;float:right;'  value='"+bestellung[0].nachname+"' onkeypress='change()' onkeyup='change()'></input><br><br><input type='text' placeholder='Unternehmensdetails' id='locality' class='unternehmensdetails_input'  style='width:100%;float:left;'  value='"+bestellung[0].unternehmensdetails+"' onkeypress='change()' onkeyup='change()'></input><br><br><input type='text' placeholder='Adresse' id='route' class='adresse_input' value='"+bestellung[0].adresse+"' style='width:100%;float:left;' onkeypress='change()' onkeyup='change()'></input><br><br><input type='text' placeholder='PLZ' maxlength='5' id='postal_code' class='plz_input' value='"+bestellung[0].plz+"' style='width:40%;float:left;' onkeypress='change()' onkeyup='change()'></input><input type='text' placeholder='Stadt' id='locality' class='stadt_input'  style='width:50%;float:right;'  value='"+bestellung[0].stadt+"' onkeypress='change()' onkeyup='change()'></input></div>";
	
	
	uebersicht=uebersicht+"<div class='adresse_anzeigen' style='display:block;float:left'>"+bestellung[0].vorname+" "+bestellung[0].nachname+"</div><br>";
	if(bestellung[0].unternehmensdetails!="")
		uebersicht=uebersicht+"<div class='adresse_anzeigen' style='display:block;float:left'>"+bestellung[0].unternehmensdetails+"</div><br>";
	uebersicht=uebersicht+"<div class='adresse_anzeigen' style='display:block;float:left'>"+bestellung[0].adresse+"</div><br>";
	


	
	uebersicht=uebersicht+"<div class='plz_stadt_anzeigen' style='display:block;float:left;'>"+bestellung[0].plz+" "+bestellung[0].stadt+"</div><br><br>";

	uebersicht=uebersicht+"<div id='lieferhinweise_headline'><br><br><b>Lieferhinweise: </b><br></div>";
	uebersicht=uebersicht+"<div class='lieferhinweise_anzeigen' style='display:block;float:left;width:100%;'>"+bestellung[0].lieferdetails+"</div>";
	uebersicht=uebersicht+"<div class='lieferhinweise_bearbeiten' style='display:none;float:left;width:100%;'><textarea class='textarea_lieferhinweise' id='lieferdetails_textarea' name='html_elemente' cols='50' rows='15' maxlength='10000'  placeholder='Bitte gib hier Details zur Sendungsübergabe an.' onkeypress='change()' onkeyup='change()'>"+bestellung[0].lieferdetails+"</textarea></div>";

	
	maxim[0].innerHTML=uebersicht;

	if(bestellung[0].lieferdetails=="")
		document.getElementById("lieferhinweise_headline").style.display="none";
	
}





function replace_dot_comma(zahl)
{
	var zahl_=	zahl.toFixed(2);
	zahl_ = zahl_.toString();
	return zahl_.replace(".", ",");
}

function compareLastColumn(a, b) {
    if (a[4] === b[4]) {
        return 0;
    }
    else {
        return (a[4] < b[4]) ? -1 : 1;
    }
}

