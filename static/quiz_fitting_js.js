var seite,vorseite,loaded;
var fortschrittsbalken_links;
var band_click_first_id,cup_click_first_id,brand_click_first_id;
var band_click_second_id,cup_click_second_id,brand_click_second_id;
var question_2,question_3,question_4,question_5,question_6,question_6a,question_8,question_9,question_10,panty_id;


function next_quiz_page(seite_,vorseite_)
{
	seite=seite_
	vorseite=vorseite_
	i=0;
	while (i<=18)
	{
		document.getElementsByClassName("content_quiz_fitting_question")[i].style.display="none";	
		document.getElementsByClassName("content_quiz_fitting_question")[i].style.opacity="0";		
		i=i+1;
	}


	if(seite>5)
	{
		headline_second_size="Trägst Du immer Größe "+document.getElementsByClassName ("band")[band_click_first_id].innerHTML+document.getElementsByClassName ("cup")[cup_click_first_id].innerHTML+" von "+document.getElementsByClassName("brand_selection_first")[0].value+"?"
		
		document.getElementById("headline_second_size").innerHTML=headline_second_size
		}	
	

	if(seite==5) //antwort 3: wie passen die Cups?
	{
			document.getElementById("fitting_quiz_answer_3_0").style.display="none"
			document.getElementById("fitting_quiz_answer_3_1").style.display="none"
			document.getElementById("fitting_quiz_answer_3_2").style.display="none"
		if(question_3==0)
			document.getElementById("fitting_quiz_answer_3_0").style.display="block"

		if(question_3==1)
			document.getElementById("fitting_quiz_answer_3_1").style.display="block"
			
		if(question_3==2)
			document.getElementById("fitting_quiz_answer_3_2").style.display="block"		
	}	
	
	if(seite==7) //antwort 4: wie passt das band?
	{
		
			document.getElementById("fitting_quiz_answer_4_0").style.display="none"
			document.getElementById("fitting_quiz_answer_4_1").style.display="none"
			document.getElementById("fitting_quiz_answer_4_2").style.display="none"	
			
		if(question_4==0)
			document.getElementById("fitting_quiz_answer_4_0").style.display="block"

		if(question_4==1)
			document.getElementById("fitting_quiz_answer_4_1").style.display="block"
			
		if(question_4==2)
			document.getElementById("fitting_quiz_answer_4_2").style.display="block"		
	}	
	
	if(seite==9) //antwort 5: wie passt das band?
	{
		
			document.getElementById("fitting_quiz_answer_5_0").style.display="none";
		
			document.getElementById("fitting_quiz_answer_5_2").style.display="none";
			
		if(question_5==0)
			document.getElementById("fitting_quiz_answer_5_0").style.display="block";

		if(question_5==1)
			seite=seite+1;
			
		if(question_5==2)
		{
			if(question_4==1)
			{
				document.getElementById("fitting_quiz_answer_5_2").style.display="block";
			}
			else
			{
				seite=seite+1;
			}
		}
	}		
	
	
	if(seite==13)
		if(question_6a==0)
			seite=seite+1;
	
		if(seite==11) //antwort 6: wie passen die träger?
	{
			document.getElementById("fitting_quiz_answer_6_0").style.display="none"
			document.getElementById("fitting_quiz_answer_6_1").style.display="none"		
			
			if(question_6==0)
			document.getElementById("fitting_quiz_answer_6_0").style.display="block"

		if(question_6==1)
			document.getElementById("fitting_quiz_answer_6_1").style.display="block"
			
		if(question_6==2)
			seite=seite+1
	}		
	
	
		if(seite==15) 
	{
			document.getElementById("fitting_quiz_answer_8_0").style.display="none"
			document.getElementById("fitting_quiz_answer_8_1").style.display="none"		
			document.getElementById("fitting_quiz_answer_8_2").style.display="none"		
			document.getElementById("fitting_quiz_answer_8_3").style.display="none"		
			document.getElementById("fitting_quiz_answer_8_4").style.display="none"		
			document.getElementById("fitting_quiz_answer_8_5").style.display="none"		
			document.getElementById("fitting_quiz_answer_8_6").style.display="none"		
			document.getElementById("fitting_quiz_answer_8_7").style.display="none"		
			
			
			
			
			
		if(question_8==0)
			document.getElementById("fitting_quiz_answer_8_0").style.display="block"

		if(question_8==1)
			document.getElementById("fitting_quiz_answer_8_1").style.display="block"
			

		if(question_8==2)
			document.getElementById("fitting_quiz_answer_8_2").style.display="block"
			
		if(question_8==3)
			document.getElementById("fitting_quiz_answer_8_3").style.display="block"
			
		if(question_8==4)
			document.getElementById("fitting_quiz_answer_8_4").style.display="block"
			
		if(question_8==5)
			document.getElementById("fitting_quiz_answer_8_5").style.display="block"
			
		if(question_8==6)
			document.getElementById("fitting_quiz_answer_8_6").style.display="block"
			
		if(question_8==7)
			document.getElementById("fitting_quiz_answer_8_7").style.display="block"
			

	}	

	unfade(document.getElementsByClassName("content_quiz_fitting_question")[seite])
	window.scrollTo(0, 0);
	if(seite==18)
	{
		fbq('track', 'QuizCompleted');

		if(login=="true" || document.getElementById("email_provided_quiz").innerHTML!="")
			document.getElementById("email_showroom").style.display="none"
	}
		
	define_fortschrittsbalken();		
	
	
	if(seite==1 || seite ==2 || seite ==4 || seite ==6 || seite ==8 || seite ==10 || seite ==12 || seite ==13 || seite ==14 || seite ==16 || seite ==17)
	{
	
			$.ajax({
			timeout:2000,
 			error: function(){

 			},
			type: "GET",
			url: "/save_preliminary_quiz_results/",
			dataType: "json",
			data: { "band_click_first_id":band_click_first_id,"cup_click_first_id":cup_click_first_id,"brand_click_first_id":brand_click_first_id, "band_click_second_id":band_click_second_id,"cup_click_second_id":cup_click_second_id,"brand_click_second_id":brand_click_second_id,"question_2":question_2,"question_3":question_3,"question_4":question_4,"question_5":question_5,"question_6":question_6,"question_6a":question_6a,"question_8":question_8,"question_9":question_9,"panty_id":panty_id },
			success: function(data) {
				
				
			}
			
			})
	}
	
	
}





				


