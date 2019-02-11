var seite,vorseite;
var band_click_first_id,cup_click_first_id,brand_click_first_id;
var question_2,question_3,question_4,question_5,question_6


function next_quiz_page(seite_,vorseite_)
{
	seite=seite_
	vorseite=vorseite_
	i=0;
	while (i<=17)
	{
		document.getElementsByClassName("content_quiz_fitting_question")[i].style.display="none";		
		i=i+1;
	}
	
	

	if(seite==5) //antwort 3: wie passen die Cups?
	{
		if(question_3==0)
			document.getElementById("fitting_quiz_answer_3_0").style.display="block"

		if(question_3==1)
			document.getElementById("fitting_quiz_answer_3_1").style.display="block"
			
		if(question_3==2)
			document.getElementById("fitting_quiz_answer_3_2").style.display="block"		
	}	
	
	if(seite==7) //antwort 4: wie passt das band?
	{
		if(question_4==0)
			document.getElementById("fitting_quiz_answer_4_0").style.display="block"

		if(question_4==1)
			document.getElementById("fitting_quiz_answer_4_1").style.display="block"
			
		if(question_4==2)
			document.getElementById("fitting_quiz_answer_4_2").style.display="block"		
	}	
	
	if(seite==9) //antwort 5: wie passt das band?
	{
		if(question_5==0)
			document.getElementById("fitting_quiz_answer_5_0").style.display="block"

		if(question_5==1)
			document.getElementById("fitting_quiz_answer_5_1").style.display="block"
			
		if(question_5==2)
			seite=seite+1;
	}		
	
		if(seite==11) //antwort 6: wie passen die träger?
	{
		if(question_6==0)
			document.getElementById("fitting_quiz_answer_6_0").style.display="block"

		if(question_6==1)
			document.getElementById("fitting_quiz_answer_6_1").style.display="block"
			
		if(question_6==2)
			seite=seite+1
	}		
	unfade(document.getElementsByClassName("content_quiz_fitting_question")[seite])


}

function back_quiz_page(seite_,vorseite_)
{
		seite=seite_
	vorseite=vorseite_
	unfade(document.getElementsByClassName("content_quiz_fitting_question")[vorseite])
	document.getElementsByClassName("content_quiz_fitting_question")[seite].style.display="none";		
	
}



function enter_band_first(element)
{
	if(element.id!=band_click_first_id)
	{
		element.style.border="0.5px solid #d27786";
		element.style.backgroundColor="#d27786";	
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
		element.style.border="0.5px solid #d27786";
		element.style.backgroundColor="#d27786";	
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
	element.style.backgroundColor="#f7e8ea"
}

function leave_picture(element)
{
	element.style.backgroundColor="#ffffff"
}


function enter_balken(element){
	if(element.id!=cup_click_first_id)
		  element.style.backgroundColor="#f7e8ea";
  
}

function leave_balken(element){
	if(element.id!=cup_click_first_id)
  		element.style.backgroundColor="#ffffff";
  
}

function select_picture(element)
{
	question_3=element.id;
	next_quiz_page(5,3);	
	
}


function select_picture_question_4(element)
{
	question_4=element.id;
	next_quiz_page(7,5);	
	
}



function select_picture_question_5(element)
{
	question_5=element.id;
	next_quiz_page(9,7);	
	
}


function select_picture_question_6(element)
{
	question_6=element.id;
	next_quiz_page(11,9);	
	
}


function select_picture_question_7(element)
{
	question_7=element.id;
	next_quiz_page(13,11);	
	
}






function balken_fitting_quiz_question_2(element)
{
	question_2=element.id;
	next_quiz_page(3,2);
	
	element.style.border="0.5px solid #c34a5e";
	element.style.backgroundColor="#c34a5e";
}

function band_click_first(id)
{
	i=0;
	band_click_first_id=-1
	while(i<=8)
	{	
		if(i==id)
		{
			document.getElementsByClassName ("circle_band_first")[i].style.border="0.5px solid #c34a5e";
			document.getElementsByClassName ("circle_band_first")[i].style.backgroundColor="#c34a5e";
			band_click_first_id=id
  			unfade(document.getElementById("cup_sizing_first"))
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


function cup_click_first(id)
{
	i=0;
	cup_click_first_id=-1
	while(i<=8)
	{	
		if(i==id)
		{
			document.getElementsByClassName ("circle_cup_first")[i].style.border="0.5px solid #c34a5e";
			document.getElementsByClassName ("circle_cup_first")[i].style.backgroundColor="#c34a5e";
			document.getElementsByClassName ("circle_cup_first")[i].style.color="#ffffff";	
			cup_click_first_id=id
  			unfade(document.getElementById("brand_sizing_first"))
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
	brand_click_first_id="false"
	if(document.getElementsByClassName("brand_selection_first")[0].value!="")
	{
		unfade(document.getElementById("button_sizing_first"))
		brand_click_first_id="true"
	}
}






function unfade(element) {
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


function initiate_values()
{
	
	seite=0;	
	document.getElementsByClassName("header-bottom")[0].style.display="none";		
	
	document.getElementsByClassName("header_top_all")[1].style.display="none";
}






  
  