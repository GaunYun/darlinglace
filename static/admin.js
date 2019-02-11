var links;
function admin_uebersicht()
{

	links=JSON.parse(document.getElementsByClassName("links_data")[0].innerHTML)		
	
	i=0;
	block=""
	
	while(i<=links.length-1)
	{

		block=block+"<div class='links' onclick='open_link("+i+")'>"+links[i].linkname+"</div>"

		
		i=i+1;	
	}
	
	document.getElementById("links").innerHTML=block;

}


function open_link(i)
{
	
	 		$.ajax({
		type: "GET",
		url: "/admin/uebersicht/"+links[i].link+"/",
		dataType: "json",
		data: { "":""},
		success: function(data) {

				alert("Successful")

 		}
 	})

	
	
}


function user_anzeigen()
{
	userdaten=JSON.parse(document.getElementsByClassName("userdaten_data")[0].innerHTML)		

	i=0;
	block=""
//	block=block+"<div class='gruppe'>"
	block=block+"<div class='gruppe'><div class='header_feld'>Nachname, Vorname</div><br><div class='feld' id='name'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Mobilnummer</div><br><div class='feld' id='mobilnummer'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>User-Id</div><br><div class='feld' id='user_id'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>E-Mail</div><br><div class='feld' id='email'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Mitglied seit</div><br><div class='feld' id='member_since'></div></div></div>"
	/*block=block+"<div class='gruppe'><div class='header_feld'>Subscription model user</div><br><div class='feld' id='subscription_model_user'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Umsatz mit Kunde</div><br><div class='feld' id='revenue'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Retouren-Quote</div><br><div class='feld' id='retouren_quote'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Bestellungen ansehen</div><br><div class='feld' id='bestellungen_ansehen_button'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Ticket erstellen: Text</div><br><div class='feld' id='ticket_erstellen_text'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Ticket erstellen: absenden</div><br><div class='feld' id='ticket_erstellen_button'></div></div></div>"
*/
	document.getElementById("userdaten").innerHTML=block;

	while(i<=userdaten.length-1)
	{
		document.getElementById("name").innerHTML=document.getElementById("name").innerHTML+"<div class='feld_inhalt' >"+userdaten[i].nachname+", "+userdaten[i].vorname+" </div><br><br>"
		document.getElementById("mobilnummer").innerHTML=document.getElementById("mobilnummer").innerHTML+"<div class='feld_inhalt' >"+userdaten[i].mobilnummer+" </div><br><br>"
		document.getElementById("user_id").innerHTML=document.getElementById("user_id").innerHTML+"<div class='feld_inhalt' >"+userdaten[i].userid+" </div><br><br>"
		document.getElementById("member_since").innerHTML=document.getElementById("member_since").innerHTML+"<div class='feld_inhalt' >"+userdaten[i].mitglied_seit+" </div><br><br>"
		document.getElementById("email").innerHTML=document.getElementById("email").innerHTML+"<div class='feld_inhalt' >"+userdaten[i].email+" </div><br><br>"
	/*	document.getElementById("subscription_model_user").innerHTML=document.getElementById("subscription_model_user").innerHTML+"<div class='feld_inhalt' >"+userdaten[i].subscription_model_user+" </div><br><br>"
		document.getElementById("revenue").innerHTML=document.getElementById("revenue").innerHTML+"<div class='feld_inhalt' >"+userdaten[i].revenue+" </div><br><br>"
		document.getElementById("retouren_quote").innerHTML=document.getElementById("retouren_quote").innerHTML+"<div class='feld_inhalt' >"+userdaten[i].retouren_quote+" </div><br><br>"
		document.getElementById("bestellungen_ansehen_button").innerHTML=document.getElementById("bestellungen_ansehen_button").innerHTML+"<button class='feld_inhalt' onclick='bestellungen_ansehen_user("+i+")'>Ansehen</button><br><br>"	
		document.getElementById("ticket_erstellen_text").innerHTML=document.getElementById("ticket_erstellen_text").innerHTML+"<input class='feld_inhalt_ticket' value=''><br><br>"
		document.getElementById("ticket_erstellen_button").innerHTML=document.getElementById("ticket_erstellen_button").innerHTML+"<button class='feld_inhalt' onclick='ticket_erstellen_user("+i+")'>Erstellen</button><br><br>"	*/
	

		i=i+1;	
	}

}