function back_quiz_page(seite_,vorseite_)
{
		seite=seite_
	vorseite=vorseite_
	if(band_click_second_id==-1 && vorseite==13)
		vorseite=12;
	unfade(document.getElementsByClassName("content_quiz_fitting_question")[vorseite])
	document.getElementsByClassName("content_quiz_fitting_question")[seite].style.display="none";		
	document.getElementsByClassName("content_quiz_fitting_question")[seite].style.opacity="0";
	define_fortschrittsbalken();		
	
}




function enter_panty(element)
{
	if(element.id!=panty_id)
	{
		element.style.border="0.5px solid #f0d1d6";
		element.style.backgroundColor="#f0d1d6";	
		element.style.color="#ffffff";	
	}	
}



function leave_panty(element)
{
	if(element.id!=panty_id)
	{
		element.style.border="0.5px solid #da8e9a";
		element.style.backgroundColor="#f7e8ea";		
		element.style.color="#4E4E4E";	
	}	
}






function enter_band_second(element)
{
	if(element.id!=band_click_second_id)
	{
		element.style.border="0.5px solid #f0d1d6";
		element.style.backgroundColor="#f0d1d6";	
		element.style.color="#ffffff";	
	}	
}


function leave_band_second(element)
{
	if(element.id!=band_click_second_id)
	{
		element.style.border="0.5px solid #da8e9a";
		element.style.backgroundColor="#f7e8ea";		
		element.style.color="#4E4E4E";	
	}
}


function enter_cup_second(element)
{
	if(element.id!=cup_click_second_id)
	{
		element.style.border="0.5px solid #f0d1d6";
		element.style.backgroundColor="#f0d1d6";	
		element.style.color="#ffffff";	
	}	
}


function leave_cup_second(element)
{
	if(element.id!=cup_click_second_id)
	{
		element.style.border="0.5px solid #da8e9a";
		element.style.backgroundColor="#f7e8ea";		
		element.style.color="#4E4E4E";	
	}
}







function enter_band_first(element)
{
	if(element.id!=band_click_first_id)
	{
		element.style.border="0.5px solid #f0d1d6";
		element.style.backgroundColor="#f0d1d6";	
		element.style.color="#ffffff";	
	}	
}


