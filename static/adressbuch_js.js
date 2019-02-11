var adressen;
var margintop;
var asd;

function adressen_hinzufuegen()
{
	
	document.getElementsByClassName("header_style")[0].style.display="block"
	document.getElementsByClassName("button_main")[0].style.opacity="0.3"
	document.getElementsByClassName("button_main")[0].style.pointerEvents = 'none';

	
}
function check_mobilnummer(index)
{
	if (index==-1)
		index=0;
	else
		index=index+1;

		if(document.getElementsByClassName("eingabefelder_telefonnummer")[index].value!="")
		{
			$.ajax({
			type: "POST",
			url: "/check_mobilnummer/",
			dataType: "json",
			data: { "telefonnummer": document.getElementsByClassName("eingabefelder_telefonnummer")[index].value },
			success: function(data) {
	
				if(data=="")
				{
					alert_userdata("MOBILNUMMER NICHT KORREKT","Die eingegebene Mobilnummer ist nicht gültig. Bitte gib eine andere Mobilnummer an.")
					document.getElementsByClassName("eingabefelder_telefonnummer")[index].style.border="1px solid red";	
	
				}
				else
				{
					document.getElementsByClassName("eingabefelder_telefonnummer")[index].value=data
					document.getElementsByClassName("eingabe_fehler")[index].innerHTML=""
				}
	
			}
			});
		}
				
	
}


function adresse_speichern(index)
{

	if (index==-1)
		index_2=0;
	else
		index_2=index+1;

		if(check_field_empty(index_2)=="ok")
			$.ajax({
			type: "POST",
			url: "/check_mobilnummer/",
			dataType: "json",
			data: { "telefonnummer": document.getElementsByClassName("eingabefelder_telefonnummer")[index_2].value },
			success: function(data) {

				if(data=="")
				{

					alert_userdata("MOBILNUMMER NICHT KORREKT","Die eingegebene Mobilnummer ist nicht gültig. Bitte gib eine andere Mobilnummer an.")

					document.getElementsByClassName("eingabefelder_telefonnummer")[index_2].style.border="1px solid red";	


				}
				else
				{

					document.getElementsByClassName("eingabefelder_telefonnummer")[index_2].value=data
				//	document.getElementsByClassName("eingabe_fehler")[index_2].innerHTML=""
	
						initMap(document.getElementsByClassName("eingabefelder_adresse")[index_2].value,document.getElementsByClassName("eingabefelder_plz")[index_2].value,document.getElementsByClassName("eingabefelder_stadt")[index_2].value,index,index_2);
				}
	
			}
			});
		
		

		
		

}


 function input_on_change(element)
{

	element.style.border="1px solid #e6e6e6 ";	
	element.style.color="#4E4E4E";
}



function check_field_empty(index_2)
{
	list=new Array(10)
	list[0]="eingabefelder_vorname"
	list[1]="eingabefelder_nachname"
	list[2]="eingabefelder_telefonnummer"
	list[3]="eingabefelder_adresse"
	list[4]="eingabefelder_stadt"
	list[5]="eingabefelder_plz"

	status_="ok"
	i=0;
	while (i<=5)
	{
		if (document.getElementsByClassName(list[i])[index_2].value=="")
		{
			status_="nicht ok";
			document.getElementsByClassName("warnhinweis")[index_2].innerHTML=unescape("Bitte alle ben%F6tigten Felder ausf%FCllen.");		
			document.getElementsByClassName(list[i])[index_2].style.border="1px solid red";	
		}
		i=i+1;
	}

	
	if(status_=="ok")
		document.getElementsByClassName("warnhinweis")[index_2].innerHTML="";		
		
	return status_

}




function reset_fields(i)
{
	document.getElementsByClassName("eingabefelder_vorname")[i].value=""
	input_on_change(document.getElementsByClassName("eingabefelder_vorname")[i])
	
	document.getElementsByClassName("eingabefelder_nachname")[i].value=""
	input_on_change(document.getElementsByClassName("eingabefelder_nachname")[i])

	document.getElementsByClassName("eingabefelder_telefonnummer")[i].value=""
	input_on_change(document.getElementsByClassName("eingabefelder_telefonnummer")[i])
	
	document.getElementsByClassName("eingabefelder_adresse")[i].value=""
	input_on_change(document.getElementsByClassName("eingabefelder_adresse")[i])
	
	document.getElementsByClassName("eingabefelder_unternehmensdetails")[i].value=""
	input_on_change(document.getElementsByClassName("eingabefelder_unternehmensdetails")[i])
	
	document.getElementsByClassName("eingabefelder_stadt")[i].value=""
	input_on_change(document.getElementsByClassName("eingabefelder_stadt")[i])
	
	document.getElementsByClassName("lieferhinweise")[i].value=""
	input_on_change(document.getElementsByClassName("lieferhinweise")[i])
	
	document.getElementsByClassName("eingabefelder_plz")[i].value=""	
	input_on_change(document.getElementsByClassName("eingabefelder_plz")[i])
}




