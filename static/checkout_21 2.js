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
	   


function initiate_cart_fb(content_id_list,contents_list,value_)
{
    fbq('track', 'InitiateCheckout', {
      content_category: "Sets", 
      content_ids: content_id_list, 
      contents: contents_list, 
      value: value_,
      currency: 'EUR' 
    });  	

}

function show_VIP_AGB(status_)
{

		document.getElementById("headline_VIP_AGB").style.display=status_;
		document.getElementById("VIP_terms_conditions_checkbox_text").style.display=status_;	

		
		
}

function check_VIP_terms_and_conditions()
{

	if(document.getElementsByClassName ("VIP_terms_and_conditions")[0].innerHTML=="false")
		document.getElementById("VIP_terms_conditions_checkbox").checked=false;
	else
		document.getElementById("VIP_terms_conditions_checkbox").checked=true;

	if(document.getElementsByClassName ("VIP_terms_and_conditions")[0].innerHTML=="false" && shopping_type=="VIP")
		show_VIP_AGB("block")
	else
		show_VIP_AGB("none")	
	
	
	
}   
function show_VIP_terms_conditions()
{
	document.getElementById("alert_box_headline_VIP").innerHTML="VIP Programm FAQ";
	
	box="<b>Was ist das VIP Programm?</b><br>"
	box=box+"Unser VIP Programm bietet Dir viele attraktive Vorteile wie z.B. 10€ Rabatt auf Deine Unterwäsche zu jeder Zeit oder jedes 6. gekaufte Set ist umsonst. Unser VIP Programm gibt Dir jeden Monat die Möglichkeit Lingerie im Wert von 29,95€ zu kaufen - du kannst uns selbstverständlich jeden Monat mitteilen, wann du nicht einkaufen möchtest. Außerdem kannst Du unser VIP Programm jederzeit wieder verlasen.<br><br>"
	
	
	box=box+"<b>Muss ich jeden Monat etwas einkaufen?</b><br>"
	box=box+"Nein, musst Du nicht. Klick in Deinem Profil einfach auf 'Diesen Monat nicht einkaufen'. Du behälst alle Deine Vorteile, musst aber nichts kaufen.<br><br>"


	box=box+"<b>Was passiert, wenn ich vergesse im Profil 'Diesen Monat nicht einkaufen' auszuwählen?</b><br>"
	box=box+"Kein Problem. Wir erstatten Dir das Budget auch noch 90 Tage später zurück. Danach ist das Budget ein Store Credit, welchen Du für Deine Käufe nutzen kannst.<br><br>"
	
	box=box+"<b>Wie flexibel kann ich das VIP Programm verlassen?</b><br>"
	box=box+"Du kannst das VIP Modell jederzeit mit wenigen Klicks in Deinem Profil wieder deaktivieren. <br><br>"		
	document.getElementById("alert_box_body_VIP").innerHTML=box

	$('#alert_box_VIP_FAQ').modal('show');	
}


function show_klarna_agb()
 {

	
}


function zur_kasse()
{
	feedback="true"



	if(feedback=="true")
	{

		 button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")
		 

		$.ajax({
			type: "POST",
			url: "/zur_kasse/",
			dataType: "json",
			data: {"VIP":shopping_type },
			success: function(data) {	
				if(data=="successful")
					window.top.location.href = "/checkout/"
				else
					button_logo(1,"add_to_cart_text","add_to_cart_logo","add_to_cart")
			}
			
		}) 
	}
	
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



 function click_checkbox(id)
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
		
		
		box=box+"<div class='benachrichtigungen_text' onclick='unternehmen_check(this.id)' id='"+i+"'><input type='checkbox' class='checkbox_unternehmensangaben' style='cursor:pointer;float:left;'   id='checkbox_unternehmen'></input><div style='cursor:pointer;float:left;width:90%;margin-left:10px;margin-top:-2px;' id='"+i+"' onclick='click_checkbox(this.id)'>Zu einem Unternehmen liefern</div></div><br>"
	
		box=box+"<br><div class='address_unternehmensangaben_input_header' style='display:none'>Unternehmensangaben<br><input type='text' class='unternehmensdetails' id='unternehmensdetails_id' placeholder=''></input><br><br></div>";
				   
				   
		box=box+"<div style='width:100%;'>"
		
		box=box+"<div><div class='address_other_input_header' style='float:left;width:45%'>Anrede<br><select class='adresse_other' style='width:100%'";
		box=box+"type='text' onchange='felder_adresse_zuruecksetzen_adresse_other(0,"+i+")' value=''><option></option><option>Frau</option><option>Herr</option></select></div>"
	
		box=box+"<div class='address_other_input_header' style='float:right;width:45%'>Vorname<br><input class='adresse_other' style='width:100%'";
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen_adresse_other(1,"+i+")' onkeydown='felder_adresse_zuruecksetzen_adresse_other(1,"+i+")' value=''></div></div><br><br><br>"	
	
		box=box+"<div><div class='address_other_input_header' style='float:left;width:45%' >Nachname<br><input class='adresse_other' style='width:100%'";
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen_adresse_other(2,"+i+")' onkeydown='felder_adresse_zuruecksetzen_adresse_other(2,"+i+")'></input></div>"
		
		box=box+"<div class='address_mobilnummer_input_header' style='float:right;width:45%'>Mobilnummer<br><input class='adresse_mobilnummer' onkeypress='validate(event)' maxlength='20' style='width:100%'"
		box=box+" type='text' onkeyup='felder_adresse_zuruecksetzen_adresse_mobilnummer(0,"+i+")' onkeydown='felder_adresse_zuruecksetzen_adresse_mobilnummer(0,"+i+")'  ></input><div class='vorwahl'>+49</div></div><div class='eingabe_fehler' style='font-size:12px;color:#C80000;position:absolute;margin-top:10px;'></div></div></div><br>";
	
//onblur='check_mobilnummer()' 
		
		if(i==1)
			box=box+"<br><br><br></div>"
		else
			box=box+"</div><br>"
		i=i+1
	}
	box=box+"<div class='benachrichtigungen_text' onclick='click_checkbox_abweichende_lieferadresse()' ><input type='checkbox' class='checkbox_abweichende_lieferadresse' style='cursor:pointer;float:left;'   id='checkbox_abweichende_lieferadresse'></input><div style='cursor:pointer;float:left;width:90%;margin-left:10px;margin-top:-2px;' id='0' onclick='click_abweichende_lieferadresse_checkbox(this.id)'>Abweichende Lieferadresse</div></div><br><br>"
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

