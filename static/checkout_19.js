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
		document.getElementById("VIP_terms_conditions_checkbox").style.display=status_;
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
	document.getElementById("alert_box_headline").innerHTML="AGB VIP Programm";
	document.getElementById("alert_box_body").innerHTML="XYZ";
	$('#alert_box').modal('show');	
}

function click_VIP_terms_conditions_checkbox()
{
	document.getElementById("VIP_terms_conditions_checkbox_text").style.color="#808080"	
}
function zur_kasse()
{
	feedback="true"

	
	if(document.getElementById("VIP_terms_conditions_checkbox").checked==false && shopping_type=="VIP" && document.getElementById("VIP_block").style.display=="block")
	{
					document.getElementById("VIP_terms_conditions_checkbox_text").style.color="red"
					alert_userdata("VIP AGB","Bitte akzeptiere noch unsere AGB für die VIP Mitgliedschaft.")			
					feedback="false"
		
	}

	if(feedback=="true")
	{

		 button_logo("0","add_to_cart_text","add_to_cart_logo","add_to_cart")

		$.ajax({
			type: "POST",
			url: "/zur_kasse/",
			dataType: "json",
			data: { "VIP_terms_and_conditions":"true","VIP":shopping_type },
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

function adresse_uebertragen(strasse_, nummer_, plz_, stadt_, vorname_, nachname_, telefonnummer_, unternehmensdetails_,lieferhinweise_,land_)
{
	

	strasse=strasse_
	nummer=nummer_

	plz=plz_
	stadt=stadt_
	vorname=vorname_
	nachname=nachname_
	telefonnummer=telefonnummer_
	unternehmensdetails=unternehmensdetails_
	lieferhinweise=lieferhinweise_
	land=land_
	
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




function adresse_anzeigen(strasse_, nummer_, plz_, stadt_, vorname_, nachname_, telefonnummer_, unternehmensdetails_,adresse_neu_,land_)
{


	adresse_neu=adresse_neu_;
	
	if (strasse_=="")
	{
		var box="<div class='adressdetails'><div id='locationField'><div class='address_text' style='width:100%;' >Adresse<br><input class='adresse_input' id='strasse' placeholder='Adresse eingeben'";
		box=box+"onFocus='geolocate()'  type='text' style='width:100%;' onkeyup='felder_adresse_zuruecksetzen(0)' onkeydown='felder_adresse_zuruecksetzen(0)'></input></div></div><br>";
		box=box+"<div ><div class='address_text' style='float:left;width:50%'>Stadt<br><input class='adresse' id='locality' placeholder=''";
		box=box+"type='text' style='width:100%' onkeyup='felder_adresse_zuruecksetzen(1)' onkeydown='felder_adresse_zuruecksetzen(1)'></input></div><div class='address_text' style='float:right;width:40%;'>Postleitzahl<br><input class='adresse' id='postal_code' placeholder=''";
		box=box+"type='text' onkeypress='validate(event)' maxlength='5' style='width:100%;' onkeyup='felder_adresse_zuruecksetzen(2)' onkeydown='felder_adresse_zuruecksetzen(2)'></div></div><br><br><br><br>"
		box=box+"<div class='land_text' style='width:100%;' >Land<br><input class='land_input' id='land' placeholder='Land eingeben'";
		box=box+"type='text' style='width:100%;' onkeyup='felder_adresse_zuruecksetzen(-1)' onkeydown='felder_adresse_zuruecksetzen(-1)'></input></div></div><br>";
		
		
		box=box+"<div class='benachrichtigungen_text' onclick='unternehmen_check()' ><input type='checkbox' class='checkbox_unternehmensangaben' style='cursor:pointer;float:left;'   id='checkbox_unternehmen'></input><div style='cursor:pointer;float:left;width:90%;margin-left:10px;margin-top:6px;' id='0' onclick='click_checkbox(this.id)'>Zu einem Unternehmen liefern</div></div><br>"
		
		
	//	box=box+"<input type='checkbox' id='checkbox_unternehmen' onclick='unternehmen_check()'>Zu einem Unternehmen liefern</input><br>";
		box=box+"<br><div class='unternehmensdetails'>Unternehmensangaben<br><input type='text' class='unternehmensdetails' id='unternehmensdetails_id' placeholder=''></input><br></div>";
				   
		box=box+"<div style='width:100%;'><div class='address_text'>Vorname<br><input class='adresse' id='street_number' style='width:90%'";
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(3)' onkeydown='felder_adresse_zuruecksetzen(3)'></input></div><div class='address_text' >Nachname<br><input class='adresse' id='nachname' style='width:90%'";
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(4)' onkeydown='felder_adresse_zuruecksetzen(4)'></input></div><div class='address_mobilnummer' >Mobilnummer<br><input class='adresse' id='street_number' onkeypress='validate(event)' maxlength='20'"
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(5)' onkeydown='felder_adresse_zuruecksetzen(5)' style='padding-left:45px;' onblur='check_mobilnummer()' ></input><div class='vorwahl'>+49</div><div class='eingabe_fehler' style='font-size:12px;color:#C80000;position:absolute;margin-top:10px;'></div></div></div><br></div>";
		document.getElementsByClassName("button_check")[0].style.display="block";
		
	}
	else
	{
		
		
		var box="<div class='adressdetails'><div id='locationField'><div class='address_text' style='width:100%;' >Adresse<br><input class='adresse_input' id='strasse' placeholder='Adresse eingeben' value='"+strasse_+"'";
		box=box+"onFocus='geolocate()'  type='text' style='width:100%;' onkeyup='felder_adresse_zuruecksetzen(0)' onkeydown='felder_adresse_zuruecksetzen(0)'></input></div></div><br>";
		box=box+"<div ><div class='address_text' style='float:left;width:60%'>Stadt<br><input class='adresse' id='locality' placeholder='' value='"+stadt_+"'";
		box=box+"type='text' style='width:100%' onkeyup='felder_adresse_zuruecksetzen(1)' onkeydown='felder_adresse_zuruecksetzen(1)'></input></div><div class='address_text' style='float:right;width:30%;'>Postleitzahl<br><input class='adresse' id='postal_code' placeholder=''";
		box=box+"type='text' onkeypress='validate(event)' maxlength='5' style='width:100%;' onkeyup='felder_adresse_zuruecksetzen(2)' onkeydown='felder_adresse_zuruecksetzen(2)' value='"+plz_+"'></div></div><br><br><br><br><br>";
		box=box+"<div class='land_text' style='width:100%;' >Land<br><input class='land_input' id='land' placeholder='Land eingeben'";
		box=box+"type='text' style='width:100%;' onkeyup='felder_adresse_zuruecksetzen(-1)' onkeydown='felder_adresse_zuruecksetzen(-1)'></input></div></div><br><br><br><br><br>";		

		box=box+"<input type='checkbox' id='checkbox_unternehmen' onclick='unternehmen_check()'>Zu einem Unternehmen liefern</input><br>";
		box=box+"<br><div class='unternehmensdetails'>Unternehmensangaben<br><input class='unternehmensdetails' id='unternehmensdetails_id' placeholder='' value='"+unternehmensdetails_+"'></input><br></div>";
				   
		box=box+"<div style='width:100%;'><div class='address_text'>Vorname<br><input class='adresse' id='street_number' style='width:90%'";
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(3)' onkeydown='felder_adresse_zuruecksetzen(3)' value='"+vorname_+"'></input></div><div class='address_text' >Nachname<br><input class='adresse' id='nachname' style='width:90%'";
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(4)' onkeydown='felder_adresse_zuruecksetzen(4)' value='"+nachname_+"'></input></div><div class='address_mobilnummer'>Mobilnummer<br><input class='adresse' id='street_number' onkeypress='validate(event)' maxlength='20'"
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(5)' onkeydown='felder_adresse_zuruecksetzen(5)' value='"+telefonnummer_+"' style='padding-left:35px;width:130%;' onblur='check_mobilnummer()' ></input><div class='vorwahl'>+49</div><div class='eingabe_fehler' style='font-size:12px;color:#C80000;position:absolute;margin-top:10px;'></div></div></div><br></div>";
		document.getElementsByClassName("button_check")[0].style.display="block";
		
		
		


		
	}
	

	document.getElementById("total_address").innerHTML=box;
	
	
	if (unternehmensdetails_=="")
	{
		document.getElementsByClassName("unternehmensdetails")[0].style.display="none";
		document.getElementsByClassName("unternehmensdetails")[1].style.display="none";
		document.getElementById("checkbox_unternehmen").checked=false;
		
	}
	else
	{
		document.getElementById("checkbox_unternehmen").checked=true;
		document.getElementsByClassName("unternehmensdetails")[0].style.display="block";
		document.getElementsByClassName("unternehmensdetails")[1].style.display="block";
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
		document.getElementById("x-mask").style.opacity=0.4;

	}
	else
	{
		document.getElementsByClassName ("overlay")[0].style.visibility = "hidden"
		document.getElementById("x-mask").style.opacity=1.0;
	}
		

	

	

}



function check_address()
{


	var status=0;

	if(document.getElementsByClassName("adresse_input")[0].value=="")
	{
		
		document.getElementById("buttons_address_text").innerHTML="Bitte alle benötigten Felder ausfüllen.";
		document.getElementsByClassName("adresse_input")[0].style.border="1px solid red";	
		document.getElementsByClassName("address_text")[0].style.color="red";		
		status=1;
		
	}	
	

	var i=0;
	while(i<=3)
	{

		if(document.getElementsByClassName("adresse")[i].value=="")
		{

			document.getElementById("buttons_address_text").innerHTML="Bitte alle benötigten Felder ausfüllen.";

			document.getElementsByClassName("adresse")[i].style.border="1px solid red";	

			document.getElementsByClassName("address_text")[i+1].style.color="red";		




			status=1;
	
		}	

		i=i+1;
		

		


	}

	if(document.getElementsByClassName("adresse")[4].value=="")
	{
		document.getElementsByClassName("adresse")[4].style.border="1px solid red";	
		document.getElementsByClassName("address_mobilnummer")[0].style.color="red";	
			document.getElementById("buttons_address_text").innerHTML="Bitte alle benötigten Felder ausfüllen.";
			status=1;
			
	}

	if(document.getElementsByClassName("land_input")[0].value=="")
	{
		document.getElementsByClassName("land_input")[0].style.border="1px solid red";	
		document.getElementsByClassName("land_text")[0].style.color="red";	
			document.getElementById("buttons_address_text").innerHTML="Bitte alle benötigten Felder ausfüllen.";
			status=1;
			
	}

	if(document.getElementsByClassName("unternehmensdetails")[0].style.display=="block" && document.getElementsByClassName("unternehmensdetails")[1].value=="")
	{
		
					document.getElementById("buttons_address_text").innerHTML="Bitte alle benötigten Felder ausfüllen.";
			document.getElementsByClassName("unternehmensdetails")[1].style.border="1px solid red";	
			document.getElementsByClassName("unternehmensdetails")[0].style.color="red";	
			status=1;

	}

	
	if(status==0)
	{

		
		if(adresse_neu!="")
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
					alert_userdata("MOBILNUMMER NICHT KORREKT","Die eingegebene Mobilnummer ist nicht gültig. Bitte gib eine andere Mobilnummer an.")
				}
				else
				{


					document.getElementsByClassName("adresse")[4].value=data
					document.getElementById("buttons_address_text").innerHTML=""
					var strasse=document.getElementsByClassName("adresse_input")[0].value;
		
					var plz=document.getElementsByClassName("adresse")[1].value;
					var stadt=document.getElementsByClassName("adresse")[0].value;
					var land=document.getElementsByClassName("land_input")[0].value;
					var vorname=document.getElementsByClassName("adresse")[2].value;
					var nachname=document.getElementsByClassName("adresse")[3].value;
					var telefonnummer=document.getElementsByClassName("adresse")[4].value;
					lieferhinweise="";
					var unternehmensdetails=document.getElementById("unternehmensdetails_id").value

					initMap(strasse,plz,stadt,vorname,nachname,telefonnummer,unternehmensdetails,lieferhinweise,land);
					
				}
	
			}
			});
		
		
			


		}


		
	}
	
	if(document.getElementsByClassName("button_check")[0].style.display!="none")
	{
		var i=0;
		while(i<=3)
		{
			
			if(document.getElementsByClassName("adresse")[i].value=="")
			{

				document.getElementById("buttons_address_text").innerHTML="Bitte alle benötigten Felder ausfüllen.";
				document.getElementsByClassName("adresse")[i].style.border="1px solid red";	
				document.getElementsByClassName("address_text")[i+1].style.color="red";		
				status=1;
				
			}	
			i=i+1;
		}
	}
	
	if(document.getElementsByClassName("button_check")[0].style.display=="none" && document.getElementsByClassName("button_check")[1].style.display=="none")
		document.getElementsByClassName("button_check")[0].style.display="none";

}




