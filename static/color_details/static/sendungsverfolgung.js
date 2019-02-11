var bestellung, sendungsverfolgung;

function sendungsverfolgung_anzeigen()
{
	sendungsverfolgung=JSON.parse(document.getElementsByClassName("sendungsverfolgung_daten")[0].innerHTML)
	bestellungen=JSON.parse(document.getElementsByClassName("bestellungen_daten")[0].innerHTML)

	
	if(bestellungen[0].unternehmensdetails!="")
		document.getElementsByClassName("vorname_nachname")[0].innerHTML=bestellungen[0].vorname+" "+bestellungen[0].nachname+"<br>"+bestellungen[0].unternehmensdetails
	else
		document.getElementsByClassName("vorname_nachname")[0].innerHTML=bestellungen[0].vorname+" "+bestellungen[0].nachname
	
	document.getElementsByClassName("adresse")[0].innerHTML=bestellungen[0].adresse
	document.getElementsByClassName("stadt_plz")[0].innerHTML=bestellungen[0].plz+" "+bestellungen[0].stadt;
	


	

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


	if(bestellungen[0].status=="Zugestellt")
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
		box=box+"<div class='ort'>"+sendungsverfolgung[i].location+"</div>"
		box=box+"<div class='uhrzeit'>"+sendungsverfolgung[i].time+"</div>"
		
		box=box+"<div class='untere_linie'>"
		box=box+"<div class='linie_2'></div>"
		box=box+"</div>"

		i=i-1;
	}
	
	document.getElementsByClassName("trackingbox_content")[0].innerHTML=box

	
}

function profil_hauptseite()
{
	
	window.location.href="/hello/account_page/";
}

function bestellung_bearbeiten_hauptseite()
{
	window.location.href="/hello/account_page/bestellungen_ansehen/";
}