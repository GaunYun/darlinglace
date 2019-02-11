var bestellung,bestelldetails, ruecksendungen;

function ruecksendungen_anzeigen()
{
	ruecksendungen=JSON.parse(document.getElementsByClassName("ruecksendungen_daten")[0].innerHTML)
	
	i=0;
	box=""
	zaehler=0;
	while(i<=ruecksendungen.length-1)
	{
		
		j=i;
		gesamt=0;
		
		while(j<=ruecksendungen.length-1)
		{

			if(ruecksendungen[j].id!=ruecksendungen[i].id)
			{
				box=box+"</div>"
				break;
			}
			else
			{
				index=j;
				j=j+1;
			}
		}

		gesamt=ruecksendungen[i].verrechnungmitrabatt

	
		
		box=box+"<div class='header_style_3'>";
		
		
		box=box+"<div class='oberes_feld' style='width:100%;height:100px;'>"
		box=box+"<div class='adressdetails'>";
		box=box+"<div style='vertical-align:middle;height:100px;display:table-cell;''>"
		box=box+"<div class='adresse_name'>Rücksende-Nr.: "+ruecksendungen[i].id+"<br>"
		box=box+"</div>"
		box=box+"<b>Erstattung: "+replace_dot_comma(gesamt)+" €</b>"

		box=box+"</div>"
		box=box+"</div>"
		
		

		
		box=box+"<div class='standard_feld_zurueckschicken'>"	
		box=box+"<div class='shop_2'>Zurückschicken bis:<br><b>"+ruecksendungen[i].dateofmaxreturn		
		box=box+"</b></div></div>"


		box=box+"<div class='standard_feld'>"	
		box=box+"<div class='shop_2'>Status:<br><b>"+ruecksendungen[i].status		
		box=box+"</b></div></div>"	
		
		box=box+"<div style='float:left;width:2%;height:100px;border-left: 1px solid #e6e6e6 ;'>"		
		box=box+"</div>"
		box=box+"<div style='float:left;width:10%;height:100px;'>"		
		box=box+"<div class='bearbeiten_feld' onclick='details_ansehen("+zaehler+")'>Details</div>"
		box=box+"</div>"
		box=box+"</div>"


	

		box=box+"<div class='zusammenfassung' style='display:none;'>\r"

		box=box+"<b>Kostenlose Sets: "+(ruecksendungen[index].bra4free).toString()+"</b><br>"
		box=box+"<b>Freundschaftswerbung: "+replace_dot_comma(parseFloat(ruecksendungen[index].credit))+" €</b><br>"
		box=box+"<b>Storecredit: "+replace_dot_comma(-parseFloat(ruecksendungen[index].storecredit))+" €</b><br>"
		
		box=box+"<div class='untere_linie'>"
		box=box+"<div class='linie_2_ruecksendungen'></div>"
		box=box+"</div>"
		j=i;
		
		while(j<=ruecksendungen.length-1)
		{
			if(ruecksendungen[j].id!=ruecksendungen[i].id)
			{
				box=box+"</div>"
				break;
			}
				
			else
			{
		pictures_ruecksendungen=JSON.parse(ruecksendungen[j].picture_link_small)
				box=box+"<div style='float:left;width:100%;'>"
				box=box+"<div class='block_left'>"
				box=box+"<img src='"+pictures_ruecksendungen[0].link+"' style='height:100px;float:left;'/>"
				box=box+"<div style='margin-left:10px;float:left;'/><b>"+ruecksendungen[j].style+"</b></div>"

				

				box=box+"<br><div style='float:left;font-size:12px;margin-left:10px;'>"+ruecksendungen[j].bhgroesse+"</div> <br>"
				box=box+"<div style='float:left;font-size:12px;margin-left:10px;'>"+ruecksendungen[j].slipgroesse+"</div><br><br>"
				
				box=box+"<div style='float:left;font-size:12px;margin-left:10px;'>Zurücksenden: "+ruecksendungen[j].anzahl+"x</div>"
				box=box+"</div>";
				
				box=box+"<div class='ruecksendegrund' style='display:block'>"
				box=box+"<div class='block_right'><b>Rücksendegrund: "+ruecksendungen[j].grund+"</b></div>"
				box=box+"</div></div>"
				
				
				box=box+"<div class='untere_linie'>"
				box=box+"<div class='linie_2_ruecksendungen'></div>"
				box=box+"</div>"

				
				
				
				j=j+1;
			}
		}
		box=box+"</div>"

			
		i=j;
		zaehler=zaehler+1;
		
	}

	
	document.getElementById("existierende_rueckmeldungen_anzeigen").innerHTML =box;
	
}