function lieferkosten_aktualisieren()
{

		$.ajax({
			type: "GET",
			url: "/select_shopping_type/",
			dataType: "json",
			data: { "shopping_type":  shopping_type,"land":land},
			success: function(data)		{
					page_load(1);
					rebates=JSON.parse(data)
					if(cart=="")
						window.top.location.href = "/"

					

					if (shopping_type=="Regular")
					{
						lingerie_anzeigen()
						bestelluebersicht(rebates[0].coupon,"no");
						preise_laden("no")
						insert_cart_content_in_header();

					}
					else
					{
						lingerie_anzeigen()
						bestelluebersicht(rebates[0].coupon,"yes");
						preise_laden("yes")
						insert_cart_content_in_header();

					}

			}
			})
						


			
	
}




function adressbuch_aktualisieren()
{

	if(adresse_neu!=-2 )
	{			
		if(adresse_neu==-1)
			hinzufuegen=1;
		else
			hinzufuegen=0;
		
		if (adressbuch.length==0)
		{
			standard_="ja"
			index_=0;
		}
		else
		{
			if(adresse_neu==-1)
			{
				standard_="nein"
				index_=adressbuch.length
			}
			else
			{
				standard_="nein"
				index_=adresse_neu
				
				
			}
		}


			strasse__=strasse
			plz__=plz
			stadt__=stadt
			unternehmensdetails__=unternehmensdetails
			vorname__=vorname
			nachname__=nachname
			lieferhinweise__=lieferhinweise
			telefonnummer__=telefonnummer
			land__=land

		$.ajax({
		type: "POST",
		url: "/account_page/adresse_speichern/",
		dataType: "json",
		data: { "hinzufuegen":hinzufuegen,"indexnummer":index_,"vorname": vorname,"nachname": nachname,"telefonnummer": telefonnummer,
		"adresse": strasse,"unternehmensdetails": unternehmensdetails,
		"stadt": stadt,"plz": plz,"lieferdetails": lieferhinweise,"standard":standard_,"land":land},
		success: function(data) {
			strasse=strasse__
			plz=plz__
			stadt=stadt__
			unternehmensdetails=unternehmensdetails__
			vorname=vorname__
			nachname=nachname__
			lieferhinweise=lieferhinweise__
			telefonnummer=telefonnummer__
			land=land__

			adresse_neu=-2
			document.getElementsByClassName("adressbuch_daten")[0].innerHTML=data;

			adressbuch=JSON.parse(document.getElementsByClassName("adressbuch_daten")[0].innerHTML)

			i=0;
			zaehler=0;
			while(i<=adressbuch.length-1)
			{	
				if(strasse__==adressbuch[i].adresse)
					zaehler=i;
				i=i+1;
			}

			

	//		var huelle=adressbuch[0]
	   
	//		adressbuch[0]=adressbuch[index_];
	//		adressbuch[index_]=huelle;
			



			var strasse=document.getElementsByClassName("adresse_input")[0].value;
			var land=document.getElementsByClassName("land_input")[0].value;
			var plz=document.getElementsByClassName("adresse")[1].value;

			var stadt=document.getElementsByClassName("adresse")[0].value;


			var vorname=document.getElementsByClassName("adresse")[2].value;

			var nachname=document.getElementsByClassName("adresse")[3].value;

			var telefonnummer=document.getElementsByClassName("adresse")[4].value;

			var unternehmensdetails=document.getElementById("unternehmensdetails_id").value


			adresse_wechseln(zaehler)
			initMap(strasse,plz,stadt,vorname,nachname,telefonnummer,unternehmensdetails,lieferhinweise,land);
			

			
			
			
			
			
			
			


		},
				error: function(data)
				{
		
				}
		});
		
		
	}
	
}



  
  document.onclick = function adresse_feld() {
  
	  var adresse= strasse+"<br>"+plz+" "+stadt;

	  if(output_adresse_clicked==0 && output_adresse_show==1)
	  {

		 var box="<div class='output_adresse' style='background-color:#f2f2f2;' onclick='adresse_bearbeiten()'><div style='float:left;margin-left:10px;margin-Top:10px'>"+adresse+"</div></div>";
		document.getElementsByClassName("side3")[0].innerHTML=box;
		
		document.getElementsByClassName("side3")[0].style.backgroundColor="#f2f2f2";
		output_adresse_show=0;
		
	  }
	  output_adresse_clicked=0;  

  }
  
  
  

  function button_logo(index,text_area,logo_area,button_)
 {

	 if (index==0)
	 {
		document.getElementById(""+text_area+"").style.display="none";

		document.getElementById(""+logo_area+"").style.display="block";

		document.getElementById(""+button_+"").style.pointerEvents = 'none';

	 }
	 else
	 {
		document.getElementById(""+text_area+"").style.display="block";
		document.getElementById(""+logo_area+"").style.display="none";	
		document.getElementById(""+button_+"").style.pointerEvents = 'auto';
		
		 
	 }
	 
 }
 


