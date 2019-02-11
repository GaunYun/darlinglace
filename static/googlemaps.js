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
		
		
		
		
		var input = document.getElementById('strasse');
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
				
				felder_adresse_zuruecksetzen(3);
				
				  
			  }
			  
			  if (place.address_components[i].types[0]=="locality")
			  {
				var stadt = place.address_components[i][componentForm[place.address_components[i].types[0]]];  
				felder_adresse_zuruecksetzen(2);

				  
			  }
			  
			  
			  i=i+1;			
			

		}
		
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
			  strasse=results[0].address_components[i][componentForm[results[0].address_components[i].types[0]]];
			  strasse_eingegeben=1;
		  }
		  if (results[0].address_components[i].types[0]=="street_number")			  
		  {
			  nummer=results[0].address_components[i][componentForm[results[0].address_components[i].types[0]]];
			  street_number_eingegeben=1;
		  }
		  if (results[0].address_components[i].types[0]=="postal_code")			  
		  {
			  plz=results[0].address_components[i][componentForm[results[0].address_components[i].types[0]]];
			  plz_eingegeben=1;		
		  }
		  if (results[0].address_components[i].types[0]=="locality")			  
		  {
			  stadt=results[0].address_components[i][componentForm[results[0].address_components[i].types[0]]];
			  stadt_eingegeben=1;		  
		  }
			  
			  
		  
		  i=i+1;
		}

		ausgefuellt=strasse_eingegeben+street_number_eingegeben+plz_eingegeben+stadt_eingegeben;
		
		if(strasse_eingegeben==0)
			var box="<img class='schliessen_alert' src='x.png' width='15' onclick='alert_click_schliessen()' height='15'/></img><br><b>ADRESSANGABE ÜBERPRÜFEN</b><br><br><p>Bitte überprüfe die Straßendetails. Wir konnten die Straße nicht finden.</p>";
		if(street_number_eingegeben==0)
			var box="<img class='schliessen_alert' src='x.png' width='15' onclick='alert_click_schliessen()' height='15'/></img><br><b>ADRESSANGABE ÜBERPRÜFEN</b><br><br><p>Bitte überprüfe die Straßendetails. Wir konnten die Hausnummer nicht finden.</p>";
		if(plz_eingegeben==0)
			var box="<img class='schliessen_alert' src='x.png' width='15' onclick='alert_click_schliessen()' height='15'/></img><br><b>ADRESSANGABE ÜBERPRÜFEN</b><br><br><p>Bitte überprüfe die Ortsangaben. Wir konnten die Postleitzahl nicht finden.</p>";
		if(stadt_eingegeben==0)
			var box="<img class='schliessen_alert' src='x.png' width='15' onclick='alert_click_schliessen()' height='15'/></img><br><b>ADRESSANGABE ÜBERPRÜFEN</b><br><br><p>Bitte überprüfe die Ortsangaben. Wir konnten die Stadt nicht finden.</p>";
		
			

		
		if (ausgefuellt==4)
		{
			
			var i=0;
			status=0;

			while(i<=zugelassene_plz_max)
			{
				
				if(plz==zugelassene_plz[i])
					status=1;
				i=i+1;
			}


			
			if(status==1)
			{
				vorname=document.getElementsByClassName("adresse")[4].value;
				nachname=document.getElementsByClassName("adresse")[5].value;
				telefonnummer=document.getElementsByClassName("adresse")[6].value;
				apt=document.getElementsByClassName("adresse")[1].value;
				if(document.getElementById("checkbox_unternehmen").checked==true)
					unternehmensdetails=document.getElementsByClassName("unternehmensdetails")[1].value;
				else
					unternehmensdetails="";
				
				
				
				document.getElementById("buttons_address_text").innerHTML="";
				document.getElementsByClassName("button_check")[0].style.display="none";
				document.getElementById("buttons_address_text").style.dispatchEvent="none";
				var box="<div style='width:186px;height:186px;border: 1px solid #e6e6e6;float:left;pointer-events: none;' id='map'></div>";
				box=box+"<div style='float:right;' id='feld_kreditkarte_bearbeiten'><div class='output_adresse' style='	' onclick='adresse_bearbeiten()'></div></div><br><br><br><br>";
				
				box=box+"<br><div style='float:right;'>Lieferhinweise<br><textarea name='html_elemente' cols='50' rows='15' maxlength='10000' style='width:350px;height:70px;resize: none;font-family:Century Gothic;font-size:12px;' placeholder='Bite gib hier Details zur Sendungsübergabe an.'></textarea></div>";
				document.getElementById("total_address").innerHTML=box;
				document.getElementsByClassName("output_adresse")[0].innerHTML=strasse+" "+nummer+"<br>"+plz+" "+stadt;

				
				
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
			}
			else
			 {
				  var box="<img class='schliessen_alert' src='x.png' width='15' onclick='alert_click_schliessen()' height='15'/></img><br><b>ADRESSBEREICH NOCH NICHT VERFÜGBAR</b><br><br><p>Der PLZ-Bereich ist leider noch nicht verfügbar. Hier findest du Infos zu unserem Liefergebiet</p>";
					var winheight= window.innerHeight || (document.documentElement || document.body).clientHeight
					var docheight = getDocHeight()
					var scrollTop = window.pageYOffset || (document.documentElement || document.body.parentNode || document.body).scrollTop
					el = document.getElementById("overlay");
					el.style.marginTop=scrollTop+"px";
					scroll_position_absolute=scrollTop;
					document.getElementById("alert_address").innerHTML=box;
					el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
					document.getElementById("x-mask").style.opacity="0.4";
				  
			  }
		
		  }
		  else
		  {

			el = document.getElementById("overlay");
			el.style.marginTop=scroll_position()+"px";
			document.getElementById("alert_address").innerHTML=box;
			el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
			document.getElementById("x-mask").style.opacity="0.4";
			  
		  }
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
