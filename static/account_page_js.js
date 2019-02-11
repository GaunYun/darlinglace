function freunde_einladen_alert()
{

	
	
}






function check_VIP(VIP)
{

	if(VIP=="Regular")
		document.getElementsByClassName("links_gruppen")[2].style.display="none"
}

function profil_bearbeiten()
{
	
	window.location.href="/account_page/profil_bearbeiten";
}


function passwort_bearbeiten()
{
	
	window.location.href="/account_page/passwort_bearbeiten";
}


function VIP_bearbeiten()
{
	
	window.location.href="/account_page/VIP_bearbeiten";
}



function adressbuch_bearbeiten()
{
	
	window.location.href="/account_page/adressbuch_bearbeiten";
}

function zahlungsmethoden_bearbeiten()
{
	
	window.location.href="/account_page/zahlungsmethoden_bearbeiten";
}

function bestellungen_bearbeiten()
{
	
	window.location.href="/account_page/bestellungen_ansehen";
}

function bestellung_zuruecksenden()
{
	
	window.location.href="/account_page/bestellung_zuruecksenden";
}

function verschickte_gutscheine_sehen()
{
	
	window.location.href="/account_page/verschickte_gutscheine";
}

function verschicke_gutscheine()
{
	
	window.location.href="/account_page/freunde_einladen";
}



function gutscheinkonto_sehen()
{
	
	window.location.href="/account_page/gutscheinkonto";
}

function showroom_bearbeiten()
{
	
	quiz_laden();
}

function link_check()
{

	if(document.getElementsByClassName("bereitsbestellt")[0].innerHTML=="no")
	{

		document.getElementById("vergangene_bestellungen").style.opacity="0.4";
		document.getElementById("vergangene_bestellungen").style.pointerEvents="none";
		document.getElementById("bestellung_zuruecksenden").style.opacity="0.4";
		document.getElementById("bestellung_zuruecksenden").style.pointerEvents="none";
	}
	else
	{
		if(document.getElementsByClassName("bereitsversandt")[0].innerHTML=="no")
		{		
			document.getElementById("bestellung_zuruecksenden").style.opacity="0.4";
			document.getElementById("bestellung_zuruecksenden").style.pointerEvents="none";	
		}
	}	
}


