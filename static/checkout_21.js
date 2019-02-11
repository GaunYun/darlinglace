	var zutaten=new Array(50);
   var gerichte = new Array(20); 
   var cart=new Array(10);
   var datum_text=new Array(4);
   var max;
   var kreditkarten_nummer=new Array(15);
   var kreditkarten_nummer_stelle;
   var string_;
   var datum_in_cart=new Array(12);
   var gesamt;
   var preis;
	var strasse;
	var VIP;
	var nummer;
	var apt;
	var plz;
	var stadt;
	var land;
	var vorname;
	var nachname;
	var telefonnummer;
	var unternehmensdetails;
	var zahlungsoption;
	var kreditkarten_nummer_;
	var kreditkarten_nummer__;
	var ablaufdatum;
	var pruefnummer;
	var preis_;
	var rabatt_;
	var rabatt;
	var name_karteninhaber;
	var fahrer_kapazitaet;
	var lieferkosten;
	var credit;
	var credit_;
	
	var adressbuch;
	var adresse_neu;
	var zahlungsmethoden;
	var gesamtzahl_gerichte;
	var shopping_type;
	var lieferhinweise;
	var bra_for_free;
	var bra_for_freecount;
	var bra_for_freevalue;
	var first_height;
	var subscription;
	var storecredit,storecredit_to_be_used;
	var rebates;
	var VIP_or_pay_as_you_go_selected;
	var cart_page;
	var selected_zahlungsoption;
	   
function check_login_window()
{
	if(document.getElementById("login_window").innerHTML=="true" && login=="false")
	
			$('#login').modal({backdrop: 'static', keyboard: false})  

}



function send_data_gtag(content_id_list)
{
	contents_list=document.getElementById("contents_list").innerHTML
	
	
	google_content_list=contents_list[0].google
	

    
    
 gtag('event', 'checkout_progress', {
  "items":google_content_list,
  "coupon": rebates[0].couponcode
});	
	
	
}

function initiate_cart_fb(content_id_list,contents_list,value_)
{
	






	contents_list=JSON.parse(document.getElementById("contents_list").innerHTML)
	content_id_list=document.getElementById("content_id_list").innerHTML
	
	
	facebook_content_list=contents_list[0].facebook
	google_content_list=contents_list[0].google
	
	
	

    fbq('track', 'InitiateCheckout', {
      content_category: "Sets",
      value: rebates[0].gesamtpreis,
      currency: 'EUR' 
    });  	
    
    

    
    
 gtag('event', 'begin_checkout', {
  "items":google_content_list,
  "coupon": rebates[0].couponcode
});



}

function show_VIP_AGB(status_)
{

		document.getElementById("headline_VIP_AGB").style.display=status_;
		document.getElementById("VIP_terms_conditions_checkbox_text").style.display=status_;	

		
		
}


function show_VIP_terms_conditions()
{
	document.getElementById("alert_box_headline_VIP").innerHTML="VIP Programm FAQ";
	
	box="<b>Was ist VIP?</b><br>"
	box=box+"Unsere VIP Mitgliedschaft gibt Dir noch günstigere Preise und weitere Vorteile. Du erhältst auf jedes BH Set 10 € Rabatt und bekommst noch dazu jedes sechste BH Set von uns geschenkt. Du fragst Dich, wie Du diese tollen Vorteile ohne Kosten genießen kannst? Ganz einfach: Jeden Monat entweder ein BH Set kaufen, oder den Monat „pausieren“. Solltest Du vor dem 10. des Monats weder einkaufen noch in Deinem Kundenkonto die Option „pausieren“ wählen, dann wird Dir am 11. des Monats ein VIP-Mitglieder-Credit von 29,95 € berechnet, den Du jederzeit zum Einkaufen bei Darling Lace nutzen kannst. <br><br>"
	
	
	box=box+"<b>Wie oft hintereinander kann ich pausieren?</b><br>"
	box=box+"So oft Du willst! Wenn Du nichts kaufen möchtest, kannst Du einfach immer wieder bis zum 10. des Monats in Deinem Kundenkonto die Option „diesen Monat pausieren“ anklicken. So bleibet Deine VIP Mitgliedschaft immer kostenfrei.<br><br>"


	box=box+"<b>Ich habe bereits „pausieren“ gewählt, möchte aber nun doch etwas kaufen &ndash; geht das?</b><br>"
	box=box+"Natürlich! Du kannst jederzeit einkaufen und Deine VIP Vorteile nutzen. Lege einfach Ware in Deinen Warenkorb und gehe zum Check-Out. Du bekommst automatisch den günstigen VIP Preis berechnet und jeder Einkauf bringt Dich näher an Dein kostenloses sechstes Set.<br><br>"
	
	box=box+"<b>Muss ich jeden Monat etwas kaufen? </b><br>"
	box=box+"Nein, natürlich nicht. Du kannst immer bis zum 10. eines Monats in Deinem Kundenkonto auswählen „diesen Monat pausieren“ &ndash; so bleibt Deine VIP Mitgliedschaft für Dich jeden Monat kostenfrei.<br><br>"		
	



	box=box+"<b>Was passiert, wenn ich bis zum 10. eines Monats weder etwas kaufe noch „pausieren“ wähle?</b><br>"
	box=box+"Wenn Du bis zum 10. eines Monats weder ein BH Set kaufst noch „pausieren“ wählst, dann wird Dir am 11. des Monats ein VIP-Mitglieder-Credit von 29,95 € berechnet, den Du jederzeit zum Einkaufen bei Darling Lace nutzen kannst. Den Betrag buchen wir von Deinem hinterlegten Zahlungsmittel ab und schreiben ihn Dir umgehend auf Deinem Kundenkonto als VIP-Guthaben gut. Solltest Du einmal vergessen bis zum 10. eines Monats „pausieren“ zu wählen und möchtest nichts kaufen, dann kannst Du jederzeit die Auszahlung Deines VIP Guthabens in Deinem Kundenkonto wählen. Wir erstatten Dir Dein VIP Guthaben umgehend zurück &ndash; ohne Wenn und Aber, jederzeit.<br><br>"		
	
	
	box=box+"<b>Verfällt VIP-Guthaben bei Darling Lace?</b><br>"
	box=box+"Nein, natürlich nicht! VIP-Guthaben hast Du bei uns eingezahlt und kannst es jederzeit zum Einkaufen nutzen, es verfällt nie.<br><br>"		



	box=box+"<b>Wie kann ich VIP kündigen? </b><br>"
	box=box+"Du kannst jederzeit in Deinem Kundenkonto die VIP Mitgliedschaft beenden. Es gibt keine Frist und keine Mindestlaufzeit. Von Dir bereits bezahltes und noch nicht zum Einkaufen genutztes VIP-Guthaben wird Dir natürlich erstattet.<br><br>"		
	
	
		
	document.getElementById("alert_box_body_VIP").innerHTML=box

	$('#alert_box_VIP_FAQ').modal('show');	
}


function show_klarna_agb()
 {

	
}


function zur_kasse()
{
	if(document.getElementById("gutschein_input").value!="" && document.getElementById("gutschein_button_id_text").innerHTML=="Überprüfen" && document.getElementsByClassName("promo_code")[0].innerHTML!="<b>+</b> Gutschein-Code hinzufügen")
	
				alert_userdata("GUTSCHEIN ÜBERPRÜFEN","Lass den eingegebenen Gutschein-Code überprüfen indem Du auf den Button Überprüfen klickst.")
		else
			window.top.location.href = "/checkout/"

		
}
      


 function validate(evt) {
	 
  var theEvent = evt || window.event;
  var key = theEvent.keyCode || theEvent.which;
  key = String.fromCharCode( key );
  var regex = /[0-9]|\./;
  if( !regex.test(key) && theEvent.keyCode!=8 && theEvent.keyCode !=9) {
    theEvent.returnValue = false;
    if(theEvent.preventDefault) theEvent.preventDefault();
  }
}



 function click_checkbox_unternehmensangaben(id)
{
	if(document.getElementsByClassName ("checkbox_unternehmensangaben")[id].checked==true)
	{
		document.getElementsByClassName ("checkbox_unternehmensangaben")[id].checked=false
	}
	else
	{

		document.getElementsByClassName ("checkbox_unternehmensangaben")[id].checked=true

	}
		

}


 function click_abweichende_lieferadresse_checkbox(id)
{
	if(document.getElementsByClassName ("checkbox_abweichende_lieferadresse")[id].checked==true)
	{
		document.getElementsByClassName ("checkbox_abweichende_lieferadresse")[id].checked=false
	}
	else
	{

		document.getElementsByClassName ("checkbox_abweichende_lieferadresse")[id].checked=true

	}
}
		





function click_checkbox_abweichende_lieferadresse()
{

	if(document.getElementById("rubrik_abweichende_lieferadresse").style.display=="none")
	{
		document.getElementById("rubrik_abweichende_lieferadresse").style.display="block";
		document.getElementById("title_rechnungsadresse").innerHTML="Rechnungsadresse";
	}
	else
	{
		document.getElementById("rubrik_abweichende_lieferadresse").style.display="none";	
		document.getElementById("title_rechnungsadresse").innerHTML="Rechnungsadresse/ Lieferadresse";
	}	
	
}

function adresse_anzeigen(existent_rechnungsadresse,existent_lieferadresse)
{
	box=""
	
	i=0;

	while(i<=1)
	{
		if(i==0)
		{
			box="<b><div id='title_rechnungsadresse'>Rechnungsadresse/ Lieferadresse</div></b><br><input id='existent_rechnungsadresse' type='hidden' value='"+existent_rechnungsadresse+"' />"
		}
		else
		{
			box=box+"<br><br><br><div id='rubrik_abweichende_lieferadresse' style='display:none'><b><div id='title_lieferadresse'>Abweichende Lieferadresse</div></b><input id='existent_lieferadresse' type='hidden' value='"+existent_lieferadresse+"' /><br>"
		}
			
		box=box+"<div class='adressdetails'>"
		
		box=box+"<div class='address_input_header' style='width:60%;float:left;' >Adresse<br><input class='adresse_input'  placeholder='Adresse eingeben'";
		box=box+"  type='text' style='width:100%;' onkeyup='felder_adresse_zuruecksetzen_adresse(0,"+i+")' onkeydown='felder_adresse_zuruecksetzen_adresse(0,"+i+")'></input></div>";
	
		box=box+"<div class='address_input_header' style='width:30%;float:right;' >Hausnummer<br><input class='adresse' placeholder=''";
		box=box+"  type='text' style='width:100%;' onkeyup='felder_adresse_zuruecksetzen_adresse(1,"+i+")' onkeydown='felder_adresse_zuruecksetzen_adresse(1,"+i+")'></input></div><br><br><br>";
				
		box=box+"<div ><div class='address_input_header' style='float:left;width:60%'>Stadt<br><input class='adresse' placeholder=''";
		box=box+"type='text' style='width:100%' onkeyup='felder_adresse_zuruecksetzen_adresse(2,"+i+")' onkeydown='felder_adresse_zuruecksetzen_adresse(2,"+i+")'></input></div>"
		
		box=box+"<div class='address_input_header' style='float:right;width:30%;'>Postleitzahl<br><input class='adresse'  placeholder=''";
		box=box+"type='text' onkeypress='validate(event)' style='width:100%;' onkeyup='felder_adresse_zuruecksetzen_adresse(3,"+i+")' onkeydown='felder_adresse_zuruecksetzen_adresse(3,"+i+")'></div></div><br><br><br>"
		
		box=box+"<div class='address_input_header' style='width:100%;' >Land<br><input class='adresse' placeholder=''";
		box=box+"type='text' style='width:100%;' onkeyup='felder_adresse_zuruecksetzen_adresse(4,"+i+")' onkeydown='felder_adresse_zuruecksetzen_adresse(4,"+i+")'></input></div></div><br>";
		
		
		box=box+"<div class='benachrichtigungen_text' onclick='unternehmen_check(this.id)' id='"+i+"'><input type='checkbox' class='checkbox_unternehmensangaben' style='cursor:pointer;float:left;'   id='checkbox_unternehmen'></input><div style='cursor:pointer;float:left;width:80%;margin-left:10px;margin-top:-2px;' id='"+i+"' onclick='click_checkbox_unternehmensangaben(this.id)'>Zu einem Unternehmen liefern</div></div><br>"
	
		box=box+"<br><div class='address_unternehmensangaben_input_header' style='display:none'>Unternehmensangaben<br><input type='text' class='unternehmensdetails' id='unternehmensdetails_id' placeholder=''></input><br><br></div>";
				   
				   
		box=box+"<div style='width:100%;'>"
		
		box=box+"<div><div class='address_other_input_header' style='float:left;width:45%'>Anrede<br><select class='adresse_other' style='width:100%'";
		box=box+"type='text' onchange='felder_adresse_zuruecksetzen_adresse_other(0,"+i+")' value=''><option></option><option>Frau</option><option>Herr</option></select></div>"
	
		box=box+"<div class='address_other_input_header' style='float:right;width:45%'>Vorname<br><input class='adresse_other' style='width:100%'";
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen_adresse_other(1,"+i+")' onkeydown='felder_adresse_zuruecksetzen_adresse_other(1,"+i+")' value=''></div></div><br><br><br>"	
	
		box=box+"<div><div class='address_other_input_header' style='float:left;width:45%' >Nachname<br><input class='adresse_other' style='width:100%'";
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen_adresse_other(2,"+i+")' onkeydown='felder_adresse_zuruecksetzen_adresse_other(2,"+i+")'></input></div>"
		
		box=box+"<div class='address_mobilnummer_input_header' style='float:right;width:45%'>Mobilnummer<br><input class='adresse_mobilnummer' onkeypress='validate(event)' maxlength='20' style='width:100%;padding-left:40px;'"
		box=box+" type='text' onkeyup='felder_adresse_zuruecksetzen_adresse_mobilnummer(0,"+i+")' onkeydown='felder_adresse_zuruecksetzen_adresse_mobilnummer(0,"+i+")'  ></input><div class='vorwahl'>+49</div></div><div class='eingabe_fehler' style='font-size:12px;color:#C80000;position:absolute;margin-top:10px;'></div></div></div><br>";
	
//onblur='check_mobilnummer()' 
		
		if(i==1)
			box=box+"<br><br><br></div>"
		else
			box=box+"</div><br>"
		i=i+1
	}
	box=box+"<div class='benachrichtigungen_text' onclick='click_checkbox_abweichende_lieferadresse()' ><input type='checkbox' class='checkbox_abweichende_lieferadresse' style='cursor:pointer;float:left;'   id='checkbox_abweichende_lieferadresse'></input><div style='cursor:pointer;float:left;width:80%;margin-left:10px;margin-top:-2px;' id='0' onclick='click_abweichende_lieferadresse_checkbox(this.id)'>Abweichende Lieferadresse</div></div><br><br>"
	document.getElementsByClassName("button_check")[0].style.display="block";
	document.getElementById("total_address").innerHTML=box;
	
	if(existent_rechnungsadresse!=existent_lieferadresse)
	{
		click_abweichende_lieferadresse_checkbox(0);
		click_checkbox_abweichende_lieferadresse()
		document.getElementById("title_rechnungsadresse").innerHTML="Rechnungsadresse";
		
	}


	initialize();


}