function print_label(i)
{
	window.open(ruecksendungen[i].versandlabel); 
}


function details_ansehen(index)
{
	if(document.getElementsByClassName("bearbeiten_feld")[index].innerHTML=="Details")
	{
		document.getElementsByClassName("oberes_feld")[index].style.borderBottom="1px solid #e6e6e6";
		document.getElementsByClassName("zusammenfassung")[index+1+1].style.display="block";
		document.getElementsByClassName("bearbeiten_feld")[index].innerHTML="Schließen"
	}
	else
	{
		document.getElementsByClassName("oberes_feld")[index].style.borderBottom="";
		document.getElementsByClassName("zusammenfassung")[index+1+1].style.display="none";
		document.getElementsByClassName("bearbeiten_feld")[index].innerHTML="Details"
	}		
}

function zuruecksenden_hinzufuegen()
{

	document.getElementsByClassName("header_style")[0].style.display="block"
	document.getElementsByClassName("button_bestellung_zuruecksenden")[0].style.opacity="0.3"
	document.getElementsByClassName("button_bestellung_zuruecksenden")[0].style.pointerEvents = 'none';
	document.getElementsByClassName("neue_ruecksendung_button")[0].style.opacity="0.3"
	document.getElementsByClassName("neue_ruecksendung_button")[0].style.pointerEvents = 'none';	
	

	
}


function select_ruecksendung()
{

	if(document.getElementsByClassName("eingabefeld_bestellnummer")[0].selectedIndex>=1)
	{
		document.getElementsByClassName("neue_ruecksendung_button")[0].style.opacity="1.0"
		document.getElementsByClassName("neue_ruecksendung_button")[0].style.pointerEvents = 'auto';	
	}
	else
	{
		document.getElementsByClassName("neue_ruecksendung_button")[0].style.opacity="0.3"
		document.getElementsByClassName("neue_ruecksendung_button")[0].style.pointerEvents = 'none';	
	}
		

}

function load_bestellnummern()
{

	bestellung=JSON.parse(document.getElementsByClassName("bestellungen")[0].innerHTML);

	i=0;

	document.getElementsByClassName("eingabefeld_bestellnummer")[0].innerHTML="<option></option>"

	while(i<=bestellung.length-1)
	{

		if(bestellung[i].status!="Zugestellt")
			document.getElementsByClassName("eingabefeld_bestellnummer")[0].innerHTML=document.getElementsByClassName("eingabefeld_bestellnummer")[0].innerHTML+"<option>"+bestellung[i].bestellnummer+" vom "+bestellung[i].datum+"</option>"
		else
			document.getElementsByClassName("eingabefeld_bestellnummer")[0].innerHTML=document.getElementsByClassName("eingabefeld_bestellnummer")[0].innerHTML+"<option disabled='true'>"+bestellung[i].bestellnummer+" vom "+bestellung[i].datum+" (Noch nicht zugestellt)</option>"		
		i=i+1;
	}

}