function leave_band_first(element)
{
	if(element.id!=band_click_first_id)
	{
		element.style.border="0.5px solid #da8e9a";
		element.style.backgroundColor="#f7e8ea";		
		element.style.color="#4E4E4E";	
	}
}


function enter_cup_first(element)
{
	if(element.id!=cup_click_first_id)
	{
		element.style.border="0.5px solid #f0d1d6";
		element.style.backgroundColor="#f0d1d6";	
		element.style.color="#ffffff";	
	}	
}


function leave_cup_first(element)
{
	if(element.id!=cup_click_first_id)
	{
		element.style.border="0.5px solid #da8e9a";
		element.style.backgroundColor="#f7e8ea";		
		element.style.color="#4E4E4E";	
	}
}

function enter_picture(element)
{
	if(element.id!=question_8)
		element.style.backgroundColor="#f7e8ea"
}

function leave_picture(element)
{
	if(element.id!=question_8)
		element.style.backgroundColor="#ffffff"
}


function enter_balken(element){
	if(element.id!=question_2)
		  element.style.backgroundColor="#f7e8ea";
  
}

function leave_balken(element){
	
	if(element.id!=question_2)
  		element.style.backgroundColor="#ffffff";
  
}



function enter_balken_different_size(element){
	if(element.id!=question_6a)
		  element.style.backgroundColor="#f7e8ea";
  
}

function leave_balken_different_size(element){
	
	if(element.id!=question_6a)
  		element.style.backgroundColor="#ffffff";
  
}


function enter_balken_sizing(element){
	if(element.id!=question_9)
		  element.style.backgroundColor="#f7e8ea";
  
}

function leave_balken_sizing(element){
	
	if(element.id!=question_9)
  		element.style.backgroundColor="#ffffff";
  
}




function enter_picture_cups(element){
	if(element.id!=question_3)
		element.style.backgroundColor="#f7e8ea"
  
}

function leave_picture_cups(element){
	
	if(element.id!=question_3)
		element.style.backgroundColor="#ffffff"
  
}


function enter_picture_band(element){
	if(element.id!=question_4)
		element.style.backgroundColor="#f7e8ea"
  
}

function leave_picture_band(element){
	
	if(element.id!=question_4)
		element.style.backgroundColor="#ffffff"
  
}



function enter_picture_band_2(element){
	if(element.id!=question_5)
		element.style.backgroundColor="#f7e8ea"
  
}

function leave_picture_band_2(element){
	
	if(element.id!=question_5)
		element.style.backgroundColor="#ffffff"
  
}


function enter_picture_stripes(element){
	if(element.id!=question_6)
		element.style.backgroundColor="#f7e8ea"
  
}

function leave_picture_stripes(element){
	
	if(element.id!=question_6)
		element.style.backgroundColor="#ffffff"
  
}







function select_picture_question_4(id)
{
	i=0;
	question_4=-1
	while(i<=2)
	{	
		if(i==id)
		{
			if(i==0)
			{
				document.getElementsByClassName ("block_0_question_4")[i].style.backgroundColor="#efbcc4";
				document.getElementsByClassName ("block_0_question_4")[i].style.color="#ffffff";
			}
			else
			{
				document.getElementsByClassName ("block_0_question_4_ML")[i-1].style.backgroundColor="#efbcc4";
				document.getElementsByClassName ("block_0_question_4_ML")[i-1].style.color="#ffffff";
			}
			question_4=id;
			
		  		  			gtag('event', 'quiz',{
				  
				  'event_label':id,
				  'event_category': 'Wie sitzt das Band?'
				});

		}
		else
		{
			if(i==0)
			{
				document.getElementsByClassName ("block_0_question_4")[i].style.backgroundColor="#ffffff";
				document.getElementsByClassName ("block_0_question_4")[i].style.color="#4E4E4E";
			}
			else
			{
				document.getElementsByClassName ("block_0_question_4_ML")[i-1].style.backgroundColor="#ffffff";
				document.getElementsByClassName ("block_0_question_4_ML")[i-1].style.color="#4E4E4E";
			}			
		}	
		i=i+1;
	}
	
	if(question_4!=-1)
	{
			document.getElementById("button_quiz_band").style.display="block"
  			next_quiz_page(7,6);		
	}
	
}


