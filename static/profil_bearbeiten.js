 var telefon_nummer=new Array(13);
 var string_;
 
 
 function click_checkbox(id)
{
	if(document.getElementsByClassName ("sms_benachrichtigung")[id].checked==true)
		document.getElementsByClassName ("sms_benachrichtigung")[id].checked=false
	else
		document.getElementsByClassName ("sms_benachrichtigung")[id].checked=true
		

}




function profil_laden()
{
	profil=JSON.parse(document.getElementsByClassName("profil_daten")[0].innerHTML)



	password_check(profil[0].passwordcheck)
	document.getElementById("vorname").value=profil[0].vorname;
	document.getElementById("nachname").value=profil[0].nachname;
	document.getElementById("email").value=profil[0].email;
	document.getElementById("telefonnummer").value=profil[0].telefon;
//	if(profil[0].persmsbenachrichtigtwerden=="true")
//		document.getElementsByClassName("sms_benachrichtigung")[0].checked="true";


	if(profil[0].newsletter=="true")
		document.getElementsByClassName("sms_benachrichtigung")[0].checked="true";
			
		
	if(profil[0].telefon!="")
	{
		document.getElementsByClassName("benachrichtigungen_text")[0].style.opacity="1.0";
		document.getElementsByClassName("benachrichtigungen_text")[0].style.pointerEvents ="auto";
		
		
	}
	
	
	
	
	
	
}

function reset_fields_passwort_vergessen()
{

	document.getElementById("email").value="";

}


function password_check_2(passwort)
{

	if (passwort=="not ok")
		document.getElementsByClassName("eingabefelder_headline_pw")[0].style.display="none";
}

function alert_click_schliessen()
{
	
	window.location.href="/account_page/";
	enableScroll();
	
	
}


function alert_click_schliessen_2()
{
	enableScroll();
	el.style.visibility = "hidden"
	document.getElementsByClassName ("overlay")[0].style.visibility = "hidden"
	document.getElementById("x-mask").style.opacity="1.0";
	document.getElementById("x-mask_2").style.opacity="1.0";
}




function onlyAlphabets(e, t) {

            try {
                if (window.event) {
                    var charCode = window.event.keyCode;

                }
                else if (e) {
                    var charCode = e.which;
                }
                else { return true; }

                if ((charCode > 64 && charCode < 91) || (charCode > 96 && charCode < 123) || (charCode == 0) || (charCode == 8) || (charCode == 32) || (charCode == 45))
                    return true;
                else
                    return false;
            }
            catch (err) {
            	id=0;
            }
        }



function check_changes_passwort_vergessen_neu()
{

	if(document.getElementById("neues_passwort").value!="" && document.getElementById("neues_passwort_wiederholen").value!="")
	{
		document.getElementsByClassName ("button_main")[0].style.opacity="1.0";
		document.getElementsByClassName ("button_main")[0].style.pointerEvents="auto";
		document.getElementsByClassName ("button_main")[0].style.cursor="pointer";
	}
	else
	{
		document.getElementsByClassName ("button_main")[0].style.opacity="0.4";
		document.getElementsByClassName ("button_main")[0].style.pointerEvents="none";
		document.getElementsByClassName ("button_main")[0].style.cursor="auto";
	}	
	
}



function check_changes_passwort_vergessen()
{

	if(document.getElementById("email").value!="")
	{
		document.getElementsByClassName ("button_main")[0].style.opacity="1.0";
		document.getElementsByClassName ("button_main")[0].style.pointerEvents="auto";
		document.getElementsByClassName ("button_main")[0].style.cursor="pointer";
	}
	else
	{
		document.getElementsByClassName ("button_main")[0].style.opacity="0.4";
		document.getElementsByClassName ("button_main")[0].style.pointerEvents="none";
		document.getElementsByClassName ("button_main")[0].style.cursor="auto";
	}	
	
}

