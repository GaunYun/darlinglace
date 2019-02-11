var address;	 
var strasse;
var nummer;
var plz;
var stadt;  
var vorname;
var nachname;
var land;
var telefonnummer;
var apt;
var unternehmensdetails;
var allowed_countries;

var output_adresse_clicked;
var output_adresse_show;
	 var ausgefuellt; 	
	 var adresse_index;
	 var autocomplete=new Array(2);

var lieferhinweise;
var show_error_message_google;


function load_error_message_google_variable()
{
	show_error_message_google="true";
	
}

		 var componentForm = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',

  postal_code: 'short_name'
      };
	  

    	  
    initialize = function () {
	allowed_countries=JSON.parse(document.getElementsByClassName("allowed_countries")[0].innerHTML)	 

	var input = document.getElementsByClassName('adresse_input')
	 add_google_maps(input,allowed_countries,0)	
	 add_google_maps(input,allowed_countries,1)	

}



function add_google_maps(input,allowed_countries,j)
{
		     var options = {
	            componentRestrictions: {country: ['de','at','ch']}
	        };
			autocomplete[j] =new Array; 
	        autocomplete[j] = new google.maps.places.Autocomplete(input[j], options)
			autocomplete[j].inputId = input[j].id;



       		autocomplete[j].addListener('place_changed',  function(){
			

			var place = this.getPlace();

			var i=0;
			strasse="";
			nummer="";
			plz="";
			stadt="";
			land=""
			


			var components = place.address_components;
		    for (var i = 0, component; component = components[i]; i++) {
		        console.log(component);
		        if (component.types[0] == 'country') 
		        {
		            land = component['long_name'];
		        }
		        if (component.types[0] == 'route') 
		        {
		            strasse = component['long_name'];
		        }
		        if (component.types[0] == 'street_number') 
		        {
		            nummer = component['long_name'];
		        }
		        if (component.types[0] == 'postal_code') 
		        {
		            plz = component['long_name'];
		        }
		        if (component.types[0] == 'locality') 
		        {
		            stadt = component['long_name'];
		        }
		    }


			k=0;
			erlaubt="nein";
			while(k<=allowed_countries.length-1)
			{
				if(land.toLowerCase()==allowed_countries[k].land.toLowerCase())
					erlaubt="ja";
				k=k+1;	
			}



					document.getElementsByClassName('adresse_input')[j].value= strasse;
					felder_adresse_zuruecksetzen_adresse(0,j);
					document.getElementsByClassName('adresse')[j*4].value= nummer;
					felder_adresse_zuruecksetzen_adresse(1,j);
					document.getElementsByClassName('adresse')[j*4+2].value = plz;
					felder_adresse_zuruecksetzen_adresse(2,j);
					document.getElementsByClassName('adresse')[j*4+1].value = stadt;
					felder_adresse_zuruecksetzen_adresse(3,j);
					document.getElementsByClassName('adresse')[j*4+3].value = land;
					felder_adresse_zuruecksetzen_adresse(4,j);
	
		
		});	
	
}



    
    google.maps.event.addDomListener(window, 'load', initialize);
	
    submitform = function () {
		
        searchplace = autocomplete.getPlace();
        console.log(searchplace.name);
		
		
    }
	
	
	

	