function select_picture_question_5(id)
{
	i=0;
	question_5=-1
	while(i<=2)
	{	
		if(i==id)
		{
			if(i==0)
			{
				document.getElementsByClassName ("block_0_question_5")[i].style.backgroundColor="#efbcc4";
				document.getElementsByClassName ("block_0_question_5")[i].style.color="#ffffff";
			}
			else
			{
				document.getElementsByClassName ("block_0_question_5_ML")[i-1].style.backgroundColor="#efbcc4";
				document.getElementsByClassName ("block_0_question_5_ML")[i-1].style.color="#ffffff";
			}
			question_5=id;
		  		  			gtag('event', 'quiz',{
				  
				  'event_label':id,
				  'event_category': 'Wie trägst du das Band?'
				});
		}
		else
		{
			if(i==0)
			{
				document.getElementsByClassName ("block_0_question_5")[i].style.backgroundColor="#ffffff";
				document.getElementsByClassName ("block_0_question_5")[i].style.color="#4E4E4E";
			}
			else
			{
				document.getElementsByClassName ("block_0_question_5_ML")[i-1].style.backgroundColor="#ffffff";
				document.getElementsByClassName ("block_0_question_5_ML")[i-1].style.color="#4E4E4E";
			}			
		}	
		i=i+1;
	}
	
	if(question_5!=-1)
	{
			document.getElementById("button_quiz_band_2").style.display="block"
  			next_quiz_page(9,8);		
	}
	
}


function select_picture_question_6(id)
{
	i=0;
	question_6=-1;
	while(i<=2)
	{	
		if(i==id)
		{
			if(i==0)
			{
				document.getElementsByClassName ("block_0_question_6")[i].style.backgroundColor="#efbcc4";
				document.getElementsByClassName ("block_0_question_6")[i].style.color="#ffffff";
			}
			else
			{
				document.getElementsByClassName ("block_0_question_6_ML")[i-1].style.backgroundColor="#efbcc4";
				document.getElementsByClassName ("block_0_question_6_ML")[i-1].style.color="#ffffff";
			}
			question_6=id;
		  		  			gtag('event', 'quiz',{
				  
				  'event_label':id,
				  'event_category': 'Wie sitzen die Träger?'
				});
		}
		else
		{
			if(i==0)
			{
				document.getElementsByClassName ("block_0_question_6")[i].style.backgroundColor="#ffffff";
				document.getElementsByClassName ("block_0_question_6")[i].style.color="#4E4E4E";
			}
			else
			{
				document.getElementsByClassName ("block_0_question_6_ML")[i-1].style.backgroundColor="#ffffff";
				document.getElementsByClassName ("block_0_question_6_ML")[i-1].style.color="#4E4E4E";
			}			
		}	
		i=i+1;
	}
	
	if(question_6!=-1)
	{
			document.getElementById("button_quiz_stripes").style.display="block"
  			next_quiz_page(11,10);		
	}
	
}


function select_picture_question_8(id)
{
	i=0;
			question_8=-1
	while(i<=7)
	{	
		
		if(i==id)
		{
			document.getElementsByClassName ("block_1_question_8")[i].style.backgroundColor="#efbcc4";
			document.getElementsByClassName ("block_1_question_8")[i].style.color="#ffffff";
			question_8=id;
			
					  		  			gtag('event', 'quiz',{
				  
				  'event_label':id,
				  'event_category': 'Welche Brustform?'
				});

		}
		else
		{
			document.getElementsByClassName ("block_1_question_8")[i].style.backgroundColor="#ffffff";
			document.getElementsByClassName ("block_1_question_8")[i].style.color="#4E4E4E";

			
		}	
		i=i+1;
	}
	
	if(question_8!=-1)
	{
  		next_quiz_page(15,14);		
			document.getElementById("button_quiz_form_details").style.display="block"
			
	}
	
}