function check_changes()
{

	if(document.getElementById("vorname").value!=profil[0].vorname || document.getElementById("nachname").value!=profil[0].nachname || document.getElementById("email").value!=profil[0].email ||document.getElementById("telefonnummer").value!=profil[0].telefon || profil[0].newsletter!=document.getElementsByClassName("sms_benachrichtigung")[0].checked.toString())
	{
		document.getElementsByClassName ("button_main")[0].style.opacity="1.0";
		document.getElementsByClassName ("button_main")[0].style.pointerEvents="auto";
		document.getElementsByClassName ("button_main")[0].style.cursor="pointer";
	}
	else
	{
		document.getElementsByClassName ("button_main")[0].style.opacity="0.4";
		document.getElementsByClassName ("button_main")[0].style.pointerEvents="none";
		document.getElementsByClassName ("button_main")[0].style.cursor="auto";
	}	
	
}


 $('#alert_box_load_account').on('hide.bs.modal', function () {
  window.location.href="/account_page/";

});


  function alert_userdata_load_account_page(content1,content2)
 {	 
	
	document.getElementById("alert_box_load_account_headline").innerHTML=content1;
	document.getElementById("alert_box_load_account_body").innerHTML=content2;
	$('#alert_box_load_account').modal('show');
 }


function profil_aktualisieren()
{

		vorname=document.getElementById("vorname").value

		nachname=document.getElementById("nachname").value

		email=document.getElementById("email").value

		telefonnummer=document.getElementById("telefonnummer").value

		button_logo("0","button_main_profil_text","button_main_profil_logo","button_main_profil")	
		$.ajax({
				timeout:15000,
	 			error: function(){	
					button_logo("1","button_main_profil_text","button_main_profil_logo","button_main_profil")	
						},
			type: "POST",
			url: "/account_page/profil_aktualisieren/",
			dataType: "json",
			data: { "vorname": vorname,"nachname": nachname,"passwort": document.getElementById("passwort_eingabefeld").value,"email": email,"telefonnummer": telefonnummer,"newsletter":document.getElementsByClassName("sms_benachrichtigung")[0].checked  },
			success: function(data) {
				button_logo("1","button_main_profil_text","button_main_profil_logo","button_main_profil")
	
				if (data=="ok")
					alert_userdata_load_account_page("DATEN GEÄNDERT","Du hast Dein Profil erfolgreich geändert")

				else
				{
					if(data=="")
						{
							alert_userdata("PASSWORT STIMMT NICHT","Das eingegebene Passwort stimmt nicht. Bitte überprüfe Deine Eingabe.")
							 
							document.getElementById("passwort_text").style.color="red";	
							document.getElementById("passwort_eingabefeld").style.border="1px solid red";	
	
						}
					else
					{
						if(data=="exists already")
							{
								alert_userdata("E-MAIL-ADRESSE EXISTIERT BEREITS","Die eingegebene E-Mail-Adresse existiert bereits bei einem anderen User. Bitte nutze eine andere E-Mail-Adresse.")
								document.getElementById("email_headline").style.color="red";	
								document.getElementById("email").style.border="1px solid red ";	
		
							}
							else
							{
								if(data=="e-mail nicht ok")
									{
										alert_userdata("E-MAIL-ADRESSE NICHT GÜLTIG","Die eingegebene E-Mail-Adresse ist nicht gültig. Bitte ändere Deine E-Mail-Adresse.")
										document.getElementById("email_headline").style.color="red";	
										document.getElementById("email").style.border="1px solid red ";	
				
									}
									else		
									{

										if(data=="mobilnummer nicht korrekt")
											{
												alert_userdata("MOBILNUMMER NICHT KORREKT","Die eingegebene Mobilnummer ist nicht gültig. Bitte gib eine andere Mobilnummer an.")
												document.getElementById("telefonnummer_headline").style.color="red";	
												document.getElementById("telefonnummer").style.border="1px solid red ";	
						
											}				
							}		
							}
					}
				}
												
					
	
	
			}
		});
	
	
}

 function input_on_change(element,element2)
{
	
	element.style.border="1px solid #e6e6e6 ";	
	element2.style.color="#4E4E4E";
	check_changes();
}