function show_maps(standard_rechnungsadresse,standard_lieferadresse)
{
	document.getElementById("total_address").innerHTML=""
	geocoder = new google.maps.Geocoder();
	adressbuch=JSON.parse(document.getElementsByClassName("adressbuch_daten")[0].innerHTML)
	if(standard_rechnungsadresse==standard_lieferadresse)
		max=0;
	else
		max=1;

	if(max==0)
		address_1=adressbuch[standard_rechnungsadresse].strasse+" "+adressbuch[standard_rechnungsadresse].hausnummer+", "+adressbuch[standard_rechnungsadresse].plz+" "+adressbuch[standard_rechnungsadresse].stadt+", "+adressbuch[standard_rechnungsadresse].land
	else
	{
		address_1=adressbuch[standard_rechnungsadresse].strasse+" "+adressbuch[standard_rechnungsadresse].hausnummer+", "+adressbuch[standard_rechnungsadresse].plz+" "+adressbuch[standard_rechnungsadresse].stadt+", "+adressbuch[standard_rechnungsadresse].land
		
		address_2=adressbuch[standard_lieferadresse].strasse+" "+adressbuch[standard_lieferadresse].hausnummer+", "+adressbuch[standard_lieferadresse].plz+" "+adressbuch[standard_lieferadresse].stadt+", "+adressbuch[standard_lieferadresse].land
	}
		//		document.getElementsByClassName("side3")[0].innerHTML="<div style='float:left;margin-left:10px;margin-Top:10px;' >"+adressbuch[standard_rechnungsadresse].strasse+" "+adressbuch[standard_rechnungsadresse].hausnummer+"<br>"+adressbuch[standard_rechnungsadresse].plz+" "+adressbuch[standard_rechnungsadresse].stadt+"</div>";
				
				
				
		//						box=box+"<div class='side3' onclick='adresse_bearbeiten(1,"+standard_rechnungsadresse+","+standard_lieferadresse+")'></div></div>"
	document.getElementById("total_address").innerHTML="<div class='haelfte_rechnungsadresse'></div><div class='haelfte_lieferadresse'></div><br><br><br>";
	
	rechnungsadresse="<b>Rechnungsadresse</b><input id='existent_rechnungsadresse' type='hidden' value='"+standard_rechnungsadresse+"' /><br>";

	
	rechnungsadresse=rechnungsadresse+adressbuch[standard_rechnungsadresse].anrede+" "+adressbuch[standard_rechnungsadresse].vorname+" "+adressbuch[standard_rechnungsadresse].nachname+"<br>";
	if(adressbuch[standard_rechnungsadresse].unternehmensdetails!="")
		rechnungsadresse=rechnungsadresse+adressbuch[standard_rechnungsadresse].unternehmensdetails	
	rechnungsadresse=rechnungsadresse+adressbuch[standard_rechnungsadresse].strasse+" "+adressbuch[standard_rechnungsadresse].hausnummer+"<br>"
	rechnungsadresse=rechnungsadresse+adressbuch[standard_rechnungsadresse].plz+" "+adressbuch[standard_rechnungsadresse].stadt+"<br>"
	rechnungsadresse=rechnungsadresse+adressbuch[standard_rechnungsadresse].land+"<br>"
	rechnungsadresse=rechnungsadresse+"T: +49 "+adressbuch[standard_rechnungsadresse].telefonnummer+"<br>"
	rechnungsadresse=rechnungsadresse+"<br><button class='adresse_aendern' onclick='adresse_laden("+standard_rechnungsadresse+","+standard_lieferadresse+")'>Ändern</button><br><br>"



	lieferadresse="<b>Lieferadresse</b><input id='existent_lieferadresse' type='hidden' value='"+standard_lieferadresse+"' /><br>";

	lieferadresse=lieferadresse+adressbuch[standard_lieferadresse].anrede+" "+adressbuch[standard_lieferadresse].vorname+" "+adressbuch[standard_lieferadresse].nachname+"<br>";
	if(adressbuch[standard_lieferadresse].unternehmensdetails!="")
		lieferadresse=lieferadresse+adressbuch[standard_lieferadresse].unternehmensdetails	
	lieferadresse=lieferadresse+adressbuch[standard_lieferadresse].strasse+" "+adressbuch[standard_lieferadresse].hausnummer+"<br>"
	lieferadresse=lieferadresse+adressbuch[standard_lieferadresse].plz+" "+adressbuch[standard_lieferadresse].stadt+"<br>"
	lieferadresse=lieferadresse+adressbuch[standard_lieferadresse].land	+"<br>"
	lieferadresse=lieferadresse+"T: +49 "+adressbuch[standard_lieferadresse].telefonnummer+"<br>"
	lieferadresse=lieferadresse+"<br><button class='adresse_aendern' onclick='adresse_laden("+standard_rechnungsadresse+","+standard_lieferadresse+")'>Ändern</button><br><br>"
	
	document.getElementsByClassName("haelfte_rechnungsadresse")[0].innerHTML=rechnungsadresse
	document.getElementsByClassName("haelfte_lieferadresse")[0].innerHTML=lieferadresse	
	document.getElementById("check_address").style.display="none";
		document.getElementsByClassName("sidebar_checkout")[0].style.display ="block";	
		document.getElementsByClassName("headline")[2].style.display ="block";		
		document.getElementsByClassName("zahlungs_container")[0].style.display ="block";
 	document.getElementById("kreditkarten").style.display="block";
}


