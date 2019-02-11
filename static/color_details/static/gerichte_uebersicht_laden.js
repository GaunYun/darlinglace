	var filter=new Array(5);
	var scroll_position_absolute;
   var gerichte = new Array(50);
	var cart=new Array(10);
	var cart_gesamt;
	var gewaehltes_datum;
	var auswahl_tag_final;
   /* 
   
   
   
   
   i,0,0: Name
   i,1,var: Filter: 1) Vegan, 2) Vegetarisch, 3) Gluten-frei, 4) Laktosefrei, 5) Nussfrei, 6) Ei-frei*/
   
 window.onload=function datum_abrufen()
 {
	
	 alert("asd");
	 
	 
	 
	document.getElementsByClassName("filter_leer")[0].style.display="none";
	var jetzt = new Date();
	var Tag = jetzt.getDate();
	var Jahresmonat = jetzt.getMonth();
	var Monat = new Array("Januar", "Februar", "März", "April", "Mai", "Juni","Juli", "August", "September", "Oktober", "November", "Dezember");

	//document.getElementById("aktuelles_Datum").innerHTML="Heute, " + Tag + ". " + Monat[Jahresmonat];
	
	for (var i=0; i<=5; i++) 
	{
		filter[i]=new Array;
	}
	var maxim= document.getElementsByClassName("gericht_auswahl_text");
	var maxim_2= document.getElementsByClassName("bild-laden");


	   

	   

   
   
	i=0;
	
	var variable="";
	var variable_2="";
	
	
	while( i <= gerichte.length-1)
	{

		variable_2 = "<img src='"+gerichte[i][2]+"'	width='100%' ></img>";
		variable="<br>"+gerichte[i][1]+"";	

			
		if(gerichte[i][4]=="true")
		{
			variable = variable+ "<img src='/static/vegan.PNG'  width='15' height='15'></img>";		
		}
		
		if(gerichte[i][5]=="true")
		{
			variable = variable+ "<img src='/static/vegetarian.png'  width='15' height='15'></img>";		
		}
		
		if(gerichte[i][6]==="true")
		{
			variable = variable+ "<img src='/static/gluten-free.png'  width='15' height='15'></img>";		
		}
		if(gerichte[i][7]==="true")
		{
			variable = variable+ "<img src='/static/dairy-free.png'  width='15' height='15'></img>";		
		}
		
		if(gerichte[i][8]==="true")
		{
			variable = variable+ "<img src='/static/nut-free.png'  width='15' height='15'></img>";		
		}
		
		if(gerichte[i][9]==="true")
		{
			variable = variable+ "<img src='/static/egg-free.png'  width='15' height='15'></img>";		
		}

		variable=variable+"<br><br>";
		maxim[i].innerHTML=variable;
		maxim_2[i].innerHTML=variable_2;
		variable="";
		variable_2="";

		i=i+1;
	}
	   
	 
 }
 

   
   
   
function filter_(clicked_id)
{

	var maxim= document.getElementsByClassName("box");
	var filter_var=document.getElementsByClassName("filter");

	if(filter_var[clicked_id].style.backgroundColor=="")
	{

		filter_var[clicked_id].style.backgroundColor="#e6e6e6";
		filter[clicked_id]=1;
		
		j=0;
		i=0;
		var nicht_zeigen=0;
		while(i<maxim.length)	
		{
			nicht_zeigen=0;
			j=0;
			while(j<=5)
			{
				if (filter[j]==1 && gerichte[i][1][j]=="no")
				{
					nicht_zeigen=1;
				}
				j=j+1;
			}
			
			if(nicht_zeigen==1)
			{
				
				maxim[i].style.display="none";	
				
			}
			else
			{
				maxim[i].style.display="block";	
				
			}
			i=i+1;
		}	
	}
	else
	{

		var nicht_zeigen=0;
		filter_var[clicked_id].style.backgroundColor="";
		filter[clicked_id]=0;

		
		j=0;
		i=0;
		while(i<maxim.length)	
		{
			nicht_zeigen=0;
			j=0;
			while(j<=5)
			{
				if (filter[j]==1 && gerichte[i][1][j]=="no")
				{
					nicht_zeigen=1;
				}
				j=j+1;
			}
			
			if(nicht_zeigen==1)
			{
				
				maxim[i].style.display="none";	
				
			}
			else
			{
				maxim[i].style.display="block";	
				
			}
			i=i+1;
		}								

	}
	
	
	i=0;
	var status=0;
	while(i<maxim.length)	
	{
		if(maxim[i].style.display=="block")
			status=1;
		
		i=i+1;
	}
	

	
	if(status==0)
		document.getElementsByClassName("filter_leer")[0].style.display="block";
	else
			document.getElementsByClassName("filter_leer")[0].style.display="none";
		
	
	
	
	

}