function bestellungen_anzeigen_pro_user()
{
	bestellungen=JSON.parse(document.getElementsByClassName("bestellungen_data")[0].innerHTML)		

	i=0;
	block=""
//	block=block+"<div class='gruppe'>"
	block=block+"<div class='gruppe'><div class='header_feld'>Nachname, Vorname</div><br><div class='feld' id='name'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Bestellnummer</div><br><div class='feld' id='bestellnummer'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Adresse</div><br><div class='feld' id='adresse'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Zahlungsmittel</div><br><div class='feld' id='zahlungsmittel'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Bestellte Artikel</div><br><div class='feld' id='bestellte_artikel'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Warenwert</div><br><div class='feld' id='warenwert'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Lieferkosten</div><br><div class='feld' id='lieferkosten'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Rabatt</div><br><div class='feld' id='rabatt'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Gesamtpreis</div><br><div class='feld' id='gesamtpreis'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Rabattcode</div><br><div class='feld' id='rabattcode'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Status</div><br><div class='feld' id='status'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Liefertermin</div><br><div class='feld' id='liefertermin'></div></div></div>"

	
	document.getElementById("bestellungen").innerHTML=block;

	while(i<=bestellungen.length-1)
	{
		document.getElementById("name").innerHTML=document.getElementById("name").innerHTML+"<div class='feld_inhalt' >"+bestellungen[i].nachname+", "+bestellungen[i].vorname+" </div><br><br>"
		document.getElementById("bestellnummer").innerHTML=document.getElementById("bestellnummer").innerHTML+"<div class='feld_inhalt' >"+bestellungen[i].bestellnummer+" </div><br><br>"
		document.getElementById("adresse").innerHTML=document.getElementById("adresse").innerHTML+"<div class='feld_inhalt' >"+bestellungen[i].adresse+", "+bestellungen[i].stadt+" "+bestellungen[i].land+" </div><br><br>"
		document.getElementById("zahlungsmittel").innerHTML=document.getElementById("zahlungsmittel").innerHTML+"<div class='feld_inhalt' >"+bestellungen[i].zahlungsoption+" </div><br><br>"
		j=0;
		while(j<=bestellteartikel.length-1)
		{
			if(bestellteartikel[j].bestellnummer==bestellungen[j].bestellnummer)
				document.getElementById("bestellte_artikel").innerHTML=document.getElementById("bestellte_artikel").innerHTML+"<div class='feld_inhalt' >"+bestellteartikel[i].style+", "+bestellteartikel[i].bhgroesse+" "+bestellteartikel[i].slipgroesse+": "+bestellteartikel[i].anzahl+" </div><br><br>"
			j=j+1;	
		} 


		j=0;
		while(j<=rebates.length-1)
		{
			if(rebates[j].bestellnummer==bestellungen[j].bestellnummer)
			{
				document.getElementById("warenwert").innerHTML=document.getElementById("warenwert").innerHTML+"<div class='feld_inhalt' >"+rabates[i].warenwert+"</div><br><br>"
				document.getElementById("rabatt").innerHTML=document.getElementById("rabatt").innerHTML+"<div class='feld_inhalt' >"+rabates[i].rabatt+"</div><br><br>"
				document.getElementById("gesamtpreis").innerHTML=document.getElementById("gesamtpreis").innerHTML+"<div class='feld_inhalt' >"+rabates[i].gesamtpreis+"</div><br><br>"
			}
			j=j+1;	
		} 
		
		document.getElementById("rabattcode").innerHTML=document.getElementById("rabattcode").innerHTML+"<div class='feld_inhalt' >"+bestellungen[i].rabattcode+" </div><br><br>"
		document.getElementById("status").innerHTML=document.getElementById("status").innerHTML+"<div class='feld_inhalt' >"+bestellungen[i].status+" </div><br><br>"
		document.getElementById("liefertermin").innerHTML=document.getElementById("liefertermin").innerHTML+"<div class='feld_inhalt' >"+bestellungen[i].liefertermin+" </div><br><br>"



		i=i+1;	
	}
}