function make_address_validation(i,existent_rechnungsadresse,existent_lieferadresse,wie_viele_adressen_checken)
{
	strasse=document.getElementsByClassName('adresse_input')[i].value;
		hausnummer=document.getElementsByClassName('adresse')[i*4].value
		plz=document.getElementsByClassName('adresse')[i*4+2].value;
		stadt=document.getElementsByClassName('adresse')[i*4+1].value;
		land=document.getElementsByClassName('adresse')[i*4+3].value;
		
		address=strasse+" "+hausnummer+", "+plz+" "+stadt+", "+land



											if(i==wie_viele_adressen_checken)
											{
						
												adressbuch_aktualisieren(wie_viele_adressen_checken,existent_rechnungsadresse,existent_lieferadresse);
											}
											else
												make_address_validation(1,existent_rechnungsadresse,existent_lieferadresse,1);
	/*											
												
			geocoder.geocode( { 'address': address}, function(results, status) {	

				feedback=false;
				
				if (status == google.maps.GeocoderStatus.OK) 
				{
					feedback=true
				 var k=0;
				 var strasse_eingegeben=0;
				 var hausnummer_eingegeben=0;
				 var plz_eingegeben=0;
				 var stadt_eingegeben=0;
				 var land_eingegeben=0;
				 while (k<=results[0].address_components.length-1)
				{

				  if (results[0].address_components[k].types[0]=="route")
				  {
					  strasse_=results[0].address_components[k]['long_name'];[componentForm[results[0].address_components[k].types[0]]];
					  
					  strasse_eingegeben=1;
				  }
				  if (results[0].address_components[k].types[0]=="street_number")			  
				  {
					  hausnummer_=results[0].address_components[k]['long_name'];[componentForm[results[0].address_components[k].types[0]]];
					  
					  hausnummer_eingegeben=1;
				  }
				  if (results[0].address_components[k].types[0]=="postal_code")			  
				  {
					  plz_=results[0].address_components[k]['long_name'];[componentForm[results[0].address_components[k].types[0]]];
					  
					  plz_eingegeben=1;		
				  }
				  if (results[0].address_components[k].types[0]=="locality")			  
				  {
					  stadt_=results[0].address_components[k]['long_name'];[componentForm[results[0].address_components[k].types[0]]];
					  
					  stadt_eingegeben=1;		  
				  }
				  if (results[0].address_components[k].types[0]=="country")			  
				  {
					  land_=results[0].address_components[k]['long_name'];[componentForm[results[0].address_components[k].types[0]]];
					  land_eingegeben=1;		  
				  }			  
				  k=k+1;
				}
				ausgefuellt=strasse_eingegeben+hausnummer_eingegeben+plz_eingegeben+stadt_eingegeben+land_eingegeben;
		
				if(strasse_eingegeben==0 && show_error_message_google=="true")
				{
					button_logo("1","check_address_text","check_address_logo","check_address")
					alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Straßendetails. Wir konnten die Straße nicht finden.")
					document.getElementsByClassName("adresse_input")[i].style.border="1px solid red";	
					document.getElementsByClassName("address_input_header")[i*5].style.color="red";		
					ausgefuellt=0;
					show_error_message_google="false";
					

				}
		
				if(hausnummer_eingegeben==0 && show_error_message_google=="true")
				{
					button_logo("1","check_address_text","check_address_logo","check_address")
					alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Straßendetails. Wir konnten die Straße nicht finden.")
					document.getElementsByClassName("adresse")[i*4].style.border="1px solid red";	
					document.getElementsByClassName("address_input_header")[i*5+1].style.color="red";		
					ausgefuellt=0;

				}
	
				if(plz_eingegeben==0 && show_error_message_google=="true")
				{
					button_logo("1","check_address_text","check_address_logo","check_address")
					alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Ortsangaben. Wir konnten die Straße nicht finden.")
					document.getElementsByClassName("adresse")[i*4+2].style.border="1px solid red";	
					document.getElementsByClassName("address_input_header")[i*5+2].style.color="red";		
					ausgefuellt=0;
					show_error_message_google="false";
				}
				if(stadt_eingegeben==0 && show_error_message_google=="true")
				{
					button_logo("1","check_address_text","check_address_logo","check_address")
					alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Ortsangaben. Wir konnten die Straße nicht finden.")
					document.getElementsByClassName("adresse")[i*4+1].style.border="1px solid red";	
					document.getElementsByClassName("address_input_header")[i*5+1].style.color="red";		
					ausgefuellt=0;
					show_error_message_google="false";

				}
				if(land_eingegeben==0 && show_error_message_google=="true")
				{
					button_logo("1","check_address_text","check_address_logo","check_address")
					alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Angaben zum Land. Wir konnten das Land nicht finden.")
					document.getElementsByClassName("adresse")[i*4+3].style.border="1px solid red";	
					document.getElementsByClassName("address_input_header")[i*5+4].style.color="red";		
					ausgefuellt=0;
					show_error_message_google="false";
				}
				
				if (ausgefuellt==5)
				{
						if(strasse_+" "+hausnummer_!=strasse+" "+hausnummer && show_error_message_google=="true")
						{
							button_logo("1","check_address_text","check_address_logo","check_address")		
							alert_userdata("STRASSENANGABEN ÜBERPRÜFEN","Deine eingegebene Straße ist nicht korrekt. Bitte überprüfe unseren Vorschlag.")
							document.getElementsByClassName("adresse_input")[i].style.border="1px solid red";	
							document.getElementsByClassName("adresse_input")[i].value=strasse_
							document.getElementsByClassName("address_input_header")[i*5].style.color="red";		
							
							document.getElementsByClassName("adresse")[i*4].style.border="1px solid red";	
							document.getElementsByClassName("adresse")[i*4].value=hausnummer_
							document.getElementsByClassName("address_input_header")[i*5+1].style.color="red";	
							show_error_message_google="false";
						}
						else
						{
						
							if(plz_!=plz && show_error_message_google=="true")
							{
								button_logo("1","check_address_text","check_address_logo","check_address")
								alert_userdata("POSTLEIZTAHL ÜBERPRÜFEN","Deine eingegebene Postleitzahl ist nicht korrekt. Bitte überprüfe unseren Vorschlag.")
								document.getElementsByClassName("adresse")[i*4+2].style.border="1px solid red";	
								document.getElementsByClassName("adresse")[i*4+2].value=plz_
								document.getElementsByClassName("address_input_header")[i*5+2].style.color="red";	
								show_error_message_google="false";
							}
							else
							{
								if(stadt_!=stadt && show_error_message_google=="true")
								{
									button_logo("1","check_address_text","check_address_logo","check_address")
									alert_userdata("STADT ÜBERPRÜFEN","Deine eingegebene Stadt ist nicht korrekt. Bitte überprüfe unseren Vorschlag.")
									document.getElementsByClassName("adresse")[i*4+1].style.border="1px solid red";	
									document.getElementsByClassName("adresse")[i*4+1].value=stadt_
									document.getElementsByClassName("address_input_header")[i*5+1].style.color="red";	
									show_error_message_google="false";	
								}
								else
								{ 
									if(land_!=land && show_error_message_google=="true")
									{
										button_logo("1","check_address_text","check_address_logo","check_address")
										alert_userdata("LAND ÜBERPRÜFEN","Dein eingegebenes Land ist nicht korrekt. Bitte überprüfe unseren Vorschlag.")
										document.getElementsByClassName("adresse")[i*4+3].style.border="1px solid red";	
										document.getElementsByClassName("adresse")[i*4+3].value=land_
										document.getElementsByClassName("address_input_header")[i*5+4].style.color="red";	
										show_error_message_google="false";
									}
									else
									{
										j=0;
										erlaubt="nein";
										while(j<=allowed_countries.length-1)
										{
											if(land==allowed_countries[j].land)
												erlaubt="ja";
											j=j+1;	
										}

											if(i==wie_viele_adressen_checken)
											{
						
												adressbuch_aktualisieren(wie_viele_adressen_checken,existent_rechnungsadresse,existent_lieferadresse);
											}
											else
												make_address_validation(1,existent_rechnungsadresse,existent_lieferadresse,1);


										
									}
								}
							}
						}				
					}				
				}

				if(feedback==false)
				{
					button_logo("1","check_address_text","check_address_logo","check_address")
					alert_userdata("ADRESSE NICHT GEFUNDEN","Leider konnten wir Deine Adresse nicht finden. Bitte überprüfe Deine Angaben.")	
				}
				return feedback;
		    });

	
 */
	
	
}


  function check_addresses() {
	  geocoder = new google.maps.Geocoder();	 
	if(check_whether_address_fields_were_filled_out()==0)
	{

		button_logo("0","check_address_text","check_address_logo","check_address")
		document.getElementById("buttons_address_text").innerHTML="";
		if(document.getElementsByClassName ("checkbox_abweichende_lieferadresse")[0].checked==true)	
		{	
			$.ajax({
			timeout:15000,
 			error: function(){			
 						button_logo("1","check_address_text","check_address_logo","check_address")
	},
			type: "POST",
			url: "/check_mobilnummer/",
			dataType: "json",
			data: { "telefonnummer": document.getElementsByClassName("adresse_mobilnummer")[0].value,"telefonnummer2": document.getElementsByClassName("adresse_mobilnummer")[1].value},
			success: function(data) {
						telefonnummern=JSON.parse(data)
						if(telefonnummern[0].telefonnummer=="")
						{
							button_logo("1","check_address_text","check_address_logo","check_address")
							alert_userdata("MOBILNUMMER NICHT KORREKT","Die eingegebene Mobilnummer ist nicht gültig. Bitte gib eine andere Mobilnummer an.")
							document.getElementsByClassName("adresse_mobilnummer")[0].style.border="1px solid red";	
							document.getElementsByClassName("address_mobilnummer_input_header")[0].style.color="red";	
						}
						else
						{
							if(telefonnummern[0].telefonnummer2=="")
							{
								button_logo("1","check_address_text","check_address_logo","check_address")
								alert_userdata("MOBILNUMMER NICHT KORREKT","Die eingegebene Mobilnummer ist nicht gültig. Bitte gib eine andere Mobilnummer an.")
								document.getElementsByClassName("adresse_mobilnummer")[1].style.border="1px solid red";	
								document.getElementsByClassName("address_mobilnummer_input_header")[1].style.color="red";
							}
							else
							{
								document.getElementsByClassName("adresse_mobilnummer")[1].value=telefonnummern[0].telefonnummer2;
								document.getElementsByClassName("adresse_mobilnummer")[0].value=telefonnummern[0].telefonnummer;
								if(document.getElementById("existent_rechnungsadresse").value==document.getElementById("existent_lieferadresse").value)
									existent_lieferadresse="nein"
								else
									existent_lieferadresse=document.getElementById("existent_lieferadresse").value;		
								existent_rechnungsadresse=document.getElementById("existent_rechnungsadresse").value;

								make_address_validation(1,existent_rechnungsadresse,existent_lieferadresse,1)
							}
						}
				}
			})
		}
		else
		{
			$.ajax({
			type: "POST",
			url: "/check_mobilnummer/",
			dataType: "json",
			data: { "telefonnummer": document.getElementsByClassName("adresse_mobilnummer")[0].value },
			success: function(data) {
						telefonnummern=JSON.parse(data)

						if(telefonnummern[0].telefonnummer=="")
						{
							button_logo("1","check_address_text","check_address_logo","check_address")
							alert_userdata("MOBILNUMMER NICHT KORREKT","Die eingegebene Mobilnummer ist nicht gültig. Bitte gib eine andere Mobilnummer an.")
							document.getElementsByClassName("adresse_mobilnummer")[0].style.border="1px solid red";	
							document.getElementsByClassName("address_mobilnummer_input_header")[0].style.color="red";

						}
						else
						{

							document.getElementsByClassName("adresse_mobilnummer")[0].value=telefonnummern[0].telefonnummer;
							existent_rechnungsadresse=document.getElementById("existent_rechnungsadresse").value;
							make_address_validation(0,existent_rechnungsadresse,"",0)
						}
				}
			})
		}	
	}
}
  
  

	  
	  
  
  
  function adresse_bearbeiten(index,standard_rechnungsadresse,standard_lieferadresse)
  {


		output_adresse_clicked=1;

		i=0;
		box="";
		while(i<=adressbuch.length-1)
		{
			adresse= adressbuch[i].strasse+" "+adressbuch[i].hausnummer+"<br>"+adressbuch[i].plz+" "+adressbuch[i].stadt

			if(index==0 && adressbuch[i].standard_rechnungsadresse=="ja")
			{
				box=box+"<div class='output_adresse' style='border:1px solid #e65c00' ><div style='float:left;margin-left:10px;margin-Top:10px;'>"+adresse+"</div><div style='float:left;color:red;margin-Top:20px;cursor:pointer;margin-left:20px;' onclick='adresse_laden("+standard_rechnungsadresse+","+standard_lieferadresse+")'>Bearbeiten</div></div>";
			}
			else
				box=box+"<div class='output_adresse' style='border:1px solid #e65c00' onclick='adresse_wechseln("+standard_rechnungsadresse+","+standard_lieferadresse+","+i+","+index+")' ><div style='float:left;margin-left:10px;margin-Top:10px'>"+adresse+"</div></div></div>";

			i=i+1;
		}

	box=box+"<div class='output_adresse' style='border-bottom:1px solid #e65c00;border-left:1px solid #e65c00;border-right:1px solid #e65c00;cursor:pointer;' onclick='new_address()' ><div style='float:left;margin-top:5px;font-weight:bold;margin-left:10px;'>+ Neue Adresse</div></div>";		
	 document.getElementsByClassName("side3")[0].innerHTML=box;


  }
  
 function new_address()
 {
 	adresse_anzeigen("nein","nein")
 }
  
  function adresse_wechseln(standard_rechnungsadresse,standard_lieferadresse,i,index)
  {
	if(index==0)
		standard_rechnungsadresse=i
	else
		standard_lieferadresse=i
	fuege_adressen_hinzu(hinzufuegen,standard_rechnungsadresse,standard_lieferadresse,index,wie_viele_adressen_checken,"","","")

  }