function input_on_change_passwort_neu(element,element2)
{
	
	element.style.border="1px solid #e6e6e6 ";	
	element2.style.color="#4E4E4E";
	check_changes_passwort_vergessen_neu();
}

 function input_on_change_passwort_vergessen(element,element2)
{
	
	element.style.border="1px solid #e6e6e6 ";	
	element2.style.color="#4E4E4E";
	check_changes_passwort_vergessen();
}

 function input_on_change_passwort(element,element2)
{


	if((document.getElementsByClassName("eingabefelder_pw")[0].value!="" || document.getElementsByClassName("eingabefelder_pw")[0].offsetWidth==0) && document.getElementsByClassName("eingabefelder_pw")[1].value!="" && document.getElementsByClassName("eingabefelder_pw")[2].value!="")
	{
		document.getElementsByClassName("button_main")[0].style.pointerEvents = 'auto';
		document.getElementsByClassName("button_main")[0].style.cursor = 'pointer';
		
		document.getElementsByClassName("button_main")[0].style.opacity = '1.0';
		
	}
	else
	{
		document.getElementsByClassName("button_main")[0].style.pointerEvents = 'none';
		document.getElementsByClassName("button_main")[0].style.cursor = 'auto';
		document.getElementsByClassName("button_main")[0].style.opacity = '0.4';
	}
	
	element.style.border="1px solid #e6e6e6 ";	
	element2.style.color="#4E4E4E";
}



function check_mobilnummer()
{
		$.ajax({
				timeout:15000,
	 			error: function(){	
					
						},
		type: "POST",
		url: "/check_mobilnummer/",
		dataType: "json",
		data: { "telefonnummer": document.getElementById("telefonnummer").value },
		success: function(data) {
			telefonnummern=JSON.parse(data)
			if(telefonnummern[0].telefonnummer=="")
			{
				document.getElementById("eingabe_fehler").innerHTML ="Bitte gib eine richtige Mobilnummer an."
				document.getElementById("telefonnummer_headline").style.color="red";	
				document.getElementById("telefonnummer").style.border="1px solid red";
				document.getElementsByClassName("benachrichtigungen_text")[0].style.opacity="0.4";
				document.getElementsByClassName("benachrichtigungen_text")[0].style.pointerEvents ="none";
				
			}
			else
			{

					document.getElementById("telefonnummer").value=telefonnummern[0].telefonnummer
	
	
				document.getElementById("eingabe_fehler").innerHTML=""
				document.getElementById("telefonnummer_headline").style.color="#000000";	
				document.getElementById("telefonnummer").style.border="1px solid #e6e6e6";
				document.getElementsByClassName("benachrichtigungen_text")[0].style.opacity="1.0";
				document.getElementsByClassName("benachrichtigungen_text")[0].style.pointerEvents ="auto";
			}
		}
		})
			
	
}




 function validate(evt) {
 	  check_changes();
 	input_on_change(document.getElementById('telefonnummer'),document.getElementById('telefonnummer_headline'))
  var theEvent = evt || window.event;
  var key = theEvent.keyCode || theEvent.which;

  key = String.fromCharCode( key );

  var regex = /[0-9]|\./;

  if( !regex.test(key) && theEvent.keyCode!=8 && theEvent.keyCode !=9) {
    theEvent.returnValue = false;
    if(theEvent.preventDefault) theEvent.preventDefault();
  }

}


function passwort_vergessen_beantragen()
{			



	$.ajax({
				timeout:15000,
	 			error: function(){	
					
						},
				type: "POST",
				url: "/account_page/request_passwort_vergessen/",
				dataType: "json",
				data: { "email": document.getElementsByClassName ("eingabefelder_profil")[0].value},
				success: function(data) {
					
					alert_userdata_box_password_changed("PASSWORT VERGESSEN","Wir haben dir einen Link an deine E-Mail Adresse geschickt. Mit dem Link kannst du dein Passwort zurücksetzen.")

				}
				
	})
	
}


function newsletter_abmelden(security_key)
{
			$.ajax({
				timeout:15000,
	 			error: function(){	
					
						},
				type: "POST",
				url: "/newsletter_abmelden/",
				dataType: "json",
				data: { "security_key":security_key},
				success: function(data) {

						alert_userdata_box_password_changed("NEWSLETTER ABMELDUNG BESTÄTIGT","Du hast Dich erfolgreich vom Newsletter abgemeldet")

				}
			});	
}




function anmeldung_bestaetigen(security_key)
{
        page_load(0);
			$.ajax({
				timeout:15000,
	 			error: function(){	
	 					
						},

				type: "POST",
				url: "/email_adresse_zu_bestaetigen/",
				dataType: "json",
				data: { "code":security_key},
				success: function(data) {
												alert_userdata_box_password_changed("ANMELDUNG BESTÄTIGT","Du hast Deine Anmeldung erfolgreich bestätigt.")
												        page_load(1);


				}
			});	

}