function bestellungen_ansehen_user(i)
{
	
	window.top.location.href = "/admin/admin_user_ansehen/"+bestellungen[i].usercode
	
	
}



function bestellungen_anzeigen()
{
	bestellungen=JSON.parse(document.getElementsByClassName("bestellungen_data")[0].innerHTML)		

	i=0;
	block=""
//	block=block+"<div class='gruppe'>"
	block=block+"<div class='gruppe'><div class='header_feld'>Nachname, Vorname</div><br><div class='feld' id='name'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Bestellnummer</div><br><div class='feld' id='bestellnummer'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Gesamtpreis</div><br><div class='feld' id='preis'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Status</div><br><div class='feld' id='status'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Liefertermin</div><br><div class='feld' id='liefertermin'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Versenden</div><br><div class='feld' id='versenden_button'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Versandettiket</div><br><div class='feld' id='versandettiket_button'></div></div></div>"

	document.getElementById("bestellungen").innerHTML=block;

	while(i<=bestellungen.length-1)
	{
		document.getElementById("name").innerHTML=document.getElementById("name").innerHTML+"<div class='feld_inhalt' >"+bestellungen[i].nachnamerechnung+", "+bestellungen[i].vornamerechnung+" </div><br><br>"
		document.getElementById("bestellnummer").innerHTML=document.getElementById("bestellnummer").innerHTML+"<div class='feld_inhalt' >"+bestellungen[i].bestellnummer+" </div><br><br>"
		document.getElementById("status").innerHTML=document.getElementById("status").innerHTML+"<div class='feld_inhalt' >"+bestellungen[i].status+" </div><br><br>"
		
		gesamtpreis=parseFloat(bestellungen[i].bestellungspreis)-parseFloat(bestellungen[i].lieferkosten)-parseFloat(bestellungen[i].lieferkosten)-parseFloat(bestellungen[i].creditused)-parseFloat(bestellungen[i].braforfreevalue)-parseFloat(bestellungen[i].rabatt)
		document.getElementById("preis").innerHTML=document.getElementById("preis").innerHTML+"<div class='feld_inhalt' >"+gesamtpreis+" </div><br><br>"
		
		document.getElementById("liefertermin").innerHTML=document.getElementById("liefertermin").innerHTML+"<input class='feld_inhalt_liefertermin' value='"+bestellungen[i].liefertermin+"'><br><br>"

		if(bestellungen[i].status=="Bestellt")
			document.getElementById("versenden_button").innerHTML=document.getElementById("versenden_button").innerHTML+"<button class='feld_inhalt' onclick='versenden("+i+")'>Versenden</button><br><br>"		
		else
			document.getElementById("versenden_button").innerHTML=document.getElementById("versenden_button").innerHTML+"<button class='feld_inhalt' onclick='versenden("+i+")' disabled>Versenden</button><br><br>"		
		
		document.getElementById("versandettiket_button").innerHTML=document.getElementById("versandettiket_button").innerHTML+"<button class='feld_inhalt' onclick='versandettikett_drucken("+i+")'>Drucken</button><br><br>"		

		i=i+1;	
	}

}