function datum_auswahl(ausgewaehlter_tag) 	
{
	
	
		var maxim= document.getElementsByClassName("datum_auswahl");
		
		
		var jetzt = new Date();
		var Tag = jetzt.getDate();
		var Jahresmonat = jetzt.getMonth();
		var TagInWoche = jetzt.getDay();
		var Wochentag = new Array("SO", "MO", "DI", "MI",
		"DO", "FR", "SA");
		var Monat = new Array("Januar", "Februar", "März", "April",
		"Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember");
		
		var Wochentag_ausfuehrlich = new Array("Sonntag", "Montag", "Dienstag", "Mittwoch",
		"Donnerstag", "Freitag", "Samstag");
		
		j=0;
		tage=jetzt.getDate();

		var day = jetzt.getDate();

		
		 ;/* hier eintragen, auf welchen Tag User geklick hat */
		

		var DatumZeitJetzt = new Date();
		var DatumZukunft = new Date();
		var DatumZukunft_ = new Date();
		
		var AnzahlTage = 0;
		var msProTag = 86400000;
		
		if (ausgewaehlter_tag>4)
			window.location.href="/polls/hello/4/";

		DatumZukunft.setTime(DatumZeitJetzt.getTime() + AnzahlTage * msProTag);
		auswahl_tag=0;
		TagInWoche = DatumZukunft.getDay();
		DatumZukunft.setTime(DatumZeitJetzt.getTime() + ausgewaehlter_tag * msProTag);
		
		alert("asd");
		
		
		
		/*if (TagInWoche == 6 || TagInWoche == 0)
		{	

				if(ausgewaehlter_tag==6)
				{
					ausgewaehlter_tag=ausgewaehlter_tag+2;
					
				}
				else
				{
					
					ausgewaehlter_tag=ausgewaehlter_tag+1;
				}
		}
		
		
		var TagInWoche = jetzt.getDay();

		auswahl_tag_merker=0;

		while(auswahl_tag<ausgewaehlter_tag)
		{
			

			
			if (TagInWoche == 6 || TagInWoche == 0)
			{
				
				if (TagInWoche==6)
					AnzahlTage=AnzahlTage+2;
				else
					AnzahlTage=AnzahlTage+1;
				TagInWoche=1;
				
				auswahl_tag_merker=-1;
				DatumZukunft.setTime(DatumZeitJetzt.getTime() + AnzahlTage * msProTag);
			}
			else
			{
				
				TagInWoche=TagInWoche+1;
				AnzahlTage=AnzahlTage+1;

				DatumZukunft.setTime(DatumZeitJetzt.getTime() + AnzahlTage * msProTag);				
			}
				

			auswahl_tag=auswahl_tag+1;

			
		}

		
		var jahr=DatumZukunft.getYear()+1900;

		gewaehltes_datum=DatumZukunft.getDate() + ". " + Monat[DatumZukunft.getMonth()] + " "+jahr;
		if (auswahl_tag==0)
			document.getElementById("aktuelles_Datum").innerHTML="Heute, " + DatumZukunft.getDate() + ". " + Monat[DatumZukunft.getMonth()] + " "+jahr;
		else
			if (auswahl_tag==1)
				document.getElementById("aktuelles_Datum").innerHTML="Morgen, " + DatumZukunft.getDate() + ". " + Monat[DatumZukunft.getMonth()] + " "+jahr;
			else
				document.getElementById("aktuelles_Datum").innerHTML=Wochentag_ausfuehrlich[TagInWoche]+", " + DatumZukunft.getDate() + ". " + Monat[DatumZukunft.getMonth()] + " "+jahr;
				
			
		
		maxim[auswahl_tag].innerHTML="<div class='box_datum'><a class='box_datum_css_haupt' href='"+auswahl_tag+"' ><font size='0.5' color='#808080'>"+Wochentag[TagInWoche]+"</font><br>"+DatumZukunft.getDate()+"</a></div>";
		auswahl_tag_final=auswahl_tag;
		TagInWoche=TagInWoche+1;
		AnzahlTage=AnzahlTage+1;
		DatumZukunft.setTime(DatumZeitJetzt.getTime() + AnzahlTage * msProTag);
		j=j+1;
		auswahl_tag=auswahl_tag+1;
		if(auswahl_tag>6)
		{
				auswahl_tag=0;
				AnzahlTage=0;
				DatumZukunft.setTime(DatumZeitJetzt.getTime() + AnzahlTage * msProTag);
				TagInWoche = DatumZukunft.getDay();
			
		}
		

		while (j<7)
		{
			if (TagInWoche == 6 || TagInWoche == 0)
			{
				DatumZukunft_.setTime(DatumZukunft.getTime() + 1 * msProTag);
				maxim[auswahl_tag].innerHTML="<div class='box_datum'><div class='box_datum_css_wochenende'><font size='0.5' color='#808080'>Geschlossen</font><br>"+"<font color='#808080'>"+DatumZukunft.getDate()+"-"+DatumZukunft_.getDate()+"</div></div>";
				if (TagInWoche==6)
					AnzahlTage=AnzahlTage+2;
				else
					AnzahlTage=AnzahlTage+1;
				
				TagInWoche=1;

				DatumZukunft.setTime(DatumZeitJetzt.getTime() + AnzahlTage * msProTag);

			}
			else
			{

				maxim[auswahl_tag].innerHTML="<div class='box_datum'><a class='box_datum_css' href='"+auswahl_tag+"' ><font size='1.5' color='#808080'>"+Wochentag[TagInWoche]+"</font><br>"+DatumZukunft.getDate()+"</a></div>";
			
				TagInWoche=TagInWoche+1;
				AnzahlTage=AnzahlTage+1;
				DatumZukunft.setTime(DatumZeitJetzt.getTime() + AnzahlTage * msProTag);
			}
		
			j=j+1;
			auswahl_tag=auswahl_tag+1;
			if(auswahl_tag>6)
			{
				auswahl_tag=0;
				AnzahlTage=0;
				DatumZukunft.setTime(DatumZeitJetzt.getTime() + AnzahlTage * msProTag);
				TagInWoche = DatumZukunft.getDay();

				
			}
		}*/
}

 


 
 
 
 function arrow_laden_filter(id) 
{

	var maxim= document.getElementsByClassName("arrow_filter");
	if (id==0)
	{
		variable = "/static/arrow_up.png";	
		maxim[0].src=variable;

	}
	else
	{
		variable = "/static/arrow_down.png";	
		maxim[0].src=variable;

		
	}
		
	
 }
 
  function arrow_laden_plz(id) 
{

	var maxim= document.getElementsByClassName("arrow_plz");
	if (id==0)
	{
		variable = "/static/arrow_up.png";	
		maxim[0].src=variable;

	}
	else
	{
		variable = "/static/arrow_down.png";	
		maxim[0].src=variable;

		
	}
		
	
 }
 
 
   function arrow_laden_datum(id) 
{

	var maxim= document.getElementsByClassName("arrow_plz");
	if (id==0)
	{
		variable = "/static/arrow_up.png";	
		maxim[1].src=variable;

	}
	else
	{
		variable = "/static/arrow_down.png";	
		maxim[1].src=variable;

		
	}
		
	
 }
 
 
 
 function submit_zip()
 
 {
	 

		var submit_plz_input=document.getElementById("eingabe1").value;
		if(isNaN(submit_plz_input) ==true || submit_plz_input.length<5)
		{
			document.getElementById("plz_fehler").innerHTML="Bitte eine fünfstellige PLZ angeben";
		}
		else
		{
			
				document.getElementById("plz_fehler").innerHTML="";

			
		}
	 
	 
	 
	 
 }
 
 
 
 
 
 
 
 function overlay() {
	
	
		var submit_plz_input=document.getElementById("eingabe1").value;
		if(isNaN(submit_plz_input) ==true || submit_plz_input.length<5)
		{
			document.getElementById("plz_fehler").innerHTML="Bitte eine fünfstellige PLZ angeben";
		}
		else
		{
			
			el = document.getElementById("overlay");
			el.style.marginTop=scroll_position()+"px";
			el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
			document.getElementById("x-mask").style.opacity="0.4";
			document.getElementById("plz_fehler").innerHTML="";
			
		}


	
	
	


}