function passwort_aendern(security_key)
{

	passwort="not ok"
	if(check_vollstaendigkeit_passwort(passwort,"",document.getElementsByClassName("eingabefelder_pw")[0],document.getElementsByClassName("eingabefelder_pw")[1]))
	{

		if(passwort_lang_genug_check_passwort_vergessen(passwort))
		{

			if(passwort=="not ok")
				aktuelles_passwort=""

			$.ajax({
								timeout:15000,
	 			error: function(){	
	 							
						},
				type: "POST",
				url: "/account_page/passwort_aendern_passwort_vergessen/",
				dataType: "json",
				data: { "security_key":security_key,"neues_passwort": document.getElementById("neues_passwort").value},
				success: function(data) {

					if (data=="ok")


						alert_userdata_box_password_changed("PASSWORT GEÄNDERT","Du hast Dein Passwort erfolgreich geändert.")

					else
						window.location.href="/";


				}
			});
		}
	}
		
	
}


  function alert_userdata_box_password_changed(content1,content2)
 {	 
	
	document.getElementById("alert_box_password_changed_headline").innerHTML=content1;
	document.getElementById("alert_box_password_changed_body").innerHTML=content2;
	$('#alert_box_password_changed').modal('show');
 }
 
  $('#alert_box_password_changed').on('hide.bs.modal', function () {
  window.location.href="/";

});




function passwort_aktualisieren(passwort)
{

	if(check_vollstaendigkeit_passwort(passwort,document.getElementsByClassName("eingabefelder_pw")[0],document.getElementsByClassName("eingabefelder_pw")[1],document.getElementsByClassName("eingabefelder_pw")[2]))
	{

		if(passwort_lang_genug_check(passwort))
		{

			if(passwort=="not ok")
				aktuelles_passwort=""
			else
				aktuelles_passwort=document.getElementById("aktuelles_passwort").value

			button_logo("0","button_main_password_text","button_main_password_logo","button_main_password")
			$.ajax({
								timeout:15000,
	 			error: function(){	
	 							
						},
				type: "POST",
				url: "/account_page/passwort_aktualisieren/",
				dataType: "json",
				data: { "altes_passwort": aktuelles_passwort,"neues_passwort": document.getElementById("neues_passwort").value},
				success: function(data) {
					button_logo("1","button_main_password_text","button_main_password_logo","button_main_password")
					if (data=="ok")

						alert_userdata_load_account_page("PASSWORT GEÄNDERT","Du hast Dein Passwort erfolgreich geändert.")
					else
					{
						alert_userdata("AKTUELLES PASSWORT STIMMT NICHT","Das eingegebene aktuelle Passwort stimmt nicht.")
						document.getElementById("aktuelles_passwort_text").style.color="red";	
						document.getElementById("aktuelles_passwort").style.border="1px solid red ";	
					}


				}
			});
		}
	}
		
	
}




 function check_vollstaendigkeit_passwort(passwort,element0,element1,element2)
 {

	 if (passwort=="not ok")
	 {
		 if(element1.value=="" || element2.value=="")
			document.getElementById("eingabe_fehler").innerHTML="Bitte Passwort angeben";
		else
		  return true		 
	 }
	 else
	 {
		 if(element0.value=="" || element1.value=="" || element2.value=="")
			document.getElementById("eingabe_fehler").innerHTML="Bitte Passwort angeben";
		else
		  return true	
		 
	 }
		 
	 
 }
 
 
  function passwort_lang_genug_check_passwort_vergessen(passwort)
 {
 	

	if(document.getElementsByClassName("eingabefelder_pw")[0].value.length<6 || document.getElementsByClassName("eingabefelder_pw")[1].value.length<6 )
	{
		alert_userdata("PASSWORT NICHT LANG GENUG","Das neue Passwort muss mindestens sechs Stellen haben")
						document.getElementById("neues_passwort_text").style.color="red";	
						document.getElementById("neues_passwort").style.border="1px solid red ";	
						document.getElementById("neues_passwort_wiederholen_text").style.color="red";	
						document.getElementById("neues_passwort_wiederholen").style.border="1px solid red ";		
	}
	else
		if(document.getElementsByClassName("eingabefelder_pw")[0].value!=document.getElementsByClassName("eingabefelder_pw")[1].value)
		{
			alert_userdata("PASSWÖRTER NICHT GLEICH","Die neuen Passwörter sind nicht gleich")
						document.getElementById("neues_passwort_text").style.color="red";	
						document.getElementById("neues_passwort").style.border="1px solid red ";	
						document.getElementById("neues_passwort_wiederholen_text").style.color="red";	
						document.getElementById("neues_passwort_wiederholen").style.border="1px solid red ";	
		}
		else
			return true
	 
	 
 }
 
 
 function passwort_lang_genug_check(passwort)
 {
 	

	if(document.getElementsByClassName("eingabefelder_pw")[1].value.length<6 || document.getElementsByClassName("eingabefelder_pw")[2].value.length<6 )
	{
		alert_userdata("PASSWORT NICHT LANG GENUG","Das neue Passwort muss mindestens sechs Stellen haben")
						document.getElementById("neues_passwort_text").style.color="red";	
						document.getElementById("neues_passwort").style.border="1px solid red ";	
						document.getElementById("neues_passwort_wiederholen_text").style.color="red";	
						document.getElementById("neues_passwort_wiederholen").style.border="1px solid red ";		
	}
	else
		if(document.getElementsByClassName("eingabefelder_pw")[1].value!=document.getElementsByClassName("eingabefelder_pw")[2].value)
		{
			alert_userdata("PASSWÖRTER NICHT GLEICH","Die neuen Passwörter sind nicht gleich")
						document.getElementById("neues_passwort_text").style.color="red";	
						document.getElementById("neues_passwort").style.border="1px solid red ";	
						document.getElementById("neues_passwort_wiederholen_text").style.color="red";	
						document.getElementById("neues_passwort_wiederholen").style.border="1px solid red ";	
		}
		else
			return true
	 
	 
 }