function ruecksendungen_anzeigen()
{
	ruecksendungen=JSON.parse(document.getElementsByClassName("ruecksendungen_data")[0].innerHTML)	


	i=0;
	block=""
//	block=block+"<div class='gruppe'>"
	block=block+"<div class='gruppe'><div class='header_feld'>Rücksendungs-ID</div><br><div class='feld' id='id'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Bestellnummer/ Ware</div><br><div class='feld' id='bestellnummer'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Status</div><br><div class='feld' id='status'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Rückversand erhalten</div><br><div class='feld' id='rueckversanderhalten_button'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Erstattungsbetrag</div><br><div class='feld' id='erstattungsbetrag'></div></div></div>"
	block=block+"<div class='gruppe'><div class='header_feld'>Rückerstattung veranlassen</div><br><div class='feld' id='rueckerstattung_veranlassen_button'></div></div></div>"
	document.getElementById("bestellungen").innerHTML=block;
	zaehler=0;
	while(i<=ruecksendungen.length-1)
	{
		
		erstattungsbetrag=0
		document.getElementById("id").innerHTML=document.getElementById("id").innerHTML+"<div class='feld_inhalt' >"+ruecksendungen[i].id+" </div><br><br>"
		document.getElementById("status").innerHTML=document.getElementById("status").innerHTML+"<div class='feld_inhalt' >"+ruecksendungen[i].status+" </div><br><br>"
		document.getElementById("bestellnummer").innerHTML=document.getElementById("bestellnummer").innerHTML+"<div class='feld_inhalt' >"+ruecksendungen[i].bestellnummer+" </div><br><br>"		
	
		document.getElementById("rueckversanderhalten_button").innerHTML=document.getElementById("rueckversanderhalten_button").innerHTML+"<button class='feld_inhalt' disabled>Ware erhalten</button><br><br>"	

		erstattungsbetrag=-parseFloat(ruecksendungen[i].verrechnungmitrabatt)-parseFloat(ruecksendungen[i].lieferkosten)
		document.getElementById("erstattungsbetrag").innerHTML=document.getElementById("erstattungsbetrag").innerHTML+"<input class='feld_inhalt_erstattungsbetrag' value=''><br><br>"
		alert(ruecksendungen[i].preis+","+ruecksendungen[i].verrechnungmitrabatt+","+ruecksendungen[i].lieferkosten)
		if(ruecksendungen[i].geldzurueckueberwiesen=="false")		
			document.getElementById("rueckerstattung_veranlassen_button").innerHTML=document.getElementById("rueckerstattung_veranlassen_button").innerHTML+"<button class='feld_inhalt' onclick='rueckerstattung_veranlassen_button("+zaehler+","+i+")'>Rückerstatten</button><br><br>"	
		else
			document.getElementById("rueckerstattung_veranlassen_button").innerHTML=document.getElementById("rueckerstattung_veranlassen_button").innerHTML+"<button class='feld_inhalt' onclick='rueckerstattung_veranlassen_button("+zaehler+","+i+")' disabled>Rückerstatten</button><br><br>"			
		zaehler_1=zaehler;
		zaehler=zaehler+1;

		j=i;
		while(j<=ruecksendungen.length-1)
		{
			if(ruecksendungen[j].id!=ruecksendungen[i].id)
			{

				break;
			}
			else
			{
				alert(ruecksendungen[j].preis+","+ruecksendungen[j].verrechnungmitrabatt+","+ruecksendungen[j].lieferkosten)
				erstattungsbetrag=erstattungsbetrag+parseFloat(ruecksendungen[j].preis)*parseInt(ruecksendungen[j].anzahl)
				document.getElementById("id").innerHTML=document.getElementById("id").innerHTML+"<div class='feld_inhalt' ></div><br><br>"
				document.getElementById("status").innerHTML=document.getElementById("status").innerHTML+"<div class='feld_inhalt' ></div><br><br>"
				document.getElementById("bestellnummer").innerHTML=document.getElementById("bestellnummer").innerHTML+"<div class='feld_inhalt'  style='font-style:italic;font-size:14px;'>"+ruecksendungen[j].anzahl+"x"+ruecksendungen[j].style+":"+ruecksendungen[j].bhgroesse+ruecksendungen[j].slipgroesse +"</div><br><br>"					
				if(ruecksendungen[j].status!="Zurueckgesandt")			
					document.getElementById("rueckversanderhalten_button").innerHTML=document.getElementById("rueckversanderhalten_button").innerHTML+"<button class='feld_inhalt' onclick='rueckversanderhalten_button("+j+")'>Ware erhalten</button><br><br>"	
				else
					document.getElementById("rueckversanderhalten_button").innerHTML=document.getElementById("rueckversanderhalten_button").innerHTML+"<button class='feld_inhalt' onclick='rueckversanderhalten_button("+j+")' disabled>Ware erhalten</button><br><br>"					
				
		
				document.getElementById("erstattungsbetrag").innerHTML=document.getElementById("erstattungsbetrag").innerHTML+"<input class='feld_inhalt_erstattungsbetrag' value='' disabled><br><br>"
				
				document.getElementById("rueckerstattung_veranlassen_button").innerHTML=document.getElementById("rueckerstattung_veranlassen_button").innerHTML+"<button class='feld_inhalt' ></button><br><br>"		
				zaehler=zaehler+1;		
				
			}
			j=j+1;	
		}
		alert(erstattungsbetrag)
		document.getElementsByClassName("feld_inhalt_erstattungsbetrag")[zaehler_1].value=erstattungsbetrag
		i=j-1
		i=i+1;	
	}

}


