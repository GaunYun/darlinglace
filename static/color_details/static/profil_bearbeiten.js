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
	if(profil[0].persmsbenachrichtigtwerden=="true")
		document.getElementsByClassName("sms_benachrichtigung")[0].checked="true";


	if(profil[0].newsletter=="true")
		document.getElementsByClassName("sms_benachrichtigung")[1].checked="true";
			
		
	if(profil[0].telefon!="")
	{
		document.getElementsByClassName("benachrichtigungen_text")[0].style.opacity="1.0";
		document.getElementsByClassName("benachrichtigungen_text")[0].style.pointerEvents ="auto";
		
		
	}
	
	
	
	
	
	
}


function password_check_2(passwort)
{

	if (passwort=="not ok")
		document.getElementsByClassName("eingabefelder_headline_pw")[0].style.display="none";
}

function alert_click_schliessen()
{
	
	window.location.href="/hello/account_page/";
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
                if ((charCode > 64 && charCode < 91) || (charCode > 96 && charCode < 123))
                    return true;
                else
                    return false;
            }
            catch (err) {
                alert(err.Description);
            }
        }



function check_changes()
{

	if(document.getElementById("vorname").value!=profil[0].vorname || document.getElementById("nachname").value!=profil[0].nachname || document.getElementById("email").value!=profil[0].email ||document.getElementById("telefonnummer").value!=profil[0].telefon || profil[0].persmsbenachrichtigtwerden!=document.getElementsByClassName("sms_benachrichtigung")[0].checked.toString() || profil[0].newsletter!=document.getElementsByClassName("sms_benachrichtigung")[1].checked.toString())
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
  window.location.href="/hello/account_page/";

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



		$.ajax({
			type: "POST",
			url: "/hello/account_page/profil_aktualisieren/",
			dataType: "json",
			data: { "vorname": vorname,"nachname": nachname,"passwort": document.getElementById("passwort_eingabefeld").value,"email": email,"telefonnummer": telefonnummer,"benachrichtigung":document.getElementsByClassName("sms_benachrichtigung")[0].checked,"newsletter":document.getElementsByClassName("sms_benachrichtigung")[1].checked  },
			success: function(data) {

	
				if (data=="ok")
					alert_userdata_load_account_page("DATEN GEÄNDERT","Du hast Dein Profil erfolgreich geändert")

				else
				{
					if(data=="")
						{
							alert_userdata("PASSWORT STIMMT NICHT","Das eingegebene aktuelle Passwort stimmt nicht. Bitte überprüfe deine Eingabe.")
							document.getElementById("passwort_text").style.color="red";	
							document.getElementById("passwort_eingabefeld").style.border="1px solid red ";	
	
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
										alert_userdata("E-MAIL-ADRESSE NICHT GÜLTIG","Die eingegebene E-Mail-Adresse ist nicht gültig. Bitte ändere deine E-Mail-Adresse.")
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
		type: "POST",
		url: "/hello/check_mobilnummer/",
		dataType: "json",
		data: { "telefonnummer": document.getElementById("telefonnummer").value },
		success: function(data) {

			if(data=="")
			{
				document.getElementById("eingabe_fehler").innerHTML ="Bitte gib eine richtige Mobilnummer an."
				document.getElementById("telefonnummer_headline").style.color="red";	
				document.getElementById("telefonnummer").style.border="1px solid red";
				document.getElementsByClassName("benachrichtigungen_text")[0].style.opacity="0.4";
				document.getElementsByClassName("benachrichtigungen_text")[0].style.pointerEvents ="none";
				
			}
			else
			{
				document.getElementById("telefonnummer").value=data
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
  if( !regex.test(key) && theEvent.keyCode!=8) {
    theEvent.returnValue = false;
    if(theEvent.preventDefault) theEvent.preventDefault();
  }

}


function passwort_aktualisieren(passwort)
{

	if(check_vollstaendigkeit_passwort(passwort))
	{

		if(passwort_lang_genug_check(passwort))
		{

			if(passwort=="not ok")
				aktuelles_passwort=""
			else
				aktuelles_passwort=document.getElementById("aktuelles_passwort").value


			$.ajax({
				type: "POST",
				url: "/hello/account_page/passwort_aktualisieren/",
				dataType: "json",
				data: { "altes_passwort": aktuelles_passwort,"neues_passwort": document.getElementById("neues_passwort").value},
				success: function(data) {

					if (data=="ok")

						alert_userdata_load_account_page("PASSWORT GEÄNDERT","Du hast Dein Passwort erfolgreich geändert")
					else
					{
						alert_userdata("ALTES PASSWORT STIMMT NICHT","Das eingegebene aktuelle Passwort stimmt nicht.")
					}


				}
			});
		}
	}
		
	
}

 function check_vollstaendigkeit_passwort(passwort)
 {

	 if (passwort=="not ok")
	 {
		 if(document.getElementsByClassName("eingabefelder_pw")[1].value=="" || document.getElementsByClassName("eingabefelder_pw")[2].value=="")
			document.getElementById("eingabe_fehler").innerHTML="Bitte Passwort angeben";
		else
		  return true		 
	 }
	 else
	 {
		 if(document.getElementsByClassName("eingabefelder_pw")[0].value=="" || document.getElementsByClassName("eingabefelder_pw")[1].value=="" || document.getElementsByClassName("eingabefelder_pw")[2].value=="")
			document.getElementById("eingabe_fehler").innerHTML="Bitte Passwort angeben";
		else
		  return true	
		 
	 }
		 
	 
 }
 
 
 function passwort_lang_genug_check(passwort)
 {
 	

	if(document.getElementsByClassName("eingabefelder_pw")[1].value.length<6 || document.getElementsByClassName("eingabefelder_pw")[2].value.length<6 )
		alert_userdata("PASSWORT NICHT LANG GENUG","Das Passwort muss mindestens 6 Stellen haben")
	else
		if(document.getElementsByClassName("eingabefelder_pw")[1].value!=document.getElementsByClassName("eingabefelder_pw")[2].value)
			alert_userdata("PASSWÖRTER NICHT GLEICH","Die neuen Passwörter sind nicht gleich")
		else
			return true
	 
	 
 }


function profil_hauptseite()
{
	
	window.location.href="/hello/account_page/";
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


