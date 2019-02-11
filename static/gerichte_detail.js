	var zutaten=new Array(50);
	   var gerichte = new Array(20); 
	   var cart=new Array(10);/*
   
   
   
   i,0,0: Name
   i,1,var: Filter: 1) Vegan, 2) Vegetarisch, 3) Gluten-frei, 4) Laktosefrei, 5) Nussfrei, 6) Ei-frei
   i,2,var:Zutaten*/

   
function add_cart()
{


	cart[0]=cart[0]+1;
	
	if(cart[0]>0)
	{

		document.getElementById("cart_image").innerHTML=cart[0]+" Mal im Warenkorb";
		document.getElementById("cart_image").style.display="block";
		document.getElementById("erase_from_cart").style.display="block";
		
		
	}
	else
	{
		document.getElementById("cart_image").style.display="none";
		document.getElementById("erase_from_cart").style.display="none";
		
	}
	
}


function erase_cart()
{

	if (cart[0]!=0)
	{
		cart[0]=cart[0]-1;
		
		if(cart[0]>0)
		{

			document.getElementById("cart_image").innerHTML=cart[0]+" Mal im Warenkorb";
			document.getElementById("cart_image").style.display="block";
			document.getElementById("erase_from_cart").style.display="block";
			
			
		}
		else
		{
			document.getElementById("cart_image").style.display="none";
			document.getElementById("erase_from_cart").style.display="none";
			
		}
	}
	
}



   
 window.onload=function datum_abrufen()
 {
	 load_header();
	var maxim= document.getElementsByClassName("bild-laden");
	
	
	
	
	
	maxim[0].src=gerichte[0][2];
	cart[0]=new Array;
	
	cart[0]=0;
	
	
	
	if(cart[0]>0)
	{
		
		document.getElementById("cart_image").innerHTML=cart[0]+" Mal im Warenkorb";
		
	}
	else
	{
		document.getElementById("cart_image").style.display="none";
		document.getElementById("erase_from_cart").style.display="none";
		
	}
	
		//width='550' height='550' style='border:1px solid #e6e6e6 ;'/></img>";
	
	var inhalt=gerichte[0][1];
	document.getElementById("header_beschreibung").innerHTML=inhalt.toUpperCase();
	
	document.getElementById("preis").innerHTML="$7.95";
	
	document.getElementById("ingredients").innerHTML="red onion, cilantro, roasted peanut, lime";
	document.getElementById("star").style.width="79%";
	document.getElementById("star_bewertungen").innerHTML="(100)";
	
	
	var i=0;

	
	zutaten[0]="Jasminreis";
	zutaten[1]="Knoblauch";
	zutaten[2]="Zucker";
	zutaten[3]="Zitronengras";
	zutaten[4]="Jasminreis";
	zutaten[5]="Knoblauch";
	zutaten[6]="Zucker";
	zutaten[7]="Zitronengras";
	zutaten[8]="Jasminreis";
	zutaten[9]="Knoblauch";
	zutaten[10]="Zucker";
	zutaten[11]="Zitronengras";
	zutaten[12]="Zucker";
	zutaten[13]="Zitronengras";
	zutaten[14]="Jasminreis";
	zutaten[15]="Knoblauch";
	zutaten[16]="Zucker";
	zutaten[17]="Zitronengras";
	zutaten[18]="Zitronengras";
	zutaten[19]="Jasminreis";
	zutaten[20]="Knoblauch";
	zutaten[21]="Zucker";
	zutaten[22]="Zitronengras";
	
	
	
	details_abrufen()
	   
	 
 }
 

 
 
 function details_abrufen()
 {
	 var text= "<div style='margin-left:20px;margin-top:10px;margin-right:20px;'>"+gerichte[0][10]+"</div>"

	 

	 var box_1="<div style='width:453px;height:90px;text-align: leftfloat:left;border-bottom:1px solid #e6e6e6;'><br>";
	
	if(gerichte[0][4]=="true")
	{
		box_1 = box_1+ "<img src='/static/vegan.png'  width='40' height='40' style='float:left;margin-left:20px;'><div class='asd' style='float:left;margin-top:40px;margin-left:-35px;'>Vegan</img></div>";		

	}
	
	if(gerichte[0][5]=="true")
	{
		box_1 = box_1+ "<img src='/static/vegetarian.png'  width='40' height='40' style='float:left;margin-left:20px;'><div class='asd' style='float:left;margin-top:40px;margin-left:-35px;'>Vegetarisch</img></div>";

	
	}	
	
	if(gerichte[0][6]=="true")
	{
		box_1 = box_1+ "<img src='/static/gluten-free.png'  width='40' height='40' style='float:left;margin-left:20px;'><div class='asd' style='float:left;margin-top:40px;margin-left:-35px;'>Gluten-frei</img></div>";		

	
	}
	if(gerichte[0][7]=="true")
	{
		box_1 = box_1+ "<img src='/static/dairy-free.png' width='40' height='40' style='float:left;margin-left:20px;'><div class='asd' style='float:left;margin-top:40px;margin-left:-35px;'>Laktose-frei</img></div>";	

	}
	
	if(gerichte[0][8]=="true")
	{
		box_1 = box_1+ "<img src='/static/nut-free.png'  width='40' height='40' style='float:left;margin-left:20px;'><div class='asd' style='float:left;margin-top:40px;margin-left:-35px;'>Nuss-frei</img></div>";	

	}
	
	if(gerichte[0][9]=="true")
	{
		box_1 = box_1+ "<img src='/static/egg-free.png' width='40' height='40' style='float:left;margin-left:20px;'><div class='asd' style='float:left;margin-top:40px;margin-left:-35px;'>Ei-frei</img></div>";	

	}
	 
	 box_1=box_1+"</div>";

	 

	 document.getElementById("gerichte_info_box").innerHTML=box_1+text;
	 
	var maxim= document.getElementsByClassName("button_detail");
	maxim[0].style.borderBottom="1px solid #e65c00";
	maxim[1].style.borderBottom="1px solid #e6e6e6";
	maxim[2].style.borderBottom="1px solid #e6e6e6";
	maxim[3].style.borderBottom="1px solid #e6e6e6";
	

	
	 
 }
 
 
  function prep_abrufen()
 {
	var string="";
	 var notes= gerichte[0][11];

	 var oven= gerichte[0][12];
	 var microwave=gerichte[0][13];
	 var serve=gerichte[0][14];
	 
	 
	 string="<b>Hinweise</b><br>"+notes;
	 if(oven!="")
	 {
		 	 string=string+"<b><br><br>Im Ofen</b><br>"+oven;
		 
	 }
	 
	 
	 if(serve!="")
	 {
		 	 string=string+"<br><br><b>Servieren</b><br>"+serve;
		 
	 }
	 
	 
	 var box_1="<div class='test' style='width:250px;height:150px;border:1px;margin-top:20px;margin-left:20px;'>"+string+"</div>";
	 if (microwave!="")
	 {
		 var box_2="<div class='test' style='width:250px;height:10px;border:1px;margin-top:-100px;margin-left:290px;'><b>In der Mikrowelle</b><br>"+microwave;
		 
	 }

	 
	 document.getElementById("gerichte_info_box").innerHTML=box_1+box_2;
	 
	 	var maxim= document.getElementsByClassName("button_detail");
	maxim[1].style.borderBottom="1px solid #e65c00";
	maxim[0].style.borderBottom="1px solid #e6e6e6";
	maxim[2].style.borderBottom="1px solid #e6e6e6";
	maxim[3].style.borderBottom="1px solid #e6e6e6";
	 
 }
   
   
    
