var zahlungsmethoden;
var margintop;
var string_;
   var kreditkarten_nummer=new Array(15);
  		 var monat=new Array(12);
	 var jahr=new Array(6);

   
function felder_reset()
{
	document.getElementsByClassName("eingabefelder_karteninhaber")[0].value="";
	document.getElementsByClassName("eingabefelder_kartennummer")[0].value="";
	document.getElementsByClassName("eingabefelder_ablaufdatum_monat")[0].value="";
	document.getElementsByClassName("eingabefelder_ablaufdatum_jahr")[0].value="";
	
	
	document.getElementsByClassName("eingabefelder_pruefziffer")[0].value="";
	
	
	
}
function zahlungsmethoden_hinzufuegen()
{

	felder_reset()

	document.getElementsByClassName("header_style")[0].style.display="block"
	document.getElementsByClassName("button_main")[0].style.opacity="0.3"
	document.getElementsByClassName("button_main")[0].style.pointerEvents = 'none';
	
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



function zahlungsmethode_speichern(index)
{
	
	form.get(0).submit();
	
	/*

	if (index==-1)
		index_2=0;
	else
		index_2=index+1;
		
	kreditkarten_show("",index)

	if(check_field_empty(index_2)=="ok")
	{


	
			if (index==-1)
			{
				var hinzufuegen="1";
				index=0
				index_2=0;
				indexnummer=""
				standard="nein"
			}
			else
			{	
				var hinzufuegen="0";
				index_2=index+1
				indexnummer=zahlungsmethoden[index].indexnummer
				standard="nein"
			}
			
			if(zahlungsmethoden=="")
				standard="ja"
			

		
		card_number=document.getElementsByClassName("eingabefelder_kartennummer")[index_2].value.replace(/-/g , "")
		card_type=detectCardType(card_number)

		if(card_type=="visa" || card_type=="mastercard")
		{		
				
			$.ajax({
				type: "POST",
				url: "/hello/account_page/zahlungsmethode_speichern/",
				dataType: "json",
				data: { "hinzufuegen":hinzufuegen,"indexnummer":indexnummer,"name": document.getElementsByClassName("eingabefelder_karteninhaber")[index_2].value,"kreditkartennummer": document.getElementsByClassName("eingabefelder_kartennummer")[index_2].value,"ablaufmonat": document.getElementsByClassName("eingabefelder_ablaufdatum_monat")[index_2].value,
				"ablaufjahr": document.getElementsByClassName("eingabefelder_ablaufdatum_jahr")[index_2].value,"sicherheitscode": document.getElementsByClassName("eingabefelder_pruefziffer")[index_2].value,"zahlungsoption": "0","standard":standard,"card_type":card_type},
				success: function(data) {

					if(data!="existiert")
					{
						document.getElementsByClassName("zahlungsmethoden_daten")[0].innerHTML=data
	
						zahlungsmethode_hinzufuegen_schliessen();
	
						zahlungsmethode_abbrechen(-1)
	
						zahlungsmethoden_laden()
					}
					else
						alert_userdata("KARTENNUMMER WIRD BEREITS VON DIR VERWENET","Die eingegebene Kreditkartennummer wird bereits von dir verwendet. Wähle sie als Zahlungsmittel aus.")
					
	
				}
			});
		}
		else
			alert_userdata("KREDITKARTE WIRD NICHT UNTERSTÜTZT","Es werden nur Master- oder Visa-Kreditkarten unterstützt. Bitte gib eine andere Kreditkarte ein.")
	}
	
	
	*/
	
	
}

 function input_on_change(element)
{

	element.style.border="1px solid #e6e6e6 ";	
	element.style.color="#4E4E4E";
}




function zahlungsmethode_hinzufuegen_schliessen()
{
	document.getElementsByClassName("header_style")[0].style.display="none"
	document.getElementsByClassName("button_main")[0].style.opacity="1.0"
	document.getElementsByClassName("button_main")[0].style.pointerEvents = 'auto';

	
}




function zahlungsmethode_loeschen(index)
{

	var hinzufuegen="-1";
	index_2=index+1


				
	$.ajax({
		type: "POST",
		url: "/hello/account_page/zahlungsmethode_speichern/",
		dataType: "json",
		data: { "hinzufuegen":hinzufuegen,"indexnummer":zahlungsmethoden[index].indexnummer,"name": document.getElementsByClassName("eingabefelder_karteninhaber")[index_2].value,"kreditkartennummer": document.getElementsByClassName("eingabefelder_kartennummer")[index_2].value,"ablaufmonat": document.getElementsByClassName("eingabefelder_ablaufdatum_monat")[index_2].value,
		"ablaufjahr": document.getElementsByClassName("eingabefelder_ablaufdatum_jahr")[index_2].value,"sicherheitscode": document.getElementsByClassName("eingabefelder_pruefziffer")[index_2].value,"zahlungsoption": "0"},
		success: function(data) {

			document.getElementsByClassName("zahlungsmethoden_daten")[0].innerHTML=data
			zahlungsmethode_abbrechen(-1)
			zahlungsmethoden_laden()

		}
	});
	
}

function monat_jahr_select_fuellen(index)
{

	 
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
	 
	 
	box="";
	 var i=0;
	 while (i<=12)
	 {
		box=box+"<option>"+monat[i]+"</option>";
		 i=i+1;
	 }
	 
	 
	 box_2="";
	 var i=0;
	 while (i<=6)
	 {
		box_2=box_2+"<option>"+jahr[i]+"</option>";
		 i=i+1;
	 }
	 

	 document.getElementsByClassName("eingabefelder_ablaufdatum_monat")[index].innerHTML=box;
	 document.getElementsByClassName("eingabefelder_ablaufdatum_jahr")[index].innerHTML=box_2;

}


function zahlungsmethoden_laden(daten)
{


	monat_jahr_select_fuellen(0)
	margintop=0;
	
	zahlungsmethoden=JSON.parse(document.getElementsByClassName("zahlungsmethoden_daten")[0].innerHTML)
	
	 
	


		var box="";
		
	i=0;
	if (zahlungsmethoden!="")
	{
		while (i<=zahlungsmethoden.length-1)
		{
			
			box=box+"<div class='header_style_3' >";
			
			
			box=box+"<div class='oberes_feld' style='width:100%;height:100px;'>"
			box=box+"<div class='kartendetails'>";
			box=box+"<div style='vertical-align:middle;width:30%;height:100px;display:table-cell;''>"
			box=box+"****-****-****-"+zahlungsmethoden[i].kreditkartennummer+"<br>"
			box=box+"<div class='gueltigkeitsdatum'>Gültig: "+zahlungsmethoden[i].ablaufmonat+" "+zahlungsmethoden[i].ablaufjahr
			box=box+"</div>"
			box=box+"</div>"
			box=box+"</div>"
			
			
			box=box+"<div class='card_type'>"	
			
			if(zahlungsmethoden[i].cardtype=="visa")
				box=box+"<div style='vertical-align:middle;height:100px;display:table-cell;'><img src='/static/"+zahlungsmethoden[i].cardtype+"_card.png'  width='45' height='18'> </div>";
			else
				box=box+"<div style='vertical-align:middle;height:100px;display:table-cell;'><img src='/static/"+zahlungsmethoden[i].cardtype+"_card.png'  width='54' height='40' ></div>";
			box=box+"</div>"
			
			box=box+"<div class='standard_feld'>"	
			box=box+"<div class='shop_2'><div class='shop' standard_aendern("+i+",0)></div></div>"		
			box=box+"</div>"
			
			
			box=box+"<div style='float:left;width:2%;height:100px;border-left: 1px solid #e6e6e6 ;'>"		
			box=box+"</div>"
			box=box+"<div style='float:left;width:10%;height:100px;'>"		
			box=box+"<div class='bearbeiten_feld' onclick='zahlunsgmethode_bearbeiten("+i+")'>Bearbeiten</div>"
			box=box+"</div>"
			box=box+"</div>"
			



			box=box+"<div class='zusammenfassung' style='display:none;'>"
			box=box+"<div class='eingabefelder_headline'><b>Karteninhaber</b><br>"
			box=box+"<input class='eingabefelder_karteninhaber' onkeydown='input_on_change(this)'  type='text' value='"+zahlungsmethoden[i].name+"'/>"
			box=box+"</div>"
					
			box=box+"<div class='eingabefelder_headline'><b>Kartennummer</b><br>"
			box=box+"<input class='eingabefelder_kartennummer' placeholder='' type='text' onKeyUp='kreditkarten_show(event,"+i+")' onKeyDown='kreditkarten_show(event,"+i+")' maxlength='19' onBlur='kreditkarten_show(event,"+i+")' />"
			box=box+"</div>"
								
			box=box+"<div class='eingabefelder_headline'><b>Ablaufdatum</b><br>"
			box=box+"<select class='eingabefelder_ablaufdatum_monat' style='width:45%;float:left;' onclick='input_on_change(this)' ></select>"
			box=box+"<select class='eingabefelder_ablaufdatum_jahr' style='width:45%;float:right;' onclick='input_on_change(this)' ></select>"
			box=box+"</div>	"
					
					
			box=box+"<div class='eingabefelder_headline'><b>Prüfziffer</b><br>"
			box=box+"<input type='text' class='eingabefelder_pruefziffer' maxlength='3' onkeydown='input_on_change(this)' />"
			box=box+"</div>"
					
			box=box+"<div class='warnhinweis' style='color:red;float:left;'> </div>"
			box=box+"<br><br><br>"
			box=box+"<div class='button_loeschen' onclick='zahlungsmethode_loeschen("+i+")'>Löschen</div><br><br>";
			box=box+"<div class='adresse_speichern_button' onclick='zahlungsmethode_speichern("+i+")'>Speichern</div>";	
			box=box+"<div class='button_abbrechen' onclick='zahlungsmethode_abbrechen("+i+")'>Abbrechen</div>";
			
			box=box+"</div>"
			box=box+"</div>"
			
				
				

			i=i+1;
		}
	}

	
	document.getElementById("existierende_zahlungsmethoden_anzeigen").innerHTML=box; 
//document.getElementsByClassName("header_style_3")[0].style.marginTop="40px";
//	document.getElementsByClassName("header_style_3")[i-1].style.marginBottom="40px";
	j=0;	
	while(j<=i)
	{
		monat_jahr_select_fuellen(j)
		j=j+1;
	}
	
	
	i=0;
	if (zahlungsmethoden!="")
	{
		while (i<=zahlungsmethoden.length-1)
		{
			var j=0;
			while (j<=12)
			{

				if(zahlungsmethoden[i].ablaufmonat==monat[j])
					document.getElementsByClassName("eingabefelder_ablaufdatum_monat")[i+1].selectedIndex=j;
				j=j+1;
			}
			var j=0;
			while (j<=6)
			{
				if(zahlungsmethoden[i].ablaufjahr==jahr[j])
					document.getElementsByClassName("eingabefelder_ablaufdatum_jahr")[i+1].selectedIndex=j;
				j=j+1;
			}
			i=i+1;
		}
	 }
	 
	 
	 
	for (var i = 0; i <= zahlungsmethoden.length-1; i++) {
		
		if (zahlungsmethoden[i].standard=="ja")
			addRatingWidget(buildShopItem("1",i), i,"1");
		else
			addRatingWidget(buildShopItem("1",i), i,"0");
			

      }



	





	hoehe_anpassen()
	
}



function zahlunsgmethode_bearbeiten(index)
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


function zahlungsmethode_abbrechen(index)
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

	}
}


