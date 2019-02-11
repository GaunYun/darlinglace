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
	  var autocomplete=new Array(100);
	 var index;
	 var index_2;


		 var componentForm = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',

  postal_code: 'short_name'
      };
	  
	  
    initialize = function () {





			
			var input = document.getElementsByClassName('eingabefelder_adresse')

			address=input;
			
	        var options = {
	            
	        };
	        	j=0
	        	
		while(j<=adressen.length)
		{	

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

			document.getElementsByClassName('eingabefelder_adresse')[this.inputId].value= strasse+" "+nummer;
			document.getElementsByClassName('eingabefelder_plz')[this.inputId].value = plz;
			document.getElementsByClassName('eingabefelder_stadt')[this.inputId].value = stadt;
		

	});
	j=j+1
		}
    }
    google.maps.event.addDomListener(window, 'load', initialize);
    
    submitform = function () {
        searchplace = autocomplete.getPlace();
        console.log(searchplace.name);
		
	
    }
	
	
	
	var geocoder;
  var map;
  
  
  
  function initMap(strasse_,plz_,stadt_,index_,index_2_) {

    geocoder = new google.maps.Geocoder();

	index=index_;
	index_2=index_2_;
   

	
	
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
			document.getElementsByClassName("eingabefelder_adresse")[index_2].style.border="1px solid red";	
		}

		if(street_number_eingegeben==0)
		{
			alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Straßendetails. Wir konnten die Straße nicht finden.")
			document.getElementsByClassName("eingabefelder_adresse")[index_2].style.border="1px solid red";	
		}

		if(plz_eingegeben==0)
		{
			alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Ortsangaben. Wir konnten die Straße nicht finden.")
			document.getElementsByClassName("eingabefelder_plz")[index_2].style.border="1px solid red";	
		}
		if(stadt_eingegeben==0)
		{
			alert_userdata("ADRESSANGABE ÜBERPRÜFEN","Bitte überprüfe die Ortsangaben. Wir konnten die Straße nicht finden.")
			document.getElementsByClassName("eingabefelder_stadt")[index_2].style.border="1px solid red";	
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
					document.getElementsByClassName("eingabefelder_adresse")[index_2].value=strasse_+" "+nummer_
					document.getElementsByClassName("eingabefelder_adresse")[index_2].style.border="1px solid red";	
					
				}
				else
				{
					if(plz_!=plz)
					{
						alert_userdata("POSTLEIZTAHL ÜBERPRÜFEN","Deine eingegebene Postleitzahl ist nicht korrekt. Bitte überprüfe unseren Vorschlag.")
						document.getElementsByClassName("eingabefelder_plz")[index_2].value=plz_
						document.getElementsByClassName("eingabefelder_plz")[index_2].style.border="1px solid red";	

						
					}
					else
					{
						if(stadt_!=stadt)
						{
							alert_userdata("STADT ÜBERPRÜFEN","Deine eingegebene Stadt ist nicht korrekt. Bitte überprüfe unseren Vorschlag.")
							document.getElementsByClassName("eingabefelder_stadt")[index_2].value=stadt_
							document.getElementsByClassName("eingabefelder_stadt")[index_2].style.border="1px solid red";	
						}
						else
						{
							if (status==1)
								adresse_ok(index);
						}
					}
				}

			}
			else
			 {

			 	alert_userdata("ADRESSBEREICH NOCH NICHT VERFÜGBAR","Der PLZ-Bereich ist leider noch nicht verfügbar. Hier findest du Infos zu unserem Liefergebiet.")
				  
			  }
		
		  }
	}
	else
	{
		alert_userdata("ADRESS ÜBERPRÜFEN","Deine eingegebene Adresse ist nicht korrekt. Bitte überprüfe deine Eingabe.")
		document.getElementsByClassName("eingabefelder_adresse")[index_2].style.border="1px solid red";			
		document.getElementsByClassName("eingabefelder_stadt")[index_2].style.border="1px solid red";			
		document.getElementsByClassName("eingabefelder_plz")[index_2].style.border="1px solid red";			
		
	}


    });

  }
  
  
  





