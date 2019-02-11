
var gerichte;
var bestellung;
var height;
var fahrer_kapazitaet;
var gerichte;
var aenderung;
var min_height;
var rebates;




function check_google_analytics()
{
	




	if(bestellung[0].datasenttogoogleanalytics!="ja")
	{		
	
	
		contents_list=JSON.parse(document.getElementById("contents_list").innerHTML)
	
	
	google_content_list=contents_list[0].google
				
		  fbq('track', 'Purchase', {
	    value: document.getElementsByClassName("bestellung_gesamt")[0].innerHTML,
	    currency: 'EUR',
	    content_ids: document.getElementsByClassName("stylecodes_colorcodes")[0].innerHTML,
	    content_type: 'Sets',
	  });

		gtag('event', 'purchase', {
  			"transaction_id":bestellung[0].bestellnummer,
  "affiliation": "Darling Lace",
  "value": String(parseFloat(document.getElementsByClassName("bestellung_gesamt")[0].innerHTML)/1.19),
  "currency": "EUR",
  "tax": String(parseFloat(document.getElementsByClassName("bestellung_gesamt")[0].innerHTML)-parseFloat(document.getElementsByClassName("bestellung_gesamt")[0].innerHTML)/1.19),
  "shipping": 0,
  "items":google_content_list
  });




			$.ajax({
			type: "GET",
			url: "/cart_data_sent_to_google_analytics/",
			dataType: "json",
			data: { "bestellnummer":bestellung[0].bestellnummer,"usercode":bestellung[0].usercode},
			success: function(data) {

				
				}
			
		})
	}


	

}



function status_anzeigen(j)
{

	if(bestelldetails[j].status=="Bestellt")
		return ""
	else
		return bestelldetails[j].status;
	
}


function bestellte_lingerie_anzeigen()
{

	
	box="";
	var j=0;
	height=0;


	while(j<=bestelldetails.length-1)
	{
		pictures_bestelldetails=JSON.parse(bestelldetails[j].picture_link_small)
			box=box+"<div style='float:left;width:100%;margin-bottom:10px;'>"
			box=box+"<img src='"+pictures_bestelldetails[0].link+"' width='100' style='float:left;'/>"
			box=box+"<div style='margin-left:10px;float:left;'/><b>"+bestelldetails[j].style+"</b></div>"

			box=box+"<div class='anzahl_anzeigen' style='float:right;'>Anzahl: "+bestelldetails[j].anzahl+"</div>"
					
			
			box=box+"<br><div class='details_order'>"+bestelldetails[j].bhgroesse+"</div> <br>"
			box=box+"<div class='details_order'>"+bestelldetails[j].slipgroesse+"</div><br><br>"
			box=box+"<div class='details_order'>"+replace_dot_comma(parseFloat(bestelldetails[j].preis)*bestelldetails[j].anzahl)+" EUR</div> </div>";


		
		j=j+1;
	}
	

	document.getElementsByClassName ("lingerie_i")[0].innerHTML=box;
	

	j=0;
	zaehler=0;
	
	



}


 function alert_click_schliessen1() {
	$('#alert_box_rechnungsbetrag').modal('hide');
	$('#alert_box_reload').modal('hide');
}

function weiter_einkaufen()
{
	window.location.href="https://www.darlinglace.com/Produktauswahl/BH%20Sets/";
	
	
}

function bearbeitungsblock_hinzufuegen()
{
	var block="";
	/*j=0;
	while(j<=bestelldetails.length-1)
	{
		if(status_anzeigen(j)=="")
		{
			
			block=block+"<div  class='button_uebernehmen' style='margin-top:25px;margin-Bottom:25px;display:none' onclick='bestellung_bearbeiten_uebernehmen()' onmouseenter='button_bearbeiten_onmouseenter()' onmouseout='button_bearbeiten_onmouseleave()'>Übernehmen</div>"
			block=block+"<div  class='button_bearbeiten' style='margin-top:25px;margin-Bottom:25px;' onclick='bestellung_bearbeiten()' onmouseenter='button_bearbeiten_onmouseenter()' onmouseout='button_bearbeiten_onmouseleave()'>Bearbeiten</div>";
			block=block+"<div class='button_abbrechen' style='margin-top:25px;margin-Bottom:25px;display:none;max-width:100px;float:right;margin-right:10px;' onclick='bestellung_bearbeiten_abbrechen()' onmouseenter='button_bearbeiten_onmouseenter()' onmouseout='button_bearbeiten_onmouseleave()'>Abbrechen</div>"
			break;
		}
		j=j+1;
	}*/
	
	
	block=block+"<button name='submit' id='order_summary_button_zurueck'  onclick='bestellung_bearbeiten_hauptseite()' >"
	block=block+"<i class='fa fa-circle-o-notch fa-spin' id='button_zurueck_id_logo' style='display:none'></i>"
	block=block+"<div id='button_zurueck_id_text'>Bestellungen</div>"
	block=block+"</button>"
	
	block=block+"<button  id='button_weitershoppen' name='submit' class='button_order_summary_weitershoppen'  onclick='weiter_einkaufen()' >"
	block=block+"<i class='fa fa-circle-o-notch fa-spin' id='button_weitershoppen_logo' style='display:none'></i>"
	block=block+"<div id='button_weitershoppen_text'>Weiter einkaufen</div>"
	block=block+"</button>"
	

	block=block+"<br><br><br>";
	
	document.getElementsByClassName("bearbeitunsblock_hinzufuegen")[0].innerHTML=block;
}








 function input_on_change(element,element2)
{
	element.style.border="1px solid #e6e6e6 ";	
	element2.style.color="#4E4E4E";
}
 
 