function adresse_ok(index)
{

	if (index==-1)
	{
		var hinzufuegen="1";

		index_2=0;
		index=0;
		indexnummer=""
		standard="nein"
	}
	else
	{	
		var hinzufuegen="0";
		index_2=index+1
		indexnummer=adressen[index_2-1].indexnummer

		standard=adressen[index_2-1].standard
	}
	
	if(adressen=="")
		standard="ja"
		


	$.ajax({
		type: "POST",
		url: "/account_page/adresse_speichern/",
		dataType: "json",
		data: { "hinzufuegen":hinzufuegen,"indexnummer":indexnummer,"vorname": document.getElementsByClassName("eingabefelder_vorname")[index_2].value,"nachname": document.getElementsByClassName("eingabefelder_nachname")[index_2].value,"telefonnummer": document.getElementsByClassName("eingabefelder_telefonnummer")[index_2].value,
		"adresse": document.getElementsByClassName("eingabefelder_adresse")[index_2].value,"unternehmensdetails": document.getElementsByClassName("eingabefelder_unternehmensdetails")[index_2].value,
		"stadt": document.getElementsByClassName("eingabefelder_stadt")[index_2].value,"plz": document.getElementsByClassName("eingabefelder_plz")[index_2].value,"lieferdetails": document.getElementsByClassName("lieferhinweise")[index_2].value,"standard":standard},
		success: function(data) {

				reset_fields(index_2)
			
			document.getElementsByClassName("adressbuch_daten")[0].innerHTML=data
			adresse_abbrechen(-1)
			
			adressen_laden()

			adresse_hinzufuegen_schliessen();
			


		}
	});
	
}


function adresse_hinzufuegen_schliessen()
{
	document.getElementsByClassName("header_style_2")[0].style.display="none"
	document.getElementsByClassName("button_main")[0].style.opacity="1.0"
	document.getElementsByClassName("button_main")[0].style.pointerEvents = 'auto';
	margintop=margintop-700;

	
}

function adresse_loeschen(index)
{

	
	var hinzufuegen="-1";
	index_2=index+1
	$.ajax({
		type: "POST",
		url: "/account_page/adresse_speichern/",
		dataType: "json",
		data: { "hinzufuegen":hinzufuegen,"indexnummer":adressen[index].indexnummer,"vorname": document.getElementsByClassName("eingabefelder_vorname")[index_2].value,"nachname": document.getElementsByClassName("eingabefelder_nachname")[index_2].value,"telefonnummer": document.getElementsByClassName("eingabefelder_telefonnummer")[index_2].value,
		"adresse": document.getElementsByClassName("eingabefelder_adresse")[index_2].value,"unternehmensdetails": document.getElementsByClassName("eingabefelder_unternehmensdetails")[index_2].value,
		"stadt": document.getElementsByClassName("eingabefelder_stadt")[index_2].value,"plz": document.getElementsByClassName("eingabefelder_plz")[index_2].value,"lieferdetails": document.getElementsByClassName("lieferhinweise")[index_2].value},
		success: function(data) {
			document.getElementsByClassName("adressbuch_daten")[0].innerHTML=data
			adresse_abbrechen(-1)
			adressen_laden()
			
			


		}
	});
	
}




