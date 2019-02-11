	
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
	var zugelassene_plz=new Array(100);
	var adresse_neu;
	var zahlungsmethoden;
	var gesamtzahl_gerichte;
	   
	   

      


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

function adresse_uebertragen(strasse_, nummer_, apt_, plz_, stadt_, vorname_, nachname_, telefonnummer_, unternehmensdetails_)
{
	strasse=strasse_
	nummer=nummer_
	apt=apt_
	plz=plz_
	stadt=stadt_
	vorname=vorname_
	nachname=nachname_
	telefonnummer=telefonnummer_
	unternehmensdetails=unternehmensdetails_

	
}

function define_zugelassene_plz()
{
	
		zugelassene_plz[0]=new Array;
		zugelassene_plz[0]="80337";
		zugelassene_plz[1]=new Array;
		zugelassene_plz[1]="58313";
		
		zugelassene_plz_max=1;
}

function adresse_anzeigen(strasse_, nummer_, apt_, plz_, stadt_, vorname_, nachname_, telefonnummer_, unternehmensdetails_,adresse_neu_)
{

	adresse_neu=adresse_neu_;
	
	if (strasse_=="")
	{
		var box="<div class='adressdetails'><div id='locationField'><div class='address_text' style='float:left;'>Adresse<br><input class='adresse' id='strasse' placeholder='Adresse eingeben'";
		box=box+"onFocus='geolocate()'  type='text' style='width:400px;' onkeyup='felder_adresse_zuruecksetzen(0)' onkeydown='felder_adresse_zuruecksetzen(0)'></input></div><div class='address_text' style='float:right;'>Apartment<br><input class='adresse' id='route' placeholder=''";
		box=box+"type='text' style='width:120px;' onkeyup='felder_adresse_zuruecksetzen(1)' onkeydown='felder_adresse_zuruecksetzen(1)'></input></div></div><br><br><br><br>";
		box=box+"<div ><div class='address_text' style='float:left;'>Stadt<br><input class='adresse' id='locality' placeholder=''";
		box=box+"type='text' style='width:400px;' onkeyup='felder_adresse_zuruecksetzen(2)' onkeydown='felder_adresse_zuruecksetzen(2)'></input></div><div class='address_text' style='float:right;'>Postleitzahl<br><input class='adresse' id='postal_code' placeholder=''";
		box=box+"type='text' onkeypress='validate(event)' maxlength='5' style='width:120px;' onkeyup='felder_adresse_zuruecksetzen(3)' onkeydown='felder_adresse_zuruecksetzen(3)'></div></div><br><br><br><br><br>";
		box=box+"<input type='checkbox' id='checkbox_unternehmen' onclick='unternehmen_check()'>Zu einem Unternehmen liefern</input><br><br>";
		box=box+"<div class='unternehmensdetails'>Unternehmensangaben</div><input class='unternehmensdetails' id='unternehmensdetails_id' placeholder=''></input><br><br>";
				   
		box=box+"<div style=''><div class='address_text' style='float:left;'>Vorname<br><input class='adresse' id='street_number' style='width:150px'";
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(4)' onkeydown='felder_adresse_zuruecksetzen(4)'></input></div><div class='address_text' style='float:left;margin-left:9%;'>Nachname<br><input class='adresse' id='nachname' style='width:150px'";
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(5)' onkeydown='felder_adresse_zuruecksetzen(5)'></input></div><div style='float:right;' class='address_text'>Telefonnummer<br><input class='adresse' id='street_number' onkeypress='validate(event)' maxlength='20' style='width:150px'";
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(6)' onkeydown='felder_adresse_zuruecksetzen(6)'></input></div></div><br></div>";
		document.getElementsByClassName("button_check")[0].style.display="block";
		
	}
	else
	{
		
		var box="<div class='adressdetails'><div id='locationField'><div class='address_text' style='float:left;'>Adresse<br><input class='adresse' id='strasse' placeholder='Adresse eingeben' value='"+strasse_+"'";

		box=box+"onFocus='geolocate()'  type='text' style='width:400px;' onkeyup='felder_adresse_zuruecksetzen(0)' onkeydown='felder_adresse_zuruecksetzen(0)'></input></div><div class='address_text' style='float:right;'>Apartment<br><input class='adresse' id='route' placeholder=''";

		box=box+"type='text' style='width:120px;' onkeyup='felder_adresse_zuruecksetzen(1)' onkeydown='felder_adresse_zuruecksetzen(1)' value='"+apt_+"'></input></div></div><br><br><br><br>";

		box=box+"<div ><div class='address_text' style='float:left;'>Stadt<br><input class='adresse' id='locality' placeholder='' value='"+stadt_+"'";

		box=box+"type='text' style='width:400px;' onkeyup='felder_adresse_zuruecksetzen(2)' onkeydown='felder_adresse_zuruecksetzen(2)'></input></div><div class='address_text' style='float:right;'>Postleitzahl<br><input class='adresse' id='postal_code' placeholder=''";
		box=box+"type='text' onkeypress='validate(event)' maxlength='5' style='width:120px;' onkeyup='felder_adresse_zuruecksetzen(3)' onkeydown='felder_adresse_zuruecksetzen(3)' value='"+plz_+"'></div></div><br><br><br><br><br>";

		box=box+"<input type='checkbox' id='checkbox_unternehmen' onclick='unternehmen_check()'>Zu einem Unternehmen liefern</input><br><br>";
		box=box+"<div class='unternehmensdetails'>Unternehmensangaben</div><input class='unternehmensdetails' id='unternehmensdetails_id' placeholder='' value='"+unternehmensdetails_+"'></input><br><br>";
				   
				   
	   
		box=box+"<div style=''><div class='address_text' style='float:left;'>Vorname<br><input class='adresse' id='street_number' style='width:150px'";

		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(4)' onkeydown='felder_adresse_zuruecksetzen(4)' value='"+vorname_+"'></input></div><div class='address_text' style='float:left;margin-left:9%;' >Nachname<br><input class='adresse' id='nachname' style='width:150px'";

		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(5)' onkeydown='felder_adresse_zuruecksetzen(5)' value='"+nachname_+"'></input></div><div style='float:right;' class='address_text'>Telefonnummer<br><input class='adresse' id='street_number' onkeypress='validate(event)' maxlength='20' style='width:150px'";

		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(6)' onkeydown='felder_adresse_zuruecksetzen(6)' value='"+telefonnummer_+"'></input></div></div><br></div>";
		
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
	
	initialize()

}


function getDocHeight() {
    var D = document;
    return Math.max(
        D.body.scrollHeight, D.documentElement.scrollHeight,
        D.body.offsetHeight, D.documentElement.offsetHeight,
        D.body.clientHeight, D.documentElement.clientHeight
    )
}
 
var docheight = getDocHeight()



function check_address()
{

	
	var status=0;
			
	var i=1;
	while(i<=6)
	{
		
		if(document.getElementsByClassName("adresse")[i].value=="")
		{
			
			document.getElementById("buttons_address_text").innerHTML="Bitte alle benötigten Felder ausfüllen.";
			document.getElementsByClassName("adresse")[i].style.border="1px solid red";	
			document.getElementsByClassName("address_text")[i].style.color="red";		
			status=1;
			
		}	
		if(i==1)
			i=3	
		i=i+1;

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
		//document.getElementById("total_address").style.display="none";
		
		if(adresse_neu!="")
		{
			
				var strasse=document.getElementsByClassName("adresse")[0].value;

			var plz=document.getElementsByClassName("adresse")[3].value;
			var stadt=document.getElementsByClassName("adresse")[2].value;
			
			var apt=document.getElementsByClassName("adresse")[1].value;
			var vorname=document.getElementsByClassName("adresse")[4].value;
			var nachname=document.getElementsByClassName("adresse")[5].value;
			var telefonnummer=document.getElementsByClassName("adresse")[6].value;
			var unternehmensdetails=document.getElementById("unternehmensdetails_id").value

			initMap(strasse,plz,stadt,apt,vorname,nachname,telefonnummer,unternehmensdetails);

		}

		
//		document.getElementsByClassName("button_check")[0].style.display="none";
		
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
				document.getElementsByClassName("address_text")[i].style.color="red";		
				status=1;
				
			}	
			i=i+1;
		}
	}
	
	if(document.getElementsByClassName("button_check")[0].style.display=="none" && document.getElementsByClassName("button_check")[1].style.display=="none")
		document.getElementsByClassName("button_check")[0].style.display="none";


}




  window.onscroll = function () 
{


	el = document.getElementById("overlay");

	
	if (el.style.visibility =="visible")
	{
		if(scroll_position_absolute==0)
			scroll_position_absolute=scroll_position();
		window.scrollTo(0,scroll_position_absolute);
	}
	else
		scroll_position_absolute=0;
}


  var scroll_position_absolute;
  function scroll_position()
  {
	  
	  
	  					
	var winheight= window.innerHeight || (document.documentElement || document.body).clientHeight;
	var docheight = getDocHeight();
	var scrollTop = window.pageYOffset || (document.documentElement || document.body.parentNode || document.body).scrollTop;
	return scrollTop;
	  
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

		$.ajax({
		type: "POST",
		url: "/hello/account_page/adresse_speichern/",
		dataType: "json",
		data: { "hinzufuegen":hinzufuegen,"indexnummer":index_,"vorname": vorname,"nachname": nachname,"telefonnummer": telefonnummer,
		"adresse": strasse,"apt": apt,"unternehmensdetails": unternehmensdetails,
		"stadt": stadt,"plz": plz,"lieferdetails": "","standard":standard_},
		success: function(data) {
			adresse_neu=-2
			document.getElementsByClassName("adressbuch_daten")[0].innerHTML=data;

			adressbuch=JSON.parse(document.getElementsByClassName("adressbuch_daten")[0].innerHTML)


	//		var huelle=adressbuch[0]
	   
	//		adressbuch[0]=adressbuch[index_];
	//		adressbuch[index_]=huelle;
			
			
			
			
			var strasse=document.getElementsByClassName("adresse")[0].value;
			
			var plz=document.getElementsByClassName("adresse")[2].value;
			var stadt=document.getElementsByClassName("adresse")[3].value;
			
			var apt=document.getElementsByClassName("adresse")[1].value;
			var vorname=document.getElementsByClassName("adresse")[4].value;
			var nachname=document.getElementsByClassName("adresse")[5].value;
			var telefonnummer=document.getElementsByClassName("adresse")[6].value;
			var unternehmensdetails=document.getElementById("unternehmensdetails_id").value

		//initMap(strasse,plz,stadt,apt,vorname,nachname,telefonnummer,unternehmensdetails);
			

			
			
			
			
			
			
			


		}
		});
		
		
	}
	
}



  
  document.onclick = function adresse_feld() {
	  var adresse= strasse+"<br>"+plz+" "+stadt;

	  if(output_adresse_clicked==0 && output_adresse_show==1)
	  {
		 var box="<div class='output_adresse' style='background-color:#f2f2f2;' onclick='adresse_bearbeiten()'><div style='float:left;margin-left:10px;margin-Top:10px'>"+adresse+"</div></div>";
		document.getElementsByClassName("sidebar_2")[0].innerHTML=box;
		
		document.getElementsByClassName("sidebar_2")[0].style.backgroundColor="#f2f2f2";
		output_adresse_show=0;
		
	  }
	  output_adresse_clicked=0;  

  }
  
  
  

  function button_logo(index,text_area,logo_area,button_)
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
 