function check_mobilnummer()
{

		if(document.getElementsByClassName("adresse")[4].value!="")
		{	
			$.ajax({
			timeout:15000,
 			error: function(){},
			type: "POST",
			url: "/check_mobilnummer/",
			dataType: "json",
			data: { "telefonnummer": document.getElementsByClassName("adresse")[4].value },
			success: function(data) {
				
	
				if(data=="")
				{
					document.getElementById("buttons_address_text").innerHTML ="Bitte gib eine richtige Mobilnummer an."
					document.getElementsByClassName("adresse")[4].style.border="1px solid red";	
					document.getElementsByClassName("address_mobilnummer")[0].style.color="red";		
				}
	
				else
				{
					document.getElementsByClassName("adresse")[4].value=data
					document.getElementById("buttons_address_text").innerHTML=""
					document.getElementsByClassName("adresse")[4].style.border="1px solid #e6e6e6";	
					document.getElementsByClassName("address_mobilnummer")[0].style.color="#4E4E4E";			
				}
	
			}
			});
		}
			
	
}


		

	

	



  function felder_adresse_zuruecksetzen_adresse(class_id,index)
 {
	if(class_id==0)
	{
		document.getElementsByClassName("adresse_input")[index].style.border="1px solid #e6e6e6" ;
		document.getElementsByClassName("address_input_header")[index*4].style.color="#4E4E4E";
	}
	else
	{
		document.getElementsByClassName("adresse")[index*4+class_id-1].style.border="1px solid #e6e6e6" ;
		document.getElementsByClassName("address_input_header")[index*4+class_id].style.color="#4E4E4E";		
	}
 }
 
 
 
   function felder_adresse_zuruecksetzen_adresse_other(class_id,index)
 {
	document.getElementsByClassName("adresse_other")[index*3+class_id].style.border="1px solid #e6e6e6" ;
	document.getElementsByClassName("address_other_input_header")[index*3+class_id].style.color="#4E4E4E";		
 }
 


   function felder_adresse_zuruecksetzen_adresse_mobilnummer(class_id,index)
 {
	document.getElementsByClassName("adresse_mobilnummer")[index+class_id].style.border="1px solid #e6e6e6" ;
	document.getElementsByClassName("address_mobilnummer_input_header")[index+class_id].style.color="#4E4E4E";		
 }
 
 


function check_whether_address_fields_were_filled_out()
{

	var status=0;
/*	max=0
	j=0;
	if(document.getElementsByClassName ("checkbox_abweichende_lieferadresse")[0].checked==true)
		max=1;
		
	document.getElementById("buttons_address_text").innerHTML="";
	while(j<=max)
	{

		if(document.getElementsByClassName("adresse_input")[j].value=="")
		{
			document.getElementById("buttons_address_text").innerHTML="Bitte alle benötigten Felder ausfüllen.";
			document.getElementsByClassName("adresse_input")[j].style.border="1px solid red";	
			document.getElementsByClassName("address_input_header")[j*4].style.color="red";		
			status=1;
		}	
		
	
		var i=0;
		while(i<=3)
		{
	
			if(document.getElementsByClassName("adresse")[parseInt(i+4*j)].value=="")
			{
				document.getElementById("buttons_address_text").innerHTML="Bitte alle benötigten Felder ausfüllen.";
				document.getElementsByClassName("adresse")[parseInt(i+4*j)].style.border="1px solid red";	
				document.getElementsByClassName("address_input_header")[parseInt(i+4*j+1)].style.color="red";		
				status=1;
			}	
	
			i=i+1;
		}
		
		var i=0;
		while(i<=2)
		{
	
			if(document.getElementsByClassName("adresse_other")[parseInt(i+3*j)].value=="")
			{
				document.getElementById("buttons_address_text").innerHTML="Bitte alle benötigten Felder ausfüllen.";
				document.getElementsByClassName("adresse_other")[parseInt(i+3*j)].style.border="1px solid red";	
				document.getElementsByClassName("address_other_input_header")[parseInt(i+3*j)].style.color="red";		
				status=1;
			}	
	
			i=i+1;
		}
		
	
		if(document.getElementsByClassName("adresse_mobilnummer")[j].value=="")
		{
			document.getElementsByClassName("adresse_mobilnummer")[j].style.border="1px solid red";	
			document.getElementsByClassName("address_mobilnummer_input_header")[j].style.color="red";	
			document.getElementById("buttons_address_text").innerHTML="Bitte alle benötigten Felder ausfüllen.";
			status=1;	
		}
	

	
		if(document.getElementsByClassName("address_unternehmensangaben_input_header")[j].style.display=="block" && document.getElementsByClassName("unternehmensdetails")[j].value=="")
		{
			document.getElementById("buttons_address_text").innerHTML="Bitte alle benötigten Felder ausfüllen.";
			document.getElementsByClassName("unternehmensdetails")[j].style.border="1px solid red";	
			document.getElementsByClassName("address_unternehmensangaben_input_header")[j].style.color="red";	
				status=1;
		}
		j=j+1;
	}*/

	return status;

}





function fuege_adressen_hinzu(hinzufuegen_,standard_rechnungsadresse_,standard_lieferadresse_,index_,wie_viele_adressen_checken,hinzufuegen_2,standard_rechnungsadresse_2,index_2)
{
		strasse=[]
		hausnummer=[]
		stadt=[]
		plz=[]
		land_neu=[]
		anrede=[]
		vorname=[]
		nachname=[]
		mobilnummer=[]
		unternehmensdetails=[]
		index=[]
		standard_lieferadresse=[]
		standard_rechnungsadresse=[]
		hinzufuegen=[]
		index=[]
		standard_lieferadresse[0]=standard_lieferadresse_;
		standard_lieferadresse[1]=standard_lieferadresse_;
		standard_rechnungsadresse[0]=standard_rechnungsadresse_;
		standard_rechnungsadresse[1]=standard_rechnungsadresse_2;

		hinzufuegen[0]=hinzufuegen_;
		hinzufuegen[1]=hinzufuegen_2;		

		index[0]=index_;
		index[1]=index_2;		
		
		i=0;
		while(i<=1)
		{	

			strasse[i]=document.getElementsByClassName('adresse_input')[i].value;
			hausnummer[i]=document.getElementsByClassName('adresse')[i*4].value
			stadt[i]=document.getElementsByClassName('adresse')[i*4+1].value;
			plz[i]=document.getElementsByClassName('adresse')[i*4+2].value;
			land_neu[i]=document.getElementsByClassName('adresse')[i*4+3].value;
			anrede[i]=document.getElementsByClassName('adresse_other')[i*3].value
			vorname[i]=document.getElementsByClassName('adresse_other')[i*3+1].value
			nachname[i]=document.getElementsByClassName('adresse_other')[i*3+2].value
			mobilnummer[i]=document.getElementsByClassName('adresse_mobilnummer')[i].value
			if(document.getElementsByClassName('address_unternehmensangaben_input_header')[i].style.display!="none")
				unternehmensdetails[i]=document.getElementsByClassName('unternehmensdetails')[i].value
			else
				unternehmensdetails[i]=""
			i=i+1
		}

		button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
		page_load(0);
		$.ajax({
			timeout:15000,
 			error: function(){		
 					button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
					page_load(1);
					button_logo("1","check_address_text","check_address_logo","check_address");},
			type: "POST",
			url: "/account_page/adresse_speichern/",
			dataType: "json",
			data: { "wie_viele_adressen_checken":wie_viele_adressen_checken,"vorname": vorname[0],"nachname": nachname[0],"telefonnummer": mobilnummer[0],
			"strasse": strasse[0],"unternehmensdetails": unternehmensdetails[0],
			"stadt": stadt[0],"plz": plz[0],"land":land_neu[0],"anrede":anrede[0],"hausnummer":hausnummer[0],"vorname_lieferadresse": vorname[1],"nachname_lieferadresse": nachname[1],"telefonnummer_lieferadresse": mobilnummer[1],
			"strasse_lieferadresse": strasse[1],"unternehmensdetails_lieferadresse": unternehmensdetails[1],
			"stadt_lieferadresse": stadt[1],"plz_lieferadresse": plz[1],"land_lieferadresse":land_neu[1],"anrede_lieferadresse":anrede[1],"hausnummer_lieferadresse":hausnummer[1],"standard_lieferadresse":standard_lieferadresse[1],"standard":standard_rechnungsadresse[0],"standard_2":standard_rechnungsadresse[1],"hinzufuegen":hinzufuegen[0],"hinzufuegen_lieferadresse":hinzufuegen[1],"indexnummer":index[0],"indexnummer_lieferadresse":index[1]},
			success: function(data) {
					button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
					button_logo("1","check_address_text","check_address_logo","check_address")
				page_load(1);
					feedback=JSON.parse(data)
	
					postion_data_entry_1=feedback[0].postion_data_entry_1
					postion_data_entry_2=feedback[0].postion_data_entry_2
					adressbuch=JSON.parse(feedback[0].adressbuch)


	
					rebates=JSON.parse(feedback[0].rebates)
					
					
					
					if(cart=="")
						window.top.location.href = "/"
						
					if(shopping_type=="VIP")
						load_VIP_topics()
					else
						load_pay_as_you_go_topics()
		
							
					
					if(wie_viele_adressen_checken==0)
					{
						new_index_rechnungsadresse=postion_data_entry_1;
						new_index_lieferadresse=postion_data_entry_1;
					}
					else
					{
						new_index_rechnungsadresse=postion_data_entry_1;
						new_index_lieferadresse=postion_data_entry_2;					
					}
					document.getElementsByClassName("adressbuch_daten")[0].innerHTML=feedback[0].adressbuch
					if(adressbuch[0].land!=land)
						select_shopping_type(shopping_type)
					land=adressbuch[0].land
					show_maps(new_index_rechnungsadresse,new_index_lieferadresse)
	
				
			}	
		})



}


function adressbuch_aktualisieren(wie_viele_adressen_checken,existent_rechnungsadresse,existent_lieferadresse)
{

		
	new_index_rechnungsadresse=-1;
	new_index_lieferadresse=-1;
	standard_rechnungsadresse="ja";
	standard_lieferadresse="ja"
	
	
	
	
	if(wie_viele_adressen_checken==0)
	{
		index=0
		if(existent_rechnungsadresse!="nein")
		{
			hinzufuegen=0;
			
			index=adressbuch[existent_rechnungsadresse].indexnummer
		}
		else
			hinzufuegen=1;		

		fuege_adressen_hinzu(hinzufuegen,standard_rechnungsadresse,standard_lieferadresse,index,wie_viele_adressen_checken,"","","")
	}
	


	if(wie_viele_adressen_checken==1)
	{
		index=0
		if(existent_rechnungsadresse!="nein")
		{
			hinzufuegen=0;
			index=adressbuch[existent_rechnungsadresse].indexnummer
		}
		else
			hinzufuegen=1;		



		standard_rechnungsadresse_2="nein"
		index_2=existent_lieferadresse
		if(existent_lieferadresse!="nein")
		{
			hinzufuegen_2=0;
			index_2=adressbuch[existent_lieferadresse].indexnummer;
		}
		else
			hinzufuegen_2=1;	
		fuege_adressen_hinzu(hinzufuegen,standard_rechnungsadresse,standard_lieferadresse,index,wie_viele_adressen_checken,hinzufuegen_2,standard_rechnungsadresse_2,index_2)

	}

		  		  			gtag('event', 'checkout',{
				  
				  'event_label':1,
				  'event_category': 'adress data provided'
				});


 		check_error_button() 


	
}


function check_zahlunsmethoden()
{

	feedback="ok";

	if(selected_zahlungsoption==4 && document.getElementById("agb_klarna_checkbox").checked==false)
	{
		feedback="not ok"
		alert_userdata("KLARNA AGB AKZEPTIEREN","Bitte akzeptiere noch die AGB von Klarna. Dann kann Deine Bestellung abgeschickt werden.")
	}
	else
		if(selected_zahlungsoption==0 || selected_zahlungsoption==3)
		{
			i=0;
			selected_credit_card=-1;
			zaehler=0;
			while (i<=zahlungsmethoden.length-1)
			{
				if(zahlungsoption==zahlungsmethoden[i].zahlungsoption)
				{
					if (document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[zaehler].innerHTML!="")
						selected_credit_card=document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[zaehler].id;
					zaehler=zaehler+1;
				}
				i=i+1;
			}
			if(selected_credit_card==-1)
				feedback="not ok"
		}
		else
			if(	zahlungsmethoden!="" || zahlungsoption==1 || zahlungsoption==2)
				feedback="ok";
			else
				if(zahlungsoption==4)
					if(document.getElementById("geburtsdatum_tag").selectedIndex>0 && document.getElementById("geburtsdatum_monat").selectedIndex>0 && document.getElementById("geburtsdatum_jahr").selectedIndex>0)
						feedback="ok";
					else
						feedback="not ok";
					
	return feedback
	
}



 function alert_userdata_empty_cart(content1,content2)
 {	 


	document.getElementById("alert_box_empty_cart_headline").innerHTML=content1;

	document.getElementById("alert_box_empty_cart_body").innerHTML=content2;
	$('#alert_box_empty_cart').modal('show');
	$('#login').modal('hide');




 }
 
  $('#alert_box_empty_cart').on('hide.bs.modal', function () {
  	
  	
  		$.ajax({
	timeout:15000,
 	error: function(){	},
	type: "GET",
	url: "/delete_empty_cart_message/",
	dataType: "json",
	data: { "":""},
	success: function(data)		{
		window.top.location.href = "https://www.darlinglace.com/Produktauswahl/BH%20Sets/" 
	}
	})

});
 
 

function check_empty_cart()
{
	if(document.getElementById("messageshownwarenkorbleer").innerHTML=="yes")
		alert_userdata_empty_cart("WARENKORB LEER","Dein Warenkorb ist leer. Du wirst nun zu unserer Produktübersicht weitergeleitet.")
	
	
}


function zurueck_button()
{
	if(document.getElementById("letzteshoppingsicht").innerHTML!="")
		if(document.getElementById("letztefilter").innerHTML!="")
			window.location= document.getElementById("letzteshoppingsicht").innerHTML+"?clientfilter=yes"
		else
			window.location= document.getElementById("letzteshoppingsicht").innerHTML
	else
		window.location= "https://www.darlinglace.com/Produktauswahl/BH%20Sets"
	
	
}

function get_selected_credit_card()
{
	i=0;
	selected_credit_card=-1;
	zaehler=0;
	while (i<=zahlungsmethoden.length-1)
	{
		if(zahlungsoption==zahlungsmethoden[i].zahlungsoption)
		{
			if (document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[zaehler].innerHTML!="")
				selected_credit_card=document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[zaehler].id;
			zaehler=zaehler+1;
		}
		i=i+1;
	}
	
	return selected_credit_card
}