function hoehe_anpassen()
{
	
	document.getElementsByClassName("header-bottom")[0].style.marginTop=margintop+"px";
}


function profil_hauptseite()
{
	
	window.location.href="/hello/account_page/";
}


function array_definieren()
{
	i=0;


	while(i<=15)
	{	
		kreditkarten_nummer[i]=new Array;
		i=i+1;
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
	
	

	if (zahlungsmethoden[data].standard=="ja")
		zahlungsmethoden[data].standard="nein"
	else
		zahlungsmethoden[data].standard="ja"

	
	i=0;
	while(i<=zahlungsmethoden.length-1)
	{
		if (data!=i && zahlungsmethoden[i].standard!="nein")
		{
			zahlungsmethoden[i].standard="nein"
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
		url: "/hello/account_page/zahlungsmethode_speichern/",
		dataType: "json",
		data: { "hinzufuegen":-2,"indexnummer":zahlungsmethoden[index].indexnummer,"standard":zahlungsmethoden[index].standard},
		success: function(data) {
			if (option_==0)
			{
				document.getElementsByClassName("zahlungsmethoden_daten")[0].innerHTML=data
				zahlungsmethoden_laden()
			}

			


		}
	})
	
}


function check_field_empty(index)
{
	
	list=new Array(10)
	list[0]="eingabefelder_karteninhaber"
	list[1]="eingabefelder_kartennummer"
	list[2]="eingabefelder_ablaufdatum_monat"
	list[3]="eingabefelder_ablaufdatum_jahr"
	list[4]="eingabefelder_pruefziffer"

	
	
	status_="ok"
	i=0;
	while (i<=4)
	{
		if(i==1)
		{
			if(document.getElementsByClassName(list[i])[index_2].value.length!=19)
			{
				status_="nicht ok";
				alert_userdata("FELDER AUSFLÜLLEN","Bitte alle benötigten Felder ausfüllen.");		
				document.getElementsByClassName(list[i])[index_2].style.border="1px solid red";	
			}
		}
		else
		{
			if(i==4)
			{
				if(document.getElementsByClassName(list[i])[index_2].value.length!=3)
				{
					status_="nicht ok";
					alert_userdata("FELDER AUSFLÜLLEN","Bitte alle benötigten Felder ausfüllen.");	
					document.getElementsByClassName(list[i])[index_2].style.border="1px solid red";	
				}
			}
			else
			{
				if (document.getElementsByClassName(list[i])[index_2].value=="")
				{
					status_="nicht ok";
					
					document.getElementsByClassName(list[i])[index_2].style.border="1px solid red";	
				}
				
				
			}
		}

		i=i+1;
	}
	


	
	return status_
		

	
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

      var html ="<div class='c-rating' style='margin-top:10px'></div><div class='standard_beschriftung'>Standard</div>"



      shopItem.innerHTML = html;
	  
      document.getElementsByClassName("shop")[index].appendChild(shopItem);

      return shopItem;
    }
	
	
	






 function kreditkarten_show(evt,index)
 {

	 
	 if(index==-1)
		 index=0
	 else
		 index=index+1;
		
	if(evt!="")
	{
		var theEvent = evt || window.event;
		var key = theEvent.keyCode || theEvent.which;


	}
	else
		key=""

	if(key==48 || key==49 || key==50 || key==51 || key==52 || key==53 || key==54 || key==55 || key==56 || key==57 || key==8 || key==17 || key==91 || key==67 || key==86 || key=="")	
	{

		if(document.getElementsByClassName("eingabefelder_kartennummer")[index].value!=string_ )
		{
			document.getElementsByClassName("eingabefelder_kartennummer")[index].style.border="1px solid #e6e6e6 ";	
			document.getElementsByClassName("eingabefelder_kartennummer")[index].style.color="#4E4E4E";
			string_=document.getElementsByClassName("eingabefelder_kartennummer")[index].value;
			var max=document.getElementsByClassName("eingabefelder_kartennummer")[index].value.length;


			var number=document.getElementsByClassName("eingabefelder_kartennummer")[index].value;	
			number=number.replace("-","");
			number=number.replace("-","");
			number=number.replace("-","");
			
			document.getElementsByClassName("eingabefelder_kartennummer")[index].value=number;

			var max=document.getElementsByClassName("eingabefelder_kartennummer")[index].value.length;	

			var i=0;
			var j=0;
			while(i<=max-1)
			{
				var number=document.getElementsByClassName("eingabefelder_kartennummer")[index].value.charAt(i);
				if(isNaN(number)==false)
				{
					if(i==4 || i== 8 || i== 12 )
					{
						kreditkarten_nummer[j]="-";
						j=j+1;
						max=max+1;
						kreditkarten_nummer[j]=document.getElementsByClassName("eingabefelder_kartennummer")[index].value.charAt(i);
					}
					else
					{
						kreditkarten_nummer[j]=document.getElementsByClassName("eingabefelder_kartennummer")[index].value.charAt(i);
					}
				}
				i=i+1;
				j=j+1;

			}
			
			i=0

			document.getElementsByClassName("eingabefelder_kartennummer")[index].value="";
			string_="";
			while(i<=max-1)
			{
				document.getElementsByClassName("eingabefelder_kartennummer")[index].value=document.getElementsByClassName("eingabefelder_kartennummer")[index].value+kreditkarten_nummer[i];
				i=i+1;	
			}	
			string_=document.getElementsByClassName("eingabefelder_kartennummer")[index].value;
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