function versenden(i)
{

	
	$.ajax({
		type: "POST",
		url: "/admin/bestellung_versenden/",
		dataType: "json",
		data: { "bestellnummer":bestellungen[i].bestellnummer,"usercode":bestellungen[i].usercode,"liefertermin":document.getElementsByClassName("feld_inhalt_liefertermin")[i].value},
		success: function(data) {
alert(data)
					$.ajax({
						type: "POST",
						url: "/bestellung_abrufen/",
						dataType: "json",
						data: { "bestellnummer" : "all","session_key":"all"},
						success: function(data) {

						document.getElementsByClassName("bestellungen_data")[0].innerHTML=data

							bestellungen_anzeigen()
				
				 		}
				 	})


 		}
 	})
		
	
}


function rueckerstattung_veranlassen_button(zaehler,i)
{
	alert(i)
	alert(ruecksendungen[i].id)
	alert(document.getElementsByClassName("feld_inhalt_erstattungsbetrag")[zaehler].value)
		$.ajax({
		type: "POST",
		url: "/admin/rueckerstattung_veranlassen/",
		dataType: "json",
		data: { "id":ruecksendungen[i].id,"amount":document.getElementsByClassName("feld_inhalt_erstattungsbetrag")[zaehler].value},
		success: function(data) {
				alert(data)


 		}
 	})
	
}

function rueckversanderhalten_button(i)
{
	

		$.ajax({
		type: "POST",
		url: "/admin/rueckversand_erhalten/",
		dataType: "json",
		data: { "id":ruecksendungen[i].id,"status":"Zurueckgesandt","bhgroesse":ruecksendungen[i].bhgroesse,"slipgroesse":ruecksendungen[i].slipgroesse,"anzahl":ruecksendungen[i].anzahl,"stylecode":ruecksendungen[i].stylecode,"colorcode":ruecksendungen[i].colorcode,"usercode":ruecksendungen[i].usercode},
		success: function(data) {

					$.ajax({
						type: "POST",
						url: "/ruecksendungen_abrufen/",
						dataType: "json",
						data: { "session_key":"all"},
						success: function(data) {
							document.getElementsByClassName("ruecksendungen_data")[0].innerHTML=data
							ruecksendungen_anzeigen()

				
				 		}
				 	})

 		}
 	})
	
}


function versandettikett_drucken(i)
{
	

	
	$.ajax({
		type: "POST",
		url: "/admin/versandettikett_drucken/",
		dataType: "json",
		data: { "bestellnummer":bestellungen[i].bestellnummer,"usercode":bestellungen[i].usercode},
		success: function(data) {
alert(data)
				window.open(data); 

 		}
 	})
		
	
}