function bestellen()
{	


	if(document.getElementById("gutschein_input").value!="" && document.getElementById("gutschein_button_id_text").innerHTML=="Überprüfen" && document.getElementsByClassName("promo_code")[0].innerHTML!="<b>+</b> Gutschein-Code hinzufügen")
		alert_userdata("GUTSCHEIN ÜBERPRÜFEN","Lass den eingegebenen Gutschein-Code überprüfen indem Du auf den Button Überprüfen klickst.")
	else
	{
	
		if(check_zahlunsmethoden()=="ok")
		{
	
			if(selected_zahlungsoption==0 || selected_zahlungsoption==3)
				selected_credit_card=get_selected_credit_card();
			else
				selected_credit_card=0;
				
			if(document.getElementsByClassName("button_check")[0].style.display=="none")
			{
	
				rabatt=(rabatt-credit_);
		
				if (document.getElementById("gutschein_input").value.toUpperCase()=="")
					rabattcode="";
				else
					rabattcode=document.getElementById("gutschein_input").value.toUpperCase()
	
				warenkorb_gerichte=cart[0].style;
				warenkorb_anzahl=cart[0].anzahl;
				warenkorb_groesse=cart[0].bhgroesse;
		
				
		
				i=1;
				while (i<=cart.length-1)
				{
					warenkorb_gerichte=warenkorb_gerichte+","+cart[i].style;
					warenkorb_anzahl=warenkorb_anzahl+","+cart[i].anzahl;
					warenkorb_groesse=warenkorb_groesse+","+cart[i].bhgroesse;
		
					i=i+1;
				}
				existent_rechnungsadresse=document.getElementById("existent_rechnungsadresse").value
				existent_lieferadresse=document.getElementById("existent_lieferadresse").value
		
				strasse_rechnung=adressbuch[existent_rechnungsadresse].strasse;
				hausnummer_rechnung=adressbuch[existent_rechnungsadresse].hausnummer;
				stadt_rechnung=adressbuch[existent_rechnungsadresse].stadt;
				plz_rechnung=adressbuch[existent_rechnungsadresse].plz;
				land_rechnung=adressbuch[existent_rechnungsadresse].land;
				anrede_rechnung=adressbuch[existent_rechnungsadresse].anrede;
				vorname_rechnung=adressbuch[existent_rechnungsadresse].vorname;
				nachname_rechnung=adressbuch[existent_rechnungsadresse].nachname;
				telefonnummer_rechnung=adressbuch[existent_rechnungsadresse].telefonnummer;
				unternehmensdetails_rechnung=adressbuch[existent_rechnungsadresse].unternehmensdetails;	
				
		
				strasse_lieferadresse=adressbuch[existent_lieferadresse].strasse;
				hausnummer_lieferadresse=adressbuch[existent_lieferadresse].hausnummer;
				stadt_lieferadresse=adressbuch[existent_lieferadresse].stadt;
				plz_lieferadresse=adressbuch[existent_lieferadresse].plz;
				land_lieferadresse=adressbuch[existent_lieferadresse].land;
				anrede_lieferadresse=adressbuch[existent_lieferadresse].anrede;
				vorname_lieferadresse=adressbuch[existent_lieferadresse].vorname;
				nachname_lieferadresse=adressbuch[existent_lieferadresse].nachname;
				telefonnummer_lieferadresse=adressbuch[existent_lieferadresse].telefonnummer;
				unternehmensdetails_lieferadresse=adressbuch[existent_lieferadresse].unternehmensdetails;	
				
				if(selected_zahlungsoption==4)
				{
					geburtsdatum_tag=document.getElementById("geburtsdatum_tag").value;
					geburtsdatum_monat=document.getElementById("geburtsdatum_monat").value;
					geburtsdatum_jahr=document.getElementById("geburtsdatum_jahr").value;
					
				}
				else
				{
					geburtsdatum_tag="";
					geburtsdatum_monat="";
					geburtsdatum_jahr="";					
				}
				page_load(0);
				button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
			
					  		  			gtag('event', 'checkout',{
				  
				  'event_label':1,
				  'event_category': 'order button clicked'
				});
			

				$.ajax({
				timeout:20000,
					error: function(){
								page_load(1);
								button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	},
				type: "POST",
						tryCount : 0,
  				  	retryLimit : 3,
				url: "/bestellen_pre_test/",
				dataType: "json",
				data: { 'geburtsdatum_tag':geburtsdatum_tag,'geburtsdatum_monat':geburtsdatum_monat,'geburtsdatum_jahr':geburtsdatum_jahr,'warenkorb_groesse':warenkorb_groesse,'warenkorb_gerichte':warenkorb_gerichte,'warenkorb_anzahl':warenkorb_anzahl,'zahlungsoption':zahlungsoption,'selected_zahlungsoption':selected_zahlungsoption,'preis':rebates[0].bestellung,'lieferkosten':rebates[0].lieferkosten,'rabatt':rebates[0].coupon, 'rabattcode':rebates[0].couponcode,'shopping_type':shopping_type,'braforfreecount':rebates[0].braforfreecount,'braforfreevalue':rebates[0].braforfreevalue,'storecredit_to_be_used':rebates[0].storecredit,'selected_credit_card':selected_credit_card,'strasse_rechnung':strasse_rechnung,'hausnummer_rechnung':hausnummer_rechnung,'stadt_rechnung':stadt_rechnung,'plz_rechnung':plz_rechnung,'land_rechnung':land_rechnung,'anrede_rechnung':anrede_rechnung,'vorname_rechnung':vorname_rechnung,'nachname_rechnung':nachname_rechnung,'telefonnummer_rechnung':telefonnummer_rechnung,'strasse_lieferadresse':strasse_lieferadresse,'hausnummer_lieferadresse':hausnummer_lieferadresse,'stadt_lieferadresse':stadt_lieferadresse,'plz_lieferadresse':plz_lieferadresse,'land_lieferadresse':land_lieferadresse,'anrede_lieferadresse':anrede_lieferadresse,'vorname_lieferadresse':vorname_lieferadresse,'nachname_lieferadresse':nachname_lieferadresse,'telefonnummer_lieferadresse':telefonnummer_lieferadresse,'unternehmensdetails_lieferadresse':unternehmensdetails_lieferadresse,'unternehmensdetails_rechnung':unternehmensdetails_rechnung },
				success: function(data) {		
								if (data=="not enough quantities")
								{
									page_load(1);
									button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
									alert_userdata_reload("SETS AUSVERKAUFT","Da war ein anderer Kunde schneller. Einige Artikel Deiner Bestellung sind leider nicht mehr verfügbar. Dein Warenkorb wird jetzt aktualisiert und nicht mehr verfügbare Artikel werden entfernt. Es wird noch keine Bestellung durchgeführt.")
								}
								else						
									if (data=="already ordered")
									{
										document.getElementById("messageshownwarenkorbleer").innerHTML=="yes"
										check_empty_cart()
									}
									else
										if (data=="not ok")
										{
											page_load(1);
											button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
											alert_userdata_reload("AKTUALISIERTER WARENKORB","Dein Warenkorb wurde aktualisiert. Diese Seite wird neu geladen.")
										}
										else
											if (data=="kann nicht geworben werden")
											{
												page_load(1);
												button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
												alert_userdata_reload("FREUNDE WERBEN FREUNDE NICHT EINSETZBAR","Deine eingebenen Daten wurden schon bei einem anderen User verwendet. Daher kann der Gutschein aus dem Programm Freunde werben Freunde nicht eingesetzt werden. Diese Seite wird neu geladen. Danach kannst Du den Warenkorb bestellen.")
											}
											else
												if (data=="not enough storecredit")
												{
													page_load(1);
													button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
													alert_userdata_reload("NICHT GENUG VIP GUTHABEN","Du hast nicht mehr ausreichend VIP Guthaben. Diese Seite wird neu geladen.")
												}
												else
													if (data=="not enough bra for free")
													{
														page_load(1);
														button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
														alert_userdata_reload("NICHT GENUG KOSTENLOSE SETS","Du hast nicht mehr ausreichend kostenlose VIP Sets. Diese Seite wird neu geladen.")
													}
													else
														if (data!="not ok")
														{
															if(selected_zahlungsoption==4)
																if(data!="false")
																	window.top.location.href = "/account_page/bestellungen_ansehen/"+data
																else
																{
																	page_load(1);
																	button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
																	alert_userdata_reload("Das hat leider nicht geklappt","Leider können wir Dir über Klarna keine Zahlung auf Rechnung anbieten. Aber wir haben eine ganze Reihe anderer Zahlungsmethoden für Dich zur Verfügung. Wähle einfach eine andere Zahlungsmethode aus.")
																}
															if(selected_zahlungsoption==0 || selected_zahlungsoption==3)
																if(data!="false")
																	window.top.location.href = "https://www.darlinglace.com/account_page/bestellungen_ansehen/"+data
																	
																													
															if(selected_zahlungsoption==1)
															{
																if(data.length!=8)
																{	
																	document.getElementsByClassName("paypal-checksum")[0].value=data
																	paymill.createTransaction({
																	  checksum: $('.paypal-checksum').val()
																	}, function(error) {
																	  if (error) {
			
																		// Payment setup failed, handle error and try again.
																		console.log(error);
																	  }
																	});
																}
																else
																	window.top.location.href = "/account_page/bestellungen_ansehen/"+data	
		
															}
		
															if(selected_zahlungsoption==2)
															{
		
																if(data.length!=8)
																{
		
																	sofortueberweisung=data
			
																	block="";
																	block="<form action='https://www.sofort.com/payment/start' method='post'>"
																	block=block+"<div  id='add_to_cart' name='submit' class='button_cart_large' value='Bestellen' onclick='bestellen()'><div class='button_text'>Bestellen</div><div class='button_logo'></div></div>"
																	i=0;
			
																	while(i<=sofortueberweisung.length-1)
																	{
																		block=block+"<input type='hidden' name='"+sofortueberweisung[i].name+"' value='"+sofortueberweisung[i].value+"'>";
																		i=i+1;
																	}
			
																	block=block+"</form>"
			
																	document.getElementsByClassName("order_form")[0].innerHTML=block
																	document.forms[0].submit()
																}
																else
																	window.top.location.href = "/account_page/bestellungen_ansehen/"+data
															}					
													}
										}
									});
	
			}
			else
				document.getElementById("bestellen_ueberpruefen").style.display="block";
		}	
		else
			if(selected_zahlungsoption!=4)
				document.getElementById("bestellen_ueberpruefen").style.display="block";
			else
				if(document.getElementById("geburtsdatum_tag").selectedIndex==0 || document.getElementById("geburtsdatum_monat").selectedIndex==0 || document.getElementById("geburtsdatum_jahr").selectedIndex ==0)

					alert_userdata("GEBURTSDATUM ANGEBEN","Um den Kauf über Rechnung abschließen zu können, benötigen wir noch Dein Geburtsdatum.")

	}
}










function warenkorb_aktualisieren_schliessen()
{
page_load(0);
	location.reload();
}




function preis_aufrufen(subscription)
{
	var i=0;
	var preis=0;
	while(i<=cart.length-1)
	{
		if(subscription=="yes")
			preis=preis+(cart[i].pricesubscription)*cart[i].anzahl
		else
			preis=preis+(cart[i].priceregular)*cart[i].anzahl

		
		i=i+1;
	}
	return preis;
}

function bra_for_free_rebate_aufrufen(subscription)
{
	var i=0;
	var preis=0;
	zaehler=0;
	while(i<=cart.length-1)
	{
		if(subscription=="yes")
			preis=preis+(cart[i].pricesubscription)*Math.min(parseInt(cart[i].anzahl),bra_for_free-zaehler)
		else
			preis=preis+(cart[i].priceregular)*Math.min(parseInt(cart[i].anzahl),bra_for_free-zaehler)
		zaehler=zaehler+Math.min(parseInt(cart[i].anzahl),bra_for_free-zaehler)
		
		i=i+1;
	}
	braforfreecount=zaehler;
	braforfreevalue=preis;
	
	return preis;
}



function replace_dot_comma(zahl)
{
	var zahl_=	zahl.toFixed(2);
	zahl_ = zahl_.toString();
	return zahl_.replace(".", ",");
}

function replace_comma_dot(zahl)
{
	
	var zahl_=	zahl.toFixed(2);
	zahl_ = zahl_.toString();
	return zahl_.replace(",", ".");
}

function select_shopping_type(shopping_type_)
{
	button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
	page_load(0);		
	if(shopping_type_==0)
		shopping_type="VIP"
	else
		shopping_type="Regular"
	
	$.ajax({
	timeout:15000,
 	error: function(){	
 		button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
		page_load(1);	},
	type: "GET",
	url: "/select_shopping_type/",
	dataType: "json",
	data: { "shopping_type":  shopping_type,"land":land},
	success: function(data)		{
	feedback=JSON.parse(data)
	
	data=feedback[0].warenkorb_and_rebates
			
				page_load(1);
				button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
				 check_error_message_gutscheincodes(feedback[0].error,data)
				 	
								
					
		}
	})
}


function check_error_message_gutscheincodes(error,data)
{
					feedback="ok"
				if(error=="error")
				{
					feedback="not ok"

					alert_userdata("GUTSCHEIN NICHT ERKANNT","Der Gutscheincode wurde nicht erkannt. Entweder Du hast Du Dich vertippt oder der Gutschein ist nicht mehr gültig.")
				}
				if(error=="nur Non-VIP")
				{
					feedback="not ok"

					alert_userdata("GUTSCHEIN GILT NUR FÜR NICHT VIP-MITGLIEDER","Dieser Gutschein-Code gilt nur für nicht VIP-Mitglieder.")
				}
				
				if(error=="VIP")
				{
					feedback="not ok"

					alert_userdata("GUTSCHEIN GILT NUR FÜR VIP-MITGLIEDER","Dieser Gutschein-Code gilt nur für VIP-Mitglieder. Wenn Du zum VIP Club wechselst, kannst Du den Gutschein einlösen.")
				}				
				
				if(error=="nur Neukunde")
				{
					feedback="not ok"

					alert_userdata("GUTSCHEIN GILT NUR FÜR NEUKUNDEN","Dieser Gutschein-Code gilt nur für Neukunden.")
				}		


				if(error=="nur Kunde")
				{
					feedback="not ok"

					alert_userdata("GUTSCHEIN GILT NUR FÜR KUNDEN","Für Deinen nächsten Kauf kannst Du diesen Gutschein einsetzen.")
				}		
				
				if(feedback=="ok")
				{
					
					update_cart(data)	
						

					
				}
				else
				{
					gutscheincode="";

					update_cart(data)	
					rabatt=rebates[0].coupon;					
		
				}
	
}