function bestellen()
{	

	



	if(document.getElementsByClassName("button_check")[0].style.display=="none" && zahlungsmethoden!="")
	{
		rabatt=(rabatt-credit_);
		if (document.getElementById("gutschein_input").value.toUpperCase()=="")
			rabattcode=" ";
		else
			rabattcode=document.getElementById("gutschein_input").value.toUpperCase()
		var lieferdetails=document.getElementById("lieferdetails_textarea").value;
		
		i=0;
		while (i<=zahlungsmethoden.length-1)
		{
			
			if (document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[i].innerHTML!="")
				selected_zahlungsoption=i
			i=i+1;
		}
		

		
		warenkorb_gerichte=cart[0].linkzugericht;
		warenkorb_anzahl=cart[0].anzahl;
		warenkorb_datum=cart[0].datum;
		warenkorb_uhrzeit=cart[0].uhrzeit;
		i=1;
		while (i<=cart.length-1)
		{
			warenkorb_gerichte=warenkorb_gerichte+","+cart[i].linkzugericht;
			warenkorb_anzahl=warenkorb_anzahl+","+cart[i].anzahl;
			warenkorb_datum=warenkorb_datum+","+cart[i].datum;
			warenkorb_uhrzeit=warenkorb_uhrzeit+","+cart[i].uhrzeit;
			i=i+1;
		}
				

				alert(warenkorb_uhrzeit)
				button_logo(0,"button_text","button_logo","button_cart")
				$.ajax({
					type: "POST",
					url: "/hello/check_fahrerkapazitaet_per_bestimmte_zeit/",
					dataType: "json",
					data: { 'warenkorb_datum':warenkorb_datum,'warenkorb_uhrzeit':warenkorb_uhrzeit },
					success: function(data) {		
					alert(data)
					
					if (data=="1")
					{
							$.ajax({
							type: "POST",
							url: "/hello/bestellen/",
							dataType: "json",
							data: { 'warenkorb_gerichte':warenkorb_gerichte,'warenkorb_anzahl':warenkorb_anzahl,'warenkorb_datum':warenkorb_datum,'warenkorb_uhrzeit':warenkorb_uhrzeit,'adresse':strasse,'apt':apt,'stadt':stadt,'plz':plz,'unternehmensdetails':unternehmensdetails,'vorname':vorname,'nachname':nachname,'telefonnummer':telefonnummer,'lieferdetails':lieferdetails,'zahlungsoption':zahlungsoption,'selected_zahlungsoption':selected_zahlungsoption,'preis':preis,'lieferkosten':lieferkosten,'rabatt':rabatt, 'rabattcode':rabattcode },
							success: function(data) {			
							alert(data)
				
								if (data!="not ok")
									window.top.location.href = "/hello/account_page/bestellungen_ansehen/"+data+"/"; 
								if (data=="not ok")
								{
									
									el = document.getElementById("overlay");
									box="<div>"
									box=box+"<br><b>AKTUALISIERTER WARENKORB</b><img class='schliessen_alert' src='/static/x.png' width='15' onclick='warenkorb_aktualisieren_schliessen()' height='15'/></img>";
									box=box+"<p>Dein Warenkorb wurde aktualisiert. Diese Seite wird neu geladen.</p><br>";
			
									el.innerHTML=box;
									el.style.marginTop=scroll_position()+"px";
									el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
									document.getElementById("x-mask").style.opacity="0.4";
								}
									
						
			
							},
							failure:function(){
								alert("asd")
							button_logo(1,"button_text","button_logo","button_cart")}
							
						});
					}
	}
	else
	{
		document.getElementById("bestellen_ueberpruefen").style.display="block";
	}
	
}





 function alert_click_schliessen() {

	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "hidden") ? "visible" : "hidden";
	document.getElementById("x-mask").style.opacity="1.0";
}


 function alert_click_schliessen_2() {

			$.ajax({
				type: "POST",
				url: "/hello/warenkorb_check_zeiten/",
				dataType: "json",
				data: { },
				success: function(data) {	
						location.reload();
				}
			});

}


function warenkorb_aktualisieren_schliessen()
{
	location.reload();
}




function preis_aufrufen()
{
	
	
	var i=0;
	var preis=0;

	while(i<=cart.length-1)
	{
		if(cart[i].linkzugericht!=0)
		{
			preis=preis+gericht_preis_ermitteln(cart[i].linkzugericht)*cart[i].anzahl
			
			
		}
		
		i=i+1;
	}
	
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



function bestelluebersicht(rabatt__)
{
	

	rabatt=rabatt__	
	

	preis=preis_aufrufen()
	credit_=Math.min(parseFloat(credit),preis+lieferkosten+rabatt)
	var gesamt=preis+lieferkosten+rabatt-credit_;
	

	
	preis_=	replace_dot_comma(preis);
	rabatt_=	replace_dot_comma(rabatt);
	preis_gesamt=	replace_dot_comma(gesamt);
	
	lieferkosten_=replace_dot_comma(lieferkosten);

	var maxim= document.getElementsByClassName("bestellung");
	
	var uebersicht="<div style='float:left;'>Bestellung:</div><div style='float:right;'>"+preis_+" EUR</div><br>";
	uebersicht=uebersicht+"<div style='float:left;'>Lieferkosten:</div><div style='float:right;'>"+lieferkosten_+" EUR</div><br>";

	if(rabatt!=0)
	{
		uebersicht=uebersicht+"<div style='float:left;'>Rabatt:</div><div style='float:right;'>"+rabatt_+" EUR</div><br>";	
		
	}
	
	if(credit!=0)
	{
		
		uebersicht=uebersicht+"<div style='float:left;width:30px;'>Freundschafts-\nwerbung:</div><div style='float:right;'><br>"+replace_dot_comma(-credit_)+" EUR</div><br><br>";	
		
	}
	uebersicht=uebersicht+"<div style='border-bottom:1px solid #e6e6e6 ;'></div>";
	

	
	uebersicht=uebersicht+"<div style='float:left;font-weight: bold;'>Gesamt:</div><div style='float:right;font-weight: bold;'>"+preis_gesamt+" EUR</div><br><br>";
	
	if(rabatt==0)
		var promo="<div class='promo_code' onclick='promo_code()'><b>+</b> Gutschein-Code hinzufügen</div>";
	else
		var promo="<div class='promo_code' onclick='promo_code()'><b>-</b> Gutschein-Code hinzufügen</div>";	
	uebersicht=uebersicht+promo;
	maxim[0].innerHTML=uebersicht;

	
	
}






function gutschein_einloesen()
{
	button_logo(0,"gutschein_button_text","gutschein_button_logo","gutschein_button")
	if(document.getElementsByClassName("gutschein_button_text")[0].innerHTML!="Abbrechen")
	{

		$.ajax({
			type: "POST",
			url: "/hello/gutschein_einloesen/",
			dataType: "json",
			data: { "gutscheincode":  document.getElementById("gutschein_input").value.toUpperCase() },
			success: function(data) {
				if (data!= "")
				{	
					document.getElementById("gutschein_button_id").style.backgroundColor="#808080";
					button_logo(1,"gutschein_button_text","gutschein_button_logo","gutschein_button")
					document.getElementsByClassName("gutschein_button_text")[0].innerHTML="Abbrechen";
					document.getElementById("gutschein_input").disabled=true;
					rabatt_=parseFloat(data);
					bestelluebersicht(parseFloat(data));
				}
				else
				{
					button_logo(1,"gutschein_button_text","gutschein_button_logo","gutschein_button")
					bestelluebersicht(0);
					rabatt_=0
					el = document.getElementById("overlay");
					box="<div>"
					box=box+"<br><b>GUTSCHEIN NICHT GÜTLIG</b><img class='schliessen_alert' src='/static/x.png' width='15' onclick='gutscheincode_schliessen()' height='15'/></img>";
					box=box+"<p>Dieser Gutschein-Code ist leider nicht gültig</p><br>";

					el.innerHTML=box;
					el.style.marginTop=scroll_position()+"px";
					el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
					document.getElementById("x-mask").style.opacity="0.4";
					
					
					
				}
					
		

			}
		});
		

		
		
	}
	else
	{
		gutschein_code_reset();
		button_logo(1,"gutschein_button_text","gutschein_button_logo","gutschein_button")
	}
	
	
}

function gutschein_code_reset()
{
	
	document.getElementById("gutschein_button_id").style.backgroundColor="#ff761a";
	document.getElementsByClassName("gutschein_button_text")[0].innerHTML="Überprüfen";
	document.getElementById("gutschein_input").disabled=false;
	bestelluebersicht(0);
	document.getElementById("gutschein_input").style.display ="none";
	document.getElementById("gutschein_input").value ="";
	document.getElementById("gutschein_button_id").style.display ="none";
	
	
}


 function gutscheincode_schliessen() {

	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "hidden") ? "visible" : "hidden";
	document.getElementById("x-mask").style.opacity="1.0";
}



function promo_code()
{
	
	
	if (document.getElementById("gutschein_input").style.display =="block")
	{
		document.getElementById("gutschein_input").style.display ="none";
		document.getElementsByClassName("promo_code")[0].innerHTML="<b>+</b> Gutschein-Code hinzufügen";
		document.getElementById("gutschein_button_id").style.display ="none";
		
	}
	else
	{
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

	}
	else
	{
		document.getElementsByClassName("unternehmensdetails")[0].style.display ="block";
		document.getElementsByClassName("unternehmensdetails")[1].style.display ="block";

	}
}


 function warenkorb_ermitteln(daten_2,cart_gesamt)
 {
	 

	cart=JSON.parse(document.getElementsByClassName("warenkorb_daten")[0].innerHTML)
	



	 var i=0;
	 cart_gesamt=0;
	 credit=daten_2
	 
	

	 
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
 
 
  function gerichte_ermitteln(daten)
 {
	gerichte_menu=JSON.parse(document.getElementsByClassName("menu_daten")[0].innerHTML)
	fahrer_kapazitaet=JSON.parse(document.getElementsByClassName("fahrerkapazitaet_daten")[0].innerHTML)
}


function email_check(email)
{

	if (email=="not ok")
	{
		
		
	
		
		el = document.getElementById("overlay");
		box="<div style='width:750px;height:200px;'>"
		box=box+"<br><b>EMAIL ADRESSE FESTLEGEN</b><img class='schliessen_alert' src='/static/x.png' width='15' onclick='alert_click_schliessen_();' height='15'/></img><br><br>";
		box=box+"<p style='margin-left:20px;margin-right:20px;'>Bevor der Bestellprozess abgeschlossen werden kann, muss zunächst eine E-Mail Adresse hinterlegt werden</p><br>";
		
		
		box=box+"<input class='email_eingabe' type='text' style='width:200px;height:25px;font-size:14px;color:#000000;'  placeholder='E-Mail Adresse'  />";
		box=box+"<button style='margin-left:10px;' class='button_email_eingeben' onclick='register()'>Eintragen</button><p id='email_fehler' style='font-size:10px;color:#C80000  ' ></p>";

		el.innerHTML=box+"</div>";

		//el.style.marginTop="150px";
		el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
		

		document.getElementById("x-mask").style.opacity="0.3";
	}
	
	
	
	
}


 function alert_userdata(content1,content2)
 {	 

	el = document.getElementById("overlay");
	box="<div style='width:750px;height:200px;'>"
	box=box+"<br><b>"+content1+"</b><img class='schliessen_alert' src='/static/x.png' width='15' onclick='alert_click_schliessen();' height='15'/></img><br><br>";
	box=box+"<p style='margin-left:20px;margin-right:20px;'>"+content2+"</p><br>";

	el.innerHTML=box+"</div>";
	var winheight= window.innerHeight || (document.documentElement || document.body).clientHeight
	var docheight = getDocHeight()
	var scrollTop = window.pageYOffset || (document.documentElement || document.body.parentNode || document.body).scrollTop
	el.style.marginTop=scrollTop+"px";
	scroll_position_absolute=scrollTop;
	
	//el.style.marginTop="150px";
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";

	document.getElementById("x-mask").style.opacity="0.3";

 }
 
  function alert_userdata_(content1,content2)
 {	 

	el = document.getElementById("overlay");
	box="<div style='width:750px;height:200px;'>"
	box=box+"<br><b>"+content1+"</b><img class='schliessen_alert' src='/static/x.png' width='15' onclick='alert_click_schliessen_2();' height='15'/></img><br><br>";
	box=box+"<p style='margin-left:20px;margin-right:20px;'>"+content2+"</p><br>";

	el.innerHTML=box+"</div>";
	var winheight= window.innerHeight || (document.documentElement || document.body).clientHeight
	var docheight = getDocHeight()
	var scrollTop = window.pageYOffset || (document.documentElement || document.body.parentNode || document.body).scrollTop
	el.style.marginTop=scrollTop+"px";
	scroll_position_absolute=scrollTop;
	
	//el.style.marginTop="150px";
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";

	document.getElementById("x-mask").style.opacity="0.3";

 }
 
 
 function check_vollstaendigkeit()
 {
	 if(document.getElementsByClassName("email_eingabe")[0].value=="")
		  document.getElementById("email_fehler").innerHTML="Bitte E-Mail Adresse angeben";
	  else
		  return true		 
	 
 }
 
 
 
 function register()
 {
	 if (check_vollstaendigkeit())
			 $.ajax({
				type: "POST",
				url: "/hello/register_user/",
				dataType: "json",
				data: { "item": document.getElementsByClassName("email_eingabe")[0].value+", " },
				success: function(data) {

					if(data=="exists already")
						document.getElementById("email_fehler").innerHTML="User existiert bereits";
					else	
						if(data=="email falsch")
							document.getElementById("email_fehler").innerHTML="Bitte eine gültige E-Mail Adresse angeben";
						else
						{
							 alert_click_schliessen();
							 load_header("true");
							 warenkorb_abrufen(gesamtzahl_gerichte)

						}
				}
			}); 
 }
 
 
 
 
 function alert_click_schliessen_()
 {
 
	window.location.href="/hello/0/";
 }
 
 
 window.onload=function fenster_aufrufen()
 {

	
	zahlung_click(0);
	
	
 }
 
 
 function others_laden()
 { 

	max=2;
	gutschein_code_reset();
	
	bestelluebersicht(0)
	
	document.getElementsByClassName("cart")[0].style.backgroundImage="url('/static/Cart-open.PNG')";
	
	

	document.getElementById("gutschein_input").style.display ="none";
	document.getElementById("gutschein_button_id").style.display ="none";
	//document.getElementsByClassName("unternehmensdetails")[0].style.display="none";
	//document.getElementsByClassName("unternehmensdetails")[1].style.display="none";
	


	
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
 
 
 
 
 function sort_datum()
 {
	 i=0;
	 while(i<=datum_in_cart.length-1)
	 {
		 
		 
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


function vorbestellung_abrufen(datum_,uhrzeit_)
{
	
	
	var i=0;
	var status_="";
	
	while(i<=fahrer_kapazitaet.length-1)
	{

		
		if(fahrer_kapazitaet[i].datum==datum_ && fahrer_kapazitaet[i].uhrzeit==uhrzeit_)
		{
			status_=parseInt(fahrer_kapazitaet[i].verfuegbare_fahrer);

			verbleibende_minuten=parseInt(fahrer_kapazitaet[i].verbleibende_minuten);
			
		}
		i=i+1;
	}
	
	
	if(status_<=0)
		return "Keine Bestellungen mehr möglich";
	else
		if (verbleibende_minuten <=10)
			return "Vorbestellung noch für "+verbleibende_minuten+" Minuten möglich";
		else
			return ""

	

}


function check_timing_availability()
{
	
	
		$.ajax({
			type: "POST",
			url: "/hello/zeit_verfuegbarkeit/",
			dataType: "json",
			data: { },
			success: function(data) {
				document.getElementsByClassName("fahrerkapazitaet_daten")[0].innerHTML=data
				fahrer_kapazitaet=JSON.parse(document.getElementsByClassName("fahrerkapazitaet_daten")[0].innerHTML)
				h=0;
				while(h<=datum_in_cart.length-1)	
				{
					if(datum_in_cart[h][0]!="")
					{
			
						f=0;

						while (f<=4)
						{
							status_=vorbestellung_abrufen(datum_in_cart[h][0],datum_text[f]);

							if (status_=="Keine Bestellungen mehr möglich")
							{
								document.getElementsByClassName("zeitbox")[h*5+f].style.opacity="0.3";
								document.getElementsByClassName("zeitbox")[h*5+f].style.backgroundColor="#e6e6e6"
								document.getElementsByClassName("zeitbox_kapaziaet")[h*5+f].innerHTML="Keine Bestellungen mehr möglich"
								if (document.getElementsByClassName("zeitbox")[h*5+f].style.borderBottom!="")
								{
									
									datum_click(0,1)
								}
								document.getElementsByClassName("zeitbox")[h*5+f].style.borderBottom="";

									
								
								
							}
							else
								document.getElementsByClassName("zeitbox_kapaziaet")[h*5+f].innerHTML=status_;
								
								
	
	
	
							f=f+1;
						}
					}
					h=h+1;
				}
			}
		});
	

}


 

 
 function gerichte_anzeigen()
 {
	 
	 //setInterval(check_timing_availability, 5000)
	
	
	
	i=0;
	while (i<=12)
	{
		datum_in_cart[i]=new Array;
		datum_in_cart[i][0]="";
		datum_in_cart[i][1]="";
		
		

		
		i=i+1;
	}
	
	i=0;
	j=0;
	lieferkosten=0;
	
	cart.sort(compareLastColumn);


	while (i<=cart.length-1)
	{
		vorhanden=0;
		j=0;
		stelle="";
		while (j<=12)
		{
			if(cart[i].datum==datum_in_cart[j][0] && cart[i].datum!="")	
				vorhanden="1";
			if(datum_in_cart[j][0]=="" && stelle=="")
				stelle=j;

			j=j+1;
		}

		if(vorhanden==0 && stelle != "")
		{

			datum_in_cart[stelle][0]=cart[i].datum;
			datum_in_cart[stelle][1]=cart[i].uhrzeit;			
		}
		

		

		i=i+1;
	}
	

	datum_in_cart.splice(stelle+1,12-stelle);
	
	datum_in_cart.splice(0,1);
	

	
	
	
	h=0;	
	var box="";
	
	
	while(h<=datum_in_cart.length-1)	
	{
		if(datum_in_cart[h][0]!="")
		{
			lieferkosten=lieferkosten+2.95;
			

		
			var i=0;
			
			
			box=box+"<div><div class='datum' id='inhalt_datum'>"+datum_in_cart[h][0]+"</div><div style='float:left;line-height:35px;'>, Zustellungszeit:</div></div><br><br><br>";	 
			
			datum_text[0]=new Array;
			datum_text[0]="16-17 Uhr";
			datum_text[1]=new Array;
			datum_text[1]="17-18 Uhr";
			datum_text[2]=new Array;
			datum_text[2]="18-19 Uhr";
			datum_text[3]=new Array;
			datum_text[3]="19-20 Uhr";
			datum_text[4]=new Array;
			datum_text[4]="20-21 Uhr";
			
			f=0;
			zaehler=0;
			while (f<=4)
			{
				if (vorbestellung_abrufen(datum_in_cart[h][0],datum_text[f])=="Keine Bestellungen mehr möglich")
				{
					zaehler=zaehler+1;
					box=box+"<div class='zeitbox' 	style='opacity:0.3;background-Color:#e6e6e6;' >"+datum_text[f]+"</div>";
				}
				else
					box=box+"<div class='zeitbox' id='"+parseInt(h*5+0)+"' onclick='datum_click("+parseInt(h*5)+","+parseInt(h*5+f)+")'	 >"+datum_text[f]+"</div>";
				
				f=f+1;
			}
			
			if(zaehler==5)
				alert_userdata_("WARENKORB NICHT MEHR VERFÜGBAR","Leider ist für die Lieferung für heute keine Bestellung mehr möglich. Dein Warenkorb wird aktualisiert.")

			
			
			
			box=box+"<br><br><br>"
			box=box+"<div class='zeitbox_kapaziaet' id='"+parseInt(h*5+0)+"'>"+vorbestellung_abrufen(datum_in_cart[h][0],'16-17 Uhr')+"</div>";
			box=box+"<div class='zeitbox_kapaziaet' id='"+parseInt(h*5+1)+"'>"+vorbestellung_abrufen(datum_in_cart[h][0],'17-18 Uhr')+"</div>";
			box=box+"<div class='zeitbox_kapaziaet' id='"+parseInt(h*5+2)+"'>"+vorbestellung_abrufen(datum_in_cart[h][0],'18-19 Uhr')+"</div>";
			box=box+"<div class='zeitbox_kapaziaet' id='"+parseInt(h*5+3)+"'>"+vorbestellung_abrufen(datum_in_cart[h][0],'19-20 Uhr')+"</div>";
			box=box+"<div class='zeitbox_kapaziaet' id='"+parseInt(h*5+4)+"'>"+vorbestellung_abrufen(datum_in_cart[h][0],'20-21 Uhr')+"</div>";
			
			
			
			box=box+"<br><br><br>"

			 box=box+"<div class='gericht_text'>";
			 
			 var top=100;
			 
			 
			
			 while(i<=cart.length-1)
			 {


				if(cart[i].linkzugericht!="" && cart[i].datum==datum_in_cart[h][0])
				{	
					
					
					box=box+"<div style='float:left; font-size:12px;width:575px;'><div style='float:left;'><div style='cursor:pointer' onclick='gerichte_detail("+i+")'><img src='"+gericht_bild_ermitteln(cart[i].linkzugericht)+"' style='width:45px;height:45px;float:left;'/><div style='margin-left:10px;float:left;'>"+cart[i].linkzugericht+"<br><div style='float:left;font-size:12px;'>"+replace_dot_comma(parseFloat(gericht_preis_ermitteln(cart[i].linkzugericht)))+" EUR</div> </div></div></div>";
					box=box+"<div style='float:right;'><div style='float:left;'>Anzahl</div><select class='select_anzahl' style='margin-left:10px;float:left;width:50px;' onchange='change_cart("+i+")' >";
					
					var w=0;
					
					
					min_1=parseInt(verfuegbarkeits_check(gericht_id_suchen_id(i)))+parseInt(cart[i].anzahl);

					while(w<=Math.min(min_1,10))
					{
						box=box+"<option>"+w+"</option>";
						w=w+1;
					}
					
					
					box=box+"</select><div style='float:left;cursor:pointer;font-size:12px;color:#e65c00;margin-left:10px;' id='entfernen"+i+"' onclick='entfernen("+i+")'>Entfernen</div></div></div><br><br><br>";
					top=top+50;

					
					
				}
				 i=i+1;	
			 
			 }
			 
			 
			 box=box+"<br><br>";
			 
			 document.getElementById("adressangaben").style.marginTop=top+"px";
		}
		 h=h+1;
		  
	}
	
	
		 

		 
		 var maxim= document.getElementsByClassName("gerichte_uebersicht");
		 maxim[0].innerHTML=box+"</div>";
		 
		 
		 var h=0;
		 
		 while(h<=datum_in_cart.length-1)	
		{
			if(datum_in_cart[h][0]!="")
			{
				datum_click(h*5,h*5+parseInt(datum_in_cart[h][1]));
				
				
				
			}
			h=h+1;
		}
		
		 
		 var i=0;
		 nummer=0;
		 while(i<=cart.length-1)
		 {

			var j=0;
			
			while (j<=datum_in_cart.length-1)
			{

				if(cart[i].linkzugericht!="" && cart[i].datum==datum_in_cart[j][0])
				{	
					
					document.getElementsByClassName("select_anzahl")[nummer].selectedIndex=cart[i].anzahl;
					nummer=nummer+1;
				}
				j=j+1;
			}
			i=i+1;	
		 
		 }
 }
 
 function gerichte_detail(link_)
 {
	 

	 window.top.location.href = "/hello/"+cart[link_][3]+"/"+cart[link_][0]+"/";; 	 
	 
 }
 
 
 
  function verfuegbarkeits_check(i)
 {
	 
	return (parseInt(gerichte_menu[i].gerichte_uebrig)-parseInt(gerichte_menu[i].warenkorb_menge));
 }
 
 
  function gericht_id_suchen_id(index)
 {
	
	 j=0;

	
		 var j=0;

		 while (j<=gerichte_menu.length-1)
		 {

			 if(gerichte_menu[j].datum==cart[index].datum && gerichte_menu[j].name==cart[index].linkzugericht)
			 {

				 return j
			 }
			 
			 j=j+1;
			 
		 }

	 
	 
	 
 }
 
 
 
 function change_cart(clicked_id)
 {	

	if(cart[clicked_id].anzahl!=document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex)
	{

		//pause_buttons();	
		cart[clicked_id].anzahl=document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex;
		
		$.ajax({
			type: "POST",
			url: "/hello/add/",
			dataType: "json",
			data: { "add_or_erase":"change","anzahl":cart[clicked_id].anzahl,"gerichtname": cart[clicked_id].linkzugericht, "datum":cart[clicked_id].datum, "auswahl_tag_final":"","gewaehlter_wochentag":"" },
			success: function(data) {		
				if (data=="not ok")
				{
						el = document.getElementById("overlay");
						box="<div>"
						box=box+"<br><b>ZUSÄTZLICHE MENGEN NICHT VERFÜGBAR</b><img class='schliessen_alert' src='/static/x.png' width='15' onclick='warenkorb_aktualisieren_schliessen()' height='15'/></img>";
						box=box+"<p>Da war ein anderer Kunde schneller. Zusätzliche Mengen sind von dem Gericht nicht mehr verfügbar. Diese Seite wird neu geladen.</p><br>";

						el.innerHTML=box;
						el.style.marginTop=scroll_position()+"px";
						el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
						document.getElementById("x-mask").style.opacity="0.4";
					
					
				}
				else
				{
					
					
					$.ajax({
					type: "POST",
					url: "/hello/gerichte_abrufen/",
					dataType: "json",
					data: {"bestellnummer":"","auswahl_tag":"","gerichtname":""  },
					success: function(data_2) {
						
							
							document.getElementsByClassName("warenkorb_daten")[0].innerHTML=data;
							cart=JSON.parse(document.getElementsByClassName("warenkorb_daten")[0].innerHTML);

							if(cart=="")
								window.location= "/hello/0/";	
							
							document.getElementsByClassName("menu_daten")[0].innerHTML=data_2;
							gerichte_menu=JSON.parse(document.getElementsByClassName("menu_daten")[0].innerHTML);
							
							gerichte_anzeigen();
						
						}
						});
						

				}
				



			}
		});
		

		 bestelluebersicht(0);
			

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
		document.getElementsByClassName("select_anzahl")[i].selectedIndex=cart[i].linkzugericht;
		 i=i+1;
		 
	 }
	 
	 
 }
 
 function sort_cart(clicked_id)
 {
	 var i=clicked_id;
	 
	 while(i<=9)
	 {
		 cart[i][0]=cart[i+1][0];
		 cart[i][1]=cart[i+1][1];
		 cart[i][2]=cart[i+1][2];
		 i=i+1;
	 }	 
 }
 
 function entfernen(clicked_id)
 {
	
	 
	document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex=0;
	
	change_cart(clicked_id);

	 
	 
 }
 
 function datum_abrufen()
 {
	 var jetzt = new Date();
		var Tag = jetzt.getDate();
		var Jahresmonat = jetzt.getMonth();
		var TagInWoche = jetzt.getDay();
		var Wochentag = new Array("Sonntag", "Montag", "Dienstag", "Mittwoch",
		"Donnerstag", "Freitag", "Samstag");
		var Monat = new Array("Januar", "Februar", "März", "April",
		"Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember");
		
		j=0;
		tage=jetzt.getDate();

		var day = jetzt.getDate();

		
		ausgewaehlter_tag=0; /* hier eintragen, auf welchen Tag User geklick hat */
		

		var DatumZeitJetzt = new Date();
		var DatumZukunft = new Date();
		var DatumZukunft_ = new Date();
		
		var AnzahlTage = 0;
		var msProTag = 86400000;

		DatumZukunft.setTime(DatumZeitJetzt.getTime() + AnzahlTage * msProTag);
		auswahl_tag=0;
		
		DatumZukunft.setTime(DatumZeitJetzt.getTime() + ausgewaehlter_tag * msProTag);
		TagInWoche = DatumZukunft.getDay();
		
		
		if (TagInWoche == 6 || TagInWoche == 0)
		{	
				if(ausgewaehlter_tag==6)
				{
					ausgewaehlter_tag=ausgewaehlter_tag;
					
				}
				else
				{
					ausgewaehlter_tag=ausgewaehlter_tag+1;
				}
		}
		
		
		var TagInWoche = jetzt.getDay();
		var Jahresmonat = jetzt.getMonth();
		var Jahr = jetzt.getYear()+1900;
		
		
		
		while(auswahl_tag<ausgewaehlter_tag)
		{
			if (TagInWoche == 6 || TagInWoche == 0)
			{
				
				TagInWoche=1;
				AnzahlTage=AnzahlTage+1;
				DatumZukunft.setTime(DatumZeitJetzt.getTime() + AnzahlTage * msProTag);
			}
			else
			{
				
				TagInWoche=TagInWoche+1;
				AnzahlTage=AnzahlTage+1;
				DatumZukunft.setTime(DatumZeitJetzt.getTime() + AnzahlTage * msProTag);				
			}
				

			auswahl_tag=auswahl_tag+1;

			
		}
		
		
		
		document.getElementById("inhalt_datum").innerHTML=Wochentag[TagInWoche]+", "+DatumZukunft.getDate()+". "+Monat[Jahresmonat]+" "+ Jahr;
		
		
	 
 }
 
 
 function datum_click(clicked_id_first,clicked_id)
 {

	var i=clicked_id_first;

		var maxim= document.getElementsByClassName("zeitbox");
		if(maxim[clicked_id].style.opacity=="0.3")
		{
			while(i<=clicked_id_first+4)
			{

				if(maxim[i].style.opacity!="0.3")
				{
					clicked_id=i		
					break;
				}
				i=i+1;
				
			}
		}
	
		
		 i=clicked_id_first;
		while(i<=clicked_id_first+4)
		{

			if(i==clicked_id && maxim[i].style.opacity!="0.3")
			{
				
				maxim[i].style.borderBottom="1px solid #e65c00";
				maxim[i].style.backgroundColor="#e6e6e6";
				

				$.ajax({
				type: "POST",
				url: "/hello/change_timing/",
				dataType: "json",
				data: { "item": document.getElementsByClassName("datum")[clicked_id_first/5].innerHTML+","+document.getElementsByClassName("zeitbox")[i].innerHTML},
				success: function(data) {

					document.getElementsByClassName("warenkorb_daten")[0].innerHTML=data;
					cart=JSON.parse(document.getElementsByClassName("warenkorb_daten")[0].innerHTML)
						

				}
				});
				
				
			}
			else
			{
				if(maxim[i].style.opacity!="0.3")
				{
					maxim[i].style.borderBottom="1px solid #e6e6e6";
					maxim[i].style.backgroundColor="#ffffff";
				}
				
			}
			i=i+1;
			
			
		}

	 
 }
 

 
 
  function zahlung_click(clicked_id)
 {
	 zahlungsoption=clicked_id;
	
	var i=0;
	
	var maxim= document.getElementsByClassName("zahlung");
	while(i<=2)
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
	{
		 

		//document.getElementsByClassName("header_style")[0].style.height=1200+50*(max+1)+"px";
		

	}
	else
	{

	document.getElementById("kreditkarten").innerHTML="";
	//document.getElementsByClassName("header_style")[0].style.height=1200+50*(max+1)+"px";

		
	}

	 
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
		 
		
		 
		 
		 var box="<div id='kartendetails_maske'> <div class='karten_text_css' style='float:left'>Name des Karteninhabers<br><input class='karten_css' onkeyup='felder_zuruecksetzen(0)' onkeydown='felder_zuruecksetzen(0)' type='text'></input></div><div class='karten_text_css' style='float:right;'>Kartennummer<br><input class='karten_css' placeholder='' type='text' onKeyUp='kreditkarten_show(event)' onKeyDown='kreditkarten_show(event)' maxlength='19'></input></div><br><br><br><br>";
		 box = box+"<div id='ablaufdatum_text' style='float:left;margin-right:30px;'>Ablaufdatum<br><select class='karten_css' style='height:30px;width:125px;' onchange='felder_zuruecksetzen(2)'>";
		  
		 var i=0;
		 while (i<=12)
		 {
			box=box+"<option>"+monat[i]+"</option>";
			 i=i+1;
		 }
		 
		 
		 box=box+"</select><select class='karten_css' style='height:30px;width:125px;margin-left:5px;' onchange='felder_zuruecksetzen(3)'>";
		 
		 var i=0;
		 while (i<=jahr_anzahl)
		 {
			box=box+"<option>"+jahr[i]+"</option>";
			 i=i+1;
		 }
		 
		 
		 
		box=box+"</select></div><div class='karten_text_css' style='float:right;'>Prüfnummer<br><input class='karten_css' onkeyup='felder_zuruecksetzen(4)' onkeydown='felder_zuruecksetzen(4)' type='text' maxlength='3' onkeypress='validate(event)'></input></div></div>";
		box=box+"<br><br><br><br><br><div style='float:right;'>"
		box=box+"<div  class='button_check_kreditkarte'  onclick='kreditkarten_check()'><div class='button_check_kreditkarte_text'>Überprüfen</div><div class='button_check_kreditkarte_logo'></div></div>"
		box=box+"<div class='button_abbrechen' onclick='kreditkarten_abbrechen()'>Abbrechen</div></div><br><br><br><div id='buttons_credit_card' style='float:right;color:red;font-weight:bold;'></div> ";
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

	document.getElementsByClassName("adresse")[class_id].style.border="";
	document.getElementsByClassName("address_text")[class_id].style.color="";

	
	var status_=0;
	var i=0;
	while(i<=6)
	{
		
		if(document.getElementsByClassName("adresse")[i].value=="")
			status_=1;
		i=i+1;
	}

	if(status_==0)
		document.getElementById("buttons_address_text").innerHTML="";		

	
	input_on_change(document.getElementsByClassName("adresse")[class_id],document.getElementsByClassName("address_text")[class_id])

 }
 
 
 
 function felder_zuruecksetzen(class_id)
 {

	document.getElementsByClassName("karten_css")[class_id].style.border="";
	if(class_id!=2 && class_id!=3)
		if(class_id!=4)
			document.getElementsByClassName("karten_text_css")[class_id].style.color="";
		else
			document.getElementsByClassName("karten_text_css")[2].style.color="";
			
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
	
	
	adresse_anzeigen("","","","","","","","","");
	
	

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
			

			document.getElementsByClassName("adresse")[4].value=adressbuch[i].vorname;
			document.getElementsByClassName("adresse")[5].value=adressbuch[i].nachname;
			document.getElementsByClassName("adresse")[6].value=adressbuch[i].telefonnummer;
			
			document.getElementsByClassName("adresse")[0].value=adressbuch[i].adresse;
			document.getElementsByClassName("adresse")[1].value=adressbuch[i].apt;
			document.getElementsByClassName("adresse")[2].value=adressbuch[i].stadt;
			document.getElementsByClassName("adresse")[3].value=adressbuch[i].plz;
			status_=1;
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
	
	button_logo(0,"button_check_text","button_check_logo","button_check")
	
	check_address();
	button_logo(1,"button_check_text","button_check_logo","button_check")
	
	
}


 
 
 function kreditkarten_check()
 {
	 

	button_logo(0,"button_check_kreditkarte_text","button_check_kreditkarte_logo","button_check_kreditkarte")
	
	document.getElementsByClassName("button_abbrechen")[0].style.pointerEvents = 'none';
	document.getElementsByClassName("button_check")[0].style.pointerEvents = 'none';
	document.getElementsByClassName("button_cart")[0].style.pointerEvents = 'none';
	
	
	

	 
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
		
		document.getElementsByClassName("karten_text_css")[2].style.color="red"; 

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
				url: "/hello/account_page/zahlungsmethode_speichern/",
				dataType: "json",
				data: { "hinzufuegen":1,"indexnummer":"","zahlungsoption": 0,"name": document.getElementsByClassName("karten_css")[0].value,"kreditkartennummer": document.getElementsByClassName("karten_css")[1].value,
				"ablaufmonat": document.getElementsByClassName("karten_css")[2].value,"ablaufjahr": document.getElementsByClassName("karten_css")[3].value,"sicherheitscode": document.getElementsByClassName("karten_css")[4].value,
				"standard":standard_,"card_type":card_type},
				success: function(data) {
					
					document.getElementsByClassName("zahlungsmethoden_daten")[0].innerHTML=data;
	
	
					kreditkarten_daten_laden()
	
	
					//zahlungsmethode_auswaehlen(index_)
				}
			});
		
		}
		else
		{
			alert_userdata("KREDITKARTE WIRD NICHT UNTERSTÜTZT","Es werden nur Master- oder Visa-Kreditkarten unterstützt. Bitte gebe eine andere Kreditkarte ein.")
			document.getElementsByClassName("karten_css")[1].style.border="1px solid red";	
			document.getElementsByClassName("karten_text_css")[1].style.color="red";
		}
	 }
	 button_logo(1,"button_check_kreditkarte_text","button_check_kreditkarte_logo","button_check_kreditkarte")
	document.getElementsByClassName("button_abbrechen")[0].style.pointerEvents = 'auto';
	document.getElementsByClassName("button_check")[0].style.pointerEvents = 'auto';
	document.getElementsByClassName("button_cart")[0].style.pointerEvents = 'auto';
	 
 }
 
 function input_on_change(element,element2)
{
	element.style.border="1px solid #e6e6e6 ";	
	element2.style.color="#4E4E4E";
}
 
  function button_logo(index,text_area,logo_area,button_)
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
 
 
 
 function kreditkarten_daten_laden()
 {
	 
	zahlungsmethoden=JSON.parse(document.getElementsByClassName("zahlungsmethoden_daten")[0].innerHTML)


	
	i=0;
	var box=""
	float_=0
	zaehler=0
	
	while(i<=zahlungsmethoden.length-1)
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
			box=box+"<div class='zahlungsmethoden_anzeigen' style='width:270px;height:150px;float:left;border:4px solid #e6e6e6;margin-bottom:20px;cursor:pointer;' onclick='zahlungsmethode_auswaehlen("+i+")'>";
			float_=1;
			zaehler=zaehler+1;
		}
		else
		{
			box=box+"<div class='zahlungsmethoden_anzeigen' style='width:270px;height:150px;float:right;border:4px solid #e6e6e6;margin-bottom:20px;cursor:pointer;' onclick='zahlungsmethode_auswaehlen("+i+")'>";
			float_=0;
		}
		
		box=box+"<div style='width:270px;height:60px;background-color:#ff761a;float:left;'>";

		box=box+"<div style='margin-left:20px;margin-top:20px;color:#ffffff;float:left;'>"+zahlungsmethoden[i].name+"</div></div>";
		if(zahlungsmethoden[i].cardtype=="visa")
			box=box+"<div style='margin-left:20px;margin-top:25px;color:#000000;float:left;'><b><img src='/static/"+zahlungsmethoden[i].cardtype+"_card.png'  width='40' height='15'></b></div>";
		else
			box=box+"<div style='margin-left:20px;margin-top:15px;color:#000000;float:left;'><b><img src='/static/"+zahlungsmethoden[i].cardtype+"_card.png'  width='50' height='35' ></b></div>";
		box=box+"<div style='margin-left:10px;margin-top:30px;color:#000000;float:left;'>****-****-****-"+zahlungsmethoden[i].kreditkartennummer+"</div>";
		box=box+"<div style='margin-left:15px;margin-top:30px;color:#000000;float:left;'>"+zahlungsmethoden[i].ablaufmonat+" "+zahlungsmethoden[i].ablaufjahr+"</div>"
		box=box+"<div class='ausgewaehltes_zahlungsmittel' style='margin-top:120px;text-align:center;font-style:italic;'></div></div>";
		//box=box+"<div class='kreditkarte_loeschen' onclick='kreditkarte_loeschen()'><b>X</b></div>";


		document.getElementsByClassName("zahlung")[1].style.display="none";
		document.getElementsByClassName("zahlung")[2].style.display="none";

		//document.getElementsByClassName("button_check")[1].style.display="none";
		i=i+1;
		
	}

	document.getElementById("kreditkarten").innerHTML=box+"<br><br><div class='neue_kreditkarte_hinzufuegen_check' style='margin-top:"+zaehler*170+"px' onclick='kreditkarte_hinzufuegen()'>Neue Kreditkarte hinzufügen</div><div id='kreditkarten_hinzufuegen' style='display:none;margin-top:"+zaehler*170+"px'></div>";
	kreditkarten_anzeigen()
	zahlungsmethode_auswaehlen(ausgewaehlt)
 }
 
 
 function kreditkarte_hinzufuegen()
 {
	 document.getElementById("kreditkarten_hinzufuegen").style.display="block"
	 document.getElementsByClassName("neue_kreditkarte_hinzufuegen_check")[0].style.display="none"
 }
 
 function kreditkarten_abbrechen()
 {
	 document.getElementById("kreditkarten_hinzufuegen").style.display="none"
	 document.getElementsByClassName("neue_kreditkarte_hinzufuegen_check")[0].style.display="block"
 }
 
 
 
 
 
 
 function zahlungsmethode_auswaehlen(index)
 {

	 
	 i=0;

	while(i<=zahlungsmethoden.length-1)
	{

		
		if(index==i)
		{

			document.getElementsByClassName("zahlungsmethoden_anzeigen")[i].style.borderColor="#FFD700";
			document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[i].innerHTML="Ausgewähltes Zahlungsmittel";
			zahlungsoption=zahlungsmethoden[i].zahlungsoption;
			name_karteninhaber=zahlungsmethoden[i].name;
			kreditkarten_nummer__=zahlungsmethoden[i].kreditkartennummer;

			ablaufdatum=zahlungsmethoden[i].ablaufmonat+" "+zahlungsmethoden[i].ablaufjahr;
		}
		else
		{
			document.getElementsByClassName("zahlungsmethoden_anzeigen")[i].style.borderColor="#e6e6e6";
			document.getElementsByClassName("ausgewaehltes_zahlungsmittel")[i].innerHTML="";
		}
		
		i=i+1;
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


	if(key_==48 || key_==49 || key_==50 || key_==51 || key_==52 || key_==53 || key_==54 || key_==55 || key_==56 || key_==57 || key_==9 || key_=="")
	
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
 
 
