var bestellung,bestelldetails, ruecksendungen;

function ruecksendungen_anzeigen()
{
	ruecksendungen=JSON.parse(document.getElementsByClassName("ruecksendungen_daten")[0].innerHTML)

	
	i=0;
	box=""
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
				gesamt=gesamt+ruecksendungen[j].preis*ruecksendungen[j].anzahl
				j=j+1;
			}
		}
		
	
		
		box=box+"<div class='header_style_3'>";
		
		
		box=box+"<div class='oberes_feld' style='width:100%;height:100px;'>"
		box=box+"<div class='adressdetails'>";
		box=box+"<div style='vertical-align:middle;width:30%;height:100px;display:table-cell;''>"
		box=box+"<div class='adresse_name'>Rücksende-Nr.: "+ruecksendungen[i].id+"<br>"
		box=box+"</div>"
		box=box+"<b>Erstattung: "+replace_dot_comma(gesamt)+" €</b>"

		box=box+"</div>"
		box=box+"</div>"
		
		

		
		box=box+"<div class='standard_feld'>"	
		box=box+"<div class='shop_2'>Zurückschicken bis:<br><b>"+ruecksendungen[i].dateofmaxreturn		
		box=box+"</b></div></div>"


		box=box+"<div class='standard_feld'>"	
		box=box+"<div class='shop_2'>Status:<br><b>"+ruecksendungen[i].status		
		box=box+"</b></div></div>"	
		
		box=box+"<div style='float:left;width:2%;height:100px;border-left: 1px solid #e6e6e6 ;'>"		
		box=box+"</div>"
		box=box+"<div style='float:left;width:10%;height:100px;'>"		
		box=box+"<div class='bearbeiten_feld' onclick='details_ansehen("+i+")'>Details</div>"
		box=box+"</div>"
		box=box+"</div>"


	

		box=box+"<div class='zusammenfassung' style='display:none;'>\r"
		box=box+"<div class='versandettikett_button' onclick='print_label("+i+")'>Drucke Versandettikett</div>";
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
				box=box+"<div style='float:left;width:100%;'>"
			
				box=box+"<img src='"+ruecksendungen[j].picture_link_small+"' style='height:100px;float:left;'/>"
				box=box+"<div style='margin-left:10px;float:left;'/><b>"+ruecksendungen[j].style+"</b></div>"

				
				box=box+"<div class='ruecksendegrund' style='display:block'>"
				box=box+"<div style='float:right;'><b>Rücksendegrund: "+ruecksendungen[j].grund+"</b></div>"
				box=box+"</div>"
				box=box+"<br><div style='float:left;font-size:12px;margin-left:10px;'>"+ruecksendungen[j].bhgroesse+"</div> <br>"
				box=box+"<div style='float:left;font-size:12px;margin-left:10px;'>"+ruecksendungen[j].slipgroesse+"</div><br><br>"
				
				box=box+"<div style='float:left;font-size:12px;margin-left:10px;'>"+replace_dot_comma(parseFloat(ruecksendungen[j].preis)*ruecksendungen[j].anzahl)+" EUR</div><br> "
				box=box+"<div style='float:left;font-size:12px;margin-left:10px;'>Zurücksenden: "+ruecksendungen[j].anzahl+"x</div>"
				box=box+"</div>";
				box=box+"<div class='untere_linie'>"
				box=box+"<div class='linie_2_ruecksendungen'></div>"
				box=box+"</div>"

				
				
				
				j=j+1;
			}
		}
		box=box+"</div>"
			
		i=j;
		
	}

	
	document.getElementById("existierende_rueckmeldungen_anzeigen").innerHTML =box;
	
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
	document.getElementsByClassName("button_main")[0].style.opacity="0.3"
	document.getElementsByClassName("button_main")[0].style.pointerEvents = 'none';
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
	$.ajax({
		type: "POST",
		url: "/hello/bestelldetails_abrufen/",
		dataType: "json",
		data: { "bestellnummer":bestellung[document.getElementsByClassName("eingabefeld_bestellnummer")[0].selectedIndex-1].bestellnummer},
		success: function(data) {
			bestelldetails=JSON.parse(data)
	
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

					if(ruecksendungen[i].bestellnummer==bestellung[document.getElementsByClassName("eingabefeld_bestellnummer")[0].selectedIndex-1].bestellnummer && ruecksendungen[i].slipgroesse==bestelldetails[j].slipgroesse && ruecksendungen[i].bhgroesse==bestelldetails[j].bhgroesse && ruecksendungen[i].colorcode==bestelldetails[j].color && ruecksendungen[i].stylecode==bestelldetails[j].stylecode)
					{	

						netto_anzahl=netto_anzahl-parseInt(ruecksendungen[i].anzahl)

					}
					i=i+1;
				}

				box=box+"<div style='float:left;width:100%;'>"
				box=box+"<img src='"+bestelldetails[j].picture_link_small+"' style='height:100px;float:left;'/>"
				box=box+"<div style='margin-left:10px;float:left;'/><b>"+bestelldetails[j].style+"</b></div>"
				if(netto_anzahl>0)
					box=box+"<div style='float:right;'><input type='checkbox' id='"+j+"' onclick='checkbox_click("+j+")'>Zurücksenden</input></div>"
				else
					box=box+"<div style='float:right;display:none;'><input type='checkbox' id='"+j+"' onclick='checkbox_click("+j+")'>Zurücksenden</input></div>"
				
				
				
				box=box+"<div class='ruecksendung_anzahl' style='display:none'>"

				
				box=box+"<div style='float:right;'>Anzahl: <select class='anzahl'>"
				i=1;
				while(i<=netto_anzahl)
				{
					box=box+"<option>"+i+"</option>"
					
					i=i+1;
				}
				box=box+"</select></div>"
				box=box+"</div>"
				
				box=box+"<div class='ruecksendegrund_angeben' style='display:none'>"
				box=box+"<div style='float:right;'>Rücksendegrund: <select class='ruecksendegrund_select'  onchange='ruecksendegrund_select_change("+j+")'>"
				box=box+"<option></option>"
				box=box+"<option>Zu groß ausgefallen</option>"
				box=box+"<option>Zu klein ausgefallen</option>"
				box=box+"<option>Farbe hat nicht gefallen</option>"
				box=box+"<option>Stil hat nicht gefallen</option>"
				box=box+"<option>Anderes</option>"
				box=box+"</select></div>"
				box=box+"</div>"
				box=box+"<br><div style='float:left;font-size:12px;margin-left:10px;'>"+bestelldetails[j].bhgroesse+"</div> <br>"
				box=box+"<div style='float:left;font-size:12px;margin-left:10px;'>"+bestelldetails[j].slipgroesse+"</div><br><br>"
				box=box+"<div style='float:left;font-size:12px;margin-left:10px;'>"+replace_dot_comma(parseFloat(bestelldetails[j].preis)*bestelldetails[j].anzahl)+" EUR</div><br> "
				box=box+"<div style='float:left;font-size:12px;margin-left:10px;'>Bestellt: "+bestelldetails[j].anzahl+"x</div>"
				if(netto_anzahl!=bestelldetails[j].anzahl)
					box=box+"<br><div style='float:left;font-size:12px;margin-left:10px;'>Zurückgesendet: "+parseInt(parseInt(bestelldetails[j].anzahl)-parseInt(netto_anzahl))+"x</div>"
				
				box=box+"</div>";
				box=box+"<div class='untere_linie'>"
				box=box+"<div class='linie_2_ruecksendungen'></div>"
				box=box+"</div>"
				j=j+1;
			}
			box=box+"<div class='button_main' style='opacity:0.3;pointerEvents:none;' onclick='ruecksendegrund_click()'>Rücksendung beauftragen</div>";	

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
}