function show_select_VIP_box(){
	box=""
	box=box+"<div style='width:100%;line-height:15px;float:left;margin-bottom:20px;'>"
	box=box+"<br><img style='float:left' src='/static/discount_icon.png' width='28' /><div style='margin-top:0px;margin-left:30px;'>Exkulsive <b>VIP Angebote </b></div>"
	box=box+"<br><img style='float:left' src='/static/gift.png' width='25' /><div style='margin-top:0px;margin-left:30px;'><b>Jedes sechste BH Set geschenkt</b></div>"
	box=box+"<br><img style='float:left' src='/static/shopping_bag.png' width='25'/><div style='margin-top:0px;margin-left:30px;'>Monatlich die <b>neusten Sets</b> shoppen oder ganz einfach pausieren</div>"
	box=box+"<br><img style='float:left' src='/static/Risk_free.png' width='25'/><div style='margin-top:0px;margin-left:30px;'><b>Ohne Risiko</b> ausprobieren &ndash; Du kannst jederzeit VIP beenden</div>"

 

	box=box+"</div>"

	document.getElementsByClassName("VIP_selection")[0].innerHTML =box;
	document.getElementsByClassName("shopping_selection")[0].style.backgroundColor ="#b51d36";
	document.getElementsByClassName("shopping_selection")[0].style.color ="#ffffff";
	document.getElementById("VIP_selection_image").src='/static/radio_box_check_black.png'

	
	
	document.getElementsByClassName("shopping_selection")[1].style.backgroundColor ="#ffffff";
	document.getElementsByClassName("shopping_selection")[1].style.color ="#4E4E4E";	
	document.getElementById("Reg_selection_image").src='/static/radio_box_empty_black.png'
	
}


function show_select_pay_as_you_go_box(){
	box=""
	box=box+"<div style='width:100%;line-height:15px;float:left;margin-bottom:20px;'>"
	box=box+"<br><img style='float:left' src='/static/shopping_bag_no.png' width='28' /><div style='margin-top:0px;margin-left:30px;'><b>Volle Flexibilität</b>: Kaufe ein, wann Du willst</div>"
	box=box+"<br><img style='float:left' src='/static/free_shipping.png' width='28' /><div style='margin-top:0px;margin-left:30px;'><b>Kostenloser Versand und Rückversand in Deutschland</b></div>"
	
	box=box+"</div>"
	
	document.getElementsByClassName("VIP_selection")[0].innerHTML =box;
	document.getElementsByClassName("shopping_selection")[1].style.backgroundColor ="#b51d36";
	document.getElementsByClassName("shopping_selection")[1].style.color ="#ffffff";
	document.getElementsByClassName("shopping_selection")[0].style.backgroundColor ="#ffffff";
	document.getElementsByClassName("shopping_selection")[0].style.color ="#4E4E4E";	
	
	
		document.getElementById("VIP_selection_image").src='/static/radio_box_empty_black.png'
	document.getElementById("Reg_selection_image").src='/static/radio_box_check_black.png'

}

function select_only_repeat_payment_methods()
{
	document.getElementsByClassName("zahlungs_cover")[1].style.backgroundColor="#ffffff";
	document.getElementsByClassName("zahlungs_cover")[1].style.opacity="0.5";
	document.getElementsByClassName("zahlungs_cover")[1].style.pointerEvents="none";
	
	document.getElementsByClassName("zahlungs_cover")[2].style.backgroundColor="#ffffff";
	document.getElementsByClassName("zahlungs_cover")[2].style.opacity="0.5";
	document.getElementsByClassName("zahlungs_cover")[2].style.pointerEvents="none";	
}


function select_all_payment_methods()
{
	document.getElementsByClassName("zahlungs_cover")[1].style.backgroundColor="";
	document.getElementsByClassName("zahlungs_cover")[1].style.opacity="1.0";
	document.getElementsByClassName("zahlungs_cover")[1].style.pointerEvents="auto";
	
	document.getElementsByClassName("zahlungs_cover")[2].style.backgroundColor="";
	document.getElementsByClassName("zahlungs_cover")[2].style.opacity="1.0";
	document.getElementsByClassName("zahlungs_cover")[2].style.pointerEvents="auto";	
}


function preise_laden(subscription)
{
	
	
	i=0;
	preis=0;

	while(i<=cart.length-1)
	{

		if(subscription=="yes")
		{

			if(cart[i].productgroup!="geschenkkarten")
				
				if(cart[i].rabatt!="")
				{
					block="<b><p style='text-decoration: line-through'>VIP €"+replace_dot_comma((cart[i].pricesubscription)*cart[i].anzahl)+"</b></p><br>";
					block =block+"<b><p style='color:#b51d36'> €"+replace_dot_comma((cart[i].pricesubscription+cart[i].rabatt)*cart[i].anzahl)+"</p></b>";
					document.getElementsByClassName("product_price")[i].innerHTML =block	
					
				}
				else
				{
					block="<b>VIP €"+replace_dot_comma((cart[i].pricesubscription)*cart[i].anzahl)+"</b>";
					document.getElementsByClassName("product_price")[i].innerHTML =block					
				}	
			else
				document.getElementsByClassName("product_price")[i].innerHTML ="<b> €"+replace_dot_comma((cart[i].pricesubscription)*cart[i].anzahl)+"</b>"			
			preis=preis+cart[i].pricesubscription*cart[i].anzahl;

		}
		else
		{
			if(cart[i].productgroup!="geschenkkarten")
			{

				if(cart[i].rabatt!="")
				{
					block="<b><p style='text-decoration: line-through'>Regulär €"+replace_dot_comma((cart[i].priceregular)*cart[i].anzahl)+"</p></b>";
					block =block+"<b><p style='color:#b51d36'>  €"+replace_dot_comma((cart[i].priceregular+cart[i].rabatt)*cart[i].anzahl)+"</p></b>";
					document.getElementsByClassName("product_price")[i].innerHTML =block	
					
				}
				else
				{
					block="<b>Regulär €"+replace_dot_comma((cart[i].priceregular)*cart[i].anzahl)+"</b>";	
					document.getElementsByClassName("product_price")[i].innerHTML =block					
				}			
			}
			else
				document.getElementsByClassName("product_price")[i].innerHTML ="<b> €"+replace_dot_comma((cart[i].priceregular)*cart[i].anzahl)+"</b>";
				
				


			preis=preis+cart[i].priceregular*cart[i].anzahl;

			
		}


		
		i=i+1;
	}
	

	
}



	function VIP_selection_laden(VIP_,shoppingtype,cart_page_)
{
		cart_page=cart_page_
	VIP=VIP_

		if(VIP=="false" && cart_page=="ja")
		{

				box="<br>"
				box=box+"<div class='shopping_selection' onclick='select_shopping_type(0)'><div style='margin-left:5px;margin-top:2px;margin-bottom:2px;' ><img src='/static/radio_box_check_black.png' width='25' style='float:left;padding-top:5px;margin-right:5px;' id='VIP_selection_image'></img><div style='float:left;width:105px;font-size:14px;'><b>VIP Club</b><br>Ab 24,95 € je Set</div></div></div><div class='shopping_selection' onclick='select_shopping_type(1)'><div style='margin-left:5px;margin-top:2px;margin-bottom:2px;' ><img src='/static/radio_box_empty_black.png' width='25' style='float:left;padding-top:5px;margin-right:5px;' id='Reg_selection_image'></img><div style='float:left;width:105px;font-size:14px;'><b>Als Gast kaufen</b><br>Ab 24,95 € je Set</div></div></div><div class='VIP_selection'></div>"
				
				if(window.innerWidth>=768)	
				{
					document.getElementsByClassName("VIP")[1].innerHTML =box;
					document.getElementsByClassName("VIP")[0].style.display="none";
				}
				else
				{
					document.getElementsByClassName("VIP")[1].innerHTML =box;
					document.getElementsByClassName("VIP")[0].style.display="none";
				}		


				if(shoppingtype=="VIP")
					load_VIP_topics()
				else
					load_pay_as_you_go_topics()

					
												
		}
		else
		{

				if(shoppingtype=="VIP")
					load_VIP_topics()
				else
					load_pay_as_you_go_topics()

				document.getElementsByClassName("VIP")[1].style.display="none";
				document.getElementsByClassName("headline")[0].style.display="block";
				document.getElementsByClassName("VIP")[0].style.display="none";

				document.getElementById("VIP_block").style.display ="none";
		}


}


function load_VIP_topics()
{
	bestelluebersicht("yes")
	lingerie_anzeigen("yes");
	shopping_type="VIP"
	if(VIP=="false" && cart_page=="ja")
	{
		show_VIP_AGB("block")
		show_select_VIP_box()	
	}

}


function load_pay_as_you_go_topics()
{
	bestelluebersicht("no")
	lingerie_anzeigen("no");
	shopping_type="Regular"
	if(VIP=="false" && cart_page=="ja")
	{
		show_VIP_AGB("none")
		show_select_pay_as_you_go_box()	
	}
	else
		document.getElementsByClassName("zahlungs_cover")[4].style.display="block";
}



function bestelluebersicht(subscription)
{

	var maxim= document.getElementsByClassName("bestellung");

	var uebersicht="<div style='float:left;'>Bestellung:</div><div style='float:right;'>"+replace_dot_comma(rebates[0].bestellung)+" EUR</div><br>";
	if(rebates[0].lieferkosten!="0")
		uebersicht=uebersicht+"<div style='float:left;'>Lieferkosten:</div><div style='float:right;'>"+replace_dot_comma(rebates[0].lieferkosten)+" EUR</div><br>";
	else
		uebersicht=uebersicht+"<div style='float:left;'>Lieferkosten:</div><div style='float:right;'>KOSTENLOS</div><br>";
		

	if(parseFloat(rebates[0].coupon)!=0)
	{

		uebersicht=uebersicht+"<div class='rabattname' style='float:left;'>"+rebates[0].rabattname+":</div><div class='rabattname' style='float:right;'>"+replace_dot_comma(-rebates[0].coupon)+" EUR</div><br>";	

	}


	if(parseFloat(rebates[0].braforfreevalue)!=0)
	{

		uebersicht=uebersicht+"<div style='float:left;'>Sets umsonst (VIP):</div><div style='float:right;'>"+replace_dot_comma(parseFloat(-rebates[0].braforfreevalue))+" EUR</div><br>";	

	}	
	if(parseFloat(rebates[0].storecredit)!=0)
	{
		
		uebersicht=uebersicht+"<div style='float:left;'>VIP Guthaben:</div><div style='float:right;'>"+replace_dot_comma(parseFloat(-rebates[0].storecredit))+" EUR</div><br>";	
		
	}
	
	if(parseFloat(rebates[0].credit)!=0)
	{
		
		uebersicht=uebersicht+"<div style='float:left;width:30px;line-height:25px;'>Freundschafts-\nwerbung:</div><div style='float:right;line-height:25px;'><br>"+replace_dot_comma(parseFloat(-rebates[0].credit))+" EUR</div><br><br>";	
		
	}

	uebersicht=uebersicht+"<div style='border-bottom:1px solid #e6e6e6 ;'></div>";
	

	
	uebersicht=uebersicht+"<div style='float:left;font-weight: bold;'>Gesamt:</div><div style='float:right;font-weight: bold;'>"+replace_dot_comma(parseFloat(rebates[0].gesamtpreis))+" EUR</div><br>";
	


	if(gutscheincode=="")
	{
		
		var promo="<div class='promo_code' onclick='promo_code()'><b>+</b> Gutschein-Code hinzufügen</div>";
		uebersicht=uebersicht+promo;
		maxim[0].innerHTML=uebersicht;
		document.getElementById("gutschein_input").style.display ="none";
		document.getElementById("gutschein_button_id").style.display ="none";
		
	}
	else
	{

		var promo="<div class='promo_code' onclick='promo_code()'><b>-</b> Gutschein-Code entfernen</div>";	
		uebersicht=uebersicht+promo;
		maxim[0].innerHTML=uebersicht;
		document.getElementById("gutschein_button_id_text").innerHTML="Entfernen";
		document.getElementById("gutschein_input").disabled=true;

		document.getElementById("gutschein_input").value  =gutscheincode;

		document.getElementById("gutschein_button_id").style.backgroundColor="#808080";

		
	}


	
	
}



function gutscheinfeld_freigeben()
{
		document.getElementsByClassName("promo_code")[0].innerHTML="<b>+</b> Gutschein-Code hinzufügen";
		document.getElementById("gutschein_button_id_text").innerHTML="Überprüfen";
		document.getElementById("gutschein_input").disabled=false;
		document.getElementById("gutschein_input").value  ="";
		document.getElementById("gutschein_button_id").style.backgroundColor="#b51d36";
				document.getElementById("gutschein_button_id").style.display ="none";
				document.getElementById("gutschein_input").style.display ="none";
}



function gutscheinfeld_sperren()
{
		document.getElementsByClassName("promo_code")[0].innerHTML="<b>-</b> Gutschein-Code entfernen";
		document.getElementById("gutschein_button_id_text").innerHTML="Entfernen";
		document.getElementById("gutschein_input").disabled=true;
		document.getElementById("gutschein_button_id").style.backgroundColor="#808080";
				document.getElementById("gutschein_button_id").style.display ="block";
				document.getElementById("gutschein_input").style.display ="block";
				
				document.getElementById("gutschein_input").value  =rebates[0].couponcode
}






function gutschein_einloesen()
{
			if(document.getElementById("gutschein_button_id_text").innerHTML!="Entfernen")
		{
			
			button_logo("0","gutschein_button_id_text","gutschein_button_id_logo","gutschein_button_id")
			button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	


			$.ajax({
			timeout:15000,
 			error: function(){			
 				button_logo("1","gutschein_button_id_text","gutschein_button_id_logo","gutschein_button_id")
				button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	},
			type: "GET",
			url: "/gutschein_einloesen/",
			dataType: "json",
			data: { "gutscheincode":  document.getElementById("gutschein_input").value.toUpperCase(),"art":"einloesen","land":land },
			success: function(data) {
					button_logo("1","gutschein_button_id_text","gutschein_button_id_logo","gutschein_button_id")
					button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")
					feedback=JSON.parse(data)
					data=feedback[0].warenkorb_and_rebates
				 check_error_message_gutscheincodes(feedback[0].error,data)


							
				}
			})

		}
		else
			gutschein_code_reset();
}


function update_cart(data)
{
	feedback=JSON.parse(data)
	
	cart=JSON.parse(feedback[0].warenkorb)
	document.getElementsByClassName("warenkorb_daten")[0].innerHTML=feedback[0].warenkorb;
	
	rebates=JSON.parse(feedback[0].rebates)
	
	
	
	
	if(cart=="")
	{
		document.getElementById("messageshownwarenkorbleer").innerHTML="yes"
		check_empty_cart()
	}
	if(shopping_type=="VIP")
		load_VIP_topics()
	else
		load_pay_as_you_go_topics()
	insert_cart_content_in_header();	
	if(rebates[0].rabattname!="")
		gutscheinfeld_sperren()
	else
		gutscheinfeld_freigeben()

}

