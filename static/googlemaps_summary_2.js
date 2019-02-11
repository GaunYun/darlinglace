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
	 var zugelassene_plz=new Array(100);


		 var componentForm = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',

  postal_code: 'short_name'
      };
	  
	  
    initialize = function () {

		zugelassene_plz[0]=new Array;
		zugelassene_plz[0]="80337";
		zugelassene_plz_max=0;
		
		
		
		
		var input = document.getElementById('route');
		address=input;
        var options = {
            
        };
 
        autocomplete = new google.maps.places.Autocomplete(input, options);
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
			  {
				var strasse = place.address_components[i][componentForm[place.address_components[i].types[0]]];  

				  
			  }
			  
			  if (place.address_components[i].types[0]=="street_number")
			  {
				var nummer = place.address_components[i][componentForm[place.address_components[i].types[0]]];  
				
				if (nummer==strasse)
				{
					nummer="";
				}
				  
			  }
			  
			  if (place.address_components[i].types[0]=="postal_code")
			  {
				var plz = place.address_components[i][componentForm[place.address_components[i].types[0]]];  
				

				
				  
			  }
			  
			  if (place.address_components[i].types[0]=="locality")
			  {
				var stadt = place.address_components[i][componentForm[place.address_components[i].types[0]]];  


				  
			  }
			  
			  
			  i=i+1;			
			

		}
		
		document.getElementById("route").value = strasse+" "+nummer;
		document.getElementById("postal_code").value = plz;
		document.getElementById("locality").value = stadt;
		change();

		});
    }
    google.maps.event.addDomListener(window, 'load', initialize);
    submitform = function () {
        searchplace = autocomplete.getPlace();
        console.log(searchplace.name);
		
		
    }
	
	
	
	var geocoder;
  var map;
  
  
  
  function initMap(strasse_,plz_,stadt_) {
    geocoder = new google.maps.Geocoder();
   
	

    
	
	
	strasse=strasse_;
	plz=plz_;
	stadt=stadt_;


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
		}

		if(street_number_eingegeben==0)
		{
			alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Straßendetails. Wir konnten die Straße nicht finden.")
			document.getElementsByClassName("adresse_input")[0].style.border="1px solid red";	
		}

		if(plz_eingegeben==0)
		{
			alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Ortsangaben. Wir konnten die Straße nicht finden.")
			document.getElementsByClassName("plz_input")[0].style.border="1px solid red";	
		}
		if(stadt_eingegeben==0)
		{
			alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Ortsangaben. Wir konnten die Straße nicht finden.")
			document.getElementsByClassName("stadt_input")[0].style.border="1px solid red";	
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
					
				}
				else
				{
					
					if(plz_!=plz)
					{
						alert_userdata("POSTLEIZTAHL ÜBERPRÜFEN","Deine eingegebene Postleitzahl ist nicht korrekt. Bitte überprüfe unseren Vorschlag.")
						document.getElementsByClassName("plz_input")[0].value=plz_
						document.getElementsByClassName("plz_input")[0].style.border="1px solid red";	

						
					}
					else
					{

						if(stadt_!=stadt)
						{
							alert_userdata("STADT ÜBERPRÜFEN","Deine eingegebene Stadt ist nicht korrekt. Bitte überprüfe unseren Vorschlag.")
							document.getElementsByClassName("stadt_input")[0].value=stadt_
							document.getElementsByClassName("stadt_input")[0].style.border="1px solid red";	
						}
						else
						{

			

							if(status==1)
							{
								
								if (document.getElementsByClassName("adresse_input")[0].value!=strasse_+" "+nummer_ || document.getElementsByClassName("plz_input")[0].value!=plz_ || document.getElementsByClassName("stadt_input")[0].value.toUpperCase()!=stadt_.toUpperCase())
								{

									alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Ortsangaben. Wir konnten die Straße nicht finden.")
									document.getElementsByClassName("stadt_input")[0].style.border="1px solid red";	
								}
								else
									adresse_ok();
							}
						}
					}
				}
				
				

				
				
				


				
				

			}

		
		  }
		  else
		  {

			
			  
		  }
		}
		else
		{
			alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Ortsangaben. Wir konnten die Straße nicht finden.")
			document.getElementsByClassName("stadt_input")[0].style.border="1px solid red";	
			
		}


	  

    });

  }
  
  
  
  document.onclick = function() {
	  var adresse= strasse+" "+nummer+"<br>"+plz+" "+stadt;
	  if(output_adresse_clicked==0 && output_adresse_show==1)
	  {
		 var box="<div class='output_adresse' onclick='adresse_bearbeiten()'>"+adresse+"</div>";
		document.getElementById("feld_kreditkarte_bearbeiten").innerHTML=box;
		output_adresse_show=0;
		
	  }
	  output_adresse_clicked=0;  

  }
	  
	  
  
  
  function adresse_bearbeiten()
  {
	  
		output_adresse_clicked=1;
	  var adresse= strasse+" "+nummer+"<br>"+plz+" "+stadt

	  var box="<div class='output_adresse' style='background-Color:#f2f2f2;border:1px solid #e65c00;cursor:auto;' ><div style='float:left'>"+adresse+"</div><div style='float:right;color:red;margin-Top:10px;cursor:pointer;' onclick='adresse_anzeigen(strasse, nummer, apt, plz, stadt, vorname, nachname,telefonnummer, unternehmensdetails)'>Bearbeiten</div></div>";
	  output_adresse_show=1;
	  document.getElementById("feld_kreditkarte_bearbeiten").innerHTML=box;
	  
	  //style.backgroundColor="#e6e6e6";
	 
  }
  

