var address;	 
var strasse;
var nummer;
var plz;
var stadt;  
var vorname;
var nachname;
var telefonnummer;
var apt;
var unternehmensdetails;
var zugelassene_plz_max;  
var output_adresse_clicked;
var output_adresse_show;
	 var ausgefuellt; 	
	 var adresse_index;
var zugelassene_plz=new Array(100);
var lieferhinweise;


		 var componentForm = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',

  postal_code: 'short_name'
      };
	  
	
    initialize = function () {


		
				zugelassene_plz[0]=new Array;
		zugelassene_plz[0]="80337";
		zugelassene_plz[1]=new Array;
		zugelassene_plz[1]="58313";
		zugelassene_plz_max=1;
		
		 
		var input = document.getElementById('strasse');
		address=input;
        		
		var options = {
            
        };
		page_load(0);
        autocomplete = new google.maps.places.Autocomplete(input, options);
		page_load(1);
		autocomplete.addListener('place_changed',  function(){
		

		var place = autocomplete.getPlace();
		var i=0;
		strasse="";
		nummer="";
		plz="";
		stadt="";


		while (i<=place.address_components.length-1)
		{
			

			if (place.address_components[i].types[0]=="route")		  
				var strasse = place.address_components[i][componentForm[place.address_components[i].types[0]]];  

			  
			  if (place.address_components[i].types[0]=="street_number")
					nummer=place.address_components[i][componentForm[place.address_components[i].types[0]]]

			  
			  
			  if (place.address_components[i].types[0]=="postal_code")
			  {
			  	
				var plz = place.address_components[i][componentForm[place.address_components[i].types[0]]];  
				
				felder_adresse_zuruecksetzen(1);
				
				  
			  }
			  
			  if (place.address_components[i].types[0]=="locality")
			  {
				var stadt = place.address_components[i][componentForm[place.address_components[i].types[0]]];  
				felder_adresse_zuruecksetzen(2);

				  
			  }
			  
			  
			  i=i+1;			
			

		}
		if (nummer==strasse)
			nummer="";
		

		document.getElementById("strasse").value = strasse+" "+nummer;
		document.getElementById("postal_code").value = plz;
		document.getElementById("locality").value = stadt;


		});


    }
    
    google.maps.event.addDomListener(window, 'load', initialize);
	
    submitform = function () {
		
        searchplace = autocomplete.getPlace();
        console.log(searchplace.name);
		
		
    }
	
	
	
	var geocoder;
  var map;
  
  
  
  function initMap(strasse_,plz_,stadt_,vorname_,nachname_,telefonnummer_,unternehmensdetails_,lieferhinweise_) {

	page_load(0);
    geocoder = new google.maps.Geocoder();
   
	

    
	
	
	strasse=strasse_;
	plz=plz_;
	stadt=stadt_;

	vorname=vorname_;
	nachname=nachname_;
	telefonnummer=telefonnummer_;
	unternehmensdetails=unternehmensdetails_;
	lieferhinweise_=lieferhinweise;
	
	codeAddress();
	
	
  }
	
	
	



	  
	  
  function codeAddress() {

	  address=strasse+", "+plz+" "+stadt+", Germany";
	 
	//document.getElementById("output_adresse").value=strasse+", "+plz+" "+stadt;


    geocoder.geocode( { 'address': address}, function(results, status) {
		
	  if (status == google.maps.GeocoderStatus.OK) {
		
		 
		 var i=0;
		 var strasse_eingegeben=0;
		 var street_number_eingegeben=0;
		 var plz_eingegeben=0;
		 var stadt_eingegeben=0;
		 j=0;
		 while (i<=results[0].address_components.length-1)
		{
		  
		  if (results[0].address_components[i].types[0]=="route")
		  {
			 
			  strasse_=results[0].address_components[i][componentForm[results[0].address_components[i].types[0]]];
			  
			  strasse_eingegeben=1;
		  }
		  if (results[0].address_components[i].types[0]=="street_number")			  
		  {
			  nummer_=results[0].address_components[i][componentForm[results[0].address_components[i].types[0]]];
			  
			  street_number_eingegeben=1;
		  }
		  if (results[0].address_components[i].types[0]=="postal_code")			  
		  {
			  plz_=results[0].address_components[i][componentForm[results[0].address_components[i].types[0]]];
			  plz_eingegeben=1;		
		  }
		  if (results[0].address_components[i].types[0]=="locality")			  
		  {
			  stadt_=results[0].address_components[i][componentForm[results[0].address_components[i].types[0]]];
			  stadt_eingegeben=1;		  
		  }
			  
			  
		  
		  i=i+1;
		}

		ausgefuellt=strasse_eingegeben+street_number_eingegeben+plz_eingegeben+stadt_eingegeben;

		if(strasse_eingegeben==0)
		{
			alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Straßendetails. Wir konnten die Straße nicht finden.")
			document.getElementsByClassName("adresse_input")[0].style.border="1px solid red";	
			document.getElementsByClassName("address_text")[0].style.color="red";		
			ausgefuellt=0;
		}

		if(street_number_eingegeben==0)
		{
			alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Straßendetails. Wir konnten die Straße nicht finden.")
			document.getElementsByClassName("adresse_input")[0].style.border="1px solid red";	
			document.getElementsByClassName("address_text")[0].style.color="red";		
			ausgefuellt=0;
		}

		if(plz_eingegeben==0)
		{
			alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Ortsangaben. Wir konnten die Straße nicht finden.")
			document.getElementsByClassName("adresse")[1].style.border="1px solid red";	
			document.getElementsByClassName("address_text")[2].style.color="red";		
			ausgefuellt=0;
		}
		if(stadt_eingegeben==0)
		{
			alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Ortsangaben. Wir konnten die Straße nicht finden.")
			document.getElementsByClassName("adresse")[0].style.border="1px solid red";	
			document.getElementsByClassName("address_text")[1].style.color="red";		
			ausgefuellt=0;
		}
			


		if (ausgefuellt==4)
		{
			
			var i=0;
			status=1;


			if(status==1)
			{
			

				if(strasse_+" "+nummer_!=strasse)
				{

					alert_userdata("STRASSENANGABEN ÜBERPRÜFEN","Deine eingegebene Straße ist nicht korrekt. Bitte überprüfe unseren Vorschlag.")
					document.getElementsByClassName("adresse_input")[0].value=strasse_+" "+nummer_
					document.getElementsByClassName("adresse_input")[0].style.border="1px solid red";	
					document.getElementsByClassName("address_text")[0].style.color="red";		
					
				}
				else
				{
					
					if(plz_!=plz)
					{
						alert_userdata("POSTLEIZTAHL ÜBERPRÜFEN","Deine eingegebene Postleitzahl ist nicht korrekt. Bitte überprüfe unseren Vorschlag.")
						document.getElementsByClassName("adresse")[1].value=plz_
						document.getElementsByClassName("adresse")[1].style.border="1px solid red";	
						document.getElementsByClassName("address_text")[2].style.color="red";		

						
					}
					else
					{

						if(stadt_!=stadt)
						{
							alert_userdata("STADT ÜBERPRÜFEN","Deine eingegebene Stadt ist nicht korrekt. Bitte überprüfe unseren Vorschlag.")
							document.getElementsByClassName("adresse")[0].value=stadt_
							document.getElementsByClassName("adresse")[0].style.border="1px solid red";	
							document.getElementsByClassName("address_text")[1].style.color="red";		
						}
						else
						{

			

							if(status==1)
							{


								adresse_uebertragen(strasse, nummer, plz, stadt, vorname, nachname,telefonnummer, unternehmensdetails,lieferhinweise)
								document.getElementById("buttons_address_text").innerHTML="";
								document.getElementsByClassName("button_check")[0].style.display="none";
								//document.getElementById("buttons_address_text").style.pointerEvents ="none";
								
								box="<div style='float:left;width:100%;'><div class='map' id='map'></div>";
								box=box+"<div class='side3' onclick='adresse_bearbeiten()'></div>"
								
							//	box=box+"</div><br><br><br><br><br>"
			

								if (adressbuch!="")
									box=box+"<br><div class='lieferhinweise'>Lieferhinweise<br><textarea id='lieferdetails_textarea' name='html_elemente' cols='50' rows='15' maxlength='10000' style='width:100%;height:65px;resize: none;font-family:Helvetica;font-size:12px;' placeholder='Bitte gib hier Details zur Sendungsübergabe an.'>"+lieferhinweise+"</textarea></div></div>";
								else
									box=box+"<br><div class='lieferhinweise'>Lieferhinweise<br><textarea id='lieferdetails_textarea' name='html_elemente' cols='50' rows='15' maxlength='10000' style='width:100%;height:65px;resize: none;font-family:Helvetica;font-size:12px;' placeholder='Bitte gib hier Details zur Sendungsübergabe an.'>"+lieferhinweise+"</textarea></div></div>";
								
								document.getElementById("total_address").innerHTML=box;
			
								document.getElementsByClassName("side3")[0].innerHTML="<div style='float:left;margin-left:10px;margin-Top:10px;' >"+strasse+"<br>"+plz+" "+stadt+"</div>";

								var latlng = new google.maps.LatLng(-34.397, 150.644);
								var myOptions = {
								  zoom: 17,
								  center: latlng,
								  mapTypeId: google.maps.MapTypeId.ROADMAP
								}
								map = new google.maps.Map(document.getElementById("map"), myOptions);
								map.setCenter(results[0].geometry.location);
								var marker = new google.maps.Marker({
									map: map,
									position: results[0].geometry.location
								});
								page_load(1);
								
								if (adresse_neu!=-2)
									adressbuch_aktualisieren();
							
							}
						}
					}
	
				}				
				
			}
			else
			 	alert_userdata("ADRESSBEREICH NOCH NICHT VERFÜGBAR","Der PLZ-Bereich ist leider noch nicht verfügbar. Hier findest du Infos zu unserem Liefergebiet.")
		
		  }
		}
		
		else
		{
			alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Ortsangaben. Wir konnten deine Adresse nicht finden.")
			document.getElementsByClassName("adresse")[0].style.border="1px solid red";	
			document.getElementsByClassName("address_text")[1].style.color="red";	
		}	


	  

    });
	

  }
  
  

	  
	  
  
  
  function adresse_bearbeiten()
  {

	  
		output_adresse_clicked=1;

		i=0;
		box="";
		while(i<=adressbuch.length-1)
		{


			

			adresse= adressbuch[i].adresse+"<br>"+adressbuch[i].plz+" "+adressbuch[i].stadt
			
			if(i==0)
			{
				strasse_=adressbuch[i].adresse

				nummer_=""
				apt_=adressbuch[i].apt
				plz_=adressbuch[i].plz
				stadt_=adressbuch[i].stadt
				vorname_=adressbuch[i].vorname
				nachname_=adressbuch[i].nachname
				telefonnummer_=adressbuch[i].telefonnummer
				unternehmensdetails_=adressbuch[i].unternehmensdetails
				indexnummer_=adressbuch[i].indexnummer
				lieferhinweise=adressbuch[i].lieferhinweise



				box=box+"<div class='output_adresse' style='border:1px solid #e65c00' ><div style='float:left;margin-left:10px;margin-Top:10px;'>"+adresse+"</div><div style='float:left;color:red;margin-Top:20px;cursor:pointer;margin-left:20px;' onclick='adresse_anzeigen(strasse_, nummer_, plz_, stadt_, vorname_, nachname_,telefonnummer_, unternehmensdetails_,indexnummer_)'>Bearbeiten</div></div>";

			}
			else
				box=box+"<div class='output_adresse' style='border:1px solid #e65c00' onclick='adresse_wechseln("+i+")' ><div style='float:left;margin-left:10px;margin-Top:10px'>"+adresse+"</div></div></div>";
				

			
			
			i=i+1;
		}
		
	box=box+"<div class='output_adresse' style='border-bottom:1px solid #e65c00;border-left:1px solid #e65c00;border-right:1px solid #e65c00;cursor:pointer;' onclick='neue_adresse()' ><div style='float:left;margin-top:5px;font-weight:bold;margin-left:10px;'>+ Neue Adresse</div></div>";		

	  output_adresse_show=1;
	 document.getElementsByClassName("side3")[0].innerHTML=box;
	  
	  //style.backgroundColor="#e6e6e6";
	 
  }
  
  
  function neue_adresse()
  {

	  adresse_anzeigen("", "", "", "", "", "", "", "",-1)
	  
  }
  
  function adresse_wechseln(index_)
  {

	  var huelle=adressbuch[0]
	   
	  adressbuch[0]=adressbuch[index_];
	  adressbuch[index_]=huelle;
	//  adresse= adressbuch[0][3]+"<br>"+adressbuch[0][6]+" "+adressbuch[0][7]
	 strasse=adressbuch[0].adresse
	 document.getElementsByClassName("adresse")[0]=strasse;
	 plz=adressbuch[0].plz
	stadt=adressbuch[0].stadt
	nummer=""
	
	initMap(strasse,plz,stadt);
	  //strasse=adressbuch[index_][3]
	  
	//  adresse_feld();
	  
	  
	  
	  
  }
  
  var scroll_position_absolute;
  function scroll_position()
  {
	  
	  
	  					
	var winheight= window.innerHeight || (document.documentElement || document.body).clientHeight;
	var docheight = getDocHeight();
	var scrollTop = window.pageYOffset || (document.documentElement || document.body.parentNode || document.body).scrollTop;
	return scrollTop;
	  
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