function gutschein_code_reset()
{
	if(document.getElementById("gutschein_input").value!="")
	{
		button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
		page_load(0);	
	
		$.ajax({
				timeout:15000,
	 			error: function(){	
	 						button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
							page_load(1);	},
				type: "GET",
				url: "/gutschein_einloesen/",
				dataType: "json",
				data: { "gutscheincode":  document.getElementById("gutschein_input").value.toUpperCase(),"art":"aufloesen" },
				success: function(data) {



					feedback=JSON.parse(data)
					data=feedback[0].warenkorb_and_rebates
					
						
					gutscheinfeld_freigeben()
					
		
					gutscheincode="";
					rabatt=rebates[0].coupon;	

					update_cart(data)
		
					button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")
					page_load(1);	
				}
			})
	}

}





 function gutscheincode_schliessen() {

	document.getElementsByClassName ("overlay")[0].style.visibility = "hidden"
	document.getElementById("x-mask").style.opacity="1.0";
	enableScroll();
}



function promo_code()
{



	if (rebates[0].rabattname!="")
	{

		document.getElementById("gutschein_input").style.display ="none";

		document.getElementsByClassName("promo_code")[0].innerHTML="<b>+</b> Gutschein-Code hinzufügen";

		document.getElementById("gutschein_button_id").style.display ="none";
		gutschein_code_reset();
		
		
		

		
	}
	else
	{
		
		if(document.getElementById("gutschein_input").style.display=="none")
		{
				document.getElementById("gutschein_input").value=""
				document.getElementById("gutschein_input").style.display ="block";
				document.getElementsByClassName("promo_code")[0].innerHTML="<b>-</b> Gutschein-Code entfernen";
				document.getElementById("gutschein_button_id").style.display ="block";
		}
		else
		{
			
			document.getElementById("gutschein_input").style.display ="none";

			document.getElementsByClassName("promo_code")[0].innerHTML="<b>+</b> Gutschein-Code hinzufügen";
		
			document.getElementById("gutschein_button_id").style.display ="none";
		}
		
		
	}
	
	
}


function check_error_button()
{
		if(document.getElementById("bestellen_ueberpruefen").style.display=="block")
			if(check_zahlunsmethoden()=="ok")
				if(document.getElementsByClassName("button_check")[0].style.display=="none")
					document.getElementById("bestellen_ueberpruefen").style.display="none"
}


function unternehmen_check(id)
{

	if (document.getElementsByClassName("address_unternehmensangaben_input_header")[id].style.display =="block")
		document.getElementsByClassName("address_unternehmensangaben_input_header")[id].style.display ="none";
	else
		document.getElementsByClassName("address_unternehmensangaben_input_header")[id].style.display ="block";
}


function als_gast_pop_up()
{
			 $('#als_gast_oder_anmelden').modal('hide');
			$('#als_gast_anmelden').modal({backdrop: 'static', keyboard: false})  
	
}


function amelde_pop_up()
{
			 $('#als_gast_oder_anmelden').modal('hide');
			$('#login').modal({backdrop: 'static', keyboard: false})  
	
}
 



function email_check(email)
{

	if (email=="not ok")
	
			$('#als_gast_oder_anmelden').modal({backdrop: 'static', keyboard: false})  

}


  $('#login').on('shown.bs.modal', function () {
			$('#alert_box_reload').modal('hidden');
					gtag('event', 'set_checkout_option', {
		  "checkout_step": 1,
		  "checkout_option": "registration done",
		  "value": gutscheincode
				});
 

});




  function alert_userdata_reload(content1,content2)
 {	 
	
	document.getElementById("alert_box_reload_headline").innerHTML=content1;
	document.getElementById("alert_box_reload_body").innerHTML=content2;
		$('#alert_box_reload').modal('show');

 }
 
 
 
$("#close_register").on("click", function() {

page_load(0);
		window.location= "https://www.darlinglace.com/cart/"

   })
 
  $('#alert_box_reload').on('hide.bs.modal', function () {

location.reload();

});



 
$("#close_als_anmeldung").on("click", function() {
			 $('#login').modal('hide');
			$('#als_gast_oder_anmelden').modal({backdrop: 'static', keyboard: false})  

   })



$("#close_als_gast").on("click", function() {
			 $('#als_gast_anmelden').modal('hide');
			$('#als_gast_oder_anmelden').modal({backdrop: 'static', keyboard: false})  

   })
 
 
 

 
 
 

 
 
 function check_vollstaendigkeit_email()
 {

	 if(document.getElementsByClassName("email_eingabe")[0].value=="")
		  document.getElementById("email_fehler").innerHTML="Bitte E-Mail Adresse angeben";
	  else
		  return true		 
	 
 }
 
 
 
 function register_email()
 { 	
	 if (check_vollstaendigkeit_email())
			 $.ajax({
			 	timeout:15000,
 				error: function(){},
				type: "POST",
				url: "/updater_user_registration/",
				dataType: "json",
				data: { "item": document.getElementsByClassName("email_eingabe")[0].value },
				success: function(data) {

					if(data=="exists already")
						document.getElementById("email_fehler").innerHTML="User existiert bereits";
					else	
						if(data=="email falsch")
							document.getElementById("email_fehler").innerHTML="Bitte eine gültige E-Mail Adresse angeben";
						else
						{
							 $('#login').modal('hide');
							 warenkorb_abrufen(gesamtzahl_gerichte)

						}
				},	error: function(data)
				{
					
				}
			}); 
			

 }
 



 /*   if(document.getElementsByClassName("cart_page")[0].innerHTML!="ja")
    {
    	zahlung_click(document.getElementsByClassName("selected_zahlungsoption")[0].innerHTML);
    }*/


function select_zahlungsoption()
{
	zahlungsmethoden="";
	selected_zahlungsoption="";
	if(document.getElementsByClassName("selected_zahlungsoption")[0].innerHTML!="")
		zahlung_click(document.getElementsByClassName("selected_zahlungsoption")[0].innerHTML);
	
}






function reset_input_fields_mobile()
{
	if(window.innerWidth<=767)
	{

		if(adressbuch.length-1==-1)
		{
			document.getElementsByClassName("sidebar_checkout")[0].style.display ="none";	
			document.getElementsByClassName("headline")[2].style.display ="none";
			document.getElementsByClassName("zahlungs_container")[0].style.display ="none";
	 	document.getElementById("kreditkarten").style.display="none";
	
	
	 	}
	 }



				
	
	
}


 
 function others_laden(_gutscheincode)
 { 
	document.getElementsByClassName("mobile_menu")[0].style.display ="none";	

 	cart=JSON.parse(document.getElementsByClassName("warenkorb_daten")[0].innerHTML)
 	
	rebates=JSON.parse(document.getElementsByClassName("rebates_daten")[0].innerHTML)
	
	first_height=0
 	gutscheincode=_gutscheincode;
	max=2;
	land="";

	adapt_checkout_onresize();


	
	var i=0;
	while(i<=15)
	{	
		kreditkarten_nummer[i]=new Array;
		i=i+1;
	}
	kreditkarten_nummer_stelle=0;

	stelle=0;
	string_="";
 }
	 
	 



 
 function lingerie_anzeigen(subscription)
 {
	i=0;
	j=0;
	h=0;	
	var box="<br>";

			var i=0;
			 while(i<=cart.length-1)
			 {


			 	if(i>=1)  
			 		box=box+"<br><br><br><div style='width:100%;height:1px;background-color:#e6e6e6'></div><br>"

	 				pictures_cart=JSON.parse(cart[i].picture)

					box=box+"<div style='float:left;font-size:14px;width:100%;position:relative;'><div style='width:100%;height:125px;float:left;'><div style='cursor:pointer' onclick='gerichte_detail("+i+")'><img src='"+pictures_cart[0].link+"' class='image_order'/><div class='style'><b>"+cart[i].style+"</b><br><div style='float:left;font-size:12px;'>"+cart[i].bhgroesse+"</div><br><div style='float:left;font-size:12px;'>"+cart[i].slipgroesse+"</div></div></div>";
					box=box+"<div class='product_price'>"



					if(subscription=="yes")
					{
						if(cart[i].productgroup!="geschenkkarten")
						{

							if(cart[i].rabatt!="")
							{
								box=box+"<b><p style='text-decoration: line-through;line-height:10px;'>VIP "+replace_dot_comma((cart[i].pricesubscription)*cart[i].anzahl)+" €</b></p>";
								box=box+"<b><p style='color:#b51d36;line-height:10px;'>"+replace_dot_comma((cart[i].pricesubscription+cart[i].rabatt)*cart[i].anzahl)+" €</p></b>";
							}
							else
							{
								box=box+"<b>VIP "+replace_dot_comma((cart[i].pricesubscription)*cart[i].anzahl)+" €</b>";
							}	
						}
						else
							box=box+"<b>"+replace_dot_comma((cart[i].pricesubscription)*cart[i].anzahl)+" €</b>"			
					}
					else
					{

						if(cart[i].productgroup!="geschenkkarten")
						{
							if(cart[i].rabatt!="")
							{
								box=box+"<b><p style='text-decoration: line-through'>Regulär "+replace_dot_comma((cart[i].priceregular)*cart[i].anzahl)+" €</p></b>";
								box=box+"<b><p style='color:#b51d36'>"+replace_dot_comma((cart[i].priceregular+cart[i].rabatt)*cart[i].anzahl)+" €</p></b>";
							}
							else
							{
								box=box+"<b>Regulär "+replace_dot_comma((cart[i].priceregular)*cart[i].anzahl)+" €</b>";				
							}			
						}
						else
							box=box+"<b>"+replace_dot_comma((cart[i].priceregular)*cart[i].anzahl)+" €</b>";
					}
							

					box=box+"</div><br>";

					
					
					box=box+"<div class='select_size' ><div class='anzahl' style='margin-top:5px;'>Anzahl</div><select class='select_anzahl' onchange='change_cart("+i+")' >";
					
					var w=0;
					
					
					min_1=10;
					

					while(w<=Math.min(min_1,10))
					{
						box=box+"<option>"+w+"</option>";
						w=w+1;
					}
					
					
					box=box+"</select><br><div class='entfernen' style='float:right;cursor:pointer;font-size:12px;color:#b51d36;margin-left:10px;' id='entfernen"+i+"' onclick='entfernen("+i+")'>Entfernen</div>	</div></div></div><br><br><br><br>";


			
					
				
				 i=i+1;	
			 
			 }
			 
			 
			 box=box+"<br>";
			 


	

		 

		 
		 var maxim= document.getElementsByClassName("lingerie");
		 maxim[0].innerHTML=box;
		 
		 
		 var h=0;
		 

		
		 
		 var i=0;
		 nummer=0;
		 while(i<=cart.length-1)
		 {
			document.getElementsByClassName("select_anzahl")[i].selectedIndex=cart[i].anzahl;
			i=i+1;	
		 
		 }
 }
 
 
 
 function gerichte_detail(link_)
 {
	 

	 window.top.location.href = "/Produktauswahl/"+cart[link_].link1+"/"+cart[link_].style+"/";; 	 
	 
 }
 
 
 
 