function getDocHeight() {
    var D = document;
    return Math.max(
        D.body.scrollHeight, D.documentElement.scrollHeight,
        D.body.offsetHeight, D.documentElement.offsetHeight,
        D.body.clientHeight, D.documentElement.clientHeight
    )
}
 


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


 function warteliste_click() {
	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "hidden") ? "visible" : "hidden";
	document.getElementById("x-mask").style.opacity="1.0";
}



 function warteliste_click_schliessen() {

	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "hidden") ? "visible" : "hidden";
	document.getElementById("x-mask").style.opacity="1.0";
}


	
 
 function validate(evt) {
  var theEvent = evt || window.event;
  var key = theEvent.keyCode || theEvent.which;
  key = String.fromCharCode( key );
  var regex = /[0-9]|\./;
  if( !regex.test(key) ) {
    theEvent.returnValue = false;
    
  }
}

 
 
 
 
 
 
 
function mouse_effect_in(clicked_id) 
{

	var maxim= document.getElementsByClassName("box_zusatz_2");

	maxim[clicked_id-1].value="+";


 }
 
 


function input_plz_text() 
{
	
	
		if(document.getElementById("eingabe1").value=="PLZ")
		{
			
			
			document.getElementById("eingabe1").value="";
			document.getElementById("eingabe1").style.color="#000000";
			document.getElementById("plz_fehler").innerHTML="";
			
		}
 }
 
 
 
 
 
 
 
 function add_cart(clicked_id)
{
	
	if(document.getElementsByClassName("anzahl_warenkorb")[clicked_id].innerHTML=="")
	{
		



		
		$.ajax({
			type: "POST",
			url: "/polls/hello/add/",
			dataType: "json",
			data: { "item": gerichte[clicked_id][1]+","+"1,"+gewaehltes_datum+","+auswahl_tag_final},
			success: function(data) {
				warenkorb_aufsetzen(data);


			}
		});
		
		

		

	}
	else
	{

		var i=0;
		var status=0;

		while(i<=cart.length-1)
		{

			if(cart[i][0]==gerichte[clicked_id][1] && cart[i] != "" && cart[i][2]==gewaehltes_datum)
			{	

				
				status=1;
				cart[i][1]=parseInt(cart[i][1])+1;


				$.ajax({
					type: "POST",
					url: "/polls/hello/add/",
					dataType: "json",
					data: { "item": gerichte[clicked_id][1]+","+cart[i][1]+","+cart[cart.length-1][2]+","+auswahl_tag_final },
					success: function(data) {

					}
				});

					
					document.getElementsByClassName("anzahl_warenkorb")[gericht_id_suchen(cart[i][0])].innerHTML=cart[i][1]+" X IM WARENKORB";
					
					
					
					document.getElementsByClassName("cart_image")[gericht_id_suchen(cart[i][0])].style.opacity="0.5";
					document.getElementsByClassName("delete_button")[gericht_id_suchen(cart[i][0])].style.display="block";
					
					
					document.getElementsByClassName("bild-laden")[gericht_id_suchen(cart[i][0])].style.opacity="0.2";
					cart_gesamt=cart_gesamt+1;
					

			}
			
			

			
			
			i=i+1;
		}
		
	if(cart_gesamt!=0)
		document.getElementsByClassName("cart_text")[0].innerHTML=cart_gesamt;
	else
		document.getElementsByClassName("cart_text")[0].innerHTML="";
		
	}
	

	
	
	

	
	

				
	
}