function page_load(index)
{



	if (index==0)
	{
		document.getElementsByClassName ("overlay")[0].style.visibility = "visible"
		document.getElementById("x-mask").style.opacity=0.3;

	}
	else
	{
		document.getElementsByClassName ("overlay")[0].style.visibility = "hidden"
		document.getElementById("x-mask").style.opacity=1.0;
		
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
	max=0
	j=0;
	if(document.getElementsByClassName ("checkbox_abweichende_lieferadresse")[0].checked==true)
		max=1;
		

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
	}
	
	return status;

}




function lieferkosten_aktualisieren()
{
		button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
		page_load(0);
		$.ajax({
			type: "GET",
			url: "/select_shopping_type/",
			dataType: "json",
			data: { "shopping_type":  shopping_type,"land":land},
			success: function(data)		{
	
					
					rebates=JSON.parse(data)
					
				$.ajax({
				type: "GET",
				url: "/warenkorb_abrufen/",
				dataType: "json",
				data: { "":""},
				success: function(data)		{						
			
						cart=JSON.parse(data)
						
									$.ajax({
									type: "GET",
									url: "/get_rabattname_from_request/",
									dataType: "json",
									data: { "":""},
									success: function(data)		{		
											page_load(1);
											button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
												
											document.getElementsByClassName("rabattname")[0].innerHTML=data	
						
											if(cart=="")
												window.top.location.href = "/"
						
											
						
											if (shopping_type=="Regular")
											{
												lingerie_anzeigen()
												bestelluebersicht("no");
												preise_laden("no")
												insert_cart_content_in_header();
						
											}
											else
											{
												lingerie_anzeigen()
												bestelluebersicht("yes");
												preise_laden("yes")
												insert_cart_content_in_header();
						
											}
								}
							})
					}
				})
			}
			})
						


			
	
}

function fuege_adressen_hinzu(i,hinzufuegen,existent_rechnungsadresse,existent_lieferadresse,standard_rechnungsadresse,standard_lieferadresse,index,wie_viele_adressen_checken)
{

	strasse=document.getElementsByClassName('adresse_input')[i].value;
		hausnummer=document.getElementsByClassName('adresse')[i*4].value
		stadt=document.getElementsByClassName('adresse')[i*4+1].value;
		plz=document.getElementsByClassName('adresse')[i*4+2].value;
		land=document.getElementsByClassName('adresse')[i*4+3].value;
		anrede=document.getElementsByClassName('adresse_other')[i*3].value
		vorname=document.getElementsByClassName('adresse_other')[i*3+1].value
		nachname=document.getElementsByClassName('adresse_other')[i*3+2].value
		mobilnummer=document.getElementsByClassName('adresse_mobilnummer')[i].value
		if(document.getElementsByClassName('address_unternehmensangaben_input_header')[i].style.display!="none")
			unternehmensdetails=document.getElementsByClassName('unternehmensdetails')[i].value
		else
			unternehmensdetails=""

		new_index_rechnungsadresse=existent_rechnungsadresse

		$.ajax({
			type: "POST",
			url: "/account_page/adresse_speichern/",
			dataType: "json",
			data: { "hinzufuegen":hinzufuegen,"indexnummer":index,"vorname": vorname,"nachname": nachname,"telefonnummer": mobilnummer,
			"strasse": strasse,"unternehmensdetails": unternehmensdetails,
			"stadt": stadt,"plz": plz,"standard":standard_rechnungsadresse,"land":land,"anrede":anrede,"hausnummer":hausnummer,"standard_lieferadresse":standard_lieferadresse},
			success: function(data) {
				if(i==0)
				{
					new_index_rechnungsadresse=data;
					new_index_lieferadresse=data;
				}
				else
					new_index_lieferadresse=data;
				if(i==wie_viele_adressen_checken)
				{
					

					
					$.ajax({
						type: "POST",
						url: "/get_adressbuch_daten/",
						dataType: "json",
						data: { "":""},
						success: function(data) {

								document.getElementsByClassName("adressbuch_daten")[0].innerHTML=data;
								adressbuch=JSON.parse(document.getElementsByClassName("adressbuch_daten")[0].innerHTML)

								show_maps(new_index_rechnungsadresse,new_index_lieferadresse)
						}
					})
				}
				else
					i=i+1;
				
			}
			
		})



}


function adressbuch_aktualisieren(wie_viele_adressen_checken,existent_rechnungsadresse,existent_lieferadresse)
{


//	button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
//	page_load(0);		
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
		fuege_adressen_hinzu(0,hinzufuegen,existent_rechnungsadresse,existent_lieferadresse,standard_rechnungsadresse,standard_lieferadresse,index,wie_viele_adressen_checken)
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
		fuege_adressen_hinzu(0,hinzufuegen,existent_rechnungsadresse,existent_lieferadresse,standard_rechnungsadresse,standard_lieferadresse,index,wie_viele_adressen_checken)



		standard_rechnungsadresse="nein"
		index=existent_lieferadresse
		if(existent_lieferadresse!="nein")
		{
			hinzufuegen=0;
			index=adressbuch[existent_lieferadresse].indexnummer;
		}
		else
			hinzufuegen=1;	
		fuege_adressen_hinzu(1,hinzufuegen,existent_rechnungsadresse,existent_lieferadresse,standard_rechnungsadresse,standard_lieferadresse,index,wie_viele_adressen_checken)
	}


	
}


