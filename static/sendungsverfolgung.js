var bestellung, sendungsverfolgung;





function bestellung_bearbeiten_hauptseite()
{
	
	window.location.href="/account_page/bestellungen_ansehen/";
}

function weiter_einkaufen()
{
	window.location.href="https://www.darlinglace.com/Produktauswahl/BH%20Sets/";
	
	
}



function sendungsverfolgung_anzeigen()
{
	sendungsverfolgung=JSON.parse(document.getElementsByClassName("sendungsverfolgung_daten")[0].innerHTML)
	bestellungen=JSON.parse(document.getElementsByClassName("bestellungen_daten")[0].innerHTML)

	
	if(bestellungen[0].unternehmensdetailslieferadresse!="")
		document.getElementsByClassName("vorname_nachname")[0].innerHTML=bestellungen[0].vornamelieferadresse+" "+bestellungen[0].nachnamelieferadresse+"<br>"+bestellungen[0].unternehmensdetailslieferadresse
	else
		document.getElementsByClassName("vorname_nachname")[0].innerHTML=bestellungen[0].vornamelieferadresse+" "+bestellungen[0].nachnamelieferadresse
	
	document.getElementsByClassName("adresse")[0].innerHTML=bestellungen[0].strasselieferadresse+" "+bestellungen[0].hausnummerlieferadresse
	document.getElementsByClassName("stadt_plz")[0].innerHTML=bestellungen[0].plzlieferadresse+" "+bestellungen[0].stadtlieferadresse;
	


	

	box=""
	
	if(sendungsverfolgung.length>=0)
	{
	    box=box+"<ul class='progress-indicator nocenter'>"
		box=box+"<li class='completed'> "
		box=box+"<span class='bubble'></span>"
		box=box+"Ware bestellt am <br>"+sendungsverfolgung[0].date+"</li> "
	}
	else
	{
	    box=box+"<ul class='progress-indicator nocenter'>"
		box=box+"<li class='completed'> "
		box=box+"<span class='bubble'></span>"
		box=box+"Ware noch nicht bestellt</li> "
	}



	if(sendungsverfolgung.length>=1)
	{
		box=box+"<li class='completed'> "
		box=box+"<span class='bubble'></span> "
		box=box+"Ware an DHL übergeben am <br>"+sendungsverfolgung[0].date
		box=box+"</li>"
	}
	else
	{
		box=box+"<li > "
		box=box+"<span class='bubble'></span> "
		box=box+"Ware noch nicht an DHL übergeben"
		box=box+"</li> "
	}	

	if(sendungsverfolgung[sendungsverfolgung.length-1].content=="Zugestellt" || sendungsverfolgung[sendungsverfolgung.length-1].content=="Delivered")
	{
		box=box+"<li class='completed'> "
		box=box+"<span class='bubble'></span> "
		box=box+"Ware zugestellt am <br>"+sendungsverfolgung[sendungsverfolgung.length-1].date
		box=box+"</li>"
	}
	else
	{
		box=box+"<li > "
		box=box+"<span class='bubble'></span> "
		box=box+"Ware noch nicht zugestellt"
		box=box+"</li> "
	}		


	box=box+"</ul>"
	
	document.getElementsByClassName("tracking_bar")[0].innerHTML=box

	i=sendungsverfolgung.length-1;
	box=""
	while(i>=0)
	{
		box=box+"<div class='date'>"+sendungsverfolgung[i].date+"</div>"
		box=box+"<div class='content'>"+sendungsverfolgung[i].content+"</div>"
		if(sendungsverfolgung[i].location!="")
			box=box+"<div class='ort'>"+sendungsverfolgung[i].location+"</div>"
		else
			box=box+"<div class='ort'>&nbsp</div>"		
	//	box=box+"<div class='uhrzeit'>"+sendungsverfolgung[i].time+"</div>"
		
		box=box+"<div class='untere_linie'>"
		box=box+"<div class='linie_2'></div>"
		box=box+"</div>"

		i=i-1;
	}
	
	document.getElementsByClassName("trackingbox_content")[0].innerHTML=box

	
}

function profil_hauptseite()
{
	
	window.location.href="/account_page/";
}

function bestellung_bearbeiten_hauptseite()
{
	window.location.href="/account_page/bestellungen_ansehen/";
}