function bestellung_aufrufen()
{
	
	bestellung=JSON.parse(document.getElementsByClassName("bestellung_daten")[0].innerHTML)
	rebates=JSON.parse(document.getElementsByClassName("rebates")[0].innerHTML)



	lingerieselection=JSON.parse(document.getElementsByClassName("lingerie_daten")[0].innerHTML)
		
	bestelldetails=JSON.parse(document.getElementsByClassName("bestelldetails_daten")[0].innerHTML)	

}

function profil_hauptseite()
{
	
	window.location.href="/account_page/";
}


function bestellung_bearbeiten_hauptseite()
{
	
	window.location.href="/account_page/bestellungen_ansehen/";
}



function bestellung_block()
{
	

	var maxim= document.getElementsByClassName("zahlung");

	preis_=	replace_dot_comma(parseFloat(bestellung[0].bestellungspreis));
	

	
	rabatt=parseFloat(bestellung[0].rabatt);
	var gesamt=parseFloat(bestellung[0].bestellungspreis)-parseFloat(bestellung[0].lieferkosten)+rabatt+aenderung-bestellung[0].braforfreevalue-bestellung[0].storecredit;

	preis_=	replace_dot_comma(parseFloat(bestellung[0].bestellungspreis));
	rabatt_=	replace_dot_comma(parseFloat(bestellung[0].rabatt));
	preis_gesamt=	replace_dot_comma(gesamt);
	lieferung=replace_dot_comma(parseFloat(bestellung[0].lieferkosten))


	var uebersicht="<div style='width:50%;float:left;'>Bestellung:</div><div style='float:right;width:50%;text-align:right;'>"+replace_dot_comma(rebates[0].bestellung)+" EUR</div><br>";
	if (rebates[0].aenderung!=0)
		uebersicht=uebersicht+"<div style='float:left;color:red;'>Bestelländerung:</div><div style='float:right;color:red;'>"+replace_dot_comma(parseFloat(rebates[0].aenderung))+" EUR</div><br>";





		
	if(rebates[0].lieferkosten!="0")	
		uebersicht=uebersicht+"<div style='width:50%;float:left;'>Lieferung:</div><div style='float:right;width:50%;text-align:right;'>"+replace_dot_comma(rebates[0].lieferkosten)+" EUR</div><br>";
	else		
		uebersicht=uebersicht+"<div style='width:50%;float:left;'>Lieferung:</div><div style='float:right;width:50%;text-align:right;'>KOSTENLOS</div><br>";
	
	if(rebates[0].braforfreevalue!=0)
		uebersicht=uebersicht+"<div style='width:50%;float:left;'>Sets umsonst (VIP):</div><div style='float:right;width:50%;text-align:right;'>-"+replace_dot_comma(parseFloat(rebates[0].braforfreevalue))+" EUR</div><br>";
	if(rebates[0].storecredit!=0)
		uebersicht=uebersicht+"<div style='width:50%;float:left;'>VIP Guthaben:</div><div style='float:right;width:50%;text-align:right;'>-"+replace_dot_comma(parseFloat(rebates[0].storecredit))+" EUR</div><br>";



	if(rebates[0].coupon!=0)
		uebersicht=uebersicht+"<div style='float:left;'>Rabatt:</div><div style='float:right;'>-"+replace_dot_comma(parseFloat(rebates[0].coupon))+" EUR</div><br>";	


	if(rebates[0].credit!=0)
		uebersicht=uebersicht+"<div style='float:left;'>Freundschaftswerbung:</div><div style='float:right;'>-"+replace_dot_comma(parseFloat(rebates[0].credit))+" EUR</div><br>";	
		
		
	uebersicht=uebersicht+"<div style='border-bottom:1px solid #e6e6e6 ;'></div>";
	

	if (rebates[0].aenderung!=0)
		uebersicht=uebersicht+"<div style='float:left;font-weight: bold;color:red;'>Gesamt:</div><div style='float:right;font-weight: bold;color:red;'>"+replace_dot_comma(rebates[0].gesamtpreis)+" EUR</div><br><br>";
	else
		uebersicht=uebersicht+"<div style='float:left;font-weight: bold;'>Gesamt:</div><div style='float:right;font-weight: bold;'>"+replace_dot_comma(rebates[0].gesamtpreis)+" EUR</div><br><br>";
	
	if (bestellung[0].zahlungsoption=="0")
		uebersicht=uebersicht+"<div style='line-Height:18px'>Zahlung per Kreditkarte: ****-****-****-"+bestellung[0].kartennummer+"</div>";



	if (bestellung[0].zahlungsoption=="3")
		uebersicht=uebersicht+"<div style='line-Height:18px'>Zahlung per SEPA-Lastschriftverfahren: "+bestellung[0].kartennummer+"</div>";

	if (bestellung[0].zahlungsoption=="4")
		uebersicht=uebersicht+"<div style='line-Height:18px'>Zahlung per Rechnung über Klarna</div>";	
	maxim[0].innerHTML=uebersicht+"</div>";
	




	
	
}

