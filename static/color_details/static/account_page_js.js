function freunde_einladen_alert()
{
	
/*	$.ajax({
		type: "POST",
		url: "/hello/account_page/freunde_einladen/",
		dataType: "json",
		data: { "email_empfaenger": "janet@gmail.com","email_sender":"","gutscheincode":+","+document.getElementsByClassName("email-eingabe")[0].value },
		success: function(data) {
			
			alert_click_schliessen()


		}
	});*/
	
	
}




var input = document.getElementsByClassName("gutscheincode")[0];
var copy   = document.getElementsByClassName("copybutton")[0];
copy.addEventListener('click', function(e) {

   // Select some text (you could also create a range)
   input.select(); 
	document.execCommand('copy');
   // Use try & catch for unsupported browser

});



function check_VIP(VIP)
{

	if(VIP=="false")
		document.getElementsByClassName("links_gruppen")[2].style.display="none"
}

function profil_bearbeiten()
{
	
	window.location.href="/hello/account_page/profil_bearbeiten";
}


function passwort_bearbeiten()
{
	
	window.location.href="/hello/account_page/passwort_bearbeiten";
}


function VIP_bearbeiten()
{
	
	window.location.href="/hello/account_page/VIP_bearbeiten";
}



function adressbuch_bearbeiten()
{
	
	window.location.href="/hello/account_page/adressbuch_bearbeiten";
}

function zahlungsmethoden_bearbeiten()
{
	
	window.location.href="/hello/account_page/zahlungsmethoden_bearbeiten";
}

function bestellungen_bearbeiten()
{
	
	window.location.href="/hello/account_page/bestellungen_ansehen";
}

function bestellung_zuruecksenden()
{
	
	window.location.href="/hello/account_page/bestellung_zuruecksenden";
}

function verschickte_gutscheine_sehen()
{
	
	window.location.href="/hello/account_page/verschickte_gutscheine";
}

function verschicke_gutscheine()
{
	
	window.location.href="/hello/account_page/freunde_einladen";
}



function gutscheinkonto_sehen()
{
	
	window.location.href="/hello/account_page/gutscheinkonto";
}

function showroom_bearbeiten()
{
	
	quiz_laden();
}

function link_check()
{

	if(document.getElementsByClassName("bestellungen")[0].innerHTML=="[]")
	{

		document.getElementById("vergangene_bestellungen").style.opacity="0.4";
		document.getElementById("vergangene_bestellungen").style.pointerEvents="none";
		document.getElementById("bestellung_zuruecksenden").style.opacity="0.4";
		document.getElementById("bestellung_zuruecksenden").style.pointerEvents="none";
	}
		
}