function select_picture_cups(id)
{
	i=0;
	question_3=-1
	while(i<=2)
	{	
		if(i==id)
		{
			if(i==0)
			{
				document.getElementsByClassName ("block_0_question_3")[i].style.backgroundColor="#efbcc4";
				document.getElementsByClassName ("block_0_question_3")[i].style.color="#ffffff";
			}
			else
			{
				document.getElementsByClassName ("block_0_question_3_ML")[i-1].style.backgroundColor="#efbcc4";
				document.getElementsByClassName ("block_0_question_3_ML")[i-1].style.color="#ffffff";
			}
			question_3=id;
		  		  			gtag('event', 'quiz',{
				  
				  'event_label':id,
				  'event_category': 'Wie passen die Cups?'
				});
		}
		else
		{
			if(i==0)
			{
				document.getElementsByClassName ("block_0_question_3")[i].style.backgroundColor="#ffffff";
				document.getElementsByClassName ("block_0_question_3")[i].style.color="#4E4E4E";
			}
			else
			{
				document.getElementsByClassName ("block_0_question_3_ML")[i-1].style.backgroundColor="#ffffff";
				document.getElementsByClassName ("block_0_question_3_ML")[i-1].style.color="#4E4E4E";
			}			
		}	
		i=i+1;
	}
	
	if(question_3!=-1)
	{
			document.getElementById("button_quiz_cup").style.display="block"
  			next_quiz_page(5,4);		
	}
}






function balken_fitting_quiz_question_sizing(id)
{
	i=0;
	question_9=-1
	while(i<=3)
	{	
		if(i==id)
		{
			document.getElementsByClassName ("auswahl_balken_fitting_quiz_sizing")[i].style.border="2px solid #efbcc4";
			document.getElementsByClassName ("auswahl_balken_fitting_quiz_sizing")[i].style.backgroundColor="#efbcc4";
			document.getElementsByClassName ("auswahl_balken_fitting_quiz_sizing")[i].style.color="#ffffff";
			question_9=id
			
								  		  			gtag('event', 'quiz',{
				  
				  'event_label':id,
				  'event_category': 'Wie groß bist du?'
				});

		}
		else
		{
			document.getElementsByClassName ("auswahl_balken_fitting_quiz_sizing")[i].style.backgroundColor="#ffffff";
			document.getElementsByClassName ("auswahl_balken_fitting_quiz_sizing")[i].style.color="#4E4E4E";
			document.getElementsByClassName ("auswahl_balken_fitting_quiz_sizing")[i].style.border="2px solid #f7e8ea";

			
		}	
		i=i+1;
	}
	
	if(question_9!=-1)
	{
  				next_quiz_page(17,16);		
			document.getElementById("button_quiz_body_size").style.display="block"

	}
}







function balken_fitting_quiz_question_different_size(id)
{
	i=0;
	question_6a=-1
	while(i<=1)
	{	
		if(i==id)
		{
			document.getElementsByClassName ("auswahl_balken_fitting_quiz_different_size")[i].style.border="2px solid #efbcc4";
			document.getElementsByClassName ("auswahl_balken_fitting_quiz_different_size")[i].style.backgroundColor="#efbcc4";
			document.getElementsByClassName ("auswahl_balken_fitting_quiz_different_size")[i].style.color="#ffffff";
			question_6a=id
			
					  		  			gtag('event', 'quiz',{
				  
				  'event_label':id,
				  'event_category': 'Trägst du manchmal eine andere Größe?'
				});

		}
		else
		{
			document.getElementsByClassName ("auswahl_balken_fitting_quiz_different_size")[i].style.backgroundColor="#ffffff";
			document.getElementsByClassName ("auswahl_balken_fitting_quiz_different_size")[i].style.color="#4E4E4E";
			document.getElementsByClassName ("auswahl_balken_fitting_quiz_different_size")[i].style.border="2px solid #f7e8ea";

			
		}	
		i=i+1;
	}
	
	if(question_6a!=-1)
	{
		
			document.getElementById("button_quiz_different_size").style.display="block"
			if(question_6a==1)
  				next_quiz_page(13,11);		
 			if(question_6a==0)
 			{
 				band_click_second_id=-1
 				cup_click_second_id=-1
 				brand_click_second_id=""
  				next_quiz_page(14,11);	
  			}
	}
}









function balken_fitting_quiz_question_2(id)
{
	i=0;
	question_2=-1
	while(i<=3)
	{	
		if(i==id)
		{
			document.getElementsByClassName ("auswahl_balken_fitting_quiz")[i].style.border="2px solid #efbcc4";
			document.getElementsByClassName ("auswahl_balken_fitting_quiz")[i].style.backgroundColor="#efbcc4";
			document.getElementsByClassName ("auswahl_balken_fitting_quiz")[i].style.color="#ffffff";
			question_2=id
		  		  			gtag('event', 'quiz',{
				  
				  'event_label':id,
				  'event_category': 'Wie alt ist der BH?'
				});
		}
		else
		{
			document.getElementsByClassName ("auswahl_balken_fitting_quiz")[i].style.backgroundColor="#ffffff";
			document.getElementsByClassName ("auswahl_balken_fitting_quiz")[i].style.color="#4E4E4E";
			document.getElementsByClassName ("auswahl_balken_fitting_quiz")[i].style.border="2px solid #f7e8ea";

			
		}	
		i=i+1;
	}
	
	if(question_2!=-1)
	{
			document.getElementById("button_quiz_alter").style.display="block"
  			next_quiz_page(3,2);		
	}
}