function erase_cart(clicked_id)
{
	
	var i=0;
		var status=0;


		while(i<=cart.length-1)
		{
			
			if(cart[i][0]==gerichte[clicked_id][1] && cart[i] != "" && cart[i][2]==gewaehltes_datum)
			{	
				

				
				status=1;
				cart[i][1]=parseInt(cart[i][1])-1;
				cart_gesamt=cart_gesamt-1;
				


				$.ajax({
					type: "POST",
					url: "/polls/hello/add/",
					dataType: "json",
					data: { "item": gerichte[clicked_id][1]+","+cart[i][1]+","+cart[i][2]+","+auswahl_tag_final },
					success: function(data) {
	
					}
				});
				
				if(cart[i][1]>0)
				{

					
					document.getElementsByClassName("anzahl_warenkorb")[gericht_id_suchen(cart[i][0])].innerHTML=cart[i][1]+" X IM WARENKORB";
					
					
					
					document.getElementsByClassName("cart_image")[gericht_id_suchen(cart[i][0])].style.opacity="0.5";
					document.getElementsByClassName("delete_button")[gericht_id_suchen(cart[i][0])].style.display="block";
					
					
					document.getElementsByClassName("bild-laden")[gericht_id_suchen(cart[i][0])].style.opacity="0.2";
					
				}
				else
				{	
					
					
					
					document.getElementsByClassName("anzahl_warenkorb")[gericht_id_suchen(cart[i][0])].innerHTML="";
					
					
					
					document.getElementsByClassName("cart_image")[gericht_id_suchen(cart[i][0])].style.opacity="0";
					document.getElementsByClassName("delete_button")[gericht_id_suchen(cart[i][0])].style.display="none";
					
					
					document.getElementsByClassName("bild-laden")[gericht_id_suchen(cart[i][0])].style.opacity="1.0";
					cart.splice(i,1);

				}
					

			}
			
			

			
			
			i=i+1;
		}
		
		if (cart_gesamt!=-10)
			document.getElementsByClassName("cart_text")[0].innerHTML=cart_gesamt;
		else
			document.getElementsByClassName("cart_text")[0].innerHTML="";
		
		

	
}