function ruecksendung_neu()
{
 						page_load(0);
						button_logo("0","neue_ruecksendung_button_id_text","neue_ruecksendung_button_id_logo","neue_ruecksendung_button_id")
	$.ajax({
			timeout:15000,
 			error: function(){		
 						page_load(1);
						button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	},
		type: "POST",
		url: "/bestelldetails_abrufen/",
		dataType: "json",
		data: { "bestellnummer":bestellung[document.getElementsByClassName("eingabefeld_bestellnummer")[0].selectedIndex-1].bestellnummer},
		success: function(data) {
 						page_load(1);
						button_logo("1","neue_ruecksendung_button_id_text","neue_ruecksendung_button_id_logo","neue_ruecksendung_button_id")
			bestelldetails=JSON.parse(data)
			
			
			zaehler=0;
	
			j=0;
			box="";
			document.getElementsByClassName("neue_ruecksendung_button")[0].style.opacity="0.3"
			document.getElementsByClassName("neue_ruecksendung_button")[0].style.pointerEvents = 'none';	
			while(j<=bestelldetails.length-1)
			{
				i=0;
				netto_anzahl=bestelldetails[j].anzahl
				
				while(i<=ruecksendungen.length-1)
				{
					if(bestelldetails[j].bhgroesse!="")
					{
						if(ruecksendungen[i].bestellnummer==bestellung[document.getElementsByClassName("eingabefeld_bestellnummer")[0].selectedIndex-1].bestellnummer && ruecksendungen[i].slipgroesse==bestelldetails[j].slipgroesse && ruecksendungen[i].bhgroesse==bestelldetails[j].bhgroesse && ruecksendungen[i].colorcode==bestelldetails[j].color && ruecksendungen[i].stylecode==bestelldetails[j].stylecode)
						{	
	
							netto_anzahl=netto_anzahl-parseInt(ruecksendungen[i].anzahl)
	
						}
					}
					else
					{
						if(ruecksendungen[i].bestellnummer==bestellung[document.getElementsByClassName("eingabefeld_bestellnummer")[0].selectedIndex-1].bestellnummer && ruecksendungen[i].slipgroesse==bestelldetails[j].slipgroesse && ruecksendungen[i].colorcode==bestelldetails[j].color)
						{	
	
							netto_anzahl=netto_anzahl-parseInt(ruecksendungen[i].anzahl)
	
						}
					}
					i=i+1;
				}
		pictures_bestelldetails=JSON.parse(bestelldetails[j].picture_link_small)
				box=box+"<div style='float:left;width:100%;'>"
				box=box+"<div class='block_left'><img src='"+pictures_bestelldetails[0].link+"' style='height:100px;float:left;'/>"
				box=box+"<div style='margin-left:10px;float:left;'/><b>"+bestelldetails[j].style+"</b></div>"
				box=box+"<br><div style='float:left;font-size:12px;margin-left:10px;'>"+bestelldetails[j].bhgroesse+"</div> <br>"
				box=box+"<div style='float:left;font-size:12px;margin-left:10px;'>"+bestelldetails[j].slipgroesse+"</div><br><br>"
				box=box+"<div style='float:left;font-size:12px;margin-left:10px;'></div><br> "
				box=box+"<div style='float:left;font-size:12px;margin-left:10px;'>Bestellt: "+bestelldetails[j].anzahl+"x</div>"
				if(netto_anzahl!=bestelldetails[j].anzahl)
					box=box+"<br><div style='float:left;font-size:12px;margin-left:10px;'>Zurückgesendet: "+parseInt(parseInt(bestelldetails[j].anzahl)-parseInt(netto_anzahl))+"x</div>"
					
				box=box+"</div>"


				box=box+"<div class='block_right'>"
				if(netto_anzahl>0)
					box=box+"<input type='checkbox' id='"+zaehler+"' onclick='checkbox_click("+zaehler+")'>Zurücksenden</input><br><br>"
				else
					box=box+"<div style='display:none;'><input type='checkbox' id='"+zaehler+"' onclick='checkbox_click("+zaehler+")'>Zurücksenden</input></div><br><br><br>"
				
				
				box=box+"<div style='float:left'>"
				box=box+"<div class='ruecksendung_anzahl' style='display:none;float:left;'>"

				
				box=box+"<div >Anzahl: <br><select class='anzahl'>"
				i=1;
				while(i<=netto_anzahl)
				{
					box=box+"<option>"+i+"</option>"
					
					i=i+1;
				}
				box=box+"</select></div>"
				box=box+"</div>"
				
				box=box+"<div class='ruecksendegrund_angeben' style='display:none;float:left;margin-left:10px;'>"
				box=box+"<div >Rücksendegrund: <br><select class='ruecksendegrund_select'  onchange='ruecksendegrund_select_change("+zaehler+")'>"
				box=box+"<option></option>"
				box=box+"<option>Zu groß ausgefallen</option>"
				box=box+"<option>Zu klein ausgefallen</option>"
				box=box+"<option>Farbe hat nicht gefallen</option>"
				box=box+"<option>Stil hat nicht gefallen</option>"
				box=box+"<option>Artikel beschädigt</option>"
				box=box+"<option>Falsche Lieferung</option>"
				box=box+"<option>Zu späte Lieferung</option>"
				box=box+"<option>Anderes</option>"
				box=box+"</select></div>"
				box=box+"</div>"
				box=box+"</div>"
				box=box+"</div>";
				box=box+"</div>";
				box=box+"<div class='untere_linie'>"
				box=box+"<div class='linie_2_ruecksendungen'></div>"
				box=box+"</div>"
				j=j+1;
				zaehler=zaehler+1;
			}
			
			box=box+"<button class='button_main' id='ruecksendegrund_click_id' style='opacity:0.3;pointer-events:none;width:250px;' onclick='ruecksendegrund_click()'><i class='fa fa-circle-o-notch fa-spin' id='ruecksendegrund_click_id_logo' style='display:none'></i><div id='ruecksendegrund_click_id_text'>Rücksendung beauftragen</div> </button>";	

			document.getElementsByClassName("zusammenfassung")[1].innerHTML=box;
			
		}
	});
}