function bestellnummer_abrufen()
{
	
	document.getElementsByClassName("bestellnummer")[0].innerHTML="Bestellnummer: "+bestellung[0].bestellnummer.toUpperCase();
	document.getElementsByClassName("headline_text")[0].innerHTML="Bestelldatum: "+bestellung[0].datum+"<br>Lieferdatum: "+bestellung[0].liefertermin;
	
	//.toUpperCase();
}


function lieferuebersicht()
{
	
	var maxim= document.getElementsByClassName("lieferung_i");
	uebersicht="<div style='width:45%;float:left;'><b>Rechnungsadresse:</b><br>";
	
	
	uebersicht=uebersicht+"<div class='adresse_anzeigen' style='display:block;float:left'>"+bestellung[0].anrederechnung+" "+bestellung[0].vornamerechnung+" "+bestellung[0].nachnamerechnung+"</div><br>";
	if(bestellung[0].unternehmensdetailsrechnung!="")
		uebersicht=uebersicht+"<div class='adresse_anzeigen' style='display:block;float:left'>"+bestellung[0].unternehmensdetailsrechnung+"</div><br>";
	uebersicht=uebersicht+"<div class='adresse_anzeigen' style='display:block;float:left'>"+bestellung[0].strasserechnung+" "+bestellung[0].hausnummerrechnung+"</div><br>";
	
	uebersicht=uebersicht+"<div class='plz_stadt_anzeigen' style='display:block;float:left;width:100%;'>"+bestellung[0].plzrechnung+" "+bestellung[0].stadtrechnung+"</div><br>"
	uebersicht=uebersicht+bestellung[0].landrechnung+"</div></div>";


	uebersicht=uebersicht+"<div style='width:45%;float:right;'><b>Lieferadresse:</b><br>";
	uebersicht=uebersicht+"<div class='adresse_anzeigen' style='display:block;float:left'>"+bestellung[0].anredelieferadresse+" "+bestellung[0].vornamelieferadresse+" "+bestellung[0].nachnamelieferadresse+"</div><br>";
	if(bestellung[0].unternehmensdetailslieferadresse!="")
		uebersicht=uebersicht+"<div class='adresse_anzeigen' style='display:block;float:left'>"+bestellung[0].unternehmensdetailslieferadresse+"</div><br>";
	uebersicht=uebersicht+"<div class='adresse_anzeigen' style='display:block;float:left'>"+bestellung[0].strasselieferadresse+" "+bestellung[0].hausnummerlieferadresse+"</div><br>";
	uebersicht=uebersicht+"<div class='plz_stadt_anzeigen' style='display:block;float:left;width:100%;'>"+bestellung[0].plzlieferadresse+" "+bestellung[0].stadtlieferadresse+"</div><br>"
	uebersicht=uebersicht+bestellung[0].landlieferadresse+"</div><br>";
	
	maxim[0].innerHTML=uebersicht;


	
}





function replace_dot_comma(zahl)
{
	var zahl_=	zahl.toFixed(2);
	zahl_ = zahl_.toString();
	return zahl_.replace(".", ",");
}

function compareLastColumn(a, b) {
    if (a[4] === b[4]) {
        return 0;
    }
    else {
        return (a[4] < b[4]) ? -1 : 1;
    }
}