function adressen_laden()
{
	reset_fields(0)
	adressen=JSON.parse(document.getElementsByClassName("adressbuch_daten")[0].innerHTML)

	i=0;

	
		
	var box="";

	if (adressen!="")
	{
		while (i<=adressen.length-1)
		{
			



			box=box+"<div class='header_style_3'>";
			
			
			box=box+"<div class='oberes_feld' style='width:100%;height:100px;'>"
			box=box+"<div class='adressdetails'>";
			box=box+"<div style='vertical-align:middle;width:30%;height:100px;display:table-cell;''>"
			box=box+"<div class='adresse_name'>"+adressen[i].vorname+" "+adressen[i].nachname+"<br>"
			box=box+"</div>"
			box=box+"<b>"+adressen[i].adresse+"</b>"

			box=box+"</div>"
			box=box+"</div>"
			
			

			
			box=box+"<div class='standard_feld'>"	
			box=box+"<div class='shop_2'><div class='shop' standard_aendern("+i+",0)></div></div>"		
			box=box+"</div>"
			
			
			box=box+"<div style='float:left;width:2%;height:100px;border-left: 1px solid #e6e6e6 ;'>"		
			box=box+"</div>"
			box=box+"<div style='float:left;width:10%;height:100px;'>"		
			box=box+"<div class='bearbeiten_feld' onclick='adresse_bearbeiten("+i+")'>Bearbeiten</div>"
			box=box+"</div>"
			box=box+"</div>"
			
			
	
	
	


			box=box+"<div class='zusammenfassung' style='display:none;'>\r"
			
			box=box+"<div class='block'>\r"
			box=box+"<div class='eingabefelder_headline_line_1'><b>Vorname</b><br>\r"
			box=box+"<input class='eingabefelder_vorname' onkeydown='input_on_change(this)' type='text' value='"+adressen[i].vorname+"'/>\r"
			box=box+"</div>\r"
			
			box=box+"<div class='eingabefelder_headline_line_1'><b>Nachname</b><br>\r"
			box=box+"<input class='eingabefelder_nachname' placeholder='' type='text' onkeydown='input_on_change(this)'  maxlength='19' onBlur='kreditkarten_show(event,-1)' value='"+adressen[i].nachname+"'/>\r"
			box=box+"</div>\r"
			
			
			box=box+"<div class='eingabefelder_headline_line_1'><b>Telefonnummer</b><br>\r"
			box=box+"<input type='tel' class='eingabefelder_telefonnummer' onkeypress='validate(event)' onblur='check_mobilnummer("+i+")'  onkeydown='input_on_change(this)'style='padding-left:40px;' value='"+adressen[i].telefonnummer+"'/><div class='vorwahl'>+49</div>\r"
			box=box+"</div>\r"
			box=box+"<span class='stretch'></span>\r"
			box=box+"</div>\r"
			box=box+"<br>"
			box=box+"<div class='block'>\r"
			box=box+"<div class='eingabefelder_headline_line_1'><b>Adresse</b><br>\r"
			id=i+1
			box=box+"<input type='text' class='eingabefelder_adresse' id='"+id+"' onkeydown='input_on_change(this)' value='"+adressen[i].adresse+"'/>\r"
			box=box+"</div>\r"
			
			box=box+"<div class='eingabefelder_headline_line_1'><b>Stadt</b><br>\r"
			box=box+"<input class='eingabefelder_stadt' placeholder='' type='text' onkeydown='input_on_change(this)' value='"+adressen[i].stadt+"'/>\r"
			box=box+"</div>\r"
			
			
			box=box+"<div class='eingabefelder_headline_line_1'><b>PLZ</b><br>\r"
			box=box+"<input type='text' class='eingabefelder_plz' onkeypress='validate(event)' maxlength='5' onkeydown='input_on_change(this)' value='"+adressen[i].plz+"'/>\r"
			box=box+"</div>\r"
			box=box+"<span class='stretch'></span>\r"
			box=box+"</div>\r"														
			
			box=box+"<br>"
			box=box+"<div class='eingabefelder_headline_line_2'><b>Unternehmensdetails (optional)</b><br>"
			box=box+"<input class='eingabefelder_unternehmensdetails' placeholder='' type='text' onkeydown='input_on_change(this)' value='"+adressen[i].unternehmensdetails+"'/>"
			box=box+"</div>"
			box=box+"<br><br>"
			box=box+"<div class='eingabefelder_headline_line_2'><b>Lieferhinweise</b><br><br>"
			box=box+"<textarea class='lieferhinweise' name='html_elemente' cols='50' rows='15' maxlength='10000' placeholder='Bitte gib hier Details zur Sendungsübergabe an.' >"+adressen[i].lieferhinweise+"</textarea>"
			box=box+"</div>"
					
					
			box=box+"<div class='warnhinweis' style='color:red;float:right;'> </div>"
			box=box+"<div class='adresse_speichern_button' onclick='adresse_speichern("+i+")'>Adresse speichern</div>";	
			box=box+"<div class='button_abbrechen' onclick='adresse_abbrechen("+i+")'>Abbrechen</div>";
			box=box+"<div class='button_loeschen' onclick='adresse_loeschen("+i+")'>Entfernen</div>";
			

			box=box+"</div></div>";
			
			box=box+"</div>";
			i=i+1;
		}
	}
	

	
	document.getElementById("existierende_adressen_anzeigen").innerHTML=box;

	

	

	for (var i = 0; i <= adressen.length-1; i++) {

		if (adressen[i].standard=="ja")
			addRatingWidget(buildShopItem("1",i), i,"1");
		else
			addRatingWidget(buildShopItem("1",i), i,"0");
			

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


function adresse_bearbeiten(index)
{

	if(document.getElementsByClassName("bearbeiten_feld")[index].innerHTML=="Bearbeiten")
	{
		document.getElementsByClassName("oberes_feld")[index].style.borderBottom="1px solid #e6e6e6";
		document.getElementsByClassName("zusammenfassung")[index+1].style.display="block";
		document.getElementsByClassName("bearbeiten_feld")[index].innerHTML="Schließen"

		

	}
	else
	{
		document.getElementsByClassName("oberes_feld")[index].style.borderBottom="";
		document.getElementsByClassName("zusammenfassung")[index+1].style.display="none";
		document.getElementsByClassName("bearbeiten_feld")[index].innerHTML="Bearbeiten"

		

	}		

	

	
	
	
}

function adresse_abbrechen(index)
{
	
	if (index!=-1)
	{
		document.getElementsByClassName("oberes_feld")[index].style.borderBottom="";
		document.getElementsByClassName("zusammenfassung")[index+1].style.display="none";
		document.getElementsByClassName("bearbeiten_feld")[index].innerHTML="Bearbeiten"

		
	}
	else
	{
		document.getElementsByClassName("header_style")[0].style.display="none"
		document.getElementsByClassName("button_main")[0].style.opacity="1.0"
		document.getElementsByClassName("button_main")[0].style.pointerEvents = 'auto';
		
		reset_fields(0)

	}
}




function test() 
{

	"use strict";
	function t(t,i,n,e)
	{
		function r(t,i)
		{
			for(var n=0;n<t.length;n++)
			{
				var e=t[n];i(e,n)
			}
		}
		
		function a(t)
		{
			//s(t),o(t),
			//
			u(t)
		}
		
		function s(t)
		{
			t.addEventListener("mouseover",function(i)
			{
				r(f,function(i,n)
				{
					
					n<=parseInt(t.getAttribute("data-index"))?i.classList.add("is-active"):i.classList.remove("is-active")
				})
			})
		}
		
		function o(t)
		{
			t.addEventListener("mouseout",function(t)
			{
				-1===f.indexOf(t.relatedTarget)&&c(null,!1)
			})
		}
		
		function u(t)
		{

			t.addEventListener("click",function(i)
			{

				i.preventDefault(),c(parseInt(t.getAttribute("data-index"))+1,!0)
			})
	
		}
		
		function c(t,a)
		{


		
			t&&0>t||t>n||(void 0===a&&(a=!0),i=t||i,r(f,function(t,n)
			{
				

				if(t.classList=="c-rating__item is-active")
					t.classList.remove("is-active")
				else
					t.classList.add("is-active")
			

			}
			),e&&a&&e(d()))
		}
		
		function d()
		{
			return i
		}
		
		var f=[];
		
		return function()
		{
			if(!t)throw Error("No element supplied.");
			if(!n)throw Error("No max rating supplied.");
			if(i||(i=0),0>i||i>n)throw Error("Current rating is out of bounds.");
			for(var e=0;n>e;e++)
			{
				var r=document.createElement("li");r.classList.add("c-rating__item"),r.setAttribute("data-index",e),i>e&&r.classList.add("is-active"),t.appendChild(r),f.push(r),a(r)
			}
		}(),
		{
			setRating:c,getRating:d
		}
	}
	window.rating=t
};

function aendern(data)
{

	if (adressen[data].standard=="ja")
		adressen[data].standard="nein"
	else
		adressen[data].standard="ja"

	
	i=0;
	while(i<=adressen.length-2)
	{
		if (data!=i && adressen[i].standard!="nein")
		{
			adressen[i].standard="nein"
			standard_aendern(i+1,1)
		}

		i=i+1;
	}
	standard_aendern(data+1,0)
}


function standard_aendern(index_2,option_)
{
	index=index_2-1

	$.ajax({
		type: "POST",
		url: "/account_page/adresse_speichern/",
		dataType: "json",
		data: { "hinzufuegen":-2,"indexnummer":adressen[index].indexnummer,"standard":adressen[index].standard,"plz":adressen[index].plz},
		success: function(data) {

			if (option_==0)
			{
				document.getElementsByClassName("adressbuch_daten")[0].innerHTML=data
				adressen_laden()
			}
			

			


		}
	})
	
}


    function addRatingWidget(shopItem, data,data_2) {

      var ratingElement = shopItem.querySelector('.c-rating');
      var currentRating = data_2;
      var maxRating = 1;

      var callback = function(rating) { 
    
		
		aendern(data)
	  };
      var r = rating(ratingElement,currentRating , maxRating, callback);
    }
	
	    function buildShopItem(data,index) {
      var shopItem = document.createElement('div');

      var html ="<div class='c-rating' style='margin-top:10px'></div><div class='standard_beschriftung'>Standardadresse</div>"


		
      shopItem.innerHTML = html;
	  
      document.getElementsByClassName("shop")[index].appendChild(shopItem);

      return shopItem;
    }
	
	
	


function hoehe_anpassen()
{

	
	document.getElementsByClassName("header-bottom")[0].style.marginTop=margintop+"px";

}


function profil_hauptseite()
{
	
	window.location.href="/account_page/";
}