function bestellen()
{	

	if(document.getElementsByClassName("button_check")[0].style.display=="none" && (zahlungsmethoden!="" || zahlungsoption==1 || zahlungsoption==2 || zahlungsoption==3))
	{
		page_load(0);
		rabatt=(rabatt-credit_);

		if (document.getElementById("gutschein_input").value.toUpperCase()=="")
			rabattcode="";
		else
			rabattcode=document.getElementById("gutschein_input").value.toUpperCase()
		var lieferdetails=document.getElementById("lieferdetails_textarea").value;
		
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

							$.ajax({
							type: "POST",
							url: "/bestellen_pre_test/",
							dataType: "json",
							data: { 'warenkorb_groesse':warenkorb_groesse,'warenkorb_gerichte':warenkorb_gerichte,'warenkorb_anzahl':warenkorb_anzahl,'adresse':strasse,'stadt':stadt,'plz':plz,'unternehmensdetails':unternehmensdetails,'vorname':vorname,'nachname':nachname,'telefonnummer':telefonnummer,'lieferdetails':lieferdetails,'zahlungsoption':zahlungsoption,'selected_zahlungsoption':selected_zahlungsoption,'preis':rebates[0].bestellung,'lieferkosten':rebates[0].lieferkosten,'rabatt':rebates[0].coupon, 'rabattcode':rebates[0].couponcode,'shopping_type':shopping_type,'braforfreecount':rebates[0].braforfreecount,'braforfreevalue':rebates[0].braforfreevalue,'storecredit_to_be_used':rebates[0].storecredit,'selected_credit_card':selected_credit_card,"land":land },
							success: function(data) {		
								if (data=="not enough quantities")
								{
									alert_userdata_reload("SETS AUSVERKAUFT","Leider war jemand schneller und hat bereits Sets bestellt. Diese Seite wird neu geladen, damit du siehst, welche Produkte noch verfügbar sind.")
									page_load(1);

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
										}
										else
										
											if (data=="kann nicht geworben werden")
											{
												alert_userdata_reload("GUTSCHEIN KANN NICHT EINGESETZT WERDEN","Deine eingebenen Daten wurden schon bei einem anderen User verwendet. Daher kann der Gutschein nicht eingesetzt werden. Diese Seite wird neu geladen. Danach kannst du den Warenkorb bestellen.")
												page_load(1);
											}
											else
												if (data=="not enough storecredit")
												{
													alert_userdata_reload("NICHT GENUG VIP GUTHABEN","Du hast nicht mehr ausreichend VIP Guthaben. Diese Seite wird neu geladen.")
													page_load(1);
												}
												else
													if (data=="not enough bra for free")
													{
														alert_userdata_reload("NICHT GENUG KOSTENLOSE SETS","Du hast nicht mehr ausreichend kostenlose VIP Sets. Diese Seite wird neu geladen.")
														page_load(1);
													}
													else
														if (data!="not ok")
														{
															
		
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
							button_logo(1,"button_text","button_logo","button_cart_large")}
							
						});
						

	}
	else
	{
		document.getElementById("bestellen_ueberpruefen").style.display="block";
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
		shopping_type="VIP"
		$.ajax({
		type: "GET",
		url: "/select_shopping_type/",
		dataType: "json",
		data: { "shopping_type":  shopping_type,"land":land},
		success: function(data)		{
				rebates=JSON.parse(data)
				box=""
					box=box+"<div style='width:100%;line-height:15px;float:left;margin-bottom:20px;'>"
				box=box+"<br><img style='float:left' src='/static/shopping_bag.png' width='25' height='20'/><div style='margin-top:0px;margin-left:30px;'>Kaufe Lingerie für mindestens <b>19,95€ pro Monat</b></div>"
				box=box+"<br><img style='float:left' src='/static/shopping_bag_no.png' width='25' height='20'/><div style='margin-top:0px;margin-left:30px;'><b>Keine Verpflichtung</b>: Wenn du in einem Monat keine Lingerie kaufen möchtest, sag uns bis zum 10. eines Monats Bescheid</div>"
				box=box+"<br><img style='float:left' src='/static/discount_icon.png' width='25' height='20'/><div style='margin-top:0px;margin-left:30px;'><b>Rabatt von 10€ </b>auf jedes Set</div>"
				box=box+"<br><img style='float:left' src='/static/gift.png' width='25' height='20'/><div style='margin-top:0px;margin-left:30px;'>Du bekommst ein <b>kostenloses Set</b>, wenn du sechs Sets gekauft</div>"
				box=box+"<br><img style='float:left' src='/static/free_shipping.png' width='25' height='20'/><div style='margin-top:0px;margin-left:30px;'><b>Kostenloser Versand und Rückversand</b></div>"
				
				box=box+"</div>"
			
				document.getElementsByClassName("VIP_selection")[0].innerHTML =box;
				document.getElementsByClassName("shopping_selection")[0].style.backgroundColor ="#CC3366";
				document.getElementsByClassName("shopping_selection")[0].style.color ="#ffffff";
				document.getElementsByClassName("shopping_selection")[1].style.backgroundColor ="#ffffff";
				document.getElementsByClassName("shopping_selection")[1].style.color ="#4E4E4E";
				bestelluebersicht(rebates[0].coupon,"yes")
				preise_laden("yes")
				show_VIP_AGB("block")
				
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
			document.getElementsByClassName("product_price")[i].innerHTML ="<b>VIP €"+replace_dot_comma((cart[i].pricesubscription)*cart[i].anzahl)+"</b>"
			preis=preis+cart[i].pricesubscription*cart[i].anzahl;
			if(cart_page!="ja")
				select_only_repeat_payment_methods();
		}
		else
		{

			document.getElementsByClassName("product_price")[i].innerHTML ="<b>Regulär €"+replace_dot_comma((cart[i].priceregular)*cart[i].anzahl)+"</b>";

			preis=preis+cart[i].priceregular*cart[i].anzahl;

			if(cart_page!="ja")
				select_all_payment_methods();
			
		}


		
		i=i+1;
	}
	

	
}


function select_payasyougo()
{

								shopping_type="Regular"

					$.ajax({
					type: "GET",
					url: "/select_shopping_type/",
					dataType: "json",
					data: { "shopping_type":  shopping_type,"land":land},
					success: function(data)		{
							rebates=JSON.parse(data)

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
							bestelluebersicht(rebates[0].coupon,"no")
							preise_laden("no")
							show_VIP_AGB("none")



			}
	})

}

	function VIP_selection_laden(VIP,shoppingtype,cart_page_)
{
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
									bestelluebersicht(rebates[0].coupon,"yes")
									preise_laden("yes")
									shopping_type="VIP"
								}
								else
								{
									bestelluebersicht(rebates[0].coupon,"no")
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






function bestelluebersicht(rabatt__,subscription)
{

	rabatt=rabatt__	

	
	preis=preis_aufrufen(subscription)
	
	bra_for_free_rebate=bra_for_free_rebate_aufrufen(subscription)

	credit_=Math.min(parseFloat(credit),preis+rebates[0].lieferkosten+rabatt-bra_for_free_rebate)
	storecredit_to_be_used=Math.min(preis+rebates[0].lieferkosten+rabatt-credit_-bra_for_free_rebate,storecredit)

	var gesamt=preis+lieferkosten+rabatt-credit_-bra_for_free_rebate-storecredit_to_be_used;
	
	


	
	preis_=	replace_dot_comma(preis);
	rabatt_=	replace_dot_comma(rabatt);

	preis_gesamt=	replace_dot_comma(gesamt);
	
	lieferkosten_=replace_dot_comma(lieferkosten);

	var maxim= document.getElementsByClassName("bestellung");

	var uebersicht="<div style='float:left;'>Bestellung:</div><div style='float:right;'>"+replace_dot_comma(rebates[0].bestellung)+" EUR</div><br>";
	if(rebates[0].lieferkosten!="0")
		uebersicht=uebersicht+"<div style='float:left;'>Lieferkosten:</div><div style='float:right;'>"+replace_dot_comma(rebates[0].lieferkosten)+" EUR</div><br>";
	else
		uebersicht=uebersicht+"<div style='float:left;'>Lieferkosten:</div><div style='float:right;'>KOSTENLOS</div><br>";
		
		
	if(parseFloat(rebates[0].coupon)!=0)
	{

		uebersicht=uebersicht+"<div style='float:left;'>Rabatt:</div><div style='float:right;'>"+replace_dot_comma(-rebates[0].coupon)+" EUR</div><br>";	

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
		document.getElementsByClassName("gutschein_button_text")[0].innerHTML="Abbrechen";
		document.getElementById("gutschein_input").disabled=true;
		document.getElementById("gutschein_input").value  =gutscheincode;
		document.getElementById("gutschein_button_id").style.backgroundColor="#808080";

		
	}


	
	
}






function gutschein_einloesen()
{
			if(document.getElementsByClassName("gutschein_button_text")[0].innerHTML!="Abbrechen")
		{

					
							$.ajax({
								type: "GET",
								url: "/gutschein_einloesen/",
								dataType: "json",
								data: { "gutscheincode":  document.getElementById("gutschein_input").value.toUpperCase(),"art":"einloesen" },
								success: function(data) {

								
								
					
									if (data!= "")
									{	
										gutscheincode=document.getElementById("gutschein_input").value.toUpperCase()
										document.getElementById("gutschein_button_id").style.backgroundColor="#808080";
										button_logo(1,"gutschein_button_text","gutschein_button_logo","gutschein_button")
										document.getElementsByClassName("gutschein_button_text")[0].innerHTML="Abbrechen";
										document.getElementById("gutschein_input").disabled=true;
										
										$.ajax({
										type: "GET",
										url: "/select_shopping_type/",
										dataType: "json",
										data: { "shopping_type":  shopping_type,"land":land},
										success: function(data)		{
												rebates=JSON.parse(data)				

										if (shopping_type=="Regular")
											bestelluebersicht(rebates[0].coupon,"no");
										else
											bestelluebersicht(rebates[0].coupon,"yes");
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
														if (shopping_type=="Regular")
															bestelluebersicht(rebates[0].coupon,"no");
														else
															bestelluebersicht(rebates[0].coupon,"yes");
														rabatt_=0
														alert_userdata("GUTSCHEIN NICHT GÜTLIG","Dieser Gutschein-Code ist leider nicht gültig")
									
										}
										})
										
										
									}
										
							
					
								},	error: function(data)
									{
										
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

	$.ajax({
			type: "GET",
			url: "/gutschein_einloesen/",
			dataType: "json",
			data: { "gutscheincode":  document.getElementById("gutschein_input").value.toUpperCase(),"art":"aufloesen" },
			success: function(data) {

				document.getElementById("gutschein_button_id").style.backgroundColor="#CC3366";
				document.getElementsByClassName("gutschein_button_text")[0].innerHTML="Überprüfen";
				document.getElementById("gutschein_input").disabled=false;
				document.getElementById("gutschein_input").value="";
					hilf = data.split(",");


				$.ajax({
				type: "GET",
				url: "/select_shopping_type/",
				dataType: "json",
				data: { "shopping_type":  shopping_type,"land":land},
				success: function(data)		{
						rebates=JSON.parse(data)			

									rabatt=rebates[0].coupon
							gutscheincode=""
								if (shopping_type=="Regular")
									bestelluebersicht(rebates[0].coupon,"no");
								else
									bestelluebersicht(rebates[0].coupon,"yes");
			
							
							//promo_code()
							button_logo(1,"gutschein_button_text","gutschein_button_logo","gutschein_button")
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
		button_logo(1,"gutschein_button_text","gutschein_button_logo","gutschein_button")
		
	}
	else
	{
				document.getElementById("gutschein_input").value=""
				document.getElementById("gutschein_input").style.display ="block";
				document.getElementsByClassName("promo_code")[0].innerHTML="<b>-</b> Gutschein-Code entfernen";
				document.getElementById("gutschein_button_id").style.display ="block";
		
		
	}
	
	
}


function unternehmen_check()
{
	if (document.getElementsByClassName("unternehmensdetails")[0].style.display =="block")
	{
		document.getElementsByClassName("unternehmensdetails")[0].style.display ="none";
		document.getElementsByClassName("unternehmensdetails")[1].style.display ="none";
				document.getElementsByClassName("unternehmensdetails")[1].value="";

	}
	else
	{
		document.getElementsByClassName("unternehmensdetails")[0].style.display ="block";
		document.getElementsByClassName("unternehmensdetails")[1].style.display ="block";
		document.getElementsByClassName("unternehmensdetails")[1].value="";

	}
}


 function warenkorb_ermitteln(daten_2,cart_gesamt,storecredit_)
 {
	 

	cart=JSON.parse(document.getElementsByClassName("warenkorb_daten")[0].innerHTML)



	 var i=0;
	 cart_gesamt=0;
	 credit=daten_2;
	 storecredit=storecredit_;
	 


	 
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
 
 
  function lingerie_ermitteln()
 {
 	

 	
//	lingerie_selection=JSON.parse(document.getElementsByClassName("lingerie_selection")[0].innerHTML)

}


function email_check(email)
{

	if (email=="not ok")
	{
			$('#login').modal({backdrop: 'static', keyboard: false})  
			
	
	
		
		
	/*	
		
		box=""
		box=box+"<img class='schliessen_alert' src='/static/x.png' width='15' onclick='alert_click_schliessen_();' height='15'/></img><br><b><p style='text-align:center'>EMAIL ADRESSE FESTLEGEN</p></b>";
		box=box+"<p style='margin-left:10px;margin-right:10px;font-size:14px;'>Bevor der Bestellprozess abgeschlossen werden kann, muss zunächst eine E-Mail Adresse hinterlegt werden</p>";
		
		
		box=box+"<input class='email_eingabe' type='text' style='width:200px;margin-left:10px;'  placeholder='E-Mail Adresse'  />";
		box=box+"<div class='button_alert_email' onclick='register_email()'>Eintragen</div><p id='email_fehler' style='font-size:10px;color:#C80000;margin-left:10px;' ></p>";

		document.getElementsByClassName("modal_medium")[0].innerHTML=box
		document.getElementsByClassName("modal_medium")[0].style.visibility = "visible"

		document.getElementsByClassName ("overlay")[0].style.visibility = "visible"
		document.getElementById("x-mask").style.opacity="0.4";*/
		
	}
	
	
	
	
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
    	zahlung_click(0);
}
 
 function others_laden(gutscheinwert,_gutscheincode,bra_for_free_,selected_zahlungsoption_)
 { 
	first_height=0
 	gutscheincode=_gutscheincode;
 	rabatt=parseFloat(gutscheinwert);
 	bra_for_free=bra_for_free_

	max=2;

	
	//bestelluebersicht(rabatt,"yes")
	
	document.getElementsByClassName("cart")[0].style.backgroundImage="url('/static/Cart-open.png')";
	


	selected_zahlungsoption=selected_zahlungsoption_


	
	var i=0;
	while(i<=15)
	{	
		kreditkarten_nummer[i]=new Array;
		i=i+1;
	}
	kreditkarten_nummer_stelle=0;

	
	//
	

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
 

 
 
 

function compareLastColumn(a, b) {
    if (a[2] === b[2]) {
        return 0;
    }
    else {
        return (a[2] < b[2]) ? -1 : 1;
    }
}




 

 
 function lingerie_anzeigen()
 {
	 
		 
	 //setInterval(check_timing_availability, 5000)

	
	i=0;
	j=0;
	lieferkosten=0;
	
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
			 
			 
			 box=box+"<br><br>";
			 


	

		 

		 
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
 
 
 
  function verfuegbarkeits_check(i)
 {
	 
	return (parseInt(gerichte_menu[i].gerichte_uebrig)-parseInt(gerichte_menu[i].warenkorb_menge));
 }
  
 function change_cart(clicked_id)
 {	


	if(cart[clicked_id].anzahl!=document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex)
	{


		
		cart[clicked_id].anzahl=document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex;
		page_load(0);

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
					page_load(1);
					rebates=JSON.parse(data)
					if(cart=="")
						window.top.location.href = "/"

					

					if (shopping_type=="Regular")
					{
						lingerie_anzeigen()
						bestelluebersicht(rebates[0].coupon,"no");
						preise_laden("no")
						insert_cart_content_in_header();

					}
					else
					{
						lingerie_anzeigen()
						bestelluebersicht(rebates[0].coupon,"yes");
						preise_laden("yes")
						insert_cart_content_in_header();

					}

			}
			})
						

				}
				



			},	error: function(data)
				{
					page_load(1);
				}
		});
		

		 
			

		//select_options();*/

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




 
 function select_options()
 {
	 
	 var i=0;
	 
	 while(i<=max)
	 {
		document.getElementsByClassName("select_anzahl")[i].selectedIndex=cart[i].style;
		 i=i+1;
		 
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
	var i=0;
	
	var maxim= document.getElementsByClassName("zahlung");
	while(i<=3)
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
 }
 
 
 function paypal_laden()
 {



 	document.getElementById("kreditkarten").innerHTML="<br><div style='line-height:20px;' onclick='actions.payment.create()'><b>Mit Paypal zahlen</b><br><br>Nachdem du bestellt hast, wirst du im nächsten Schritt zu Paypal weitergeleitet. Nach der Bezahlung hast, gelangst du zur Bestellbestätigung.</div>";
 	



 }
 
  
  function sofortueberweisung_laden()
 {

 	document.getElementById("kreditkarten").innerHTML="<br><div style='line-height:20px;'><b>Mit sofortüberweisung zahlen</b><br><br>Nachdem du bestellt hast, wirst du im nächsten Schritt zu sofortüberweisung.de weitergeleitet. Nach der Bezahlung hast, gelangst du zur Bestellbestätigung.</div>";
 }
 
 
 
 
 function lastschrift_anzeigen()
 {
		 var box="<div id='kartendetails_maske'> <div class='karten_text_css' >Kontoinhaber<br><input class='karten_css' onkeyup='felder_zuruecksetzen(0)' onkeydown='felder_zuruecksetzen(0)' type='text'></input></div><br><div class='karten_text_css' >IBAN<br><input class='karten_css' placeholder='' type='text' ></input></div>";

		box=box+"</select></div><div class='karten_text_css' >BIC<br><input class='karten_css' onkeyup='felder_zuruecksetzen(1)' onkeydown='felder_zuruecksetzen(1)' type='text' ></input></div></div>";
		box=box+"<br><br><br><br><br><div style='float:right;margin-bottom:40px;margin-top:40px;width:100%;'>"
		

		
		box=box+"<form id='payment-form' action='#' method='POST'>"
		box=box+"<input class='amount-int' type='hidden' value='0001' />"
		box=box+"<input class='currency' type='hidden' value='EUR' />"
		box=box+"<input class='iban' type='hidden'  value='4111111111111111'/>"
		box=box+"<input class='bic' type='hidden' value='123' />"
		box=box+"<input class='accountholder' type='hidden'   value='asdasd' />"
		box=box+"</form>"

					
		box=box+"<div  class='kreditkarte_check_button'  onclick='lastschrift_check()' >Überprüfen</div>"
		box=box+"<div  class='kreditkarte_check_button_abbrechen'  onclick='lastschrift_abbrechen()' >Abbrechen</div>"
		box=box+"</div><br><br><br><div id='buttons_credit_card' style='float:right;color:red;font-weight:bold;'></div> ";
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
		 
		
		
		 
		 var box="<div id='kartendetails_maske'> <div class='karten_text_css' >Karteninhaber<br><input class='karten_css' onkeyup='felder_zuruecksetzen(0)' onkeydown='felder_zuruecksetzen(0)' type='text'></input></div><br><div class='karten_text_css' >Kartennummer<br><input class='karten_css' placeholder='' type='text' onKeyUp='kreditkarten_show(event)' onKeyDown='kreditkarten_show(event)' maxlength='19' onBlur='kreditkarten_show(event)'></input></div>";
		 box = box+"<br><div class='ablaufdatum_text'  id='ablaufdatum_text'>Ablaufdatum<br><select class='karten_css' style='width:45%;float:left;' onchange='felder_zuruecksetzen(2)'>";
		  
		 var i=0;
		 while (i<=12)
		 {
			box=box+"<option>"+monat[i]+"</option>";
			 i=i+1;
		 }
		 
		 
		 box=box+"</select><select class='karten_css' style='width:45%;margin-left:5px;float:left;' onchange='felder_zuruecksetzen(3)'>";
		 
		 var i=0;
		 while (i<=jahr_anzahl)
		 {
			box=box+"<option>"+jahr[i]+"</option>";
			 i=i+1;
		 }
		 
		 
		 
		box=box+"</select></div><div class='karten_text_css_pruefnummer' >Prüfnummer<br><input class='karten_css' onkeyup='felder_zuruecksetzen(4)' onkeydown='felder_zuruecksetzen(4)' type='text' maxlength='3' onkeypress='validate(event)'></input></div></div>";
		box=box+"<br><br><br><br><br><div style='float:right;margin-bottom:40px;margin-top:40px;width:100%;'>"
		

		
		box=box+"<form id='payment-form' action='#' method='POST'>"
		box=box+"<input class='card-amount-int' type='hidden' value='0001' />"
		box=box+"<input class='card-currency' type='hidden' value='EUR' />"
		box=box+"<input class='card-number' type='hidden'  value='4111111111111111'/>"
		box=box+"<input class='card-cvc' type='hidden' value='123' />"
		box=box+"<input class='card-holdername' type='hidden'   value='asdasd' />"
		box=box+"<input class='card-expiry-month' type='hidden'  value='03' />"
		box=box+"<input class='card-expiry-year' type='hidden'  value='2018' />"
		box=box+"</form>"

					
		box=box+"<div  class='kreditkarte_check_button'  onclick='kreditkarten_check()' >Überprüfen</div>"
		box=box+"<div  class='kreditkarte_check_button_abbrechen'  onclick='kreditkarten_abbrechen()' >Abbrechen</div>"
		box=box+"</div><br><br><br><div id='buttons_credit_card' style='float:right;color:red;font-weight:bold;'></div> ";
		document.getElementById("kreditkarten_hinzufuegen").innerHTML=box;
		
		var i=0;
		while(i<=kreditkarten_nummer_stelle)
		{
			document.getElementsByClassName("karten_css")[1].value="";
			

			
			i=i+1;
			
		}
		
		kreditkarten_nummer_stelle=0;
	 

	 
 }
 
 



  function felder_adresse_zuruecksetzen(class_id)
 {

	if(class_id==0)
	{

		document.getElementsByClassName("adresse_input")[class_id].style.border="1px solid #e6e6e6" ;
		document.getElementsByClassName("address_text")[class_id].style.color="#4E4E4E";
	}
	else
	{
		if(class_id!=5 && class_id!=-1)
		{

			document.getElementsByClassName("adresse")[class_id-1].style.border="1px solid #e6e6e6" ;
			document.getElementsByClassName("address_text")[class_id].style.color="#4E4E4E";
		}
		else
		{
			if(class_id==5)
			{			
				document.getElementsByClassName("adresse")[4].style.border="1px solid #e6e6e6" ;
				document.getElementsByClassName("address_mobilnummer")[0].style.color="#4E4E4E";
			}
			else
			{
				document.getElementsByClassName("land_input")[0].style.border="1px solid #e6e6e6" ;
				document.getElementsByClassName("land_text")[0].style.color="#4E4E4E";		
				
			}
			
		}
	}

	
	var status_=0;
	var i=0;
	while(i<=1)
	{
		
		if(document.getElementsByClassName("adresse")[i].value=="")
			status_=1;
		i=i+1;
	}

	if(status_==0)
		document.getElementById("buttons_address_text").innerHTML="";		

	
//	input_on_change(document.getElementsByClassName("adresse")[class_id],document.getElementsByClassName("address_text")[class_id])

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
 
 
 
 function felder_zuruecksetzen(class_id)
 {

	document.getElementsByClassName("karten_css")[class_id].style.border="";
	if(class_id!=2 && class_id!=3)
		if(class_id!=4)
			document.getElementsByClassName("karten_text_css")[class_id].style.color="";
		else
			document.getElementsByClassName("karten_text_css_pruefnummer")[0].style.color="";
			
	else
		document.getElementById("ablaufdatum_text").style.color="";
	
	
	var status_=0;
	var i=0;
	while(i<=4)
	{
		
		if(document.getElementsByClassName("karten_css")[i].value=="")
			status_=1;
		i=i+1;
	}

	if(status_==0)
	{
		document.getElementById("buttons_credit_card").innerHTML="";		
		if(document.getElementsByClassName("button_check")[0].style.display=="none" && document.getElementsByClassName("button_check")[1].style.display=="none")
			document.getElementsByClassName("button_check")[0].style.display="none";
	}

	input_on_change(document.getElementsByClassName("karten_css")[class_id],document.getElementsByClassName("karten_text_css")[class_id])
	

 }
 
 function adressbuch_laden()
{
	
	
	adresse_anzeigen("","","","","","","","","","");
	land="Deutschland"

	

	adressbuch=JSON.parse(document.getElementsByClassName("adressbuch_daten")[0].innerHTML)
	

	i=0;
	while(i<=adressbuch.length-1)
	{
		
	
		if(adressbuch[i].standard=="ja")
		{
			var huelle=adressbuch[0]
			adressbuch[0]=adressbuch[i];
			adressbuch[i]=huelle;
			

		}
		i=i+1;
	}
	
	i=0;
	status_=0;
	while(i<=adressbuch.length-1)
	{
	
		if(adressbuch[i].standard=="ja")
		{
			

			document.getElementsByClassName("adressdetails")[0].style.display="none";
			

			document.getElementsByClassName("adresse")[2].value=adressbuch[i].vorname;
			document.getElementsByClassName("adresse")[3].value=adressbuch[i].nachname;
			document.getElementsByClassName("adresse")[4].value=adressbuch[i].telefonnummer;
			
			document.getElementsByClassName("adresse_input")[0].value=adressbuch[i].adresse;

			document.getElementsByClassName("adresse")[0].value=adressbuch[i].stadt;
			document.getElementsByClassName("adresse")[1].value=adressbuch[i].plz;

			document.getElementsByClassName("land_input")[0].value=adressbuch[i].land;

			land=adressbuch[i].land;

			status_=1;
			lieferhinweise=adressbuch[i].lieferhinweise
			document.getElementsByClassName("unternehmensdetails")[1].value=adressbuch[i].unternehmensdetails;
			
		}
		
		i=i+1;
	}
	
	adresse_neu=-1;
	
	//initMap(adressbuch[i][3],adressbuch[i][6],adressbuch[i][7]);

	if(status_==1)
	{
		adresse_neu=-2;
		check_address();
	}
		
	

}

function check_address_2()
{

//	button_logo(0,"button_check_text","button_check_logo","button_check")
	
	check_address();
//	button_logo(1,"button_check_text","button_check_logo","button_check")
	
	
}




 
 function kreditkarten_check()
 {

	//document.getElementById("payment-form").submit();
	


	//document.forms[1].submit()
	
	  
	
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

	 if(document.getElementsByClassName("karten_css")[4].value.length!=3)
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
		document.getElementsByClassName("karten_text_css")[2].style.border="1px solid red";	
		status=1;
	 }


	 
	 if(status==0)
	 { 
		document.getElementsByClassName("iban")[0].value=document.getElementsByClassName("karten_css")[1].value
		 document.getElementsByClassName("bic")[0].value=document.getElementsByClassName("karten_css")[2].value
		 document.getElementsByClassName("accountholder")[0].value=document.getElementsByClassName("karten_css")[0].value;

		
		page_load(0);
			
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
				data: { "hinzufuegen":1,"indexnummer":"","zahlungsoption": 3,"token":token,'standard':standard_,'zahlungsart':'lastschrift'},
				success: function(data) {
								page_load(1);
								if(data!="existiert")
								{
									
									fbq('track', 'AddPaymentInfo', {
									      content_category: "Sets", 
									      content_ids: document.getElementsByClassName("content_id_list")[0].innerHTML, 
									      contents: document.getElementsByClassName("contents_list")[0].innerHTML, 
									      value: document.getElementsByClassName("value")[0].innerHTML,
									      currency: 'EUR' 
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
				data: { "hinzufuegen":1,"indexnummer":"","zahlungsoption": 0,"card_type":card_type,"token":token,'standard':standard_,'zahlungsart':'kreditkarte'},
				success: function(data) {
								page_load(1);
								if(data!="existiert")
								{
									fbq('track', 'AddPaymentInfo', {
									      content_category: "Sets", 
									      content_ids: document.getElementsByClassName("content_id_list")[0].innerHTML, 
									      contents: document.getElementsByClassName("contents_list")[0].innerHTML, 
									      value: document.getElementsByClassName("value")[0].innerHTML,
									      currency: 'EUR' ,
									      num_items:document.getElementsByClassName("num_items")[0].innerHTML
									    });  	
									document.getElementsByClassName("zahlungsmethoden_daten")[0].innerHTML=data;
					
					
									kreditkarten_daten_laden()
									button_logo(1,"button_text","button_logo","button_cart_large")
									button_logo(1,"button_check_kreditkarte_text","button_check_kreditkarte_logo","button_check_kreditkarte")
								}
								else
									alert_userdata("KARTENNUMMER WIRD BEREITS VON DIR VERWENET","Die eingegebene Kreditkartennummer wird bereits von dir verwendet. Wähle sie als Zahlungsmittel aus.")					
						}
				});
	
		} 
		else
		{
			page_load(1);
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

	document.getElementById("kreditkarten").innerHTML=box+"<br><div class='neue_kreditkarte_hinzufuegen_check'  onclick='lastschrift_hinzufuegen()'>Neues SEPA-Lastschrift Mandat hinzufügen</div><div id='kreditkarten_hinzufuegen' style='display:none;'></div>";
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

	document.getElementById("kreditkarten").innerHTML=box+"<br><div class='neue_kreditkarte_hinzufuegen_check'  onclick='kreditkarte_hinzufuegen()'>Neue Kreditkarte hinzufügen</div><div id='kreditkarten_hinzufuegen' style='display:none;'></div>";
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
				document.getElementsByClassName("zahlungsmethoden_anzeigen")[0].style.border="4px solid #FFD700"
				document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[0].innerHTML="Ausgewähltes Zahlungsmittel";	
				name_karteninhaber=zahlungsmethoden[index].name;
				kreditkarten_nummer__=zahlungsmethoden[index].kreditkartennummer;
				ablaufdatum=zahlungsmethoden[index].ablaufmonat+" "+zahlungsmethoden[index].ablaufjahr;		
		
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
 