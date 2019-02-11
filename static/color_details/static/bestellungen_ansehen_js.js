var bestellungen;

function profil_hauptseite()
{
	
	window.location.href="/hello/account_page/";
}








function bestellungen_aufrufen()
{
	bestellungen=JSON.parse(document.getElementsByClassName("bestellungen_daten")[0].innerHTML)
	bestelldetails=JSON.parse(document.getElementsByClassName("bestelldetails_daten")[0].innerHTML)
	i=0;
	block=""

	while (i<=bestellungen.length-1)
	{
		block=block+document.getElementsByClassName("zusammenfassung")[0].innerHTML;
		i=i+1;
	}
	document.getElementsByClassName("zusammenfassung")[0].innerHTML=block
	
	i=0;

	while (i<=bestellungen.length-1)
	{
		
		
		j=0;
		while (j<=bestelldetails.length-1)
		{

			if(bestelldetails[j].bestellnummer==bestellungen[i].bestellnummer)
			{

				document.getElementsByClassName("gesamtpreis")[i].innerHTML =replace_dot_comma(parseFloat(bestellungen[i].bestellungspreis)+parseFloat(bestellungen[i].lieferkosten)+parseFloat(bestellungen[i].rabatt)-parseFloat(bestellungen[i].braforfreevalue))+" EUR"
				document.getElementsByClassName("bestelldatum")[i].innerHTML =bestellungen[i].datum
				document.getElementsByClassName("bestellnummer")[i].innerHTML =bestellungen[i].bestellnummer
				document.getElementsByClassName("lieferstatus")[i].innerHTML ="<div  id='"+i+"' onclick='bewertungen_aufrufen(this.id)' style='font-weight_bold;text-decoration: underline;color:#DB7093;cursor:pointer'>"+bestelldetails[j].status+"</div>"
				document.getElementsByClassName("lieferdatum")[i].innerHTML =bestellungen[i].bestellnummer
				document.getElementsByClassName("order_picture")[i].src=bestelldetails[j].picture_link_small
				block=""
				block=block+"<div class='button_main_2' id='"+i+"' onclick='bestellung_details_aufrufen(this.id)'>Bestelldetails ansehen</div>"
				
				if (bestelldetails[j].status=="Zugestellt")
				{
					
					block=block+"<div class='verfolge_bestellung'><div id='"+i+"' class='button_main_2' onclick='verfolge_bestellung(this.id)'>Verfolge Bestellung</div></div>"
					block=block+"<div class='button_main_2'  id='"+i+"' onclick='bewertungen_aufrufen(this.id)' >Bewertung abgeben</div>"
				}
				else
					block=block+"<div class='button_main_2' id='"+i+"' onclick='verfolge_bestellung(this.id)'>Verfolge Bestellung</div>"
				
				document.getElementsByClassName("button_block_large")[i].innerHTML=block;


				break;
			}
			j=j+1;
		}
			
		i=i+1
	}
	

			
	
	
}

function replace_dot_comma(zahl)
{

	var zahl_=	zahl.toFixed(2);
	zahl_ = zahl_.toString();
	return zahl_.replace(".", ",");
}


function bestellung_details_aufrufen(i)
{
	window.location.href="/hello/account_page/bestellungen_ansehen/"+bestellungen[i].bestellnummer;
}

function bewertungen_aufrufen(i)
{
	window.location.href="/hello/account_page/bewertungen_bearbeiten/"+bestellungen[i].bestellnummer;
}

function verfolge_bestellung(i)
{

	window.location.href="/hello/account_page/sendungsverfolgung_tracken/"+bestellungen[i].bestellnummer;
}