function warenkorb_click()
{
	
	alert("asd");

	$.ajax({
		type: "POST",
		url: "/polls/hello/warenkorb/",
		dataType: "json",
		data: { "item": "asd" },
		success: function(data) {

		}
	});
}






 
 
 function input_plz_text_blur() 
{
	if(document.getElementById("eingabe1").value=="")
	{
		document.getElementById("eingabe1").value="PLZ";
		document.getElementById("eingabe1").style.color="#808080"
		document.getElementById("plz_fehler").innerHTML="";
	}
	

 }
 
 
 function daten_ermitteln(daten)
 {


	 gerichte = daten.split(';').map(e => e.split(','));



 }
 
 function gericht_id_suchen(name)
 {
	
	 j=0;
	 while (j<=gerichte.length)
	 {
		 if (gerichte[j][1]==name)
			 return j
		 
		 j=j+1;
		 
	 }
	 
	 
 }
 
  function warenkorb_aufsetzen(daten)
 {


	
	 cart = daten.split(';').map(e => e.split(','));
	 
	 i=0;
	 cart_gesamt=0;
	 


	 
	 while (i<=cart.length-1)
	 {
		 
		 if(gewaehltes_datum==cart[i][2])
		 {

			
			if (cart[i][1]>0)
			{

				document.getElementsByClassName("anzahl_warenkorb")[gericht_id_suchen(cart[i][0])].innerHTML=cart[i][1]+" X IM WARENKORB";
				document.getElementsByClassName("cart_image")[gericht_id_suchen(cart[i][0])].style.opacity="0.5";
				document.getElementsByClassName("delete_button")[gericht_id_suchen(cart[i][0])].style.display="block";
				document.getElementsByClassName("bild-laden")[gericht_id_suchen(cart[i][0])].style.opacity="0.2";
			}
		 }
		 
		 if (parseInt(cart[i][1])>0)
			cart_gesamt=cart_gesamt+parseInt(cart[i][1]);
		
		i=i+1;
	 }

	if (cart_gesamt!=0)
		document.getElementsByClassName("cart_text")[0].innerHTML=cart_gesamt;
	else
		document.getElementsByClassName("cart_text")[0].innerHTML="";
		
		


	 
	 



 }
 

 
 
 function gerichte_laden(daten)
 {
	 
	var box=new Array(4);
	
	daten_ermitteln(daten);
	 i=0;
	 max=gerichte.length-2;
	 box[0]="<div class='filter_leer'><br><br>Keine Gerichte sind bei den gewählten Filtern verfügbar.</div>";
	 box[1]="<div class='filter_leer'><br><br>Keine Gerichte sind bei den gewählten Filtern verfügbar.</div>";
	 
	 o=0;
	 p=0;
	while (i<=max)
	{
		if (gerichte[i][24]=="Hauptgericht")
		{

			if(o==0 || o==4 || o==8 || o==12 || o==16 || o==20 || o==24 )
				box[0]=box[0]+"<div class='box' ><div class='box_1'><a href='"+gerichte[i][1]+"'><div class='image-box'><div class='bild-laden' ></div><h2 class='cart_image' ><div class='anzahl_warenkorb'></div></h2></div></a><div class='gericht_auswahl_text' ></div><div class='box_zusatz'>EUR "+gerichte[i][3]+"<input type='button' id='"+i+"' class='box_zusatz_2' value='+' onmouseover='mouse_effect_in("+i+")' onmouseout='mouse_effect_out("+i+")' onclick='add_cart("+i+")'/><input type='button' id='"+i+"' class='delete_button' value='-' onmouseover='mouse_effect_in_delete("+i+")' onmouseout='mouse_effect_out_delete("+i+")' onclick='erase_cart("+i+")'/></div></div>";
			if(o==1 || o==2 || o==5 || o==6 || o==9 || o==10 || o==13 || o==14 || o==17 || o==18 || o==21 || o==22 || o==25 || o==26)
				box[0]=box[0]+"<div class='box'><div class='box_2-3'><a href='"+gerichte[i][1]+"'><div class='image-box'><div class='bild-laden'></div><h2 class='cart_image' ><div class='anzahl_warenkorb'></div></h2></div></a><div class='gericht_auswahl_text'></div><div class='box_zusatz'>EUR "+gerichte[i][3]+"<input type='button' id='"+i+"' class='box_zusatz_2' value='+' onmouseover='mouse_effect_in("+i+")' onmouseout='mouse_effect_out("+i+")' onclick='add_cart("+i+")'/><input type='button' id='"+i+"' class='delete_button' value='-' onmouseover='mouse_effect_in_delete("+i+")' onmouseout='mouse_effect_out_delete("+i+")' onclick='erase_cart("+i+")'/></div></div>";
			if(o==3 || o==7 || o==11 || o==15 || o==19 || o==23 || o==27 )
				box[0]=box[0]+"<div class='box'><div class='box_4'><a href='"+gerichte[i][1]+"'><div class='image-box'><div class='bild-laden'></div><h2 class='cart_image' ><div class='anzahl_warenkorb'></div></h2></div></a><div class='gericht_auswahl_text'></div><div class='box_zusatz'>EUR "+gerichte[i][3]+"<input type='button' id='"+i+"' class='box_zusatz_2' value='+' onmouseover='mouse_effect_in("+i+")' onmouseout='mouse_effect_out("+i+")' onclick='add_cart("+i+")'/><input type='button' id='"+i+"' class='delete_button' value='-' onmouseover='mouse_effect_in_delete("+i+")' onmouseout='mouse_effect_out_delete("+i+")' onclick='erase_cart("+i+")'/></div></div>";
			o=o+1;
		}	
		
		if (gerichte[i][24]=="Kindergericht")
		{

			if(p==0 || p==4 || p==8 || p==12 || p==16 || p==20 || p==24 )
				box[1]=box[1]+"<div class='box' ><div class='box_1'><a href='"+gerichte[i][1]+"'><div class='image-box'><div class='bild-laden' ></div><h2 class='cart_image' ><div class='anzahl_warenkorb'></div></h2></div></a><div class='gericht_auswahl_text' ></div><div class='box_zusatz'>EUR "+gerichte[i][3]+"<input type='button' id='"+i+"' class='box_zusatz_2' value='+' onmouseover='mouse_effect_in("+i+")' onmouseout='mouse_effect_out("+i+")' onclick='add_cart("+i+")'/><input type='button' id='"+i+"' class='delete_button' value='-' onmouseover='mouse_effect_in_delete("+i+")' onmouseout='mouse_effect_out_delete("+i+")' onclick='erase_cart("+i+")'/></div></div>";
			if(p==1 || p==2 || p==5 || p==6 || p==9 || p==10 || p==13 || p==14 || p==17 || p==18 || p==21 || p==22 || p==25 || p==26)
				box[1]=box[1]+"<div class='box'><div class='box_2-3'><a href='"+gerichte[i][1]+"'><div class='image-box'><div class='bild-laden'></div><h2 class='cart_image' ><div class='anzahl_warenkorb'></div></h2></div></a><div class='gericht_auswahl_text'></div><div class='box_zusatz'>EUR "+gerichte[i][3]+"<input type='button' id='"+i+"' class='box_zusatz_2' value='+' onmouseover='mouse_effect_in("+i+")' onmouseout='mouse_effect_out("+i+")' onclick='add_cart("+i+")'/><input type='button' id='"+i+"' class='delete_button' value='-' onmouseover='mouse_effect_in_delete("+i+")' onmouseout='mouse_effect_out_delete("+i+")' onclick='erase_cart("+i+")'/></div></div>";
			if(p==3 || p==7 || p==11 || p==15 || p==19 || p==23 || p==27 )
				box[1]=box[1]+"<div class='box'><div class='box_4'><a href='"+gerichte[i][1]+"'><div class='image-box'><div class='bild-laden'></div><h2 class='cart_image' ><div class='anzahl_warenkorb'></div></h2></div></a><div class='gericht_auswahl_text'></div><div class='box_zusatz'>EUR "+gerichte[i][3]+"<input type='button' id='"+i+"' class='box_zusatz_2' value='+' onmouseover='mouse_effect_in("+i+")' onmouseout='mouse_effect_out("+i+")' onclick='add_cart("+i+")'/><input type='button' id='"+i+"' class='delete_button' value='-' onmouseover='mouse_effect_in_delete("+i+")' onmouseout='mouse_effect_out_delete("+i+")' onclick='erase_cart("+i+")'/></div></div>";
			p=p+1;		
		}
		
		
		i=i+1;
	}
	
	document.getElementsByClassName("container_gerichte")[0].innerHTML=box[0];
	document.getElementsByClassName("container_gerichte")[1].innerHTML=box[1];
	
	document.getElementsByClassName("font_festlegen")[1].style.marginTop=Math.ceil(o/4)*350+50	+"px";
	
	
	
	
	
	 
	 
 }



 
