 
 var gutscheincode;
 
 function check_plz()
 {
	 var submit_plz_input=document.getElementById("postleitzahl").value;
	 
	if(isNaN(submit_plz_input) ==true || submit_plz_input.length<5)
	{
		document.getElementById("plz_fehler").innerHTML="Bitte eine fünfstellige PLZ angeben";
	}
	else
	{
		login_logo(0,"plz_ueberpruefen_text","plz_ueberpruefen_logo","plz_ueberpruefen")
		document.getElementsByClassName("login")[0].style.pointerEvents = 'none';
		document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'none';
		document.getElementsByClassName("registrierung")[0].style.pointerEvents = 'none';
		$.ajax({
			type: "POST",
			url: "/hello/login_plz/",
			dataType: "json",
			data: { "item": document.getElementById("postleitzahl").value,"gutscheincode":gutscheincode },
			success: function(data) {
				warteliste_plz=document.getElementById("postleitzahl").value
				if (data!="nicht ok")
				{

					
					window.location.href="/hello/0/";
					
				}
				else
				{						
					el = document.getElementById("overlay");
					box=""
					box=box+"<br><b>WARTELISTE</b><img class='schliessen_alert' src='/static/x.png' width='15' onclick='alert_click_schliessen();' height='15'/></img><br><br>";
					box=box+"<p style='margin-left:20px;margin-right:20px;'>Leider sind wir in deinem Postleitzahl-Bereich noch nicht verfügbar. Setze Dich doch auf die Warteliste, damit du informiert wirst, wann wir bei Dir verfügbar sind!</p><br>";
					box=box+"<input class='email-eingabe' type='text' style='width:200px;float:left;margin-left:200px;'  placeholder='E-Mail Adresse' />";
					box=box+"<button onclick='warteliste_click()' class='button_warteliste' style='margin-left:10px;float:left;'>Auf die Warteliste</button>";
					document.getElementById("alert_address").innerHTML=box

					disableScroll();
					el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";

					//document.getElementById("x-mask").style.opacity="0.3";
	
					

					document.getElementsByClassName("transparent_background")[0].style.display="block";
					
					


				}
			}
		});
	}
 }
 
 
 
 function press_enter(event)
 {
	 document.getElementById("plz_fehler").innerHTML="";
	 if(event.keyCode==13)
		 check_plz()
	 
 }
 
  function validate(evt) {
  var theEvent = evt || window.event;
  var key = theEvent.keyCode || theEvent.which;
  key = String.fromCharCode( key );
  var regex = /[0-9]|\./;
  if( !regex.test(key) && theEvent.keyCode!=8) {
    theEvent.returnValue = false;
    if(theEvent.preventDefault) theEvent.preventDefault();
  }
}