function get_cart_from_server()
{
	alert("ja")
					$.ajax({
					timeout:2000,
					error: function(){
						get_cart_from_server();
					},


					type: "GET",
					tryCount : 0,
  				  	retryLimit : 5,
					url: "/get_cart_from_server/",
					dataType: "json",
					data: {'get_cart_data_and_rebates':'yes' },
					success: function(data) {
						alert(data)
						if(data=="lingerie not available")
							alert_userdata_reload("BH NICHT VERFÜGBAR","In Deinem gewählten Set ist leider der BH nicht mehr in zusätzlichen Mengen verfügbar. Diese Seite wird neu geladen.")
						else
							if(data=="lingerie_panty not available")
								alert_userdata_reload("SLIP NICHT VERFÜGBAR","In Deinem gewählten Set ist leider der Slip nicht mehr in zusätzlichen Mengen verfügbar. Diese Seite wird neu geladen.")
							else
								if(data=="panty not available")
									alert_userdata_reload("SLIP NICHT VERFÜGBAR","Der Slip ist leider nicht mehr in zusätzlichen Mengen verfügbar. Diese Seite wird neu geladen.")
								else
									update_cart(data)
														
					}	
		});		
	
	
}



 

 function change_cart(clicked_id)
 {	
 alert("ASD")
	if(cart[clicked_id].anzahl!=document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex)
	{
		change_cart_anzahl=document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex-cart[clicked_id].anzahl;
		
		cart[clicked_id].anzahl=document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex;

		page_load(0);
		button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	



            if(cart[clicked_id].productgroup=="lingerie")
            {
                stylecode_lingerie=cart[clicked_id].stylecode
                colorcode_lingerie=cart[clicked_id].colorcode
                bh_groesse=cart[clicked_id].bhgroesse
                slip_groesse_lingerie=cart[clicked_id].slipgroesse
                slip_groesse_panties=""
                colorcode_panties=""
                anzahl_lingerie=cart[clicked_id].anzahl
                anzahl_panties=0
            }
            else
            {
                stylecode_lingerie=""
                colorcode_panties=cart[clicked_id].colorcode
                colorcode_lingerie=""
                slip_groesse_panties=cart[clicked_id].slipgroesse
                slip_groesse_lingerie=""
                anzahl_panties=cart[clicked_id].anzahl    
                anzahl_lingerie=0   
                bh_groesse=""
            }
            

            
		$.ajax({
					timeout:3000,
					error: function(){
						get_cart_from_server();
						page_load(1);
					button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
					},
			type: "GET",
			url: "/add/",
			dataType: "json",
			data: { "add_or_erase":"change",'get_cart_data_and_rebates':'yes', "stylecode_lingerie": stylecode_lingerie,"colorcode_lingerie": colorcode_lingerie,"bh_groesse": bh_groesse,"slip_groesse_lingerie": slip_groesse_lingerie,"slip_groesse_panties":slip_groesse_panties,"colorcode_panties": colorcode_panties,'anzahl_panties':anzahl_panties, 'anzahl_lingerie':anzahl_lingerie },
			success: function(data)
			 {		
			 alert(data)

					page_load(1);
					button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	

						if(data=="lingerie not available")
							alert_userdata_reload("BH NICHT VERFÜGBAR","In Deinem gewählten Set ist leider der BH nicht mehr in zusätzlichen Mengen verfügbar. Diese Seite wird neu geladen.")
						else
							if(data=="lingerie_panty not available")
								alert_userdata_reload("SLIP NICHT VERFÜGBAR","In Deinem gewählten Set ist leider der Slip nicht mehr in zusätzlichen Mengen verfügbar. Diese Seite wird neu geladen.")
							else
								if(data=="panty not available")
									alert_userdata_reload("SLIP NICHT VERFÜGBAR","Der Slip ist leider nicht mehr in zusätzlichen Mengen verfügbar. Diese Seite wird neu geladen.")
								else
									update_cart(data)

			}
		})
	}
				

 }
 
 
 
 function detectCardType(number) {

    var re = {
        electron: /^(4026|417500|4405|4508|4844|4913|4917)\d+$/,
        maestro: /^(5018|5020|5038|5612|5893|6304|6759|6761|6762|6763|0604|6390)\d+$/,
        dankort: /^(5019)\d+$/,
        interpayment: /^(636)\d+$/,
        unionpay: /^(62|88)\d+$/,
        visa: /^4[0-9]{12}(?:[0-9]{3})?$/,
        mastercard: /^5[1-5][0-9]{14}$/,
        amex: /^3[47][0-9]{13}$/,
        diners: /^3(?:0[0-5]|[68][0-9])[0-9]{11}$/,
        discover: /^6(?:011|5[0-9]{2})[0-9]{12}$/,
        jcb: /^(?:2131|1800|35\d{3})\d{11}$/
    }

	
    for(var key in re) {

        if(re[key].test(number)) {
            
            return key
        }
    }
}





 
 function entfernen(clicked_id)
 {
	
	 alert("asdasd")
	document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex=0;
	
	change_cart(clicked_id);

	 
	 
 }
 


 

 
 
  function zahlung_click(clicked_id)
 {
 	
 	
 	document.getElementById("agb_klarna").style.display="none";
	 selected_zahlungsoption=clicked_id;
	zahlungsoption=clicked_id;
	var i=0;
	document.getElementById("bestellen_ueberpruefen").style.display="none"
	var maxim= document.getElementsByClassName("zahlung");
	while(i<=4)
	{

		if(i==clicked_id)
		{
			
			maxim[i].style.borderBottom="1px solid #b51d36";
			maxim[i].style.backgroundColor="#e6e6e6";
			
			
		}
		else
		{
			
			maxim[i].style.borderBottom="1px solid #e6e6e6";
			maxim[i].style.backgroundColor="#ffffff";
			
		}
		i=i+1;
		
		
	}
	
	if(clicked_id==0)
		kreditkarten_daten_laden();
	if(clicked_id==1)
		paypal_laden();
	if(clicked_id==2)
		sofortueberweisung_laden();
	if(clicked_id==3)
		lastschrift_daten_laden();	 
		
	if(clicked_id==4)
		rechnung_laden();	
		
	check_error_button() 
 }
 
 
  function rechnung_laden()
 {
 	document.getElementById("agb_klarna").style.display="block";


		 var tag=new Array(31);
		 var monat=new Array(12);
		 var jahr=new Array(100);
		 
		 var i=0;
		 while(i<=12)
		 {
			 monat[0]=new Array;
			 i=i+1;
		 }



		 var i=0;
		 while(i<=31)
		 {
			 tag[0]=new Array;
			 i=i+1;
		 }
		 
		 
		 var i=0;
		 while(i<=100)
		 {
			 jahr[0]=new Array;
			 i=i+1;
		 }







		 monat[0]= "Monat";
		 monat[1]= "01";
		 monat[2]= "02";
		 monat[3]= "03";
		 monat[4]= "04";
		 monat[5]= "05";
		 monat[6]= "06";
		 monat[7]= "07";
		 monat[8]= "08";
		 monat[9]= "09";
		 monat[10]= "10";
		 monat[11]= "11";
		 monat[12]= "12";
		 
		 
		 tag[0]= "Tag";
		 tag[1]= "01";
		 tag[2]= "02";
		 tag[3]= "03";
		 tag[4]= "04";
		 tag[5]= "05";
		 tag[6]= "06";
		 tag[7]= "07";
		 tag[8]= "08";
		 tag[9]= "09";


		 var i=10;
		 while(i<=31)
		 {
			 tag[i]=i
			 i=i+1;
		 }	 


		box=""
		box=box+"<select id='geburtsdatum_tag' >"


		 var i=0;
		 while (i<=31)
		 {
			box=box+"<option>"+tag[i]+"</option>";
			 i=i+1;
		 }
		 
		box=box+"</select>"
		 
		box=box+"<select id='geburtsdatum_monat' style='margin-left:10px;'>"
		 var i=0;
		 while (i<=12)
		 {
			box=box+"<option>"+monat[i]+"</option>";
			 i=i+1;
		 }
		box=box+"</select>"
		 
		box=box+"<select id='geburtsdatum_jahr' style='margin-left:10px;margin-bottom:10px;'>"
		 var i=1918;
		 box=box+"<option>Jahr</option>";
		 while (i<=2003)
		 {
			box=box+"<option>"+i+"</option>";
			 i=i+1;
		 }

		box=box+"</select>"

 	document.getElementById("kreditkarten").innerHTML="<div style='line-height:20px;' ><b>In 14 Tagen zahlen</b><br><br>Heute bestellen, aber erst in 14 Tagen bezahlen. Es entstehen Dir keine Zusatzkosten.</div><br><span id='invoicexx' style='text-decoration:underline'></span><br><br><br><p style='font-weight:500'>Geburtsdatum</p></div><br>"+box;
 	
 	document.getElementById("agb_klarna_text").innerHTML="Mit der Übermittlung der für die Abwicklung der gewählten Klarna–Zahlungsmethode und einer Identitäts– und Bonitätsprüfung erforderlichen Daten an Klarna bin ich einverstanden. Meine <span id='consentxx' style='text-decoration:underline'></span> kann ich jederzeit mit Wirkung für die Zukunft widerrufen. Es gelten die <a href='/agb/' style='text-decoration:underline' target='_blank'>AGB</a> des Händlers. "
 	
 	new Klarna.Terms.Consent({  
    el: 'consentxx',
    eid: '11054',
    locale: 'de_de',
    type: 'desktop'
});


new Klarna.Terms.Invoice({
    el: 'invoicexx',
    eid: '123',
    locale: 'de_de',
    charge: 0,
    type: 'desktop'
});


 }
 
 
 function paypal_laden()
 {



 	document.getElementById("kreditkarten").innerHTML="<div style='line-height:20px;' ><b>Mit Paypal zahlen</b><br><br>Nachdem Du bestellt hast, wirst Du im nächsten Schritt zu Paypal weitergeleitet. Nach der Bezahlung gelangst Du zur Bestellbestätigung.</div><br>";
 	



 }
 
  
  function sofortueberweisung_laden()
 {

 	document.getElementById("kreditkarten").innerHTML="<div style='line-height:20px;'><b>Mit sofortüberweisung zahlen</b><br><br>Nachdem Du bestellt hast, wirst Du im nächsten Schritt zu sofortüberweisung.de weitergeleitet. Nach der Bezahlung gelangst Du zur Bestellbestätigung.</div><br>";
 }
 
 
 
 
 
 
 
 function lastschrift_anzeigen()
 {
		 var box="<div id='kartendetails_maske'> <div class='karten_text_css' >Kontoinhaber<br><input class='karten_css' onkeyup='felder_zuruecksetzen_sepa(0)' onkeydown='felder_zuruecksetzen_sepa(0)' type='text'></input></div><br><div class='karten_text_css' >IBAN<br><input class='karten_css' placeholder='' type='text' onkeyup='felder_zuruecksetzen_sepa(1)' onkeydown='felder_zuruecksetzen_sepa(1)' ></input></div>";

		box=box+"</select></div><div class='karten_text_css' >BIC<br><input class='karten_css' onkeyup='felder_zuruecksetzen_sepa(2)' onkeydown='felder_zuruecksetzen_sepa(2)' type='text' ></input></div></div>";
		box=box+"<br><br><br><br><br><div style='float:right;margin-bottom:40px;margin-top:20px;width:100%;'>"
		

		
		box=box+"<form id='payment-form' action='#' method='POST'>"
		box=box+"<input class='amount-int' type='hidden' value='1753' />"
		box=box+"<input class='currency' type='hidden' value='EUR' />"
		box=box+"<input class='iban' type='hidden'  value='4111111111111111'/>"
		box=box+"<input class='bic' type='hidden' value='123' />"
		box=box+"<input class='accountholder' type='hidden'   value='asdasd' />"
		box=box+"</form>"


		if(shopping_type=="VIP")
			box=box+"<div class='benachrichtigungen_text' style='display:none' ><input type='checkbox'  checked=true style='cursor:pointer;float:left;'  id='zahlungsdaten_checkbox' ></input><div style='cursor:pointer;float:left;width:80%;margin-left:10px;margin-top:-2px;'  onclick='zahlungsdaten_speichern()'>Speichern für weitere Käufe</div></div><br>"
		else
			box=box+"<div class='benachrichtigungen_text' ><input type='checkbox'  checked=true style='cursor:pointer;float:left;'  id='zahlungsdaten_checkbox' ></input><div style='cursor:pointer;float:left;width:80%;margin-left:10px;margin-top:-2px;'  onclick='zahlungsdaten_speichern()'>Speichern für weitere Käufe</div></div><br>"
			
		box=box+"<button  id='kreditkarte_check_button_id' name='submit' class='kreditkarte_check_button'  onclick='lastschrift_check()'>"
		
		box=box+"<i class='fa fa-circle-o-notch fa-spin' id='kreditkarte_check_button_id_logo' style='display:none'></i>"
		box=box+"<div id='kreditkarte_check_button_id_text'>Überprüfen</div>"
		box=box+"</button>"
								

		box=box+"<div  class='kreditkarte_check_button_abbrechen'  onclick='lastschrift_abbrechen()' >Abbrechen</div>"
		box=box+"</div><br><br><div id='buttons_credit_card' style='float:right;color:red;font-weight:bold;margin-bottom:20px;'></div><br> ";
		document.getElementById("kreditkarten_hinzufuegen").innerHTML=box;

 }





 
 function kreditkarten_anzeigen()
 {

	
		 var monat=new Array(12);
		 var jahr=new Array(6);
		 
		 var i=0;
		 while(i<=12)
		 {
			 monat[0]=new Array;
			 i=i+1;
		 }
		 


		 
		 monat[0]= "";
		 monat[1]= "01 / Jan";
		 monat[2]= "02 / Feb";
		 monat[3]= "03 / Mrz";
		 monat[4]= "04 / Apr";
		 monat[5]= "05 / Mai";
		 monat[6]= "06 / Jun";
		 monat[7]= "07 / Jul";
		 monat[8]= "08 / Aug";
		 monat[9]= "09 / Sep";
		 monat[10]= "10 / Okt";
		 monat[11]= "11 / Nov";
		 monat[12]= "12 / Dez";
		 
		 var jahr_anzahl=8;
		 var jahr_start=2017;
		 var i=1;
		 
		 jahr[0]="";
		 while(i<=jahr_anzahl+1)
		 {
			 jahr[i]=new Array;
			 jahr[i]=jahr_start+i;
			 i=i+1;
			 
			 
		 }
		 
		
		
		 
		 var box="<div><img src='/static/lock_icon.png' width='25'></img><b>Sichere Übertragung Deiner Daten dank SSL-Verschlüsselung</b></div><div id='kartendetails_maske'> <div class='karten_text_css' >Karteninhaber<br><input class='karten_css' onkeyup='felder_zuruecksetzen_kreditkarte(0)' onkeydown='felder_zuruecksetzen_kreditkarte(0)' type='text'></input></div><br><div class='karten_text_css' >Kartennummer<br><input class='karten_css' placeholder='' type='text' onKeyUp='kreditkarten_show(event)' onKeyDown='kreditkarten_show(event)' maxlength='19' onBlur='kreditkarten_show(event)'></input></div>";
		 box = box+"<br><div class='ablaufdatum_text'  id='ablaufdatum_text'>Ablaufdatum<br><select class='karten_css' style='width:45%;float:left;' onchange='felder_zuruecksetzen_kreditkarte(2)'>";
		  
		 var i=0;
		 while (i<=12)
		 {
			box=box+"<option>"+monat[i]+"</option>";
			 i=i+1;
		 }
		 
		 
		 box=box+"</select><select class='karten_css' style='width:45%;margin-left:5px;float:left;' onchange='felder_zuruecksetzen_kreditkarte(3)'>";
		 
		 var i=0;
		 while (i<=jahr_anzahl)
		 {
			box=box+"<option>"+jahr[i]+"</option>";
			 i=i+1;
		 }
		 
		 
		 
		box=box+"</select></div><div class='karten_text_css_pruefnummer' >Prüfnummer<br><input class='karten_css' onkeyup='felder_zuruecksetzen_kreditkarte(4)' onkeydown='felder_zuruecksetzen_kreditkarte(4)' type='text' maxlength='4' onkeypress='validate(event)'></input></div></div>";
		box=box+"<br><br>"
		


		box=box+"<br><div style='float:right;margin-bottom:40px;margin-top:20px;width:100%;'>"
		

		
		box=box+"<form id='payment-form' action='#' method='POST'>"
		box=box+"<input class='card-amount-int' type='hidden' value='1753' />"
		box=box+"<input class='card-currency' type='hidden' value='EUR' />"
		box=box+"<input class='card-number' type='hidden'  value='4111111111111111'/>"
		box=box+"<input class='card-cvc' type='hidden' value='123' />"
		box=box+"<input class='card-holdername' type='hidden'   value='asdasd' />"
		box=box+"<input class='card-expiry-month' type='hidden'  value='03' />"
		box=box+"<input class='card-expiry-year' type='hidden'  value='2018' />"
		box=box+"</form>"

		if(shopping_type=="VIP")
			box=box+"<div class='benachrichtigungen_text' style='display:none' ><input type='checkbox'  checked=true style='cursor:pointer;float:left;'  id='zahlungsdaten_checkbox' ></input><div style='cursor:pointer;float:left;width:60%;margin-left:10px;margin-top:-2px;'  onclick='zahlungsdaten_speichern()'>Speichern für weitere Käufe</div></div><br>"
		else
			box=box+"<div class='benachrichtigungen_text' ><input type='checkbox'  checked=true style='cursor:pointer;float:left;'  id='zahlungsdaten_checkbox' ></input><div style='cursor:pointer;float:left;width:60%;margin-left:10px;margin-top:-2px;'  onclick='zahlungsdaten_speichern()'>Speichern für weitere Käufe</div></div><br>"
		
		box=box+"<button  id='kreditkarte_check_button_id' name='submit' class='kreditkarte_check_button'  onclick='kreditkarten_check()'>"
		
		box=box+"<i class='fa fa-circle-o-notch fa-spin' id='kreditkarte_check_button_id_logo' style='display:none'></i>"
		box=box+"<div id='kreditkarte_check_button_id_text'>Überprüfen</div>"
		box=box+"</button>"
		
							

		box=box+"<div  class='kreditkarte_check_button_abbrechen'  onclick='kreditkarten_abbrechen()' >Abbrechen</div>"
		box=box+"</div><br><br><div id='buttons_credit_card' style='float:right;color:red;font-weight:bold;margin-bottom:20px;'></div><br> ";
		document.getElementById("kreditkarten_hinzufuegen").innerHTML=box;
		
		var i=0;
		while(i<=kreditkarten_nummer_stelle)
		{
			document.getElementsByClassName("karten_css")[1].value="";
			

			
			i=i+1;
			
		}
		
		kreditkarten_nummer_stelle=0;
	 

	 
 }
 
 
 function zahlungsdaten_speichern()
 {
 	if(document.getElementById("zahlungsdaten_checkbox").checked==false)
 		document.getElementById("zahlungsdaten_checkbox").checked=true;
 	else
 		document.getElementById("zahlungsdaten_checkbox").checked=false;
 }
 


 
 

 function adressbuch_laden()
{
	adressbuch=JSON.parse(document.getElementsByClassName("adressbuch_daten")[0].innerHTML)
	i=0;
	standard_rechnungsadresse=-1;
	standard_lieferadresse=-1;
	while(i<=adressbuch.length-1)
	{

		if(adressbuch[i].standard_rechnungsadresse=="ja")
			standard_rechnungsadresse=i;
		if(adressbuch[i].standard_lieferadresse=="ja")
		{
			standard_lieferadresse=i;
			land=adressbuch[i].land	
		}
		i=i+1;
	}

	if(standard_rechnungsadresse==-1)
		standard_rechnungsadresse=standard_lieferadresse

	
	if(standard_rechnungsadresse!=-1)
		show_maps(standard_rechnungsadresse,standard_lieferadresse)
	else
		adresse_anzeigen("nein","nein");
}