function ruecksendegrund_select_change(id)
{

	document.getElementsByClassName("ruecksendegrund_select")[id].style.backgroundColor="#ffffff";
	document.getElementsByClassName("ruecksendegrund_select")[id].style.color="#4d4d4d"; 	
	
}

function ruecksendegrund_click()
{
	j=0;
	status="not"
	while(j<=bestelldetails.length-1)
	{
		if(document.getElementById(""+j+"").checked==true)
			if(document.getElementsByClassName("ruecksendegrund_select")[j].value=="")
			{
				document.getElementsByClassName("ruecksendegrund_select")[j].style.backgroundColor="red"
				document.getElementsByClassName("ruecksendegrund_select")[j].style.color="#ffffff"
				status="not";
				
				break;

			}
			else
				status="ok"
		j=j+1;
	}
	
	if(status=="ok")
		ruecksendung_beauftragen()
	else
		alert_userdata("RÜCKSENDEGRUND ANGEBEN","Damit Deine Artikel zurückgeschickt werden kann, gib bitte noch einen Rücksendegrund an.")

}


function checkbox_click(id)
{

	if(document.getElementById(""+id+"").checked==true)
	{


		document.getElementsByClassName("ruecksendegrund_angeben")[id].style.display="block";

		document.getElementsByClassName("ruecksendung_anzahl")[id].style.display="block";
		document.getElementsByClassName("button_main")[0].style.opacity="1.0"
		document.getElementsByClassName("button_main")[0].style.pointerEvents = 'auto';	

	}
	else
	{
		check_other_ckeckboxes();
		document.getElementsByClassName("ruecksendegrund_angeben")[id].style.display="none";
		document.getElementsByClassName("ruecksendung_anzahl")[id].style.display="none";
		document.getElementsByClassName("ruecksendegrund_select")[id].style.backgroundColor="#ffffff";
		document.getElementsByClassName("ruecksendegrund_select")[id].style.color="#4d4d4d"; 	
	}

}

function check_other_ckeckboxes()
{
		j=0;
	status="not ok"
	while(j<=bestelldetails.length-1)
	{
		if(document.getElementById(""+j+"").checked==true)
			status="ok"
		j=j+1;
	}
	
	if(status=="ok")
	{
		document.getElementsByClassName("button_main")[0].style.opacity="1.0"
		document.getElementsByClassName("button_main")[0].style.pointerEvents = 'auto';	
	}
	else
	{
		document.getElementsByClassName("button_main")[0].style.opacity="0.3"
		document.getElementsByClassName("button_main")[0].style.pointerEvents = 'none';	
	}
	
}

function replace_dot_comma(zahl)
{
	var zahl_=	zahl.toFixed(2);
	zahl_ = zahl_.toString();
	return zahl_.replace(".", ",");
}