function band_click_first(id)
{
	i=0;
	band_click_first_id=-1
	while(i<=13)
	{	
		if(i==id)
		{
			document.getElementsByClassName ("circle_band_first")[i].style.border="0.5px solid #efbcc4";
			document.getElementsByClassName ("circle_band_first")[i].style.backgroundColor="#efbcc4";
			document.getElementsByClassName ("circle_band_first")[i].style.color="#ffffff";
			band_click_first_id=id
  			unfade(document.getElementById("cup_sizing_first"))
  			
			gtag('event', 'quiz',{
				  
				  'event_label': String(i),
				  'event_category': 'First Band'
				});
								window.scrollTo(0,document.body.scrollHeight);

		}
		else
		{
			document.getElementsByClassName ("circle_band_first")[i].style.border="0.5px solid #da8e9a";
			document.getElementsByClassName ("circle_band_first")[i].style.backgroundColor="#f7e8ea";		
			document.getElementsByClassName ("circle_band_first")[i].style.color="#4E4E4E";	
				
			
		}	
		i=i+1;
	}
}


function panty_click(id)
{
	i=0;
	panty_id=-1
	while(i<=6)
	{	
		if(i==id)
		{
			document.getElementsByClassName ("circle_panty")[i].style.border="0.5px solid #efbcc4";
			document.getElementsByClassName ("circle_panty")[i].style.backgroundColor="#efbcc4";
			panty_id=id
			
			gtag('event', 'quiz',{
				  
				  'event_label': String(i),
				  'event_category': 'Panty'
				});
		}
		else
		{
			document.getElementsByClassName ("circle_panty")[i].style.border="0.5px solid #da8e9a";
			document.getElementsByClassName ("circle_panty")[i].style.backgroundColor="#f7e8ea";		
			document.getElementsByClassName ("circle_panty")[i].style.color="#4E4E4E";	
				
			
		}	
		i=i+1;
	}
	
	
	if(panty_id!=-1)
	{
			document.getElementById("button_quiz_panty").style.display="block"
  			next_quiz_page(18,17);		
	}
}



function cup_click_first(id)
{
	i=0;
	cup_click_first_id=-1
	while(i<=13)
	{	
		if(i==id)
		{
			document.getElementsByClassName ("circle_cup_first")[i].style.border="0.5px solid #efbcc4";
			document.getElementsByClassName ("circle_cup_first")[i].style.backgroundColor="#efbcc4";
			document.getElementsByClassName ("circle_cup_first")[i].style.color="#ffffff";	
			cup_click_first_id=id
  			unfade(document.getElementById("brand_sizing_first"))
  			
  			gtag('event', 'quiz',{
				  
				  'event_label': String(i),
				  'event_category': 'First Cup'
				});
				window.scrollTo(0,document.body.scrollHeight);

		}
		else
		{
			document.getElementsByClassName ("circle_cup_first")[i].style.border="0.5px solid #da8e9a";
			document.getElementsByClassName ("circle_cup_first")[i].style.backgroundColor="#f7e8ea";
			document.getElementsByClassName ("circle_cup_first")[i].style.color="#4E4E4E";	
		}	
		i=i+1;
	}
}


function click_on_competitors_first()
{
	brand_click_first_id=""
	if(document.getElementsByClassName("brand_selection_first")[0].value!="")
	{
  			gtag('event', 'quiz',{
				  
				  'event_label': document.getElementsByClassName("brand_selection_first")[0].value,
				  'event_category': 'First Competitor'
				});
		unfade(document.getElementById("button_sizing_first"))
		brand_click_first_id=document.getElementsByClassName("brand_selection_first")[0].value
		window.scrollTo(0,document.body.scrollHeight);

	}
}















