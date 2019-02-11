var check_mobile;

function send_email()
{
		button_logo(0,"send_email_text","send_email_logo","send_email")		
	 	$.ajax({
 		timeout:10000,
 		error: function(){
 			button_logo(1,"send_email_text","send_email_logo","send_email")		
		},
		type: "GET",
		url: "/verschicke_gutscheine_send_email/",
		dataType: "json",
		data: { "empfaenger":document.getElementsByClassName("eingabefelder_input_betreff")[0].value, "betreff": document.getElementsByClassName("eingabefelder_input_betreff")[1].value,"message":document.getElementsByClassName("eingabefelder_large_input")[0].value},
		success: function(data) {		
		
			button_logo(1,"send_email_text","send_email_logo","send_email")		
			if (data=="ok")
			{
				alert_userdata("FREUNDE EINGELADEN","Du hast deine Freunde erfolgreich zu "+document.getElementsByClassName("brand_name")[0].innerHTML+" eingeladen.")
				reset_fields();	
			}
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



function reset_fields()
{

	document.getElementsByClassName("eingabefelder_input_betreff")[0].value=""
	document.getElementsByClassName("eingabefelder_input_betreff")[1].value="Erhalte 15€ Rabatt für dein nächstes BH Set"
	document.getElementsByClassName("eingabefelder_large_input")[0].value=""

}
function input_on_change()
{
	document.getElementsByClassName("eingabefelder_input")[0].style.border="none";	
}


window.onload = function() {
  check_mobile = false;
  

  
  
  (function(a){if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino|android|ipad|playbook|silk/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))) check_mobile = true;})(navigator.userAgent||navigator.vendor||window.opera);

};


function send_facebook_message()
{
	
	if(check_mobile==false)
		FB.ui({
		  method: 'send',
			picture: 'https://www.darlinglace.com/static/overall_picture_bra.jpg',
		  description: 'Darling Lace - Das neue Gesicht für Lingerie, BHs und Slips/ Panties ab 24,95€ pro Set ohne Versandkosten.',
		  link: 'https://www.darlinglace.com/einladung/?gutscheincode='+document.getElementsByClassName("gutscheincode")[0].innerHTML,
		});
	else
	{
		link= 'https://www.darlinglace.com/einladung/?gutscheincode='+document.getElementsByClassName("gutscheincode")[0].innerHTML
		app_id='1796917517246883';
		window.open('fb-messenger://share?link=' + encodeURIComponent(link) + '&app_id=' + encodeURIComponent(app_id));
	}
}


function share_facebook_message()
{
	FB.ui({
	  method: 'feed',
	  link: 'https://www.darlinglace.com/einladung/?gutscheincode='+document.getElementsByClassName("gutscheincode")[0].innerHTML,
	  caption: 'Darling Lace - Das neue Gesicht für Lingerie, BHs und Slips/ Panties ab 24,95€ pro Set ohne Versandkosten.',
	}, function(response){});
}



function profil_hauptseite()
{
	
	window.location.href="/account_page/";
}