function ingredients_abrufen()
{
	
		 var box_1="<div style='width:453px;height:90px;text-align: leftfloat:left;border-bottom:1px solid #e6e6e6;'><br>";

	if(gerichte[0][4]=="true")
	{
		box_1 = box_1+ "<img src='/static/vegan.png'  width='40' height='40' style='float:left;margin-left:20px;'><div class='asd' style='float:left;margin-top:40px;margin-left:-35px;'>Vegan</img></div>";		

	}
	
	if(gerichte[0][5]=="true")
	{
		box_1 = box_1+ "<img src='/static/vegetarian.png'  width='40' height='40' style='float:left;margin-left:20px;'><div class='asd' style='float:left;margin-top:40px;margin-left:-35px;'>Vegetarisch</img></div>";

	
	}	
	
	if(gerichte[0][6]=="true")
	{
		box_1 = box_1+ "<img src='/static/gluten-free.png'  width='40' height='40' style='float:left;margin-left:20px;'><div class='asd' style='float:left;margin-top:40px;margin-left:-35px;'>Gluten-frei</img></div>";		

	
	}
	if(gerichte[0][7]=="true")
	{
		box_1 = box_1+ "<img src='/static/dairy-free.png' width='40' height='40' style='float:left;margin-left:20px;'><div class='asd' style='float:left;margin-top:40px;margin-left:-35px;'>Laktose-frei</img></div>";	

	}
	
	if(gerichte[0][8]=="true")
	{
		box_1 = box_1+ "<img src='/static/nut-free.png'  width='40' height='40' style='float:left;margin-left:20px;'><div class='asd' style='float:left;margin-top:40px;margin-left:-35px;'>Nuss-frei</img></div>";	

	}
	
	if(gerichte[0][9]=="true")
	{
		box_1 = box_1+ "<img src='/static/egg-free.png' width='40' height='40' style='float:left;margin-left:20px;'><div class='asd' style='float:left;margin-top:40px;margin-left:-35px;'>Ei-frei</img></div>";	

	}
	 
	 box_1=box_1+"</div>";

	 
	 

	var box_2="<div style='width:250px;height:10px;border:1px;margin-left:20px;margin-top:20px;line-height:1.5'><b>Zutaten</b><br>";
	i=0;

	 while(i<=22)
	 {
			
			if(gerichte[0][2][i]=="yes")
			{
				if(i==16)
				{
				box_2=box_2+"</div><div style='width:250px;height:10px;border:1px;margin-left:350px;margin-top:-10px;line-height:1.5'>";	
					
				}
				
				if(i==8)
				{
				box_2=box_2+"</div><div style='width:250px;height:10px;border:1px;margin-left:180px;margin-top:5px;line-height:1.5'>";	
					
				}
				
				
				box_2=box_2+"<br>"+zutaten[i];


				
			}
			i=i+1;
		 
	 }

	 


	 
	 document.getElementById("gerichte_info_box").innerHTML=box_1+box_2+"</div>";
	 
	 	var maxim= document.getElementsByClassName("button_detail");
	maxim[2].style.borderBottom="1px solid #e65c00";
	maxim[0].style.borderBottom="1px solid #e6e6e6";
	maxim[1].style.borderBottom="1px solid #e6e6e6";
	maxim[3].style.borderBottom="1px solid #e6e6e6";
	 
 }
 
 
 function nutrition_abrufen()
{

	var box_1="<div style='width:150px;height:70px;border:1px solid #e6e6e6;text-align: center;'><br><b>Kalorien</b><br>"+gerichte[0][16]+"</div>";
	box_1=box_1+"<div style='width:150px;height:70px;border:1px solid #e6e6e6;margin-top:-72px;margin-left:150px;text-align: center;'><br><b>Protein</b><br>"+gerichte[0][17]+"</div>";
	box_1=box_1+"<div style='width:150px;height:70px;border:1px solid #e6e6e6;margin-top:-72px;margin-left:301px;text-align: center;'><br><b>Kohlenhydrate</b><br>"+gerichte[0][18]+"</div>";
	
	
	var box_kalorien="<br><div class='nutritional_facts' style='background-Color:#e6e6e6; height:25px;line-height:2;margin-left:20px;margin-right:20px;'>";
	box_kalorien=box_kalorien+"<b><div style='margin-left:5px;'>Kalorien</div>"+"<div style='text-align: right;margin-top:-25px;margin-right:5px;'>"+gerichte[0][16]+"</b></div></div>";


	var box_fett="<br><div class='nutritional_facts' style='background-Color:#e6e6e6; height:25px;line-height:2;margin-left:20px;margin-right:20px;;margin-top:-15px''>";
	box_fett=box_fett+"<b><div style='margin-left:5px;'>Fett</div>"+"<div style='text-align: right;margin-top:-25px;margin-right:5px;'>"+gerichte[0][21]+"</b></div></div>";
		
	var box_ungesaettigt="<br><div class='nutritional_facts' style='background-Color:#ffffff; height:25px;line-height:2;margin-left:20px;margin-right:20px;margin-top:-15px'>";
	box_ungesaettigt=box_ungesaettigt+"<div style='margin-left:25px;'>Ungesättigte Fettsäuren</div>"+"<div style='text-align: right;margin-top:-25px;margin-right:5px;'>"+gerichte[0][22]+"</div></div>";
	
	var box_gesaettigt="<br><div class='nutritional_facts' style='background-Color:#ffffff; height:25px;line-height:2;margin-left:20px;margin-right:20px;margin-top:-15px'>";
	box_gesaettigt=box_gesaettigt+"<div style='margin-left:25px;'>Gesättigte Fettsäuren</div>"+"<div style='text-align: right;margin-top:-25px;margin-right:5px;'>"+gerichte[0][23]+"</div></div>";
	
	
	var box_protein="<br><div class='nutritional_facts' style='background-Color:#e6e6e6; height:25px;line-height:2;margin-left:20px;margin-right:20px;;margin-top:-15px''>";
	box_protein=box_protein+"<b><div style='margin-left:5px;'>Protein</div>"+"<div style='text-align: right;margin-top:-25px;margin-right:5px;'>"+gerichte[0][17]+"</b></div></div>";

	var box_kohlenhydrate="<br><div class='nutritional_facts' style='background-Color:#e6e6e6; height:25px;line-height:2;margin-left:20px;margin-right:20px;;margin-top:-15px''>";
	box_kohlenhydrate=box_kohlenhydrate+"<b><div style='margin-left:5px;'>Kohlenhydrate</div>"+"<div style='text-align: right;margin-top:-25px;margin-right:5px;'>"+gerichte[0][18]+"</b></div></div>";
		
	var box_zucker="<br><div class='nutritional_facts' style='background-Color:#ffffff; height:25px;line-height:2;margin-left:20px;margin-right:20px;margin-top:-15px'>";
	box_zucker=box_zucker+"<div style='margin-left:25px;'>Davon Zucker</div>"+"<div style='text-align: right;margin-top:-25px;margin-right:5px;'>"+gerichte[0][19]+"</div></div>";
	
	var box_ballaststoffe="<br><div class='nutritional_facts' style='background-Color:#ffffff; height:25px;line-height:2;margin-left:20px;margin-right:20px;margin-top:-15px'>";
	box_ballaststoffe=box_ballaststoffe+"<div style='margin-left:25px;'>Davon Ballaststoffe</div>"+"<div style='text-align: right;margin-top:-25px;margin-right:5px;'>"+gerichte[0][20]+"</div></div>";
					

	
	 document.getElementById("gerichte_info_box").innerHTML=box_1+box_kalorien+box_kohlenhydrate+box_zucker+box_ballaststoffe+box_protein+box_fett+box_ungesaettigt+box_gesaettigt;
	 var maxim= document.getElementsByClassName("button_detail");
	maxim[3].style.borderBottom="1px solid #e65c00";
	maxim[0].style.borderBottom="1px solid #e6e6e6";
	maxim[1].style.borderBottom="1px solid #e6e6e6";
	maxim[2].style.borderBottom="1px solid #e6e6e6";
	 
 }
 
 
  function daten_ermitteln(daten)
 {


	 gerichte = daten.split(';').map(e => e.split(','));




	 
	 


 }






 
 
 
 
