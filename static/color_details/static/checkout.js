	
	var zutaten=new Array(50);
   var gerichte = new Array(20); 
   var cart=new Array(10);
   var max;
   var kreditkarten_nummer=new Array(15);
   var kreditkarten_nummer_stelle;
   var string_;
   var datum_in_cart=new Array(12);
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
	var name_karteninhaber;
	var fahrer_kapaziaet;
	   
	   

      


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

function adresse_anzeigen(strasse_, nummer_, apt_, plz_, stadt_, vorname_, nachname_, telefonnummer_, unternehmensdetails_)
{


	if (strasse_=="")
	{
		var box="<div id='locationField'<div class='address_text' style='float:left;'>Adresse<br><input class='adresse' id='strasse' placeholder='Adresse eingeben'";
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
		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(6)' onkeydown='felder_adresse_zuruecksetzen(6)'></input></div></div><br>";
	}
	else
	{
		
		var box="<div id='locationField'<div class='address_text' style='float:left;'>Adresse<br><input class='adresse' id='strasse' placeholder='Adresse eingeben' value='"+strasse_+" "+nummer+"'";

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

		box=box+"type='text' onkeyup='felder_adresse_zuruecksetzen(6)' onkeydown='felder_adresse_zuruecksetzen(6)' value='"+telefonnummer_+"'></input></div></div><br>";
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
		
		var strasse=document.getElementById("strasse").value;
		
		var plz=document.getElementById("postal_code").value;
		var stadt=document.getElementById("locality").value;
		
		
		

		initMap(strasse,plz,stadt);
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


function bestellen()
{	

	//alert(document.getElementsByClassName("karten_css")[0].value)
	item=strasse+" "+nummer+","+apt+","+stadt+","+plz+","+unternehmensdetails+","+vorname+","+nachname+","+telefonnummer+",document.getElementById('lieferdetails_textarea').innerHTML,"+zahlungsoption+","+name_karteninhaber+","+kreditkarten_nummer__+","+ablaufdatum+","+pruefnummer+","+preis_+","+"2.95"+","+rabatt_+","+document.getElementById("gutschein_input").value.toUpperCase; 
			$.ajax({
			type: "POST",
			url: "/polls/hello/bestellen/",
			dataType: "json",
			data: { "item":  item },
			success: function(data) {
					
		

			}
		});
		

		
		
	
	if(document.getElementsByClassName("button_check")[0].style.display=="none" && document.getElementsByClassName("button_check")[1].style.display=="none")
	{
		alert("bestellt");
		
		

		window.top.location.href = "/polls/hello/0/"; 
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




function preis_aufrufen()
{
	
	
	var i=0;
	var preis=0;

	while(i<=cart.length-1)
	{
		if(cart[i][0]!=0)
		{
			preis=preis+gericht_details_ermitteln(cart[i][0],6)*cart[i][1]
			
			
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


function bestelluebersicht(rabatt)
{
	



	var preis=preis_aufrufen()
	var gesamt=preis+2.95+rabatt;

	
	preis_=	replace_dot_comma(preis);
	rabatt_=	replace_dot_comma(rabatt);
	preis_gesamt=	replace_dot_comma(gesamt);

	var maxim= document.getElementsByClassName("bestellung");
	
	var uebersicht="<div style='float:left;'>Bestellung:</div><div style='float:right;'>"+preis_+" EUR</div><br>";
	uebersicht=uebersicht+"<div style='float:left;'>Lieferkosten:</div><div style='float:right;'>2,95 EUR</div><br>";

	if(rabatt!=0)
	{
		uebersicht=uebersicht+"<div style='float:left;'>Rabatt:</div><div style='float:right;'>"+rabatt_+" EUR</div><br>";	
		
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
	
	if(document.getElementById("gutschein_button_id").value!="Abbrechen")
	{

		$.ajax({
			type: "POST",
			url: "/polls/hello/gutschein_einloesen/",
			dataType: "json",
			data: { "item":  document.getElementById("gutschein_input").value.toUpperCase() },
			success: function(data) {
				if (data!= "")
				{	
					document.getElementById("gutschein_button_id").style.backgroundColor="#808080";
					document.getElementById("gutschein_button_id").value="Abbrechen";
					document.getElementById("gutschein_input").disabled=true;
					rabatt_=parseFloat(data);
					bestelluebersicht(parseFloat(data));
				}
				else
				{
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
	}
	
}

function gutschein_code_reset()
{
	
	document.getElementById("gutschein_button_id").style.backgroundColor="#ff761a";
	document.getElementById("gutschein_button_id").value="Überprüfen";
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


 function warenkorb_ermitteln(daten)
 {

	 var arr1 = daten.split(";");
	var arr2 = [];
	for (i = 0; i < arr1.length; i++) {
        arr2[i]=arr1[i].split(",");
	}  
	
	
	

	
	cart=arr2;


	 var i=0;
	 cart_gesamt=0;
	 


	 
	 while (i<=cart.length-1)
	 {
		 	 
		 if (parseInt(cart[i][1])>0)
			cart_gesamt=cart_gesamt+parseInt(cart[i][1]);
		
		i=i+1;
	 }

	if (cart_gesamt!=0)
		document.getElementsByClassName("cart_text")[0].innerHTML=cart_gesamt;
	else
		document.getElementsByClassName("cart_text")[0].innerHTML="";
 }
 
 
  function gerichte_ermitteln(daten)
 {
	 var arr1 = daten.split(";;;");
	var arr2 = [];
	for (i = 0; i < arr1.length; i++) {
        arr2[i]=arr1[i].split(";;");
	}  
	
	

	
	gerichte=arr2;
}
 
 



 
 window.onload=function fenster_aufrufen()
 {
	gutschein_code_reset();

	adresse_anzeigen("","","","","","","","","");

	max=2;

	
	
	gerichte_anzeigen();

	bestelluebersicht(0);
	

	document.getElementById("gutschein_input").style.display ="none";
	document.getElementById("gutschein_button_id").style.display ="none";
	document.getElementsByClassName("unternehmensdetails")[0].style.display="none";
	document.getElementsByClassName("unternehmensdetails")[1].style.display="none";
	
	

	
	var i=0;
	while(i<=15)
	{	
		kreditkarten_nummer[i]=new Array;
		i=i+1;
	}
	kreditkarten_nummer_stelle=0;

	
	//
	zahlung_click(0);

	stelle=0;
	string_="";
	
 }
 
 function gericht_details_ermitteln(name,index)
 {
	 
	 j=0;
	 while (j<=gerichte.length)
	 {
		 if (gerichte[j][1]==name)
			 return gerichte[j][index]
		 
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

function fahrer_kapa_anzeigen(daten_)
{
	
	
	var arr1 = daten_.split(";;;");
	var arr2 = [];
	for (i = 0; i < arr1.length; i++) {
        arr2[i]=arr1[i].split(";;");
	}  
	
	

	
	fahrer_kapaziaet=arr2;

	
	
}


function vorbestellung_abrufen(datum_,uhrzeit_)
{
	
	var i=0;
	var status_="";
	while(i<=fahrer_kapaziaet.length-1)
	{
		if(fahrer_kapaziaet[i][0]==datum_ && fahrer_kapaziaet[i][1]==uhrzeit_)
			if (fahrer_kapaziaet[i][0]!=" ")
				status_=fahrer_kapaziaet[i][2];
		i=i+1;
	}
	
	if (status_!=" ")
		if(status_!=0)
			return "Noch "+status_+" Bestellungen möglich";
		else
			return "Keine Bestellungen mehr möglich";
	else
		return "";
	

}
 

 
 function gerichte_anzeigen()
 {
	
	
	
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
	

	cart.sort(compareLastColumn);

	while (i<=cart.length-1)
	{
		vorhanden=0;
		j=0;
		stelle="";
		while (j<=12)
		{
			if(cart[i][2]==datum_in_cart[j][0] && cart[i][2]!="")	
				vorhanden="1";
			if(datum_in_cart[j][0]=="" && stelle=="")
				stelle=j;

			j=j+1;
		}

		if(vorhanden==0 && stelle != "")
		{

			datum_in_cart[stelle][0]=cart[i][2];
			datum_in_cart[stelle][1]=cart[i][5];
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
		
			var i=0;
			
			
			box=box+"<div class='datum' id='inhalt_datum'>"+datum_in_cart[h][0]+"</div>";	 
			datum_text=new Array(4)
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
			while (f<=4)
			{
				if (vorbestellung_abrufen(datum_in_cart[h][0],datum_text[f])=="Keine Bestellungen mehr möglich")
					box=box+"<div class='zeitbox' 	style='opacity:0.3;background-Color:#e6e6e6;' >"+datum_text[f]+"</div>";
				else
					box=box+"<div class='zeitbox' id='"+parseInt(h*5+0)+"' onclick='datum_click("+parseInt(h*5)+","+parseInt(h*5+f)+")'	 >"+datum_text[f]+"</div>";
				
				f=f+1;
			}

			
			
			
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


				if(cart[i][0]!="" && cart[i][2]==datum_in_cart[h][0])
				{	

					box=box+"<div style='float:left; font-size:12px;width:575px;'><div style='float:left;'><a href='/polls/hello/"+cart[i][3]+"/"+cart[i][0]+"/' style='textDecoration:none;'><img src='"+gericht_details_ermitteln(cart[i][0],5)+"' style='width:45px;height:45px;float:left;'/><div style='margin-left:10px;float:left;'>"+cart[i][0]+"<br><div style='float:left;font-size:12px;'>"+replace_dot_comma(parseFloat(gericht_details_ermitteln(cart[i][0],6)))+" EUR</div> </div></a></div>";
					box=box+"<div style='float:right;'><div style='float:left;'>Anzahl</div><select class='select_anzahl' style='margin-left:10px;float:left;width:50px;' onchange='change_cart("+i+")' >";
					
					var w=0;
					
					
					min_1=parseInt(verfuegbarkeits_check(gericht_id_suchen_id(i)))+parseInt(cart[i][1]);

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

				if(cart[i][0]!="" && cart[i][2]==datum_in_cart[j][0])
				{	
					
					document.getElementsByClassName("select_anzahl")[nummer].selectedIndex=cart[i][1];
					nummer=nummer+1;
				}
				j=j+1;
			}
			i=i+1;	
		 
		 }
		
 }
 
 
 
  function verfuegbarkeits_check(i)
 {

	return (parseInt(gerichte[i][31])-parseInt(gerichte[i][32])-parseInt(gerichte[i][33])-parseInt(gerichte[i][34]));
 }
 
 
  function gericht_id_suchen_id(index)
 {
	
	 j=0;

	
		 var j=0;
		 while (j<=gerichte.length-1)
		 {

			 if(gerichte[j][30]==cart[index][2] && gerichte[j][1]==cart[index][0])
			 {

				 return j
			 }
			 
			 j=j+1;
			 
		 }

	 
	 
	 
 }
 
 
 
 function change_cart(clicked_id)
 {
	 
	 
		
	if(cart[clicked_id][1]!=document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex)
	{	
			
		 cart[clicked_id][1]=document.getElementsByClassName("select_anzahl")[clicked_id].selectedIndex;
		 
		$.ajax({
			type: "POST",
			url: "/polls/hello/add/",
			dataType: "json",
			data: { "item": cart[clicked_id][0]+","+cart[clicked_id][1]+","+cart[clicked_id][2]+","+cart[clicked_id][3] },
			success: function(data) {
					if(cart=="")
		window.location= "/polls/hello/0/";

			}
		});
		
		 if(cart[clicked_id][1]==0)
		 { 	
			cart.splice(clicked_id,1);
			
			gerichte_anzeigen();
			
		 }
		 bestelluebersicht(0);
			

		//select_options();*/

	}
 }
 
 function select_options()
 {
	 
	 var i=0;
	 
	 while(i<=max)
	 {
		document.getElementsByClassName("select_anzahl")[i].selectedIndex=cart[i][0];
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
					clicked_id=i		
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
				url: "/polls/hello/change_timing/",
				dataType: "json",
				data: { "item": document.getElementsByClassName("datum")[clicked_id_first/5].innerHTML+","+document.getElementsByClassName("zeitbox")[i].innerHTML},
				success: function(data) {
						

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
		 
		kreditkarten_anzeigen();
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
	 while (i<=11)
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
	 
	 
	 
	box=box+"</select></div><div class='karten_text_css' style='float:right;'>Prüfnummer<br><input class='karten_css' onkeyup='felder_zuruecksetzen(4)' onkeydown='felder_zuruecksetzen(4)' type='text' maxlength='3' onchange='validate(event)'></input></div></div>";
	box=box+"<br><br><br><br><br><div style='float:right;'><input type='button' class='button_check' value='Überprüfen' onclick='kreditkarten_check()'></input></div><br><br><br><div id='buttons_credit_card' style='float:right;color:red;font-weight:bold;'></div> ";
	document.getElementById("kreditkarten").innerHTML=box;
	
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

	
	

 }
 
 
 function kreditkarten_check()
 {
	 


	 
	 kreditkarten_nummer_="";
	 ablaufdatum="";
	 kreditkarten_nummer__="";
	 
	 
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

		 ablaufdatum=document.getElementsByClassName("karten_css")[2].value;
		 ablaufdatum=ablaufdatum.substr(0,2);
		 ablaufdatum=ablaufdatum+"/"+document.getElementsByClassName("karten_css")[3].value;
		 pruefnummer=document.getElementsByClassName("karten_css")[4].value
		 name_karteninhaber=document.getElementsByClassName("karten_css")[0].value;
		 
		 var box="<div style='width:300px;height:130px;border:4px solid #FFD700;float:left;'>";
		 box=box+"<div style='width:300px;height:60px;background-color:#ff761a;float:left;'>";
		 box=box+"<div style='margin-left:20px;margin-top:20px;color:#ffffff;float:left;'><b>MasterCard</b></div>";
		 box=box+"<div style='margin-left:50px;margin-top:20px;color:#ffffff;float:left;'>"+document.getElementsByClassName("karten_css")[0].value+"</div></div>";
		 box=box+"<div style='margin-left:20px;margin-top:30px;color:#000000;float:left;'><b>Bild</b></div>";
		 box=box+"<div style='margin-left:50px;margin-top:30px;color:#000000;float:left;'>"+kreditkarten_nummer_+"</div>";
		 box=box+"<div style='margin-left:15px;margin-top:30px;color:#000000;float:left;'>"+ablaufdatum+"</div></div>";
		box=box+"<div class='kreditkarte_loeschen' onclick='kreditkarte_loeschen()'><b>X</b></div>";
		
		document.getElementsByClassName("zahlung")[1].style.display="none";
		document.getElementsByClassName("zahlung")[2].style.display="none";
		document.getElementsByClassName("button_check")[1].style.display="none";



		 document.getElementById("kartendetails_maske").innerHTML=box+"<br><br><br><br><br>";
	
	 }
	 
	 
 }
 
 function kreditkarte_loeschen()
 {
	document.getElementsByClassName("zahlung")[1].style.display="block";
	document.getElementsByClassName("zahlung")[2].style.display="block";	
	kreditkarten_anzeigen();
	 
 }
 
 
 function kreditkarten_show(evt)
 {

		
		
	var theEvent = evt || window.event;
	var key = theEvent.keyCode || theEvent.which;
	key = String.fromCharCode( key );
	var regex = /[0-9]|\./;
	
	

	if(key==0 || key==1 || key==2 || key==3 || key==4 || key==5 || key==6 || key==7 || key==8 || key==9 )
	
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
 
 