function mouse_effect_out(clicked_id) 
{

		var maxim= document.getElementsByClassName("box_zusatz_2");
	maxim[clicked_id-1].value="+";
 }
 

 
 
 function filter_function() {
	if (document.getElementById("filter_dropdown").style.display=="block")
	{
		document.getElementById("myDropdown").style.display = "none";
		document.getElementById("myDropdown_").style.display = "none";
		document.getElementById("filter_dropdown").style.display = "none";
		
		arrow_laden_plz(0);
		arrow_laden_datum(0);
		arrow_laden_filter(0);
		
	}
	else
	{
		document.getElementById("filter_dropdown").style.display = "block";
		document.getElementById("myDropdown_").style.display = "none";
		document.getElementById("myDropdown").style.display = "none";
		
		arrow_laden_plz(0);
		arrow_laden_datum(0);
		arrow_laden_filter(1);
		
	}
} 

 

 
 
function myFunction() {
	if (document.getElementById("myDropdown").style.display=="block")
	{
		document.getElementById("myDropdown").style.display = "none";
		document.getElementById("myDropdown_").style.display = "none";
		document.getElementById("filter_dropdown").style.display = "none";
		arrow_laden_plz(0);
		arrow_laden_datum(0);
		arrow_laden_filter(0);
	}
	else
	{
		document.getElementById("myDropdown").style.display = "block";
		document.getElementById("myDropdown_").style.display = "none";
		document.getElementById("filter_dropdown").style.display = "none";
		arrow_laden_plz(0);
		arrow_laden_datum(1);
		arrow_laden_filter(0);
		
	}
}



function myFunction_() {
	
	if (document.getElementById("myDropdown_").style.display=="block")
	{
		document.getElementById("myDropdown_").style.display = "none";
		document.getElementById("myDropdown").style.display = "none";
		document.getElementById("filter_dropdown").style.display = "none";

		arrow_laden_plz(0);
		arrow_laden_datum(0);
		arrow_laden_filter(0);

	}
	else
	{
		
		document.getElementById("myDropdown_").style.display = "block";
		document.getElementById("myDropdown").style.display = "none";
		document.getElementById("filter_dropdown").style.display = "none";

		arrow_laden_plz(1);
		arrow_laden_datum(0);
		arrow_laden_filter(0);
	}	
}

// Close the dropdown if the user clicks outside of it
/*window.onclick = function(e) {
  
  
  if (!e.target.matches('.dropbtn_datum')) {
	arrow_laden();
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var d = 0; d < dropdowns.length; d++) {
      var openDropdown = dropdowns[d];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}*/






 
 
 
 
