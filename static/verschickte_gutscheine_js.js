function profil_hauptseite()
{
	
	window.location.href="/polls/hello/account_page/";
}

function verschickte_gutscheine_laden (daten)
{
	alert(daten)


	var arr1 = daten.split(";;;");
	var arr2 = [];
	for (i = 0; i < arr1.length; i++) {
        arr2[i]=arr1[i].split(";;");
	}  
	verschickte_gutscheine=arr2;
	

	
	
	
	
	
	

	
	i=0;
	box_1="";
	box_2="";
	box_3="";
	box_4="";
	box_5="";
	


	
	i=0;
	if (verschickte_gutscheine!="")
	{
		while (i<=verschickte_gutscheine.length-2)
		{
			
			

			
			
			if (i>=1)
			{
				box_1=box_1+"<div style='border-top:1px solid #e6e6e6 ;'><div>"+verschickte_gutscheine[i][1]+"</div></div>"
				box_2=box_2+"<div style='border-top:1px solid #e6e6e6 ;'><div>"+verschickte_gutscheine[i][0]+"</div></div>"
				box_3=box_3+"<div style='border-top:1px solid #e6e6e6 ;'><div>"+verschickte_gutscheine[i][2]+"</div></div>"
				box_4=box_4+"<div style='border-top:1px solid #e6e6e6 ;'><div>"+verschickte_gutscheine[i][3]
				
				if(verschickte_gutscheine[i][3]!="Bestellt")
					box_4=box_4+"<div class='links_2'>Nochmals absenden</div></div></div>";
				
				
				

				
			}
			else
			{
				
				box_1=box_1+verschickte_gutscheine[i][1]
				box_2=box_2+verschickte_gutscheine[i][0]
				box_3=box_3+verschickte_gutscheine[i][2]
				box_4=box_4+verschickte_gutscheine[i][3]
				if(verschickte_gutscheine[i][3]!="Bestellt")
					box_4=box_4+"<div class='links_2'>Nochmals absenden</div>";

				
			
				

			}


			
			
			
			i=i+1;
		}
	}
	
	
	document.getElementsByClassName("spalte_text_1")[0].innerHTML=box_1;
	document.getElementsByClassName("spalte_text_2")[0].innerHTML=box_2;
	document.getElementsByClassName("spalte_text_3")[0].innerHTML=box_3;
	document.getElementsByClassName("spalte_text_4")[0].innerHTML=box_4;
	document.getElementsByClassName("spalte_text_5")[0].innerHTML=box_5;
	
	alert("asd")
}
	