function profil_hauptseite()
{
	window.location.href="/account_page/";
}


function array_definieren()
{
	i=0;


	while(i<=13)
	{	
		telefon_nummer[i]=new Array;
		i=i+1;
	}
	
	
}


function telefonnummer_erkennung(evt)
 {

	 

		var theEvent = evt || window.event;
		var key = theEvent.keyCode || theEvent.which;


	
	

	if(key ==48 || key==49 || key==50 || key==51 || key==52 || key==53 || key==54 || key==55 || key==56 || key==57 || key==58)
	
	{


		if(document.getElementsByClassName("eingabefelder_profil")[3].value!=string_ )
		{
			string_=document.getElementsByClassName("eingabefelder_profil")[3].value;
			var max=document.getElementsByClassName("eingabefelder_profil")[3].value.length;


			var number=document.getElementsByClassName("eingabefelder_profil")[3].value;	
			number=number.replace("(","");
			number=number.replace(")-","");

			
			document.getElementsByClassName("eingabefelder_profil")[3].value=number;
			
			
			
			
			var max=document.getElementsByClassName("eingabefelder_profil")[3].value.length;	

			var i=0;
			var j=0;
			while(i<=max-1)
			{

				var number=document.getElementsByClassName("eingabefelder_profil")[3].value.charAt(i);
				
				if(isNaN(number)==false)
				{

					if(i==0)
					{
						telefon_nummer[j]="(";
						j=j+1;
						max=max+1;
						telefon_nummer[j]=document.getElementsByClassName("eingabefelder_profil")[3].value.charAt(i);

					}
					else
						if(i==4)
						{
							telefon_nummer[j]=")";

							j=j+1;
							max=max+1;
		

							telefon_nummer[j]=document.getElementsByClassName("eingabefelder_profil")[3].value.charAt(i);
						}


							else
							{
								telefon_nummer[j]=document.getElementsByClassName("eingabefelder_profil")[3].value.charAt(i);
							}
				}
				i=i+1;
				j=j+1;

			}
			
			i=0
			

			document.getElementsByClassName("eingabefelder_profil")[3].value="";
			string_="";
			while(i<=max-1)
			{
				
				document.getElementsByClassName("eingabefelder_profil")[3].value=document.getElementsByClassName("eingabefelder_profil")[3].value+telefon_nummer[i];

				i=i+1;
				
			}


			string_=document.getElementsByClassName("eingabefelder_profil")[3].value;

		}


		
		
	}
	else
	{
		if(theEvent.keyCode!=8)
		{
			theEvent.returnValue = false;theEvent.returnValue = false;
			if(theEvent.preventDefault) theEvent.preventDefault();
		}
		
	}


	 
 }


