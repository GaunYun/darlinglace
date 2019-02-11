var gutscheinkonto;

function profil_hauptseite()
{
	
	window.location.href="/hello/account_page/";
}

function gutscheinkonto_laden ()
{
	gutscheinkonto=JSON.parse(document.getElementsByClassName("gutscheinkonto_daten")[0].innerHTML)
	alert(gutscheinkonto)
	
	
	
	i=0;
	box_1="";
	box_2="";
	box_3="";
	box_4="";
	amount=0;

	


	
	i=0;
	if (gutscheinkonto!="")
	{
		while (i<=gutscheinkonto.length-1)
		{
			alert(gutscheinkonto)
			

			
			if (i>=0)
			{
				if (parseFloat(gutscheinkonto[i].gutscheinwert)>0)					
					box_1=box_1+"<div style='border-bottom:1px solid #e6e6e6 ;'><div>Freundschaftswerbung ("+gutscheinkonto[i].vorname+" "+gutscheinkonto[i].nachname+")</div></div>"
				else
					box_1=box_1+"<div style='border-bottom:1px solid #e6e6e6;float:left;width:500px;'><div style='float:left'>Gutscheineinlösung, Bestellnummer: </div><div class='links' style='cursor:pointer;float:left;margin-left:5px;' onclick='bestellnummer_aufrufen("+i+")'> "+gutscheinkonto[i].bestellnummer+"</div></div>"
				

				
				box_2=box_2+"<div style='border-bottom:1px solid #e6e6e6 ;'><div>"+gutscheinkonto[i].datum+"</div></div>"
				box_3=box_3+"<div style='border-bottom:1px solid #e6e6e6 ;'><div>"+replace_dot_comma(parseFloat(gutscheinkonto[i].gutscheinwert))+"</div></div>"
				amount=amount+(parseFloat(gutscheinkonto[i].gutscheinwert));
					
				
				
				
			}
			else
			{
				
				if (parseFloat(gutscheinkonto[i].gutscheinwert)>0)					
					box_1=box_1+"<div>Freundschaftswerbung ("+gutscheinkonto[i].vorname+" "+gutscheinkonto[i].nachname+")</div>"
				else
					box_1=box_1+"<div style='border-top:1px solid #e6e6e6;float:left;'>Gutscheineinlösung, Bestellnummer: <div class='links' style='cursor:pointer;float:right;margin-left:5px;' onclick='bestellnummer_aufrufen("+i+")'> "+gutscheinkonto[i].bestellnummer+"</div></div><br>"
				

				
				box_2=box_2+"<div>"+gutscheinkonto[i].datum+"</div>"
				box_3=box_3+"<div>"+replace_dot_comma(parseFloat(gutscheinkonto[i].gutscheinwert))+"</div>"
				amount=amount+(parseFloat(gutscheinkonto[i].gutscheinwert));
			}

			
			i=i+1;
		}
	}
	
	
	
	
	
	
	document.getElementsByClassName("spalte_text_1")[0].innerHTML=box_1;
	document.getElementsByClassName("spalte_text_2")[0].innerHTML=box_2;
	document.getElementsByClassName("spalte_text_3")[0].innerHTML=box_3;
	amount=Math.round(amount*100)/100

	document.getElementById("total_amount").innerHTML=replace_dot_comma(amount);


}


function bestellnummer_aufrufen(index)
{
	window.location.href="/hello/account_page/bestellungen_ansehen/"+gutscheinkonto[index].bestellnummer;
	
}


function replace_dot_comma(zahl)
{

	var zahl_=	zahl.toFixed(2);
	zahl_ = zahl_.toString();
	return zahl_.replace(".", ",");
}
	