function gutscheincode_laden(code)
{


	gutscheincode=code;
}



 
 
 
 
 function alert_userdata(content1,content2)
 {	 

	el = document.getElementById("overlay");
	box=""
	box=box+"<br><b>"+content1+"</b><img class='schliessen_alert' src='/static/x.png' width='15' onclick='alert_click_schliessen();' height='15'/></img><br><br>";
	box=box+"<p style='margin-left:20px;margin-right:20px;'>"+content2+"</p><br>";
	document.getElementById("alert_address").innerHTML=box

	disableScroll();
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";

	//document.getElementById("x-mask").style.opacity="0.3";

	

	document.getElementsByClassName("transparent_background")[0].style.display="block";

 }
 
 
 function check_vollstaendigkeit()
 {
	 if(document.getElementById("username").value=="" || document.getElementById("passwort").value=="")
		  document.getElementById("eingabe_fehler").innerHTML="Bitte E-Mail Adresse und Passwort angeben";
	  else
		  return true		 
	 
 }
 
 
 function passwort_lang_genug()
 {

	 if(document.getElementById("passwort").value.length<6)
		  document.getElementById("eingabe_fehler").innerHTML="Das Passwort muss mindestens 6 Stellen haben";
	  else
		  return true
	 
	 
 }
 
 function eingabe_fehler_herausnehmen()
 {
	 document.getElementById("eingabe_fehler").innerHTML="";
 }
 

 
 
 function register()
 {
	 
	 if (check_vollstaendigkeit())
	 {
		if(passwort_lang_genug())
		{
			
			login_logo(0,"registrierung_text","registrierung_logo","registrierung")

			document.getElementsByClassName("login")[0].style.pointerEvents = 'none';
			document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'none';
			document.getElementsByClassName("plz_ueberpruefen")[0].style.pointerEvents = 'none';
			
			 $.ajax({
				type: "POST",
				url: "/hello/register_user/",
				dataType: "json",
				data: { "item": document.getElementById("username").value+","+document.getElementById("passwort").value,"gutscheincode":gutscheincode },
				success: function(data) {

					if(data=="exists already")
					{
						alert_userdata("USER EXISTIERT BEREITS","Ein User mit dieser E-Mail Adresse existiert bereits. Versuche über Passwort vergessen ein neues Passwort abzufragen.");
						login_logo(1,"registrierung_text","registrierung_logo","registrierung")
						document.getElementsByClassName("login")[0].style.pointerEvents = 'auto';
						document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';
						document.getElementsByClassName("plz_ueberpruefen")[0].style.pointerEvents = 'auto';
					}
					else	
					{
						if(data=="email falsch")
						{
							document.getElementById("eingabe_fehler").innerHTML="Bitte eine gültige E-Mail Adresse angeben";
							login_logo(1,"registrierung_text","registrierung_logo","registrierung")
							document.getElementsByClassName("login")[0].style.pointerEvents = 'auto';
							document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';
							document.getElementsByClassName("plz_ueberpruefen")[0].style.pointerEvents = 'auto';
						}
						else
							if(data!="")
								window.location.href="/hello/"+data+"/";
							else
								window.location.href="/hello/start/";
							
					}
				}
			}); 
		}
	 }
 }
 
 
 function login_logo(index,text_area,logo_area,button_)
 {
	 
	 if (index==0)
	 {
		document.getElementsByClassName(""+text_area+"")[0].style.display="none";
		document.getElementsByClassName(""+logo_area+"")[0].style.display="block";

		document.getElementsByClassName(""+button_+"")[0].style.pointerEvents = 'none';
		

		
	 }
	 else
	 {
		document.getElementsByClassName(""+text_area+"")[0].style.display="block";
		document.getElementsByClassName(""+logo_area+"")[0].style.display="none";	
		document.getElementsByClassName(""+button_+"")[0].style.pointerEvents = 'auto';
		
		 
	 }
	 
 }
 
 
 
  function login()
 {	
 
	
	
	
	 if (check_vollstaendigkeit())
	 {
		 login_logo(0,"login_text","login_logo","login")
		document.getElementsByClassName("registrierung")[0].style.pointerEvents = 'none';
		document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'none';
		document.getElementsByClassName("plz_ueberpruefen")[0].style.pointerEvents = 'none';

		 $.ajax({
			type: "POST",
			url: "/hello/login_user/",
			dataType: "json",
			data: { "item": document.getElementById("username").value+","+document.getElementById("passwort").value },
			success: function(data) {

	
				if(data=="wrong data")
				{

					alert_userdata("FALSCHE LOGIN-DATEN","Wir konnten Dich leider mit den Login-Daten nicht finden. Bitte überprüfe noch einmal Deine E-Mail Adresse und Dein Passwort.");
					login_logo(1,"login_text","login_logo","login")
					document.getElementsByClassName("registrierung")[0].style.pointerEvents = 'auto';
					document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';
					document.getElementsByClassName("plz_ueberpruefen")[0].style.pointerEvents = 'auto';
				}
				else			
					window.location.href="/hello/"+data+"/";
				



			},
			failure: function(data){
				login_logo(1,"login_text","login_logo","login")
				document.getElementsByClassName("registrierung")[0].style.pointerEvents = 'auto';
				document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';
				document.getElementsByClassName("plz_ueberpruefen")[0].style.pointerEvents = 'auto';
				
			}
		});
	 }

		

	 
	 
 }
 
 
 
 
  function warteliste_click() {
	 

	$.ajax({
		type: "POST",
		url: "/hello/auf_warteliste_setzen/",
		dataType: "json",
		data: { "item": warteliste_plz+","+document.getElementsByClassName("email-eingabe")[0].value },
		success: function(data) {
			
			alert_click_schliessen()


		}
	});

}



 function alert_click_schliessen() {

	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "hidden") ? "visible" : "hidden";

	document.getElementsByClassName("transparent_background")[0].style.display="none";
	login_logo(1,"plz_ueberpruefen_text","plz_ueberpruefen_logo","plz_ueberpruefen")
	document.getElementsByClassName("registrierung")[0].style.pointerEvents = 'auto';
	document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';
	document.getElementsByClassName("login")[0].style.pointerEvents = 'auto';
	enableScroll();

}