function bestellen()
{	

	if(selected_zahlungsoption==4 && document.getElementById("agb_klarna_checkbox").checked==false)
		alert_userdata("KLARNA AGB AKZEPTIEREN","Bitte akzeptiere noch die AGB von Klarna. Dann kann Deine Bestellung abgeschickt werden.")
	else
	{
	
	
	
		if(document.getElementsByClassName("button_check")[0].style.display=="none" && (zahlungsmethoden!="" || zahlungsoption==1 || zahlungsoption==2 || zahlungsoption==4))
		{
			page_load(0);
			button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
			rabatt=(rabatt-credit_);
	
			if (document.getElementById("gutschein_input").value.toUpperCase()=="")
				rabattcode="";
			else
				rabattcode=document.getElementById("gutschein_input").value.toUpperCase()
	
	
			
			i=0;
			selected_credit_card=0;
	
			if(selected_zahlungsoption==0 || selected_zahlungsoption==3)
			{
				zaehler=0;
				while (i<=zahlungsmethoden.length-1)
				{
					if(zahlungsoption==zahlungsmethoden[i].zahlungsoption)
					{
						if (document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[zaehler].innerHTML!="")
						{
							selected_credit_card=document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[zaehler].id;
	
						}
						zaehler=zaehler+1;
					}
					i=i+1;
				}
			}
			else
				selected_credit_card=0
			
			
	
			
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

	
								$.ajax({
								type: "POST",
								url: "/bestellen_pre_test/",
								dataType: "json",
								data: { 'warenkorb_groesse':warenkorb_groesse,'warenkorb_gerichte':warenkorb_gerichte,'warenkorb_anzahl':warenkorb_anzahl,'zahlungsoption':zahlungsoption,'selected_zahlungsoption':selected_zahlungsoption,'preis':rebates[0].bestellung,'lieferkosten':rebates[0].lieferkosten,'rabatt':rebates[0].coupon, 'rabattcode':rebates[0].couponcode,'shopping_type':shopping_type,'braforfreecount':rebates[0].braforfreecount,'braforfreevalue':rebates[0].braforfreevalue,'storecredit_to_be_used':rebates[0].storecredit,'selected_credit_card':selected_credit_card,'strasse_rechnung':strasse_rechnung,'hausnummer_rechnung':hausnummer_rechnung,'stadt_rechnung':stadt_rechnung,'plz_rechnung':plz_rechnung,'land_rechnung':land_rechnung,'anrede_rechnung':anrede_rechnung,'vorname_rechnung':vorname_rechnung,'nachname_rechnung':nachname_rechnung,'telefonnummer_rechnung':telefonnummer_rechnung,'strasse_lieferadresse':strasse_lieferadresse,'hausnummer_lieferadresse':hausnummer_lieferadresse,'stadt_lieferadresse':stadt_lieferadresse,'plz_lieferadresse':plz_lieferadresse,'land_lieferadresse':land_lieferadresse,'anrede_lieferadresse':anrede_lieferadresse,'vorname_lieferadresse':vorname_lieferadresse,'nachname_lieferadresse':nachname_lieferadresse,'telefonnummer_lieferadresse':telefonnummer_lieferadresse,'unternehmensdetails_lieferadresse':unternehmensdetails_lieferadresse,'unternehmensdetails_rechnung':unternehmensdetails_rechnung },
								success: function(data) {		
									if (data=="not enough quantities")
									{
										alert_userdata_reload("SETS AUSVERKAUFT","Leider war jemand schneller und hat bereits Sets bestellt. Diese Seite wird neu geladen, damit du siehst, welche Produkte noch verfügbar sind.")
										page_load(1);
										button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
	
									}
									else						
										if (data=="already ordered")
										{
											window.top.location.href = "/" 
		
										}
										else
											if (data=="not ok")
											{
		
												alert_userdata_reload("AKTUALISIERTER WARENKORB","Dein Warenkorb wurde aktualisiert. Diese Seite wird neu geladen.")
												page_load(1);
												button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
											}
											else
											
												if (data=="kann nicht geworben werden")
												{
													alert_userdata_reload("GUTSCHEIN KANN NICHT EINGESETZT WERDEN","Deine eingebenen Daten wurden schon bei einem anderen User verwendet. Daher kann der Gutschein nicht eingesetzt werden. Diese Seite wird neu geladen. Danach kannst du den Warenkorb bestellen.")
													page_load(1);
													button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
												}
												else
													if (data=="not enough storecredit")
													{
														alert_userdata_reload("NICHT GENUG VIP GUTHABEN","Du hast nicht mehr ausreichend VIP Guthaben. Diese Seite wird neu geladen.")
														page_load(1);
														button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
													}
													else
														if (data=="not enough bra for free")
														{
															alert_userdata_reload("NICHT GENUG KOSTENLOSE SETS","Du hast nicht mehr ausreichend kostenlose VIP Sets. Diese Seite wird neu geladen.")
															page_load(1);
															button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
														}
														else
															if (data!="not ok")
															{
																


																if(selected_zahlungsoption==4)
																{
			
																	
																	if(data!="false")
																		window.top.location.href = "/account_page/bestellungen_ansehen/"+data
																	else
																	{
																		alert_userdata_reload("KLARNA NICHT MÖGLICH","Leider können wir Dir über Klarna keine Zahlung über Rechnung anbieten. Wähle doch eine andere Zahlungsmethode aus, um die Bestellung abzuschließen.")
																		page_load(1);
																		button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")																			
																	}
																	
																		
																}
																
																		
																if(selected_zahlungsoption==0 || selected_zahlungsoption==3)
																{
			
																	
																	if(data!="false")
																		window.top.location.href = "/account_page/bestellungen_ansehen/"+data
																		
																}
																	
																														
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
																				
									
									
										
							
				
								},
								error:function(){
									page_load(1);
	
								}
							});
							
	
		}
		else
		{
			document.getElementById("bestellen_ueberpruefen").style.display="block";
		}
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

function select_VIP()
{
		button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
		page_load(0);		
		shopping_type="VIP"
		$.ajax({
		type: "GET",
		url: "/select_shopping_type/",
		dataType: "json",
		data: { "shopping_type":  shopping_type,"land":land},
		success: function(data)		{
			rebates=JSON.parse(data)
			
				$.ajax({
				type: "GET",
				url: "/warenkorb_abrufen/",
				dataType: "json",
				data: { "":""},
				success: function(data)		{						
				
						cart=JSON.parse(data)
						$.ajax({
						type: "GET",
						url: "/get_rabattname_from_request/",
						dataType: "json",
						data: { "":""},
						success: function(data)		{		
								page_load(1);
								button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
								document.getElementsByClassName("rabattname")[0].innerHTML=data	
								
								box=""
									box=box+"<div style='width:100%;line-height:15px;float:left;margin-bottom:20px;'>"
								box=box+"<br><img style='float:left' src='/static/shopping_bag.png' width='25' height='20'/><div style='margin-top:0px;margin-left:30px;'>Kaufe Lingerie für mindestens <b>19,95€ pro Monat</b></div>"
								box=box+"<br><img style='float:left' src='/static/shopping_bag_no.png' width='25' height='20'/><div style='margin-top:0px;margin-left:30px;'><b>Keine Verpflichtung</b>: Wenn Du in einem Monat keine Lingerie kaufen möchtest, melde Dich einfach bis zum 10. eines Monats in Deinem Kundenkonto an und klicke „diesen Monat nicht einkaufen“</div>"
								box=box+"<br><img style='float:left' src='/static/discount_icon.png' width='25' height='20'/><div style='margin-top:0px;margin-left:30px;'><b>Rabatt von 10€ </b>auf jedes Set</div>"
								box=box+"<br><img style='float:left' src='/static/gift.png' width='25' height='20'/><div style='margin-top:0px;margin-left:30px;'>Du bekommst ein <b>kostenloses Set</b>, wenn du sechs Sets gekauft</div>"
								box=box+"<br><img style='float:left' src='/static/free_shipping.png' width='25' height='20'/><div style='margin-top:0px;margin-left:30px;'><b>Kostenloser Versand und Rückversand</b></div>"
								
								box=box+"</div>"
							
								document.getElementsByClassName("VIP_selection")[0].innerHTML =box;
								document.getElementsByClassName("shopping_selection")[0].style.backgroundColor ="#CC3366";
								document.getElementsByClassName("shopping_selection")[0].style.color ="#ffffff";
								document.getElementsByClassName("shopping_selection")[1].style.backgroundColor ="#ffffff";
								document.getElementsByClassName("shopping_selection")[1].style.color ="#4E4E4E";
								bestelluebersicht("yes")
								preise_laden("yes")
								show_VIP_AGB("block")
						}
					})		
				}
			})				
		}
	})



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
					block =block+"<b><p style='color:#CC3366'> €"+replace_dot_comma((cart[i].pricesubscription+cart[i].rabatt)*cart[i].anzahl)+"</p></b>";
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
			if(cart_page!="ja")
				select_only_repeat_payment_methods();
		}
		else
		{
			if(cart[i].productgroup!="geschenkkarten")
			{

				if(cart[i].rabatt!="")
				{
					block="<b><p style='text-decoration: line-through'>Regulär €"+replace_dot_comma((cart[i].priceregular)*cart[i].anzahl)+"</p></b>";
					block =block+"<b><p style='color:#CC3366'>  €"+replace_dot_comma((cart[i].priceregular+cart[i].rabatt)*cart[i].anzahl)+"</p></b>";
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

			if(cart_page!="ja")
				select_all_payment_methods();
			
		}


		
		i=i+1;
	}
	

	
}


function select_payasyougo()
{
		button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
		page_load(0);	

								shopping_type="Regular"

					$.ajax({
					type: "GET",
					url: "/select_shopping_type/",
					dataType: "json",
					data: { "shopping_type":  shopping_type,"land":land},
					success: function(data)		{
						rebates=JSON.parse(data)

						$.ajax({
						type: "GET",
						url: "/warenkorb_abrufen/",
						dataType: "json",
						data: { "":""},
						success: function(data)		{						
						
									cart=JSON.parse(data)

									$.ajax({
									type: "GET",
									url: "/get_rabattname_from_request/",
									dataType: "json",
									data: { "":""},
									success: function(data)		{		
											page_load(1);
											button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
																				
	
											document.getElementsByClassName("rabattname")[0].innerHTML=data	

											
				
											box=""
												box=box+"<div style='width:100%;line-height:15px;float:left;margin-bottom:20px;'>"
											box=box+"<br><img style='float:left' src='/static/shopping_bag_no.png' width='25' height='20'/><div style='margin-top:0px;margin-left:30px;'><b>Keine Verpflichtung</b>: Kaufe ein, wann du willst</div>"
											box=box+"<br><img style='float:left' src='/static/free_shipping.png' width='25' height='20'/><div style='margin-top:0px;margin-left:30px;'><b>Kostenloser Versand und Rückversand</b></div>"
											
											box=box+"</div>"
				
											document.getElementsByClassName("VIP_selection")[0].innerHTML =box;
											document.getElementsByClassName("shopping_selection")[1].style.backgroundColor ="#CC3366";
											document.getElementsByClassName("shopping_selection")[1].style.color ="#ffffff";
											document.getElementsByClassName("shopping_selection")[0].style.backgroundColor ="#ffffff";
											document.getElementsByClassName("shopping_selection")[0].style.color ="#4E4E4E";
											bestelluebersicht("no")
											preise_laden("no")
											show_VIP_AGB("none")
										}
								})
						}
				})

			}
	})

}

	function VIP_selection_laden(VIP,shoppingtype,cart_page_)
{
	

		button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
		page_load(0);	
	cart_page=cart_page_;

	if(cart_page=="ja")
		land="Deutschland"
	shopping_type=shoppingtype
					$.ajax({
					type: "GET",
					url: "/select_shopping_type/",
					dataType: "json",
					data: { "shopping_type":  shopping_type,"land":land},
					success: function(data)		{
						rebates=JSON.parse(data)
						
						$.ajax({
						type: "GET",
						url: "/warenkorb_abrufen/",
						dataType: "json",
						data: { "":""},
						success: function(data)		{						
						
									cart=JSON.parse(data)
									
									$.ajax({
									type: "GET",
									url: "/get_rabattname_from_request/",
									dataType: "json",
									data: { "":""},
									success: function(data)		{		
											document.getElementsByClassName("rabattname")[0].innerHTML=data	;
											button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
											page_load(1);	
											
											if(VIP=="false" && cart_page=="ja")
											{
				
													box="<br>"
													box=box+"<div class='shopping_selection'><div style='margin-left:5px;margin-top:2px;margin-bottom:2px;' onclick='select_VIP()'><b>VIP Club</b><br>Set ab €19.95</div></div><div class='shopping_selection'><div style='margin-left:5px;margin-top:2px;margin-bottom:2px;' onclick='select_payasyougo()'><b>Ohne VIP</b><br>Set ab €29.95</div></div><div class='VIP_selection'></div>"
													
													if(window.innerWidth>=768)	
													{
														document.getElementsByClassName("VIP")[1].innerHTML =box;
														document.getElementsByClassName("headline")[0].style.display="none";
														document.getElementsByClassName("VIP")[0].style.display="none";
													}
													else
													{
														document.getElementsByClassName("VIP")[0].innerHTML =box;
														document.getElementsByClassName("headline")[4].style.display="none";
														document.getElementsByClassName("VIP")[1].style.display="none";
													}		
												
													
				
										
												if(shopping_type=="VIP")
													select_VIP()
												else
													select_payasyougo()
												
											}
											else
											{
												if(shopping_type=="VIP")
												{
													bestelluebersicht("yes")
													preise_laden("yes")
													shopping_type="VIP"
												}
												else
												{
													bestelluebersicht("no")
													preise_laden("no")
													shopping_type="Regular"									
												}
				
												document.getElementsByClassName("VIP")[1].style.display="none";
												document.getElementsByClassName("headline")[0].style.display="none";
												document.getElementsByClassName("VIP")[0].style.display="none";
				
												document.getElementById("VIP_block").style.display ="none";

								
								

								
										}
									}
							})
						}
				})
					
				}
				})

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

		uebersicht=uebersicht+"<div class='rabattname' style='float:left;'>"+document.getElementsByClassName("rabattname")[0].innerHTML+":</div><div class='rabattname' style='float:right;'>"+replace_dot_comma(-rebates[0].coupon)+" EUR</div><br>";	

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
		
		uebersicht=uebersicht+"<div style='float:left;width:30px;'>Freundschafts-\nwerbung:</div><div style='float:right;'><br>"+replace_dot_comma(parseFloat(-rebates[0].credit))+" EUR</div><br><br>";	
		
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
		document.getElementById("gutschein_button_id_text").innerHTML="Abbrechen";
		document.getElementById("gutschein_input").disabled=true;

		document.getElementById("gutschein_input").value  =gutscheincode;

		document.getElementById("gutschein_button_id").style.backgroundColor="#808080";

		
	}


	
	
}






function gutschein_einloesen()
{
			if(document.getElementById("gutschein_button_id_text").innerHTML!="Abbrechen")
		{
			
			button_logo("0","gutschein_button_id_text","gutschein_button_id_logo","gutschein_button_id")
			button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	

							$.ajax({
								type: "GET",
								url: "/gutschein_einloesen/",
								dataType: "json",
								data: { "gutscheincode":  document.getElementById("gutschein_input").value.toUpperCase(),"art":"einloesen" },
								success: function(data) {

					
									if (data!= "error" && data!= "")
									{	
										gutscheincode=document.getElementById("gutschein_input").value.toUpperCase()
										document.getElementById("gutschein_button_id").style.backgroundColor="#808080";

										document.getElementById("gutschein_button_id_text").innerHTML="Abbrechen";
										document.getElementById("gutschein_input").disabled=true;
										
										$.ajax({
										type: "GET",
										url: "/select_shopping_type/",
										dataType: "json",
										data: { "shopping_type":  shopping_type,"land":land},
										success: function(data)		{
												rebates=JSON.parse(data)	

												$.ajax({
												type: "GET",
												url: "/warenkorb_abrufen/",
												dataType: "json",
												data: { "":""},
												success: function(data)		{		
												cart=JSON.parse(data)
												
													$.ajax({
													type: "GET",
													url: "/get_rabattname_from_request/",
													dataType: "json",
													data: { "":""},
													success: function(data)		{		
															document.getElementsByClassName("rabattname")[0].innerHTML=data	

															button_logo("1","gutschein_button_id_text","gutschein_button_id_logo","gutschein_button_id")
															button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
																				
					
															if (shopping_type=="Regular")
															{
																bestelluebersicht("no");
																preise_laden("no")
															}
															else
															{
																bestelluebersicht("yes");
																preise_laden("yes")
															}
														}
													})
												}
											})
										}
										})
										
									}
									else
									{
										
																				$.ajax({
										type: "GET",
										url: "/select_shopping_type/",
										dataType: "json",
										data: { "shopping_type":  shopping_type,"land":land},
										success: function(data)		{
											
											rebates=JSON.parse(data)		


												$.ajax({
												type: "GET",
												url: "/warenkorb_abrufen/",
												dataType: "json",
												data: { "":""},
												success: function(data)		{		
														cart=JSON.parse(data)
														
														$.ajax({
														type: "GET",
														url: "/get_rabattname_from_request/",
														dataType: "json",
														data: { "":""},
														success: function(data)		{		
																document.getElementsByClassName("rabattname")[0].innerHTML=data	
															button_logo("1","gutschein_button_id_text","gutschein_button_id_logo","gutschein_button_id")
															button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
																if (shopping_type=="Regular")
																{
																	bestelluebersicht("no");
																	preise_laden("no")
																}
																else
																{
																	bestelluebersicht("yes");
																	preise_laden("yes")
																}
																alert_userdata("GUTSCHEIN NICHT GÜTLIG","Dieser Gutschein-Code ist leider nicht gültig")
														}
													})														
												}
											})
									
										}
										})
										
										
									}
										
							
					
								},	error: function(data)
									{
											button_logo("1","gutschein_button_id_text","gutschein_button_id_logo","gutschein_button_id")	
											button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")									
									}
							});
							
					
							
							

						
						}

		else
		{
			gutschein_code_reset();
	
		}
}

function gutschein_code_reset()
{
	
	button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	
	page_load(0);	

	$.ajax({
			type: "GET",
			url: "/gutschein_einloesen/",
			dataType: "json",
			data: { "gutscheincode":  document.getElementById("gutschein_input").value.toUpperCase(),"art":"aufloesen" },
			success: function(data) {



				document.getElementById("gutschein_button_id").style.backgroundColor="#CC3366";
				document.getElementById("gutschein_button_id_text").innerHTML="Überprüfen";
				document.getElementById("gutschein_input").disabled=false;
				document.getElementById("gutschein_input").value="";

				$.ajax({
				type: "GET",
				url: "/select_shopping_type/",
				dataType: "json",
				data: { "shopping_type":  shopping_type,"land":land},
				success: function(data)		{
							
							rebates=JSON.parse(data);	
							$.ajax({
							type: "GET",
							url: "/warenkorb_abrufen/",
							dataType: "json",
							data: { "":""},
							success: function(data)		{						
								
								cart=JSON.parse(data)							
								
									$.ajax({
									type: "GET",
									url: "/get_rabattname_from_request/",
									dataType: "json",
									data: { "":""},
									success: function(data)		{		
											button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")
												
											document.getElementsByClassName("rabattname")[0].innerHTML=data	
								
											page_load(1);	
											
											rabatt=rebates[0].coupon;
											gutscheincode="";
										
											if (shopping_type=="Regular")
											{
												bestelluebersicht("no");
												preise_laden("no")
											}
											else
											{
												bestelluebersicht("yes");
												preise_laden("yes")
											}
									}
								})
							}
						})
					}
				})
			}
		})


	
	
}


 function gutscheincode_schliessen() {

	document.getElementsByClassName ("overlay")[0].style.visibility = "hidden"
	document.getElementById("x-mask").style.opacity="1.0";
	enableScroll();
}



function promo_code()
{

	
	if (document.getElementById("gutschein_input").style.display =="block")
	{
		document.getElementById("gutschein_input").style.display ="none";
		document.getElementsByClassName("promo_code")[0].innerHTML="<b>+</b> Gutschein-Code hinzufügen";
		document.getElementById("gutschein_button_id").style.display ="none";
		gutschein_code_reset();
		
	}
	else
	{
				document.getElementById("gutschein_input").value=""
				document.getElementById("gutschein_input").style.display ="block";
				document.getElementsByClassName("promo_code")[0].innerHTML="<b>-</b> Gutschein-Code entfernen";
				document.getElementById("gutschein_button_id").style.display ="block";
		
		
	}
	
	
}


function unternehmen_check(id)
{

	if (document.getElementsByClassName("address_unternehmensangaben_input_header")[id].style.display =="block")
		document.getElementsByClassName("address_unternehmensangaben_input_header")[id].style.display ="none";
	else
		document.getElementsByClassName("address_unternehmensangaben_input_header")[id].style.display ="block";
}


 function warenkorb_ermitteln()
 {
	cart=JSON.parse(document.getElementsByClassName("warenkorb_daten")[0].innerHTML)
	rebates=JSON.parse(document.getElementsByClassName("rebates_daten")[0].innerHTML)
	 var i=0;
	 cart_gesamt=0;

	 while (i<=cart.length-1)
	 {
		 	 
		 if (parseInt(cart[i].anzahl)>0)
			cart_gesamt=cart_gesamt+parseInt(cart[i].anzahl);
		
		i=i+1;
	 }
	 
	if (cart_gesamt!=0)
		document.getElementsByClassName("cart_text")[0].innerHTML=cart_gesamt;
	else
		document.getElementsByClassName("cart_text")[0].innerHTML="";
		
 }
 



function email_check(email)
{
	if (email=="not ok")
			$('#login').modal({backdrop: 'static', keyboard: false})  

}


  $('#login').on('shown.bs.modal', function () {
			$('#alert_box_reload').modal('hidden');
 

});




  function alert_userdata_reload(content1,content2)
 {	 
	
	document.getElementById("alert_box_reload_headline").innerHTML=content1;
	document.getElementById("alert_box_reload_body").innerHTML=content2;
		$('#alert_box_reload').modal('show');

 }
 
 
 
$("#close_register").on("click", function() {

page_load(0);

  logo_click();
   })
 
  $('#alert_box_reload').on('hide.bs.modal', function () {

location.reload();

});
 
 
 

 
 
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
 

 
window.onload = function () {
page_load(1);
    if (typeof history.pushState === "function") {

        history.pushState("jibberish", null, null);
        window.onpopstate = function () {
        	
            history.pushState('newjibberish', null, null);

           location.reload();
            // Handle the back (or forward) buttons here
            // Will NOT handle refresh, use onbeforeunload for this.
        };
    }
    else {
        var ignoreHashChange = true;
        window.onhashchange = function () {
            if (!ignoreHashChange) {
                ignoreHashChange = true;

                window.location.hash = Math.random();
                // Detect and redirect change here
                // Works in older FF and IE9
                // * it does mess with your hash symbol (anchor?) pound sign
                // delimiter on the end of the URL
            }
            else {
                ignoreHashChange = false;   
            }
        };
    }

    if(cart_page!="ja")
    {
    	zahlung_click(document.getElementsByClassName("selected_zahlungsoption")[0].innerHTML);
    }
}
 
 function others_laden(_gutscheincode)
 { 
	first_height=0
 	gutscheincode=_gutscheincode;
	max=2;
	document.getElementsByClassName("cart")[0].style.backgroundImage="url('/static/Cart-open.png')";
	selected_zahlungsoption=document.getElementsByClassName("selected_zahlungsoption")[0].innerHTML


	
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
	 
	 
 
 function gericht_preis_ermitteln(name)
 {
	 
	 j=0;
	 while (j<=gerichte_menu.length-1)
	 {
		 if (gerichte_menu[j].name==name)
			 return gerichte_menu[j].preis
		 
		 j=j+1;
		 
	 }
	 
	 
 }
 
 
  function gericht_bild_ermitteln(name)
 {
	 
	 j=0;
	 while (j<=gerichte_menu.length-1)
	 {
		 if (gerichte_menu[j].name==name)
			 return gerichte_menu[j].picture_link_small
		 
		 j=j+1;
		 
	 }
	 
	 
 }
 


 
 function lingerie_anzeigen()
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
			 		
			 		
					box=box+"<div style='float:left;font-size:14px;width:100%;'><div style='width:100%;height:125px;float:left;'><div style='cursor:pointer' onclick='gerichte_detail("+i+")'><img src='"+cart[i].picture+"' class='image_order'/><div class='style'><b>"+cart[i].style+"</b><br><div style='float:left;font-size:12px;'>"+cart[i].bhgroesse+"</div><br><div style='float:left;font-size:12px;'>"+cart[i].slipgroesse+"</div></div></div>";
	
					box=box+"<div class='product_price'><b>Regulär €"+replace_dot_comma(cart[i].priceregular)+"</b></div><br>";

					
					
					box=box+"<div class='select_size' ><div class='anzahl' style='margin-top:5px;'>Anzahl</div><select class='select_anzahl' onchange='change_cart("+i+")' >";
					
					var w=0;
					
					
					min_1=10;
					

					while(w<=Math.min(min_1,10))
					{
						box=box+"<option>"+w+"</option>";
						w=w+1;
					}
					
					
					box=box+"</select><br><div class='entfernen' style='float:right;cursor:pointer;font-size:12px;color:#CC3366;margin-left:10px;' id='entfernen"+i+"' onclick='entfernen("+i+")'>Entfernen</div>	</div></div><br><br><br><br><br>";


			
					
				
				 i=i+1;	
			 
			 }
			 
			 
			 box=box+"<br><br><br><br>";
			 


	

		 

		 
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
	 

	 window.top.location.href = "/overview/"+cart[link_].link1+"/"+cart[link_].style+"/";; 	 
	 
 }
 

 function change_cart(clicked_id)
 {	


	if(cart[clicked_id].anzahl!=document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex)
	{


		
		cart[clicked_id].anzahl=document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex;
		page_load(0);
		button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")	

		$.ajax({
			type: "GET",
			url: "/add/",
			dataType: "json",
			data: { "add_or_erase":"change","anzahl":cart[clicked_id].anzahl,"gerichtname": cart[clicked_id].style,"stylecode": cart[clicked_id].stylecode,"colorcode": cart[clicked_id].colorcode,"bh_groesse": cart[clicked_id].bhgroesse,"slip_groesse": cart[clicked_id].slipgroesse,"regular_price":cart[clicked_id].priceregular,"subscription_price":cart[clicked_id].pricesubscription,"slip_groesse_2":"","productgroup":cart[clicked_id].productgroup   },
			success: function(data) {		


				if (data=="not ok")
						alert_userdata_reload("ZUSÄTZLICHE MENGEN NICHT VERFÜGBAR","Da war ein anderer Kunde schneller. Zusätzliche Mengen sind von dem Gericht nicht mehr verfügbar. Diese Seite wird neu geladen.")
				else
				{
					cart=JSON.parse(data)
								$.ajax({
			type: "GET",
			url: "/select_shopping_type/",
			dataType: "json",
			data: { "shopping_type":  shopping_type,"land":land},
			success: function(data)		{

					rebates=JSON.parse(data)
					
				$.ajax({
				type: "GET",
				url: "/warenkorb_abrufen/",
				dataType: "json",
				data: { "":""},
				success: function(data)		{						
				
						cart=JSON.parse(data)					
									$.ajax({
									type: "GET",
									url: "/get_rabattname_from_request/",
									dataType: "json",
									data: { "":""},
									success: function(data)		{		
											page_load(1);
											button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
												
											document.getElementsByClassName("rabattname")[0].innerHTML=data	
											if(cart=="")
												window.top.location.href = "/"
	
						
	
											if (shopping_type=="Regular")
											{
												lingerie_anzeigen()
												bestelluebersicht("no");
												preise_laden("no")
												insert_cart_content_in_header();
						
											}
											else
											{
												lingerie_anzeigen()
												bestelluebersicht("yes");
												preise_laden("yes")
												insert_cart_content_in_header();
						
											}
							}
						})
					}
				})
			}
			})
						

				}
				



			},	error: function(data)
				{
					page_load(1);
					button_logo("1","add_to_cart_text","add_to_cart_logo","add_to_cart")	
				}
		});


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
	
	 
	document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex=0;
	
	change_cart(clicked_id);

	 
	 
 }
 


 

 
 
  function zahlung_click(clicked_id)
 {
	 selected_zahlungsoption=clicked_id;
	zahlungsoption=clicked_id;
	document.getElementById("agb_klarna").style.display="none";
	var i=0;
	
	var maxim= document.getElementsByClassName("zahlung");
	while(i<=4)
	{

		if(i==clicked_id)
		{
			
			maxim[i].style.borderBottom="1px solid #e65c00";
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
 }
 
 
  function rechnung_laden()
 {
 	document.getElementById("agb_klarna").style.display="block";



 	document.getElementById("kreditkarten").innerHTML="<br><div style='line-height:20px;' ><b>In 14 Tagen zahlen</b><br><br>Heute bestellen, aber erst in 14 Tagen bezahlen. Es entstehen Dir keine Zusatzkosten.</div><br>";
 	
 	document.getElementById("agb_klarna_text").innerHTML="Mit der Übermittlung der für die Abwicklung der gewählten Klarna–Zahlungsmethode und einer Identitäts– und Bonitätsprüfung erforderlichen Daten an Klarna bin ich einverstanden. Meine <span id='consentxx' style='text-decoration:underline'></span> kann ich jederzeit mit Wirkung für die Zukunft widerrufen. Es gelten die <a href='/hello/agb/' style='text-decoration:underline'>AGB</a> des Händlers. "
 	
 	new Klarna.Terms.Consent({  
    el: 'consentxx',
    eid: '11054',
    locale: 'de_de',
    type: 'desktop'
});



 }
 
 
 function paypal_laden()
 {



 	document.getElementById("kreditkarten").innerHTML="<br><div style='line-height:20px;' ><b>Mit Paypal zahlen</b><br><br>Nachdem du bestellt hast, wirst du im nächsten Schritt zu Paypal weitergeleitet. Nach der Bezahlung hast, gelangst du zur Bestellbestätigung.</div><br>";
 	



 }
 
  
  function sofortueberweisung_laden()
 {

 	document.getElementById("kreditkarten").innerHTML="<br><div style='line-height:20px;'><b>Mit sofortüberweisung zahlen</b><br><br>Nachdem du bestellt hast, wirst du im nächsten Schritt zu sofortüberweisung.de weitergeleitet. Nach der Bezahlung hast, gelangst du zur Bestellbestätigung.</div><br>";
 }
 
 
 
 
 
 
 
 function lastschrift_anzeigen()
 {
		 var box="<div id='kartendetails_maske'> <div class='karten_text_css' >Kontoinhaber<br><input class='karten_css' onkeyup='felder_zuruecksetzen_sepa(0)' onkeydown='felder_zuruecksetzen_sepa(0)' type='text'></input></div><br><div class='karten_text_css' >IBAN<br><input class='karten_css' placeholder='' type='text' onkeyup='felder_zuruecksetzen_sepa(1)' onkeydown='felder_zuruecksetzen_sepa(1)' ></input></div>";

		box=box+"</select></div><div class='karten_text_css' >BIC<br><input class='karten_css' onkeyup='felder_zuruecksetzen_sepa(2)' onkeydown='felder_zuruecksetzen_sepa(2)' type='text' ></input></div></div>";
		box=box+"<br><br><br><br><br><div style='float:right;margin-bottom:40px;margin-top:20px;width:100%;'>"
		

		
		box=box+"<form id='payment-form' action='#' method='POST'>"
		box=box+"<input class='amount-int' type='hidden' value='0001' />"
		box=box+"<input class='currency' type='hidden' value='EUR' />"
		box=box+"<input class='iban' type='hidden'  value='4111111111111111'/>"
		box=box+"<input class='bic' type='hidden' value='123' />"
		box=box+"<input class='accountholder' type='hidden'   value='asdasd' />"
		box=box+"</form>"


		if(shopping_type=="VIP")
			box=box+"<div class='benachrichtigungen_text' style='display:none' ><input type='checkbox'  checked=true style='cursor:pointer;float:left;'  id='zahlungsdaten_checkbox' ></input><div style='cursor:pointer;float:left;width:90%;margin-left:10px;margin-top:-2px;'  onclick='zahlungsdaten_speichern()'>Speichern für weitere Käufe</div></div><br>"
		else
			box=box+"<div class='benachrichtigungen_text' ><input type='checkbox'  checked=true style='cursor:pointer;float:left;'  id='zahlungsdaten_checkbox' ></input><div style='cursor:pointer;float:left;width:90%;margin-left:10px;margin-top:-2px;'  onclick='zahlungsdaten_speichern()'>Speichern für weitere Käufe</div></div><br>"
			
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
		 
		 var jahr_anzahl=5;
		 var jahr_start=2016;
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
		box=box+"<input class='card-amount-int' type='hidden' value='0001' />"
		box=box+"<input class='card-currency' type='hidden' value='EUR' />"
		box=box+"<input class='card-number' type='hidden'  value='4111111111111111'/>"
		box=box+"<input class='card-cvc' type='hidden' value='123' />"
		box=box+"<input class='card-holdername' type='hidden'   value='asdasd' />"
		box=box+"<input class='card-expiry-month' type='hidden'  value='03' />"
		box=box+"<input class='card-expiry-year' type='hidden'  value='2018' />"
		box=box+"</form>"

		if(shopping_type=="VIP")
			box=box+"<div class='benachrichtigungen_text' style='display:none' ><input type='checkbox'  checked=true style='cursor:pointer;float:left;'  id='zahlungsdaten_checkbox' ></input><div style='cursor:pointer;float:left;width:90%;margin-left:10px;margin-top:-2px;'  onclick='zahlungsdaten_speichern()'>Speichern für weitere Käufe</div></div><br>"
		else
			box=box+"<div class='benachrichtigungen_text' ><input type='checkbox'  checked=true style='cursor:pointer;float:left;'  id='zahlungsdaten_checkbox' ></input><div style='cursor:pointer;float:left;width:90%;margin-left:10px;margin-top:-2px;'  onclick='zahlungsdaten_speichern()'>Speichern für weitere Käufe</div></div><br>"
		
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
 

 
 
window.onscroll = function () {
	height=document.body.offsetHeight
	if(first_height==0)
		first_height=document.body.offsetHeight


	if(window.innerWidth>=768)	
	{
		if(document.getElementsByClassName("sidebar_checkout")[0].clientHeight+document.body.scrollTop<height+document.getElementsByClassName("header_bottom_all")[0].clientHeight)
		{
	
			document.getElementsByClassName("sidebar_checkout")[0].style.position="-webkit-sticky";
			document.getElementsByClassName("sidebar_checkout")[0].style.marginTop="0px"

	
		}
		else
		{
			document.getElementsByClassName("sidebar_checkout")[0].style.position=""

				document.getElementsByClassName("sidebar_checkout")[0].style.marginTop=first_height-document.getElementsByClassName("sidebar_checkout")[0].clientHeight-50+"px"

		}
	}
	


};
 
 

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
			standard_lieferadresse=i;		
		i=i+1;
	}

	if(standard_rechnungsadresse==-1)
		standard_rechnungsadresse=standard_lieferadresse

	
	if(standard_rechnungsadresse!=-1)
		show_maps(standard_rechnungsadresse,standard_lieferadresse)
	else
		adresse_anzeigen("nein","nein");
}

//		adresse_in_form_laden(max(0,adressbuch_standard),"")

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
	if((index_lieferadresse!="" & index_rechungsadresse!="") && index_lieferadresse!=index_rechungsadresse)
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
			
		paymill.createToken({
			
		  number: $('.card-number').val(),  // required, ohne Leerzeichen und Bindestriche
		  exp_month: $('.card-expiry-month').val(),   // required
		  exp_year: $('.card-expiry-year').val(),     // required, vierstellig z.B. "2016"
		  cvc: $('.card-cvc').val(),                  // required
		  amount_int: $('.card-amount-int').val(),    // required, integer, z.B. "15" fÃ¼r 0,15 Euro
		  currency: $('.card-currency').val(),    // required, ISO 4217 z.B. "EUR" od. "GBP"
		  cardholder: $('.card-holdername').val() // optional
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
    // Shows the error above the form
    		page_load(1);
			button_logo("1","kreditkarte_check_button_id_text","kreditkarte_check_button_id_logo","kreditkarte_check_button_id")	
			alert_userdata("KREDITKARTE WIRD NICHT UNTERSTÜTZT","Es werden nur Master- oder Visa-Kreditkarten unterstützt. Bitte gebe eine andere Kreditkarte ein.")
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

 		if(zahlungsmethoden=="")
			standard_="ja";
		else
			standard_="nein";

				$.ajax({
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
			alert_userdata("KREDITKARTE WIRD NICHT UNTERSTÜTZT","Es werden nur Master- oder Visa-Kreditkarten unterstützt. Bitte gebe eine andere Kreditkarte ein.")
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
				box=box+"<div style='margin-right:20px;color:#000000;float:right;'><b><img src='/static/mastercard.png'  width='50' height='35' ></b></div></div>";
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
				document.getElementsByClassName("zahlungsmethoden_anzeigen")[zaehler].style.border="4px solid #FFD700"
				document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[zaehler].innerHTML="Ausgewähltes Zahlungsmittel";	
				name_karteninhaber=zahlungsmethoden[index].name;
				kreditkarten_nummer__=zahlungsmethoden[index].kreditkartennummer;
				ablaufdatum=zahlungsmethoden[index].ablaufmonat+" "+zahlungsmethoden[index].ablaufjahr;
				ausgewaehlt="ja";
			}
			else
			{
				document.getElementsByClassName("zahlungsmethoden_anzeigen")[zaehler].style.border="4px solid #e6e6e6";
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


	if(key_==48 || key_==49 || key_==50 || key_==51 || key_==52 || key_==53 || key_==54 || key_==55 || key_==56 || key_==57 || key_==9 || key_=="" | key_==8 || key_==17 || key_==91 || key_==67 || key_==86)
	
	{

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
	else
	{
		if(theEvent.keyCode!=8)
		{
			theEvent.returnValue = false;theEvent.returnValue = false;
			if(theEvent.preventDefault) theEvent.preventDefault();
		}
		
		
		
	}


	 
 }
 