function adresse_laden(index_rechungsadresse,index_lieferadresse)
{

	document.getElementById("check_address").style.display="block";
	adresse_anzeigen(index_rechungsadresse,index_lieferadresse);
	adresse_in_form_laden(index_rechungsadresse,index_lieferadresse);	
}
function adresse_in_form_laden(index_rechungsadresse,index_lieferadresse)
{
	i=0;
	max=0;

	if(index_lieferadresse!=index_rechungsadresse)
		max=1;

	while(i<=max)
	{
		if(i==0)
			index=index_rechungsadresse
		else
			index=index_lieferadresse
			
		document.getElementsByClassName("adresse_input")[i].value=adressbuch[index].strasse;
		document.getElementsByClassName("adresse")[i*4].value=adressbuch[index].hausnummer;
		document.getElementsByClassName("adresse")[i*4+1].value=adressbuch[index].stadt;
		document.getElementsByClassName("adresse")[i*4+2].value=adressbuch[index].plz;
		document.getElementsByClassName("adresse")[i*4+3].value=adressbuch[index].land;

		document.getElementsByClassName("adresse_other")[i*3].value=adressbuch[index].anrede;
		document.getElementsByClassName("adresse_other")[i*3+1].value=adressbuch[index].vorname;
		document.getElementsByClassName("adresse_other")[i*3+2].value=adressbuch[index].nachname;
		document.getElementsByClassName("adresse_mobilnummer")[i].value=adressbuch[index].telefonnummer;
		if(adressbuch[index].unternehmensdetails!="")
			document.getElementsByClassName("unternehmensdetails")[i].value=adressbuch[index].unternehmensdetails;
		else
			document.getElementsByClassName("address_unternehmensangaben_input_header")[i].style.display="none";
			
		i=i+1;
	}	
}

function check_address_2()
{

	button_logo(0,"check_address_text","check_address_logo","check_address")
	button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
	
	check_address();
	button_logo(1,"check_address_text","check_address_logo","check_address")
	button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
	
	
}

function felder_zuruecksetzen_kreditkarte(index)
{

	if(index==0 || index==1)
	{
		document.getElementsByClassName("karten_css")[index].style.border="1px solid #e6e6e6";	
		document.getElementsByClassName("karten_text_css")[index].style.color="#4E4E4E";	
	}
	else
	{
		if(index!=4)
		{
			document.getElementsByClassName("karten_css")[index].style.border="1px solid #e6e6e6";	
			document.getElementsByClassName("ablaufdatum_text")[0].style.color="#4E4E4E";	
		}
		else
		{
			document.getElementsByClassName("karten_css")[index].style.border="1px solid #e6e6e6";	
			document.getElementsByClassName("karten_text_css_pruefnummer")[0].style.color="#4E4E4E";	
			
		}
	}

}