function band_click_second(id)
{
	i=0;
	band_click_second_id=-1
	while(i<=13)
	{	
		if(i==id)
		{
			document.getElementsByClassName ("circle_band_second")[i].style.border="0.5px solid #efbcc4";
			document.getElementsByClassName ("circle_band_second")[i].style.backgroundColor="#efbcc4";
			document.getElementsByClassName ("circle_band_second")[i].style.color="#ffffff";
			band_click_second_id=id
  			unfade(document.getElementById("cup_sizing_second"))
  			
  		  			gtag('event', 'quiz',{
				  
				  'event_label': String(i),
				  'event_category': 'Second Band'
				});
		}
		else
		{
			document.getElementsByClassName ("circle_band_second")[i].style.border="0.5px solid #da8e9a";
			document.getElementsByClassName ("circle_band_second")[i].style.backgroundColor="#f7e8ea";		
			document.getElementsByClassName ("circle_band_second")[i].style.color="#4E4E4E";	
				
			
		}	
		i=i+1;
	}
}


function cup_click_second(id)
{
	i=0;
	cup_click_second_id=-1
	while(i<=13)
	{	
		if(i==id)
		{
			document.getElementsByClassName ("circle_cup_second")[i].style.border="0.5px solid #efbcc4";
			document.getElementsByClassName ("circle_cup_second")[i].style.backgroundColor="#efbcc4";
			document.getElementsByClassName ("circle_cup_second")[i].style.color="#ffffff";	
			cup_click_second_id=id
  			unfade(document.getElementById("brand_sizing_second"))
  			
  			  		  			gtag('event', 'quiz',{
				  
				  'event_label': String(i),
				  'event_category': 'Second Cup'
				});
		}
		else
		{
			document.getElementsByClassName ("circle_cup_second")[i].style.border="0.5px solid #da8e9a";
			document.getElementsByClassName ("circle_cup_second")[i].style.backgroundColor="#f7e8ea";
			document.getElementsByClassName ("circle_cup_second")[i].style.color="#4E4E4E";	
		}	
		i=i+1;
	}
}


function click_on_competitors_second()
{
	brand_click_second_id=""
	if(document.getElementsByClassName("brand_selection_second")[0].value!="")
	{
		unfade(document.getElementById("button_sizing_second"))
		
		  		  			gtag('event', 'quiz',{
				  
				  'event_label': document.getElementsByClassName("brand_selection_second")[0].value,
				  'event_category': 'Second Competitor'
				});
		brand_click_second_id=document.getElementsByClassName("brand_selection_second")[0].value
	}
}











function unfade(element) {
	if(loaded==1)
	{
	    var op = 0.1;  // initial opacity
	    element.style.display = 'block';
	    var timer = setInterval(function () {
	        if (op >= 1){
	            clearInterval(timer);
	        }
	        element.style.opacity = op;
	        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
	        op += op * 0.1;
	    }, 10);
    }
}


