function send_email()
{
	 	$.ajax({
		type: "GET",
		url: "/hello/verschicke_gutscheine_send_email/",
		dataType: "json",
		data: { "empfaenger":document.getElementsByClassName("eingabefelder_input")[0].value, "betreff": document.getElementsByClassName("eingabefelder_input")[1].value,"message":document.getElementsByClassName("eingabefelder_large_input")[0].innerHTML},
		success: function(data) {		
		
			if (data=="ok")
				alert_userdata("FREUNDE EINGELADEN","Du hast deine Freunde erfolgreich zu Sensuals eingeladen.")
				
				
			if (data=="email falsch")
			{
				alert_userdata("UNGÜLTIGE E-MAIL ADRESSE","Die von Dir eingegebenen E-Mail Adressen sind leider ungültig. Bitte überprüfe noch einmal Deine Eingabe.")	
				document.getElementsByClassName("eingabefelder_input")[0].style.border="1px solid red";		
				
			}


			if (data=="keine email")
			{
				alert_userdata("KEINE E-MAIL ADRESSE","Du hast keine E-Mail Adressen angegeben. Wenn du Freunde einladen möchtest, gib deren E-Mail Adressen an.")		
				document.getElementsByClassName("eingabefelder_input")[0].style.border="1px solid red";		
				
			}	
		}
		})
}


function input_on_change()
{
	document.getElementsByClassName("eingabefelder_input")[0].style.border="none";	
}


function send_facebook_message()
{
	FB.ui({
	  method: 'send',
	  link:  'https://developers.facebook.com/docs/',
	});
}


function share_facebook_message()
{
	FB.ui({
	  method: 'feed',
	  link: 'https://developers.facebook.com/docs/',
	  caption: 'An example caption',
	}, function(response){});
}



function profil_hauptseite()
{
	
	window.location.href="/hello/account_page/";
}