function ruecksendung_beauftragen()
{
	bestellnummer=""
	stylecode=""
	colorcode=""
	anzahl=""
	grund=""
	gesamt=""
	bhgroesse=""
	slipgroesse=""
	j=0;
	zaehler=-1;
	while(j<=bestelldetails.length-1)
	{

		if(document.getElementById(""+j+"").checked==true)
		{
			bestellnummer=bestellung[document.getElementsByClassName("eingabefeld_bestellnummer")[0].selectedIndex-1].bestellnummer

			stylecode=stylecode+bestelldetails[j].stylecode+";";
			
			colorcode=colorcode+bestelldetails[j].color+";";

			anzahl=anzahl+document.getElementsByClassName("anzahl")[j].value+";";

			grund=grund+document.getElementsByClassName("ruecksendegrund_select")[j].value+";";

			gesamt=gesamt+parseFloat(bestelldetails[j].preis)*parseInt(document.getElementsByClassName("anzahl")[j].value)+";"
			bhgroesse=bhgroesse+bestelldetails[j].bhgroesse+";";
			slipgroesse=slipgroesse+bestelldetails[j].slipgroesse+";";

			zaehler=zaehler+1;
			
			
		}
		j=j+1;
		
	}

						button_logo("0","ruecksendegrund_click_id_text","ruecksendegrund_click_id_logo","ruecksendegrund_click_id")
						
		$.ajax({
				timeout:15000,
 				error: function(){								
								button_logo("1","ruecksendegrund_click_id_text","ruecksendegrund_click_id_logo","ruecksendegrund_click_id")	},
		type: "POST",
		url: "/ruecksendung_calcualte_wert/",
		dataType: "json",
		data: { "bestellnummer":bestellnummer,'stylecode':stylecode,'colorcode':colorcode,'anzahl':anzahl,'grund':grund,'item-length':zaehler,'gesamt':gesamt,'bhgroesse':bhgroesse,'slipgroesse':slipgroesse},
		success: function(data) {
						button_logo("1","ruecksendegrund_click_id_text","ruecksendegrund_click_id_logo","ruecksendegrund_click_id")
			ruecksendung_bestaetigen=JSON.parse(data)
			
			
			neue_ruecksendung=JSON.parse(ruecksendung_bestaetigen[0].neue_ruecksendung)
			alte_ruecksendung=JSON.parse(ruecksendung_bestaetigen[0].alte_ruecksendung)
			gesamtbestellung=JSON.parse(ruecksendung_bestaetigen[0].gesamtbestellung)
			
			
			erstattung=parseFloat(gesamtbestellung[0].gesamtpreis)-parseFloat(neue_ruecksendung[0].gesamtpreis)-parseFloat(alte_ruecksendung[0].erstattung)
			
			textbaustein_1="Schade, dass Dir etwas nicht gefallen hat. Bitte bestätige Deine Rücksendung. Dir wird dann an "+document.getElementById("email").innerHTML+" ein kostenfreies Rücksendeetikett von DHL gesandt. <br><br> Für Deine Rücksendung erstatten wir Dir "+replace_dot_comma(erstattung)+" € spätestens nach Erhalt der Ware.<br>"

			
			if(parseInt(gesamtbestellung[0].braforfreecount)>parseInt(neue_ruecksendung[0].braforfreecount)+parseInt(alte_ruecksendung[0].bra4free))
				if(parseInt(gesamtbestellung[0].braforfreecount)-parseInt(neue_ruecksendung[0].braforfreecount)+parseInt(alte_ruecksendung[0].bra4free)==1)
					textbaustein_1=textbaustein_1+"Zusätzlich wird Dir Deinem Kundenkonto ein kostenfreies Set für Deinen nächsten Einkauf gutgeschrieben.<br>"
				else
					textbaustein_1=textbaustein_1+"Zusätzlich werden Dir Deinem Kundenkonto "+(parseInt(gesamtbestellung[0].braforfreecount)-parseInt(neue_ruecksendung[0].braforfreecount)+parseInt(alte_ruecksendung[0].bra4free)).toString()+" kostenfreie Set für Deine nächsten Einkäufe gutgeschrieben.<br>"



			if(parseFloat(gesamtbestellung[0].storecredit)-parseFloat(neue_ruecksendung[0].storecredit)+parseFloat(alte_ruecksendung[0].storecredit))
				textbaustein_1=textbaustein_1+"Zusätzlich wird Dir "+replace_dot_comma(parseFloat(gesamtbestellung[0].storecredit)-parseFloat(neue_ruecksendung[0].storecredit)+parseFloat(alte_ruecksendung[0].storecredit))+" € VIP Credit wieder gutgeschrieben.<br>"
				
				
				
			if(parseFloat(gesamtbestellung[0].credit)-parseFloat(neue_ruecksendung[0].credit)+parseFloat(alte_ruecksendung[0].credit))
				textbaustein_1=textbaustein_1+"Zusätzlich wird Dir "+replace_dot_comma(parseFloat(gesamtbestellung[0].credit)-parseFloat(neue_ruecksendung[0].credit)+parseFloat(alte_ruecksendung[0].credit))+" € Guthaben aus Freundschaftswerbung wieder gutgeschrieben."			
							
			alert_userdata_ruecksendung_bestaetigen(textbaustein_1)
			
			

			
			}
		})			


	
	
}