function initiate_values()
{
	loaded=0;
	seite=0;	
	document.getElementById("email_showroom").value=document.getElementById("email_provided_quiz").innerHTML
	document.getElementsByClassName("header-bottom")[0].style.display="none";		
	document.getElementsByClassName("header_bottom_all")[0].style.display="none";	
	document.getElementsByClassName("header_bottom_page_infos")[0].style.display="none";		
	
	
	document.getElementsByClassName("sidebar")[0].style.display="none";
	
 	quiz_data=JSON.parse(document.getElementsByClassName("quiz_data")[0].innerHTML);
 	if(quiz_data[0].band_click_first_id!=-1)
 	{
 		band_click_first(quiz_data[0].band_click_first_id)
		document.getElementById("cup_sizing_first").style.display="block";
		document.getElementById("cup_sizing_first").style.opacity="1";
 	}
 	if(quiz_data[0].cup_click_first_id!=-1)
 	{
 		cup_click_first(quiz_data[0].cup_click_first_id)
		document.getElementById("brand_sizing_first").style.display="block"; 	
 	}
 	if(quiz_data[0].brand_click_first_id!="")
 	{
 		document.getElementsByClassName("brand_selection_first")[0].value=quiz_data[0].brand_click_first_id;
		

		document.getElementById("button_sizing_first").style.display="block";
				document.getElementById("button_sizing_first").style.opacity="1";

 		click_on_competitors_first()
 	}

 	if(quiz_data[0].band_click_second_id!=-1)
 	{
 		band_click_second(quiz_data[0].band_click_second_id)
		document.getElementById("cup_sizing_second").style.display="block";
		document.getElementById("cup_sizing_second").style.opacity="1";
 	}
 	if(quiz_data[0].cup_click_second_id!=-1)
 	{
 		cup_click_second(quiz_data[0].cup_click_second_id)
		document.getElementById("brand_sizing_second").style.display="block";
 	}
 	if(quiz_data[0].brand_click_second_id!="" && quiz_data[0].brand_click_second_id!="-1")
 	{
 		document.getElementsByClassName("brand_selection_second")[0].value=quiz_data[0].brand_click_second_id;

		document.getElementById("button_sizing_second").style.display="block";
				document.getElementById("button_sizing_second").style.opacity="1";
  		click_on_competitors_second()
  		
 	}
 		
 		
  	if(quiz_data[0].question_2!=-1)
 		balken_fitting_quiz_question_2(quiz_data[0].question_2)


  	if(quiz_data[0].question_3!=-1)
 		select_picture_cups(quiz_data[0].question_3)


  	if(quiz_data[0].question_4!=-1)
 		select_picture_question_4(quiz_data[0].question_4) 		


  	if(quiz_data[0].question_5!=-1)
 		select_picture_question_5(quiz_data[0].question_5) 		 
   	if(quiz_data[0].question_6!=-1)
 		select_picture_question_6(quiz_data[0].question_6) 		 	
    if(quiz_data[0].question_6a!=-1)
 		balken_fitting_quiz_question_different_size(quiz_data[0].question_6a) 	


   	if(quiz_data[0].question_8!=-1)
 		select_picture_question_8(quiz_data[0].question_8) 		
 
 
	if(quiz_data[0].question_9!=-1)
 		balken_fitting_quiz_question_sizing(quiz_data[0].question_9) 				


	if(quiz_data[0].panty_id!=-1)
 		panty_click(quiz_data[0].panty_id) 	 		
	seite=0;	
	vorseite=0;
	loaded=1;
	next_quiz_page(0,0)
	fortschrittsbalken_links=0;
	define_fortschrittsbalken();
	
		if(login=="true" || document.getElementById("email_provided_quiz").innerHTML!="")
			document.getElementById("email_showroom").style.display="none"		
	
}

function define_fortschrittsbalken()
{
	fortschritt=Math.floor(seite/18*100)
	document.getElementById("fortschrittsbalken_links").style.width=fortschritt.toString()+"%"	
	document.getElementById("fortschrittsbalken_rechts").style.width=(100-fortschritt).toString()+"%"	
}



function submit_quiz_results()
{
			button_logo("0","submit_quiz_text","submit_quiz_logo","submit_quiz")



		if(document.getElementById("email_showroom").display!="none")
			email=document.getElementById("email_showroom").value;
		else
			email=document.getElementById("email_provided_quiz").value;
			$.ajax({
			timeout:15000,
 			error: function(){
 							button_logo("1","submit_quiz_text","submit_quiz_logo","submit_quiz")

 			},
			type: "GET",
			url: "/submit_quiz_results/",
			dataType: "json",
			data: { "band_click_first_id":band_click_first_id,"cup_click_first_id":cup_click_first_id,"brand_click_first_id":brand_click_first_id, "band_click_second_id":band_click_second_id,"cup_click_second_id":cup_click_second_id,"brand_click_second_id":brand_click_second_id,"question_2":question_2,"question_3":question_3,"question_4":question_4,"question_5":question_5,"question_6":question_6,"question_6a":question_6a,"question_8":question_8,"question_9":question_9,"panty_id":panty_id,"email":email},
			success: function(data) {
				
				 							button_logo("1","submit_quiz_text","submit_quiz_logo","submit_quiz")
				if(data=="email falsch")
				{
					alert_userdata("GÜLTIGE E-MAIL","Bitte eine gültige E-Mail Adresse angeben")
				}
				else
					if(data=="exists already")
						alert_userdata_showroom_registration("E-MAIL EXISTIERT BEREITS","Diese E-Mail Adresse existiert bereits. Bitte logge Dich ein, damit Deine Antworten gespeichert werden können.")
					else
					{
						window.location= "https://www.darlinglace.com/Produktauswahl/Mein Showroom";
						fbq('track', 'QuizWithEmail');
	 	
					}

			}
			
			})
	
}





  
  