function checkbox_click(id)
{

	if(document.getElementById(""+id+"").checked==true)
	{


		document.getElementsByClassName("ruecksendegrund_angeben")[id].style.display="block";

		document.getElementsByClassName("ruecksendung_anzahl")[id].style.display="block";
		document.getElementsByClassName("button_main")[1].style.opacity="1.0"
		document.getElementsByClassName("button_main")[1].style.pointerEvents = 'auto';	

	}
	else
	{
		check_other_ckeckboxes();
		document.getElementsByClassName("ruecksendegrund_angeben")[id].style.display="none";
		document.getElementsByClassName("ruecksendung_anzahl")[id].style.display="none";
		document.getElementsByClassName("ruecksendegrund_select")[j].style.backgroundColor="#ffffff";
		document.getElementsByClassName("ruecksendegrund_select")[j].style.color="#4d4d4d"; 	
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
		document.getElementsByClassName("button_main")[1].style.opacity="1.0"
		document.getElementsByClassName("button_main")[1].style.pointerEvents = 'auto';	
	}
	else
	{
		document.getElementsByClassName("button_main")[1].style.opacity="0.3"
		document.getElementsByClassName("button_main")[1].style.pointerEvents = 'none';	
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


alert("jetzt")
		$.ajax({
		type: "POST",
		url: "/hello/ruecksendung_calcualte_wert/",
		dataType: "json",
		data: { "bestellnummer":bestellnummer,'stylecode':stylecode,'colorcode':colorcode,'anzahl':anzahl,'grund':grund,'item-length':zaehler,'gesamt':gesamt,'bhgroesse':bhgroesse,'slipgroesse':slipgroesse},
		success: function(data) {
			alert(data)
			ruecksendung_bestaetigen=JSON.parse(data)
			alert(ruecksendung_bestaetigen)
			if(parseFloat(ruecksendung_bestaetigen[0].verrechnungmitrabatt)>0)
				if(parseFloat(ruecksendung_bestaetigen[0].lieferkosten)>0)
				{
					//parseFloat(parseFloat(ruecksendung_bestaetigen[0].ertstattung)-parseFloat(ruecksendung_bestaetigen[0].lieferkosten))
					alert("ASD")
					alert_userdata_ruecksendung_bestaetigen("Für die Rücksendung können wir dir "+parseFloat(ruecksendung_bestaetigen[0].erstattung)-parseFloat(ruecksendung_bestaetigen[0].lieferkosten)+"erstatten:<br>Warenwert: "+ ruecksendung_bestaetigen[0].warenwert+"<br>Lieferkosten: "+ruecksendung_bestaetigen[0].lieferkosten+"<br>Rückzahlung Rabatt: "+ruecksendung_bestaetigen[0].verrechnungmitrabatt)
					alert("ASD")
				}
			
			}
		})			


	
	
}

function alert_userdata_ruecksendung_bestaetigen(text)
{
	alert(text)
	document.getElementsByClassName("ruecksendung_bestaetigen_text")[0].innerHTML=text;
	alert("iwiw")
	$('#zuruecksenden_bestaetigen').modal('show');
	alert("iwiw")
}

function ruecksendung_bestaetigt()
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

/*
		$.ajax({
		type: "POST",
		url: "/hello/account_page/ruecksendung_beauftragen/",
		dataType: "json",
		data: { "bestellnummer":bestellnummer,'stylecode':stylecode,'colorcode':colorcode,'anzahl':anzahl,'grund':grund,'item-length':zaehler,'gesamt':gesamt,'bhgroesse':bhgroesse,'slipgroesse':slipgroesse},
		success: function(data) {
			
				document.getElementsByClassName("header_style")[0].style.display="none"
				document.getElementsByClassName("button_main")[0].style.opacity="1.0"
				document.getElementsByClassName("button_main")[0].style.pointerEvents = 'auto';
				document.getElementsByClassName("ruecksendungen_daten")[0].innerHTML=data;
				document.getElementsByClassName("zusammenfassung")[1].innerHTML="";
				document.getElementsByClassName("eingabefeld_bestellnummer")[0].selectedIndex=0;
				
				ruecksendungen_anzeigen();
				
			
			
			
			}
		})*/
			
	
}



function profil_hauptseite()
{
	
	window.location.href="/hello/account_page/";
}