function replace_dot_comma(zahl)
{
	var zahl_=	zahl.toFixed(2);
	zahl_ = zahl_.toString();
	return zahl_.replace(".", ",");
}

function alert_userdata_ruecksendung_bestaetigen(text)
{

	document.getElementsByClassName("ruecksendung_bestaetigen_text")[0].innerHTML=text;

	$('#zuruecksenden_bestaetigen').modal('show');

}

function ruecksendung_abbrechen()
{
	$('#zuruecksenden_bestaetigen').modal('hide');
}

function ruecksendung_bestaetigt()
{
	$('#zuruecksenden_bestaetigen').modal('hide');
	bestellnummer=""
	stylecode=""
	colorcode=""
	anzahl=""
	grund=""
	gesamt=""
	bhgroesse=""
	slipgroesse=""
	j=0;
	zaehler=-1;
	while(j<=bestelldetails.length-1)
	{

		if(document.getElementById(""+j+"").checked==true)
		{
			bestellnummer=bestellung[document.getElementsByClassName("eingabefeld_bestellnummer")[0].selectedIndex-1].bestellnummer

			stylecode=stylecode+bestelldetails[j].stylecode+";";
			
			colorcode=colorcode+bestelldetails[j].color+";";

			anzahl=anzahl+document.getElementsByClassName("anzahl")[j].value+";";

			grund=grund+document.getElementsByClassName("ruecksendegrund_select")[j].value+";";

			gesamt=gesamt+parseFloat(bestelldetails[j].preis)*parseInt(document.getElementsByClassName("anzahl")[j].value)+";"
			bhgroesse=bhgroesse+bestelldetails[j].bhgroesse+";";
			slipgroesse=slipgroesse+bestelldetails[j].slipgroesse+";";

			zaehler=zaehler+1;
			
			
		}
		j=j+1;
		
	}

						button_logo("0","ruecksendung_bestaetigt_id_text","ruecksendung_bestaetigt_id_logo","ruecksendung_bestaetigt_id")
 						page_load(0);
 						
 						
		
		$.ajax({
				timeout:15000,
 				error: function(){								
								button_logo("1","ruecksendegrund_click_id_text","ruecksendegrund_click_id_logo","ruecksendegrund_click_id")	},
		type: "POST",
		url: "/account_page/ruecksendung_beauftragen/",
		dataType: "json",
		data: {  "bestellnummer":bestellnummer,'stylecode':stylecode,'colorcode':colorcode,'anzahl':anzahl,'grund':grund,'item-length':zaehler,'gesamt':gesamt,'bhgroesse':bhgroesse,'slipgroesse':slipgroesse},
		success: function(data) {
			document.getElementsByClassName("ruecksendungen_daten")[0].innerHTML=data;
									button_logo("1","ruecksendung_bestaetigt_id_text","ruecksendung_bestaetigt_id_logo","ruecksendung_bestaetigt_id")
				document.getElementsByClassName("header_style")[0].style.display="none"
				document.getElementsByClassName("button_bestellung_zuruecksenden")[0].style.opacity="1.0"
				document.getElementsByClassName("button_bestellung_zuruecksenden")[0].style.pointerEvents = 'auto';
				document.getElementsByClassName("ruecksendungen_daten")[0].innerHTML=data;
				document.getElementsByClassName("zusammenfassung")[1].innerHTML="";
				document.getElementsByClassName("eingabefeld_bestellnummer")[0].selectedIndex=0;
				document.getElementsByClassName("ruecksendungen_daten")[0].innerHTML=data;
				ruecksendungen_anzeigen();
 						page_load(1);
				alert_userdata("DHL RÜCKSENDELABEL VERSANDT","Dein Rücksendelabel wurde erstellt und wird an Deine E-Mail-Adresse geschickt.")
			
			
			
			}
		})
			
	
}



function profil_hauptseite()
{
	
	window.location.href="/account_page/";
}