function felder_zuruecksetzen_sepa(index)
{

		document.getElementsByClassName("karten_css")[index].style.border="1px solid #e6e6e6";	
		document.getElementsByClassName("karten_text_css")[index].style.color="#4E4E4E";	


}


 
 function kreditkarten_check()
 {
	document.getElementsByClassName("kreditkarte_check_button_abbrechen")[0].style.pointerEvents = 'none';
	document.getElementsByClassName("button_check")[0].style.pointerEvents = 'none';
	document.getElementsByClassName("button_cart_large")[0].style.pointerEvents = 'none';
	document.getElementById("buttons_credit_card").innerHTML=""
	 kreditkarten_nummer_="";
	 ablaufdatum="";
	 kreditkarten_nummer__="";
	 
	 kreditkarten_show("")
	 var i=0;
	 while (i<=18)
	 {
		kreditkarten_nummer__= kreditkarten_nummer__+kreditkarten_nummer[i]
		if(i>=15)
			kreditkarten_nummer_=kreditkarten_nummer_+kreditkarten_nummer[i];
		else
			if(kreditkarten_nummer[i]=="-")
				kreditkarten_nummer_=kreditkarten_nummer_+"-";
			else
				kreditkarten_nummer_=kreditkarten_nummer_+"*";
		
		i=i+1;
		 
	 }

	 var status=0;

	if(document.getElementsByClassName("karten_css")[1].value.length!=19)
	{
		document.getElementById("buttons_credit_card").innerHTML="Bitte alle benötigten Felder ausfüllen.";		
		document.getElementsByClassName("karten_css")[1].style.border="1px solid red";	
		document.getElementsByClassName("karten_text_css")[1].style.color="red";		
		status=1;
		
	}	

	 if(document.getElementsByClassName("karten_css")[0].value=="")
	 {
		document.getElementById("buttons_credit_card").innerHTML="Bitte alle benötigten Felder ausfüllen.";		
		document.getElementsByClassName("karten_css")[0].style.border="1px solid red";	
		document.getElementsByClassName("karten_text_css")[0].style.color="red"; 
		status=1;
		 
	 }

	 if(document.getElementsByClassName("karten_css")[4].value=="")
	 {
		document.getElementById("buttons_credit_card").innerHTML="Bitte alle benötigten Felder ausfüllen.";		
		document.getElementsByClassName("karten_css")[4].style.border="1px solid red";	
		document.getElementsByClassName("karten_text_css_pruefnummer")[0].style.color="red"; 
		status=1;
	 }


	 if(document.getElementsByClassName("karten_css")[3].value=="")
	 {

		document.getElementById("buttons_credit_card").innerHTML="Bitte alle benötigten Felder ausfüllen.";		
			
		document.getElementsByClassName("karten_css")[3].style.border="1px solid red";	
			
		document.getElementById("ablaufdatum_text").style.color="red";	
			
		status=1;
		 
	 }
	 
	 if(document.getElementsByClassName("karten_css")[2].value=="")
	 {

		document.getElementById("buttons_credit_card").innerHTML="Bitte alle benötigten Felder ausfüllen.";		
			
		document.getElementsByClassName("karten_css")[2].style.border="1px solid red";	
			
		document.getElementById("ablaufdatum_text").style.color="red";	
			
		status=1;
		 
	 }

	 
	 
	 
	 if(status==0)
	 { 
		document.getElementsByClassName("card-number")[0].value=document.getElementsByClassName("karten_css")[1].value.replace(/-/g , "")

		 
		 document.getElementsByClassName("card-cvc")[0].value=document.getElementsByClassName("karten_css")[4].value;
		 document.getElementsByClassName("card-expiry-month")[0].value=document.getElementsByClassName("karten_css")[2].value.substring(0,2);
		 document.getElementsByClassName("card-expiry-year")[0].value=document.getElementsByClassName("karten_css")[3].value;	 	 
		 document.getElementsByClassName("card-holdername")[0].value=document.getElementsByClassName("karten_css")[0].value;



		page_load(0);
		button_logo("0","kreditkarte_check_button_id_text","kreditkarte_check_button_id_logo","kreditkarte_check_button_id")	
		document.getElementsByClassName("card-amount-int")[0].value=parseInt(rebates[0].gesamtpreis*100);
	paymill.createToken({
			
		  number: $('.card-number').val(),  // required, ohne Leerzeichen und Bindestriche
		  exp_month: $('.card-expiry-month').val(),   // required
		  exp_year: $('.card-expiry-year').val(),     // required, vierstellig z.B. "2016"
		  cvc: $('.card-cvc').val(),                  // required
		  amount_int: $('.card-amount-int').val(),    // required, integer, z.B. "15" fÃ¼r 0,15 Euro
		  currency: $('.card-currency').val(),    // required, ISO 4217 z.B. "EUR" od. "GBP"
		  cardholder: $('.card-holdername').val(), // optional
		  email:          document.getElementById("email").innerHTML
		}, PaymillResponseHandler);  
	 }
	 document.getElementsByClassName("kreditkarte_check_button_abbrechen")[0].style.pointerEvents = 'auto';
	document.getElementsByClassName("button_check")[0].style.pointerEvents = 'auto';
	document.getElementsByClassName("button_cart_large")[0].style.pointerEvents = 'auto';

 }
 
 
 
 
 function lastschrift_check()
 {
 	
	document.getElementsByClassName("kreditkarte_check_button_abbrechen")[0].style.pointerEvents = 'none';
	document.getElementsByClassName("button_check")[0].style.pointerEvents = 'none';
	document.getElementsByClassName("button_cart_large")[0].style.pointerEvents = 'none';

	 var status=0;


	if(document.getElementsByClassName("karten_css")[1].value=="")
	{
		document.getElementById("buttons_credit_card").innerHTML="Bitte alle benötigten Felder ausfüllen.";		
		document.getElementsByClassName("karten_css")[1].style.border="1px solid red";	
		document.getElementsByClassName("karten_text_css")[1].style.color="red";		
		status=1;
	}	

	 if(document.getElementsByClassName("karten_css")[0].value=="")
	 {
		document.getElementById("buttons_credit_card").innerHTML="Bitte alle benötigten Felder ausfüllen.";		
		document.getElementsByClassName("karten_css")[0].style.border="1px solid red";	
		document.getElementsByClassName("karten_text_css")[0].style.color="red"; 
		status=1;
	 }

	 if(document.getElementsByClassName("karten_css")[2].value=="")
	 {
		document.getElementById("buttons_credit_card").innerHTML="Bitte alle benötigten Felder ausfüllen.";		
		document.getElementsByClassName("karten_css")[2].style.border="1px solid red";	
		document.getElementsByClassName("karten_text_css")[2].style.color="red"; 
		status=1;
	 }


	 
	 if(status==0)
	 { 
		document.getElementsByClassName("iban")[0].value=document.getElementsByClassName("karten_css")[1].value
		 document.getElementsByClassName("bic")[0].value=document.getElementsByClassName("karten_css")[2].value
		 document.getElementsByClassName("accountholder")[0].value=document.getElementsByClassName("karten_css")[0].value;

		
		page_load(0);
		 button_logo("0","kreditkarte_check_button_id_text","kreditkarte_check_button_id_logo","kreditkarte_check_button_id")	
		 
		 document.getElementsByClassName("amount-int")[0].value=1753;
		paymill.createToken({
			
		  iban: $('.iban').val(),  // required, ohne Leerzeichen und Bindestriche
		  bic: $('.bic').val(),   // required
		  amount_int: $('.amount-int').val(),    // required, integer, z.B. "15" fÃ¼r 0,15 Euro
		  currency: $('.currency').val(),    // required, ISO 4217 z.B. "EUR" od. "GBP"
		  accountholder: $('.accountholder').val() // optional
		}, PaymillResponseHandler_lastschrift);  
	 }
	 document.getElementsByClassName("kreditkarte_check_button_abbrechen")[0].style.pointerEvents = 'auto';
	document.getElementsByClassName("button_check")[0].style.pointerEvents = 'auto';
	document.getElementsByClassName("button_cart_large")[0].style.pointerEvents = 'auto'; 	

 }
  
 
 function PaymillResponseHandler(error, result) {
  if (error) {
  	
    console.log(error);

  	    // Shows the error above the form
    		page_load(1);
			button_logo("1","kreditkarte_check_button_id_text","kreditkarte_check_button_id_logo","kreditkarte_check_button_id")	
			alert_userdata("KREDITKARTE WIRD NICHT UNTERSTÜTZT","Deine Kreditkartendaten sind falsch. Bitte überprüfe Deine Eingabe.")
			document.getElementsByClassName("karten_css")[1].style.border="1px solid red";	
			document.getElementsByClassName("karten_text_css")[1].style.color="red";

  } else {
 
    var form = $("#payment-form");
    // Output token
    var token = result.token;

    // Insert token into form in order to submit to server
    form.append("");
	credit_card_successful(token)
  }
}



 function PaymillResponseHandler_lastschrift(error, result) {
  if (error) {
    // Shows the error above the form
    		page_load(1);
    		button_logo("1","kreditkarte_check_button_id_text","kreditkarte_check_button_id_logo","kreditkarte_check_button_id")	
			alert_userdata("IBAN UND BIC NICHT KORREKT","Bitte eine richtige IBAN und BIC angeben.")
			document.getElementsByClassName("karten_css")[1].style.border="1px solid red";	
			document.getElementsByClassName("karten_text_css")[1].style.color="red";
			document.getElementsByClassName("karten_css")[2].style.border="1px solid red";	
			document.getElementsByClassName("karten_text_css")[2].style.color="red";

  } else {
 
    var form = $("#payment-form");
    // Output token
    var token = result.token;

    // Insert token into form in order to submit to server
    form.append("");
	lastschrift_successful(token)
  }
}



 function lastschrift_successful(token)
 {
 	
		page_load(0);
		button_logo("0","kreditkarte_check_button_id_text","kreditkarte_check_button_id_logo","kreditkarte_check_button_id")	

 		if(zahlungsmethoden=="")
			standard_="ja";
		else
			standard_="nein";

				$.ajax({
				timeout:15000,
 				error: function(){								
 								page_load(1);
								button_logo("1","kreditkarte_check_button_id_text","kreditkarte_check_button_id_logo","kreditkarte_check_button_id")	},
				type: "POST",
				url: "/account_page/zahlungsmethode_speichern/",
				dataType: "json",
				data: { "hinzufuegen":1,"indexnummer":"","zahlungsoption": 3,"token":token,'standard':standard_,'zahlungsart':'lastschrift','speichern':document.getElementById("zahlungsdaten_checkbox").checked},
				success: function(data) {
								page_load(1);
								button_logo("1","kreditkarte_check_button_id_text","kreditkarte_check_button_id_logo","kreditkarte_check_button_id")	
								if(data!="existiert")
								{
									
									fbq('track', 'AddPaymentInfo', {
									      content_category: "Sets", 
									      content_ids: document.getElementsByClassName("content_id_list")[0].innerHTML, 
									      contents: document.getElementsByClassName("contents_list")[0].innerHTML, 
									      value: rebates[0].gesamtpreis,
									      currency: 'EUR' ,
									      num_items:document.getElementsByClassName("num_items")[0].innerHTML
									    });  	
		  		  			gtag('event', 'checkout',{
				  
				  'event_label':2,
				  'event_category': 'payment info provided'
				});


												check_error_button() 
    
									document.getElementsByClassName("zahlungsmethoden_daten")[0].innerHTML=data;
									lastschrift_daten_laden();
								}
								else
									alert_userdata("IBAN WIRD BEREITS VON DIR VERWENET","Die eingegebene IBAN wird bereits von dir verwendet. Wähle sie als Zahlungsmittel aus.");				
						}
				});
	

 
	document.getElementsByClassName("kreditkarte_check_button_abbrechen")[0].style.pointerEvents = 'auto';
	document.getElementsByClassName("button_check")[0].style.pointerEvents = 'auto';
	document.getElementsByClassName("button_cart_large")[0].style.pointerEvents = 'auto'; 
 
 }


 
 
 function credit_card_successful(token)
 {
 	
 	button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
 	button_logo("0","kreditkarte_check_button_id_text","kreditkarte_check_button_id_logo","kreditkarte_check_button_id")	
 	page_load(0);

 		if(zahlungsmethoden=="")
			standard_="ja"
		else
			standard_="nein"
		
		card_number=document.getElementsByClassName("karten_css")[1].value.replace(/-/g , "")
		card_type=detectCardType(card_number)

		if(card_type=="visa" || card_type=="mastercard")
		{			

				$.ajax({
				timeout:15000,
 				error: function(){								
 								page_load(1);
								button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
								button_logo("1","kreditkarte_check_button_id_text","kreditkarte_check_button_id_logo","kreditkarte_check_button_id")},
				type: "POST",
				url: "/account_page/zahlungsmethode_speichern/",
				dataType: "json",
				data: { "hinzufuegen":1,"indexnummer":"","zahlungsoption": 0,"card_type":card_type,"token":token,'standard':standard_,'zahlungsart':'kreditkarte','speichern':document.getElementById("zahlungsdaten_checkbox").checked},
				success: function(data) {
								page_load(1);

								button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
								button_logo("1","kreditkarte_check_button_id_text","kreditkarte_check_button_id_logo","kreditkarte_check_button_id")	
								if(data!="existiert")
								{
									fbq('track', 'AddPaymentInfo', {
									      content_category: "Sets", 
									      content_ids: document.getElementsByClassName("content_id_list")[0].innerHTML, 
									      contents: document.getElementsByClassName("contents_list")[0].innerHTML, 
									      value: rebates[0].gesamtpreis,
									      currency: 'EUR' ,
									      num_items:document.getElementsByClassName("num_items")[0].innerHTML
									    });  	
		  		  			gtag('event', 'checkout',{
				  
				  'event_label':2,
				  'event_category': 'payment info provided'
				});
												check_error_button() 
									document.getElementsByClassName("zahlungsmethoden_daten")[0].innerHTML=data;

									kreditkarten_daten_laden()

								}
								else
									alert_userdata("KARTENNUMMER WIRD BEREITS VON DIR VERWENET","Die eingegebene Kreditkartennummer wird bereits von dir verwendet. Wähle sie als Zahlungsmittel aus.")					
						}
				});
	
		} 
		else
		{
			page_load(1);
			button_logo("1","kreditkarte_check_button_id_text","kreditkarte_check_button_id_logo","kreditkarte_check_button_id")	
			button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
			alert_userdata("KREDITKARTE WIRD NICHT UNTERSTÜTZT","Deine Kreditkartendaten sind falsch. Bitte überprüfe Deine Eingabe.")
			document.getElementsByClassName("karten_css")[1].style.border="1px solid red";	
			document.getElementsByClassName("karten_text_css")[1].style.color="red";
			
		}
 
	document.getElementsByClassName("kreditkarte_check_button_abbrechen")[0].style.pointerEvents = 'auto';
	document.getElementsByClassName("button_check")[0].style.pointerEvents = 'auto';
	document.getElementsByClassName("button_cart_large")[0].style.pointerEvents = 'auto'; 
 
 }
 

 
 
 function input_on_change(element,element2)
{
	element.style.border="1px solid #e6e6e6 ";	
	element2.style.color="#4E4E4E";
}
 

 
 
  function lastschrift_daten_laden()
 {
	 
	zahlungsmethoden=JSON.parse(document.getElementsByClassName("zahlungsmethoden_daten")[0].innerHTML)


	
	i=0;
	var box=""
	float_=0
	zaehler=0
	ausgewaehlt=0;
	while(i<=zahlungsmethoden.length-1)
	{
		
		if(zahlungsmethoden[i].zahlungsart=="lastschrift")
		{
	
			if(zahlungsmethoden[i].standard=="ja")
			{
				ausgewaehlt=i;
				zahlungsoption=zahlungsmethoden[i].zahlungsoption
				name_karteninhaber=zahlungsmethoden[i].name
				lastschrift_nummer__=zahlungsmethoden[i].kontonummer
				bic=zahlungsmethoden[i].bic
				
			}
	
			if(float_==0)
			{
				box=box+"<div class='zahlungsmethoden_anzeigen'  onclick='zahlungsmethode_auswaehlen("+i+")'>";
				float_=1;
				zaehler=zaehler+1;
			}
			else
			{
				box=box+"<div class='zahlungsmethoden_anzeigen'  onclick='zahlungsmethode_auswaehlen("+i+")'>";
				float_=0;
			}
			
			box=box+"<div class='zahlungsmethoden_anzeigen_block1' >";
	
			box=box+"<div style='margin-left:20px;margin-top:10px;color:#ffffff;float:left;'>"+zahlungsmethoden[i].name+"</div>";
			box=box+"<div style='margin-right:20px;margin-top:10px;color:#ffffff;float:right;'><b>"+zahlungsmethoden[i].bic+"</b></div></div>";

			box=box+"<div style='margin-left:10px;color:#000000;float:left;'>"+zahlungsmethoden[i].iban+"</div>";
			box=box+"<div style='margin-left:15px;color:#000000;float:left;'></div>"
			box=box+"<div class='ausgewaehltes_zahlungsmittel' style='margin-top:80px;text-align:center;font-style:italic;' id='"+i+"'></div>"
	
			box=box+"</div>"
		}
		

		i=i+1;
		
	}

	document.getElementById("kreditkarten").innerHTML=box+"<div class='neue_kreditkarte_hinzufuegen_check'  onclick='lastschrift_hinzufuegen()'>Neues SEPA-Lastschrift Mandat hinzufügen</div><div id='kreditkarten_hinzufuegen' style='display:none;'></div>";
	lastschrift_anzeigen();
	zahlungsmethode_auswaehlen(ausgewaehlt)
 }
 
 
 
 
 
 function kreditkarten_daten_laden()
 {
	 
	zahlungsmethoden=JSON.parse(document.getElementsByClassName("zahlungsmethoden_daten")[0].innerHTML)
	i=0;
	var box=""
	float_=0
	zaehler=0
	ausgewaehlt=0;
	while(i<=zahlungsmethoden.length-1)
	{
		
		if(zahlungsmethoden[i].zahlungsart=="kreditkarte")
		{	
	
			if(zahlungsmethoden[i].standard=="ja")
			{
				ausgewaehlt=i;
				zahlungsoption=zahlungsmethoden[i].zahlungsoption
				name_karteninhaber=zahlungsmethoden[i].name
				kreditkarten_nummer__=zahlungsmethoden[i].kreditkartennummer
				ablaufdatum=zahlungsmethoden[i].ablaufmonat+" "+zahlungsmethoden[i].ablaufjahr
				
			}
	
			if(float_==0)
			{
				box=box+"<div class='zahlungsmethoden_anzeigen'  onclick='zahlungsmethode_auswaehlen("+i+")'>";
				float_=1;
				zaehler=zaehler+1;
			}
			else
			{
				box=box+"<div class='zahlungsmethoden_anzeigen'  onclick='zahlungsmethode_auswaehlen("+i+")'>";
				float_=0;
			}
			
			box=box+"<div class='zahlungsmethoden_anzeigen_block1' >";
	
			box=box+"<div style='margin-left:20px;margin-top:10px;color:#ffffff;float:left;'>"+zahlungsmethoden[i].name+"</div>";
			if(zahlungsmethoden[i].cardtype=="visa")
				box=box+"<div style='margin-right:20px;margin-top:10px;color:#000000;float:right;'><b><img src='/static/visa.svg'  width='40' height='15'></b></div></div>";
			else
				box=box+"<div style='margin-right:20px;color:#000000;float:right;'><b><img src='/static/mastercard.svg'  width='50' height='35' ></b></div></div>";
			box=box+"<div style='margin-left:10px;color:#000000;float:left;'>****-****-****-"+zahlungsmethoden[i].kreditkartennummer+"</div>";
			box=box+"<div style='margin-left:15px;color:#000000;float:left;'>"+zahlungsmethoden[i].ablaufmonat+" "+zahlungsmethoden[i].ablaufjahr+"</div>"
			box=box+"<div class='ausgewaehltes_zahlungsmittel' style='margin-top:80px;text-align:center;font-style:italic;' id='"+i+"'></div>"
	
			box=box+"</div>"
		}

		i=i+1;
		
	}

	document.getElementById("kreditkarten").innerHTML=box+"<div class='neue_kreditkarte_hinzufuegen_check'  onclick='kreditkarte_hinzufuegen()'>Neue Kreditkarte hinzufügen</div><div id='kreditkarten_hinzufuegen' style='display:none;'></div>";
	kreditkarten_anzeigen();
	zahlungsmethode_auswaehlen(ausgewaehlt)
 }
 
 
  function lastschrift_hinzufuegen()
 {
 	lastschrift_anzeigen()
	 document.getElementById("kreditkarten_hinzufuegen").style.display="block"
	 document.getElementsByClassName("neue_kreditkarte_hinzufuegen_check")[0].style.display="none"
 }
 
 
 function kreditkarte_hinzufuegen()
 {
 	kreditkarten_anzeigen()
	 document.getElementById("kreditkarten_hinzufuegen").style.display="block"
	 document.getElementsByClassName("neue_kreditkarte_hinzufuegen_check")[0].style.display="none"
 }
 
 function kreditkarten_abbrechen()
 {
	 document.getElementById("kreditkarten_hinzufuegen").style.display="none"
	 document.getElementsByClassName("neue_kreditkarte_hinzufuegen_check")[0].style.display="block"
	document.getElementsByClassName("karten_css")[0].value=""
	document.getElementsByClassName("karten_css")[1].value=""
	document.getElementsByClassName("karten_css")[2].value=""
	document.getElementsByClassName("karten_css")[3].value=""
	document.getElementsByClassName("karten_css")[4].value=""
 }
 
 
 
 
 
 
 function zahlungsmethode_auswaehlen(index)
 {
	 i=0;
	zaehler=0;
	ausgewaehlt="";

	while(i<=zahlungsmethoden.length-1)
	{
		if(zahlungsmethoden[i].zahlungsoption==zahlungsoption)		
		{
			if(index==i)
			{
				document.getElementsByClassName("zahlungsmethoden_anzeigen")[zaehler].style.border="1px solid #b51d36"
				document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[zaehler].innerHTML="Ausgewähltes Zahlungsmittel";	
				name_karteninhaber=zahlungsmethoden[index].name;
				kreditkarten_nummer__=zahlungsmethoden[index].kreditkartennummer;
				ablaufdatum=zahlungsmethoden[index].ablaufmonat+" "+zahlungsmethoden[index].ablaufjahr;
				ausgewaehlt="ja";
			}
			else
			{
				document.getElementsByClassName("zahlungsmethoden_anzeigen")[zaehler].style.border="1px solid #e6e6e6";
				document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[zaehler].innerHTML="";
			}
			zaehler=zaehler+1
		}
		i=i+1;
	}

	if(ausgewaehlt=="")
	{
		/*		document.getElementsByClassName("zahlungsmethoden_anzeigen")[0].style.border="4px solid #FFD700"
				document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[0].innerHTML="Ausgewähltes Zahlungsmittel";	
				name_karteninhaber=zahlungsmethoden[index].name;
				kreditkarten_nummer__=zahlungsmethoden[index].kreditkartennummer;
				ablaufdatum=zahlungsmethoden[index].ablaufmonat+" "+zahlungsmethoden[index].ablaufjahr;		*/
		
	}
 }
 

 
 
 function kreditkarten_show(evt)
 {


	if(evt!="")
	{
		var theEvent = evt || window.event;
		var key = theEvent.keyCode || theEvent.which;
		key_=key;

		key = String.fromCharCode( key );
		var regex = /[0-9]|\./;
	}
	else
		key_=""



		var status=0;
		var i=0;
		while(i<=4)
		{
			
			if(document.getElementsByClassName("karten_css")[i].value=="")
				status=1;
			i=i+1;
		}
		
		if(status==0)
			document.getElementById("buttons_credit_card").innerHTML="";	
		
			
		document.getElementsByClassName("karten_css")[1].style.border="";	
		document.getElementsByClassName("karten_text_css")[1].style.color="";	
		
		if(document.getElementsByClassName("karten_css")[1].value!=string_ )
		{
			string_=document.getElementsByClassName("karten_css")[1].value;
			var max=document.getElementsByClassName("karten_css")[1].value.length;
			

			var number=document.getElementsByClassName("karten_css")[1].value;	
			number=number.replace("-","");
			number=number.replace("-","");
			number=number.replace("-","");
			
			document.getElementsByClassName("karten_css")[1].value=number;
			
			
			
			
			var max=document.getElementsByClassName("karten_css")[1].value.length;	

			var i=0;
			var j=0;
			while(i<=max-1)
			{
				var number=document.getElementsByClassName("karten_css")[1].value.charAt(i);
				
				if(isNaN(number)==false)
				{
					if(i==4 || i== 8 || i== 12 )
					{
						kreditkarten_nummer[j]="-";
						j=j+1;
						max=max+1;
						kreditkarten_nummer[j]=document.getElementsByClassName("karten_css")[1].value.charAt(i);

					}
					else
					{
						kreditkarten_nummer[j]=document.getElementsByClassName("karten_css")[1].value.charAt(i);
					}
				}
				i=i+1;
				j=j+1;

			}
			
			i=0
			
			document.getElementsByClassName("karten_css")[1].value="";
			string_="";
			while(i<=max-1)
			{
				
				document.getElementsByClassName("karten_css")[1].value=document.getElementsByClassName("karten_css")[1].value+kreditkarten_nummer[i];
				i=i+1;
				
			}
			
			string_=document.getElementsByClassName("karten_css")[1].value;
		}

		
		



	 
 }
 