var stil,color_0,color_1,color_2,color_3,form, position,symmetrie,sitz,cup,band, age,quiztaken,competitor_brand,band_problems,cup_problems,band_recommendation,cup_recommendation,empfehlungstext_sizing,empfehlungstext_type;

function quiz_page_initialize()
{

	
			$.ajax({
			type: "POST",
			url: "/quiz_abrufen/",
			dataType: "json",
			data: {'stil':'' },
			success: function(data) {
alert(data)
					data=JSON.parse(data);
					stil=data[0].stil


					color_0=data[0].color_0
					color_1=data[0].color_1
					color_2=data[0].color_2
					color_3=data[0].color_3
					
					
					
					
					form=data[0].form
					position=data[0].position
					symmetrie=data[0].symmetrie
					sitz=data[0].sitz
					cup=data[0].cup
					band=data[0].band
					age=data[0].age
					competitor_brand=data[0].competitor_brand
					band_problems=data[0].band_problems
					cup_problems=data[0].cup_problems
					band_problems=data[0].band_recommendation
					cup_problems=data[0].cup_recommendation					


						if(cup_problems!="")
						{
							quiz_page_laden_zurueck(10)
							quiz_page_laden(10)
						}
						else
							if(band_problems!="")
							{
								quiz_page_laden_zurueck(9)
								quiz_page_laden(9)
							}
							else
								if(competitor_brand!="")
								{
									quiz_page_laden_zurueck(8)
									quiz_page_laden(8)
								}
								else
									if(sitz!=-1)
									{
										quiz_page_laden_zurueck(7)
										quiz_page_laden(7)
									}
									else		
										if(symmetrie!=-1)
										{
											quiz_page_laden_zurueck(6)
											quiz_page_laden(6)
										}
										else		
											if(position!=-1)
											{
												quiz_page_laden_zurueck(5)
												quiz_page_laden(5)
											}
											else		
												if(form!=-1)
												{
													quiz_page_laden_zurueck(4)
													quiz_page_laden(4)
												}
												else		
													if(color_0!=-1 || color_1!=-1 || color_2!=-1 || color_3!=-1)
													{
														quiz_page_laden_zurueck(3)
														quiz_page_laden(3)
													}
													else		
														if(stil!=-1)
														{
															quiz_page_laden_zurueck(2)
															quiz_page_laden(2)
														}
														else	
														{
		
															quiz_page_laden_zurueck(0);
															quiz_page_laden(0)	;
														}														

			}
		});
		


		
	
}

function quiz_page_laden(seite)
{
alert(seite)
	block=""
	headline=""


	headline=headline+"<div class='headline_overlay'>PERSONÖLICHER SHOWROOM</div><br><br>\r"
	headline=headline+"<div class='headline_overlay_subtitle'>Entdecke deine perfekte Lingerie mithilfe unseres schnellen Quiz</div>\r"



	if(seite==0)
	{
		block=block+"<div class='headline_2_overlay'>Oh Darling, hast du Probleme den richtigen BH zu finden?</div><br><br><br>\r"
		block=block+"<div class='photo_showroom_1_overlay'>\r"
		
		block=block+"<div class='showroom_container'>\r"	
		
		block=block+"<div class='block_1_text_start' style='float:left';>Dein ganz persönlicher Showroom zeigt Dir deine passende Lingerie an. Wir haben ein Lingerie Quiz entwickelt, dass dir sowohl eine Stilempfehlung als auch eine Passformempfehlung anzeigt. Dein persönlicher Showroom wird monatlich aktualisiert, um Dir die neusten Lingerie Trends zu zeigen.</div> "
		

		block=block+"<img  class='photo_showroom_start' src='/static/Janet_1.jpg'></img>\r"

		
		block=block+"</div>\r"
		block=block+"</div>\r"
		footer="<div class='button_main_showroom' style='float:right;opacity:1.0;pointerEvents:auto;' onclick='quiz_upload("+parseInt(seite+1)+")'>Weiter</div>\r"

	}	
	
	if(seite==1)
	{
		block=block+"<div class='headline_2_overlay'>1. Es ist Samstagabend: Welche Art von BH ziehst du an?</div><br><br><br>\r"
		block=block+"<div class='photo_showroom_1_overlay'>\r"
		
		block=block+"<div class='showroom_container'>\r"	
		

		
		block=block+"<div class='block_0'>\r"
		block=block+"<img  class='photo_showroom' src='/static/Janet_1.jpg' onclick='pic_change_quiz(0,3,0)'></img>\r"
		block=block+"<div class='block_1_text'>Sexy</div>\r"
	//	block=block+"<div class='block_1_text_detailliert'>...</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_0'>\r"
		block=block+"<img  class='photo_showroom' src='/static/Janet_1.jpg' onclick='pic_change_quiz(1,3,0)'></img>\r"
		block=block+"<div class='block_1_text'>Verspielt</div>\r"
	//	block=block+"<div class='block_1_text_detailliert'>...</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_0'>\r"
		block=block+"<img  class='photo_showroom' src='/static/Janet_1.jpg' onclick='pic_change_quiz(2,3,0)'></img>\r"
		block=block+"<div class='block_1_text'>Klassisch süß</div>\r"
	//	block=block+"<div class='block_1_text_detailliert'>...</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_0'>\r"
		block=block+"<img  class='photo_showroom' src='/static/Janet_1.jpg' onclick='pic_change_quiz(3,3,0)'></img>\r"
		block=block+"<div class='block_1_text'>Romantisch heiß</div>\r"
	//	block=block+"<div class='block_1_text_detailliert'>...</div>\r"
		block=block+"</div>\r"
		
		block=block+"<span class='stretch'></span>\r"
		block=block+"</div>\r"		
		
		block=block+"</div>\r"
		block=block+"</div>\r"
		footer="<div class='button_zurueck_showroom' onclick='quiz_page_laden_zurueck("+parseInt(seite-1)+")'>Zurück</div>\r"
		footer=footer+"<div class='button_main_showroom'  onclick='quiz_upload("+parseInt(seite+1)+")'>Weiter</div>\r"

	}
	
	
			if(seite==2)
	{
		block=block+"<div class='headline_2_overlay'>2. Welche Farben gefallen dir bei BHs?</div><br><br><br>\r"
		block=block+"<div class='photo_showroom_1_overlay'><br>\r"
		
		block=block+"<div style='margin-bottom:10px'><input type='checkbox' class='color_selection'  style='cursor:pointer;float:left;' id='check1' onclick='pic_change_quiz(0,3,1)'></input><div style='cursor:pointer;float:left;margin-left:5px;' id='0' onclick='click_checkbox(this.id)' >Hautfarben</div></div><br>\r"
		
		block=block+"<div style='margin-bottom:10px'><input type='checkbox' class='color_selection'  style='cursor:pointer;float:left;' id='check1' onclick='pic_change_quiz(1,3,1)'></input><div style='cursor:pointer;float:left;margin-left:5px;' id='1' onclick='click_checkbox(this.id)' >Helle Farben</div></div><br>\r"

		block=block+"<div style='margin-bottom:10px'><input type='checkbox' class='color_selection'  style='cursor:pointer;float:left;' id='check1' onclick='pic_change_quiz(2,3,1)'></input><div style='cursor:pointer;float:left;margin-left:5px;' id='2' onclick='click_checkbox(this.id)' >Dunkle Farben</div></div><br>\r"		

		block=block+"<div style='margin-bottom:10px'><input type='checkbox' class='color_selection'  style='cursor:pointer;float:left;' id='check1' onclick='pic_change_quiz(3,3,1)'></input><div style='cursor:pointer;float:left;margin-left:5px;' id='3' onclick='click_checkbox(this.id)' >Muster</div></div><br>\r"				



		
		
		
		
				
		block=block+"</div>\r"

		footer="<div class='button_zurueck_showroom' onclick='quiz_page_laden_zurueck("+parseInt(seite-1)+")'>Zurück</div>\r"
		footer=footer+"<div class='button_main_showroom'  onclick='quiz_upload("+parseInt(seite+1)+")'>Weiter</div>\r"
	}
	
	
	if(seite==3)
	{
		block=block+"<div class='headline_2_overlay'>3. Welche Form haben deine Brüste?</div><br><br><br>\r"
		block=block+"<div class='photo_showroom_1_overlay' >\r"
		block=block+"<div class='showroom_container'>\r"	
		
		
		block=block+"<div class='block_1'>\r"
		block=block+"<img  class='photo_showroom' src='/static/round_breast.png' onclick='pic_change_quiz(0,1,2)'></img>\r"
		block=block+"<div class='block_1_text'>Rund</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Brüste sind gleich voll im oberen und unteren Bereich</div>\r"
		
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_1'>\r"
		block=block+"<img  class='photo_showroom' src='/static/teardrop_breasts.png' onclick='pic_change_quiz(1,1,2)'></img>\r"
		block=block+"<div class='block_1_text'>Tropfenform</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Brüste sind voller im unteren als im oberen Bereich</div>\r"
		block=block+"</div>\r"
		
		block=block+"<span class='stretch'></span>\r"
		block=block+"</div>\r"
		
				
		block=block+"</div>\r"
		block=block+"</div>\r"
		footer="<div class='button_zurueck_showroom' onclick='quiz_page_laden_zurueck("+parseInt(seite-1)+")'>Zurück</div>\r"
		footer=footer+"<div class='button_main_showroom'  onclick='quiz_upload("+parseInt(seite+1)+")'>Weiter</div>\r"
	}

	if(seite==4)
	{
		block=block+"<div class='headline_2_overlay'>4. Wie ist die Position deiner Brüste?</div><br><br><br>\r"
		block=block+"<div class='photo_showroom_1_overlay'>\r"
		
		block=block+"<div class='showroom_container'>\r"	
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/round_breast.png' onclick='pic_change_quiz(0,2,3)'></img>\r"
		block=block+"<div class='block_1_text'>Sitzt mittig</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Brüste sind gleich voll im oberen und unteren Bereich</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/leich_nach_aussen_breasts.png' onclick='pic_change_quiz(1,2,3)'></img>\r"
		block=block+"<div class='block_1_text'>Leicht Ost-West</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Die Brüste sind ein wenig nach außen geneigt: 1-2 Finger</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/east_west_breast.png' onclick='pic_change_quiz(2,2,3)'></img>\r"
		block=block+"<div class='block_1_text'>Stark Ost-West</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Die Brüste sind stark nach außen geneigt: 3 Finger</div>\r"
		block=block+"</div>\r"
		block=block+"<span class='stretch'></span>\r"
		



		block=block+"</div>\r"
		
				
		block=block+"</div>\r"
		block=block+"</div>\r"
		footer="<div class='button_zurueck_showroom' onclick='quiz_page_laden_zurueck("+parseInt(seite-1)+")'>Zurück</div>\r"
		footer=footer+"<div class='button_main_showroom'  onclick='quiz_upload("+parseInt(seite+1)+")'>Weiter</div>\r"
	}
	
	if(seite==5)
	{
		block=block+"<div class='headline_2_overlay'>5. Wie ist die Symmetrie der Brüste?</div><br><br><br>\r"
		block=block+"<div class='photo_showroom_1_overlay' >\r"
		block=block+"<div class='showroom_container'>\r"	
		
		block=block+"<div class='block_1'>\r"
		block=block+"<img  class='photo_showroom' src='/static/round_breast.png' onclick='pic_change_quiz(0,1,4)'></img>\r"
		block=block+"<div class='block_1_text'>Symmetrie</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Beide Brüste sind gleich groß</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_1'>\r"
		block=block+"<img  class='photo_showroom' src='/static/asymmetrical_breasts.png' onclick='pic_change_quiz(1,1,4)'></img>\r"
		block=block+"<div class='block_1_text'>Asymmetrie</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Eine Brust ist größer als die andere</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<span class='stretch'></span>\r"
		block=block+"</div>\r"
		
				
		block=block+"</div>\r"
		block=block+"</div>\r"
		footer="<div class='button_zurueck_showroom' onclick='quiz_page_laden_zurueck("+parseInt(seite-1)+")'>Zurück</div>\r"
		footer=footer+"<div class='button_main_showroom'  onclick='quiz_upload("+parseInt(seite+1)+")'>Weiter</div>\r"
	}
	
	if(seite==6)
	{
		
		
		
		block=block+"<div class='headline_2_overlay'>6. Wie sitzen deine Brüste?</div><br><br><br>\r"
		block=block+"<div class='photo_showroom_1_overlay'>\r"
		
		block=block+"<div class='showroom_container'>\r"	
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/gestuetzt.png' onclick='pic_change_quiz(0,2,5)'></img>\r"
		block=block+"<div class='block_1_text'>Brüste sind gestützt</div>\r"

		block=block+"</div>\r"
		
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/halb_gestuetzt.png' onclick='pic_change_quiz(1,2,5)'></img>\r"
		block=block+"<div class='block_1_text'>Brüste sind halb gestützt</div>\r"
	
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/nach_unten_geneigt.png' onclick='pic_change_quiz(2,2,5)'></img>\r"
		block=block+"<div class='block_1_text'>Brüste fallen nach unten ab</div>\r"

		block=block+"</div>\r"
		
		


		block=block+"<span class='stretch'></span>\r"
		block=block+"</div>\r"
		
				
		block=block+"</div>\r"
		block=block+"</div>\r"
		footer="<div class='button_zurueck_showroom' onclick='quiz_page_laden_zurueck("+parseInt(seite-1)+")'>Zurück</div>\r"
		footer=footer+"<div class='button_main_showroom'  onclick='quiz_upload("+parseInt(seite+1)+")'>Weiter</div>\r"
	}
	
	



	if(seite==7)
	{
		block=block+"<div class='headline_2_overlay'>7. Welche BH Größe und hast du?</div><br><br><br>\r"
		block=block+"<div class='photo_showroom_1_overlay' style='height:150px;'>\r"

		block=block+"Der bestsitzende BH ist von der Marke <select class='brand_selection' onclick='click_on_competitors()'></select><br>"

			block=block+"<div class='size_selection_group'>\r"
		block=block+"<div class='bund_group'>Bund</div>\r"
		block=block+"<div class='circle_band' onclick='band_click(this.id)' id='0' onmouseover='band_onmouseenter(0)' onmouseleave='band_onmouseleave()'><div class='band'>60</div></div>\r"
		block=block+"<div class='circle_band' onclick='band_click(this.id)' id='1' onmouseover='band_onmouseenter(1)' onmouseleave='band_onmouseleave()'><div class='band'>65</div></div>\r"
		block=block+"<div class='circle_band' onclick='band_click(this.id)' id='2' onmouseover='band_onmouseenter(2)' onmouseleave='band_onmouseleave()'><div class='band'>70</div></div>\r"
		block=block+"<div class='circle_band' onclick='band_click(this.id)' id='3' onmouseover='band_onmouseenter(3)' onmouseleave='band_onmouseleave()'><div class='band'>75</div></div>\r"
		block=block+"<div class='circle_band' onclick='band_click(this.id)' id='4' onmouseover='band_onmouseenter(4)' onmouseleave='band_onmouseleave()'><div class='band'>80</div></div>\r"
		block=block+"<div class='circle_band' onclick='band_click(this.id)' id='5' onmouseover='band_onmouseenter(5)' onmouseleave='band_onmouseleave()'><div class='band'>85</div></div>\r"
		block=block+"<div class='circle_band' onclick='band_click(this.id)' id='6' onmouseover='band_onmouseenter(6)' onmouseleave='band_onmouseleave()'><div class='band'>90</div></div>\r"
		block=block+"<div class='circle_band' onclick='band_click(this.id)' id='7' onmouseover='band_onmouseenter(7)' onmouseleave='band_onmouseleave()'><div class='band'>95</div></div>\r"
		block=block+"<div class='circle_band' onclick='band_click(this.id)' id='8' onmouseover='band_onmouseenter(8)' onmouseleave='band_onmouseleave()'><div class='band'>100</div></div>\r"
		block=block+"</div><br><br>\r"

			block=block+"<div class='size_selection_group'>\r"
		block=block+"<div class='bund_group'>Cup</div>\r"
		block=block+"<div class='circle_cup' onclick='cup_click(this.id)' id='0' onmouseover='cup_onmouseenter(0)' onmouseleave='cup_onmouseleave()'><div class='cup'>AA</div></div>\r"
		block=block+"<div class='circle_cup' onclick='cup_click(this.id)' id='1' onmouseover='cup_onmouseenter(1)' onmouseleave='cup_onmouseleave()'><div class='cup'>A</div></div>\r"
		block=block+"<div class='circle_cup' onclick='cup_click(this.id)' id='2' onmouseover='cup_onmouseenter(2)' onmouseleave='cup_onmouseleave()'><div class='cup'>B</div></div>\r"
		block=block+"<div class='circle_cup' onclick='cup_click(this.id)' id='3' onmouseover='cup_onmouseenter(3)' onmouseleave='cup_onmouseleave()'><div class='cup'>C</div></div>\r"
		block=block+"<div class='circle_cup' onclick='cup_click(this.id)' id='4' onmouseover='cup_onmouseenter(4)' onmouseleave='cup_onmouseleave()'><div class='cup'>D</div></div>\r"
		block=block+"<div class='circle_cup' onclick='cup_click(this.id)' id='5' onmouseover='cup_onmouseenter(5)' onmouseleave='cup_onmouseleave()'><div class='cup'>E</div></div>\r"
		block=block+"<div class='circle_cup' onclick='cup_click(this.id)' id='6' onmouseover='cup_onmouseenter(6)' onmouseleave='cup_onmouseleave()'><div class='cup'>F</div></div>\r"
		block=block+"<div class='circle_cup' onclick='cup_click(this.id)' id='7' onmouseover='cup_onmouseenter(7)' onmouseleave='cup_onmouseleave()'><div class='cup'>G</div></div>\r"
		block=block+"<div class='circle_cup' onclick='cup_click(this.id)' id='8' onmouseover='cup_onmouseenter(8)' onmouseleave='cup_onmouseleave()'><div class='cup'>H</div></div>\r"

		
		block=block+"</div><br><br>\r"		
		

			block=block+"<div class='size_selection_group'>\r"
		block=block+"<div class='bund_group'>Alter (optional)</div>\r"
		block=block+"<div class='circle_age' onclick='age_click(this.id)' id='0'><div class='age'>18-24</div></div>\r"
		block=block+"<div class='circle_age' onclick='age_click(this.id)' id='1'><div class='age'>25-34</div></div>\r"
		block=block+"<div class='circle_age' onclick='age_click(this.id)' id='2'><div class='age'>35-44</div></div>\r"
		block=block+"<div class='circle_age' onclick='age_click(this.id)' id='3'><div class='age'>45-54</div></div>\r"
		block=block+"<div class='circle_age' onclick='age_click(this.id)' id='4'><div class='age'>55-64</div></div>\r"
		block=block+"<div class='circle_age' onclick='age_click(this.id)' id='5'><div class='age'>65+</div></div>\r"

		
		block=block+"</div>\r"	

		block=block+"</div>\r"
		
		block=block+"<span class='stretch'></span>\r"
		
		
		
						

		

		
		
		footer="<div class='button_zurueck_showroom' onclick='quiz_page_laden_zurueck("+parseInt(seite-1)+")'>Zurück</div>\r"
		footer=footer+"<div class='button_main_showroom'  onclick='quiz_upload("+parseInt(seite+1)+")'>Weiter</div>\r"
	}	
	
	if(seite==8)
	{
		block=block+"<div class='headline_2_overlay'>8. Wie sitzt das Unterbrustband deines Lieblings-BHs?</div><br><br><br>\r"
		block=block+"<div class='photo_showroom_1_overlay'>\r"
		
		block=block+"<div class='showroom_container'>\r"	
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/round_breast.png' onclick='pic_change_quiz(0,3,6)'></img>\r"
		block=block+"<div class='block_1_text'>Unterbrustband engt ein</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Unterbrustband bekommst du nicht einfach auf den ersten Haken</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/leich_nach_aussen_breasts.png' onclick='pic_change_quiz(1,3,6)'></img>\r"
		block=block+"<div class='block_1_text'>Unterbrustband sitzt perfekt</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Unterbrustband sitzt parallel zum Boden und liegt eng am Körper an</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/east_west_breast.png' onclick='pic_change_quiz(2,3,6)'></img>\r"
		block=block+"<div class='block_1_text'>Unterbrustband sitzt etwas locker</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Da das Unterbrustband etwas locker sitzt, verrutscht der BH ein wenig</div>\r"
		block=block+"</div>\r"
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/east_west_breast.png' onclick='pic_change_quiz(3,3,6)'></img>\r"
		block=block+"<div class='block_1_text'>Unterbrustband sitzt sehr locker</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Da das Unterbrustband sehr locker sitzt, rutscht der BH den Rücken hoch</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<span class='stretch'></span>\r"
		



		block=block+"</div>\r"
		
				
		block=block+"</div>\r"
		block=block+"</div>\r"
		footer="<div class='button_zurueck_showroom' onclick='quiz_page_laden_zurueck("+parseInt(seite-1)+")'>Zurück</div>\r"
		footer=footer+"<div class='button_main_showroom'  onclick='quiz_upload("+parseInt(seite+1)+")'>Weiter</div>\r"
	}	


	if(seite==9)
	{
		block=block+"<div class='headline_2_overlay'>9. Wie sitzen die Cups deines Lieblings-BHs?</div><br><br><br>\r"
		block=block+"<div class='photo_showroom_1_overlay'>\r"
		
		block=block+"<div class='showroom_container'>\r"	
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/round_breast.png' onclick='pic_change_quiz(0,3,7)'></img>\r"
		block=block+"<div class='block_1_text'>Cup/ Bügel drücken ein</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Ränder des Cups bzw. die Bügel schneiden ein</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/leich_nach_aussen_breasts.png' onclick='pic_change_quiz(1,3,7)'></img>\r"
		block=block+"<div class='block_1_text'>Mittelsteg steht ab</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Mittelsteg zwischen Brüsten steht leicht ab</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/east_west_breast.png' onclick='pic_change_quiz(2,3,7)'></img>\r"
		block=block+"<div class='block_1_text'>Cups sitzen perfekt</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Ränder der Cups liegen an und Bügel umfassen die Brust vollständig</div>\r"
		block=block+"</div>\r"
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/east_west_breast.png' onclick='pic_change_quiz(3,3,7)'></img>\r"
		block=block+"<div class='block_1_text'>Ränder der Cups stehen ab</div>\r"
		block=block+"<div class='block_1_text_detailliert'>Ränder der Cups stehen ab bzw. werfen leichte Falten</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<span class='stretch'></span>\r"
		



		block=block+"</div>\r"
		
				
		block=block+"</div>\r"
		block=block+"</div>\r"
		footer="<div class='button_zurueck_showroom' onclick='quiz_page_laden_zurueck("+parseInt(seite-1)+")'>Zurück</div>\r"
		footer=footer+"<div class='button_main_showroom'  onclick='quiz_upload("+parseInt(seite+1)+")'>Weiter</div>\r"
	}	
	
	
	if(seite==10)
	{
		block=block+"<div class='headline_2_overlay'>Unsere Empfehlung für Größen und BH-Typ</div><br><br><br>\r"


		block=block+"<div class='photo_showroom_1_overlay'>\r"
		
		block=block+"<div class='showroom_container'>\r"	
		
		block=block+"<div class='block_2'>\r"
		block=block+"<img  class='photo_showroom' src='/static/round_breast.png'></img>\r"

		block=block+"</div>\r"
		
		
		block=block+"<div class='block_2'>\r"
		block=block+"<div class='block_1_text'>Größenempfehlung</div>\r"
		block=block+"<div class='block_1_text_detailliert'>"+empfehlungstext_sizing+"</div>\r"
		block=block+"</div>\r"
		
		
		block=block+"<div class='block_2'>\r"
		block=block+"<div class='block_1_text'>BH-Typempfehlung</div>\r"
		block=block+"<div class='block_1_text_detailliert'>"+empfehlungstext_type+"</div>\r"
		block=block+"</div>\r"
		block=block+"<span class='stretch'></span>\r"
		
		block=block+"<div class='button_main_showroom'  onclick='quiz_beenden_vorlauf("+parseInt(seite+1)+")'>Persönlichen Showroom ansehen</div>\r"


		block=block+"</div>\r"
		
				
		block=block+"</div>\r"
		block=block+"</div>\r"
		
		
		footer="<div class='button_zurueck_showroom' onclick='quiz_page_laden_zurueck("+parseInt(seite-1)+")'>Zurück</div>\r"
		footer=footer+"<div class='button_main_showroom'  onclick='quiz_beenden_vorlauf("+parseInt(seite+1)+")'>Persönlichen Showroom ansehen</div>\r"
	}	

	document.getElementById("showroom_headline").innerHTML=headline;
	document.getElementById("showroom_body").innerHTML=block;
	document.getElementById("showroom_footer").innerHTML=footer;
	if(seite>0)
	{
		document.getElementsByClassName ("button_main_showroom")[0].style.opacity=0.4
		document.getElementsByClassName ("button_main_showroom")[0].style.pointerEvents = "none";
	}

	if(seite==7)
	{
		brand_selection=""
		brand_selection=brand_selection+"<option></option>"	
		brand_selection=brand_selection+"<option>Aubade</option>"
		brand_selection=brand_selection+"<option>Beedees</option>"
		brand_selection=brand_selection+"<option>Bon Prix</option>"
		brand_selection=brand_selection+"<option>C&A</option>"
		brand_selection=brand_selection+"<option>Calvin Klein</option>"
		brand_selection=brand_selection+"<option>Chantelle</option>"
		brand_selection=brand_selection+"<option>DIM</option>"
		brand_selection=brand_selection+"<option>Esprit</option>"
		brand_selection=brand_selection+"<option>ETAM</option>"
		brand_selection=brand_selection+"<option>Felina</option>"		
		brand_selection=brand_selection+"<option>H&M</option>"		
		brand_selection=brand_selection+"<option>Hunkemöller</option>"
		brand_selection=brand_selection+"<option>Intimissimi</option>"	
		brand_selection=brand_selection+"<option>Oysho</option>"
		brand_selection=brand_selection+"<option>Passionata</option>"		
		brand_selection=brand_selection+"<option>Tezenis</option>"				
		brand_selection=brand_selection+"<option>Triumph</option>"	
		brand_selection=brand_selection+"<option>Victoria's Secret</option>"
		brand_selection=brand_selection+"<option>Andere</option>"
		document.getElementsByClassName("brand_selection")[0].innerHTML=brand_selection
		

		band_selection=""
		band_selection=band_selection+"<option></option>"	
		band_selection=band_selection+"<option>60</option>"	
		band_selection=band_selection+"<option>65</option>"	
		band_selection=band_selection+"<option>70</option>"
		band_selection=band_selection+"<option>75</option>"
		band_selection=band_selection+"<option>80</option>"
		band_selection=band_selection+"<option>85</option>"
		band_selection=band_selection+"<option>90</option>"
		band_selection=band_selection+"<option>95</option>"
		band_selection=band_selection+"<option>100</option>"
		band_selection=band_selection+"<option>105</option>"
		band_selection=band_selection+"<option>110</option>"
		band_selection=band_selection+"<option>115</option>"
		band_selection=band_selection+"<option>120</option>"

		document.getElementsByClassName("band_selection")[0].innerHTML=band_selection	



		cup_selection=""
		cup_selection=cup_selection+"<option></option>"	
		cup_selection=cup_selection+"<option>AA</option>"	
		cup_selection=cup_selection+"<option>A</option>"	
		cup_selection=cup_selection+"<option>B</option>"	
		cup_selection=cup_selection+"<option>C</option>"	
		cup_selection=cup_selection+"<option>D</option>"	
		cup_selection=cup_selection+"<option>E</option>"	
		cup_selection=cup_selection+"<option>F</option>"	
		cup_selection=cup_selection+"<option>G</option>"	
		cup_selection=cup_selection+"<option>H</option>"	
		cup_selection=cup_selection+"<option>I</option>"	
		cup_selection=cup_selection+"<option>J</option>"
		cup_selection=cup_selection+"<option>K</option>"		
		document.getElementsByClassName("cup_selection")[0].innerHTML=cup_selection		
		
		

	}
	
}


function click_checkbox(id)
{
	if(document.getElementsByClassName ("color_selection")[id].checked==true)
		document.getElementsByClassName ("color_selection")[id].checked=false
	else
		document.getElementsByClassName ("color_selection")[id].checked=true
		
	pic_change_quiz(id,3,1)
}









function band_click(id)
{
	i=0;
	if(id<=7)
	{
		while(i<=7)
		{	
			document.getElementsByClassName ("circle_band")[i].style.opacity=1.0;
			if(i==id)
			{
				document.getElementsByClassName ("circle_band")[i].style.border="2px solid #CC3366";
				band=document.getElementsByClassName ("band")[i].innerHTML 
				document.getElementsByClassName ("band")[8].style.color="";
				document.getElementsByClassName ("band")[8].style.fontWeight="";
			}
			else
				document.getElementsByClassName ("circle_band")[i].style.border="";
	
			i=i+1;
		}
	}
	else
	{
		
		band="Keine Angabe"
		band_onmouseleave();
		document.getElementsByClassName ("band")[id].style.color="#CC3366";
		document.getElementsByClassName ("band")[id].style.fontWeight="bold";
		
		i=0;
		while(i<=7)
		{			
			document.getElementsByClassName ("circle_band")[i].style.opacity=0.4;
			i=i+1;
		}
		
		
		
	}
	check_cup_band_clicked()
	
}


function band_onmouseenter(id)
{
	i=0;
	while(i<=7)
	{		
		if(i==id)
		{
			document.getElementsByClassName ("circle_band")[i].style.border="2px solid #CC3366";
			document.getElementsByClassName ("circle_band")[i].style.opacity=1.0
		}
		i=i+1;
	}
}


function band_onmouseleave()
{

	i=0;
	while(i<=7)
	{	
		if(band!="Keine Angabe")
		{
			
			document.getElementsByClassName ("circle_band")[i].style.border="2px solid #e6e6e6";
			if(band==document.getElementsByClassName ("band")[i].innerHTML)
				document.getElementsByClassName ("circle_band")[i].style.border="2px solid #CC3366";
				
			
		}
		else
		{
			document.getElementsByClassName ("circle_band")[i].style.border="2px solid #e6e6e6";
			document.getElementsByClassName ("circle_band")[i].style.opacity=0.4
		}
			
		i=i+1;
	}
}





function click_on_competitors()
{
	competitor_brand=document.getElementsByClassName("brand_selection")[0].value;
	competitor_band=document.getElementsByClassName("band_selection")[0].value;
	competitor_cup=document.getElementsByClassName("cup_selection")[0].value;
	
	if(competitor_brand!="" && competitor_band!="" && competitor_cup!="")
	{
		document.getElementsByClassName ("button_main_showroom")[0].style.opacity=1.0;
		document.getElementsByClassName ("button_main_showroom")[0].style.pointerEvents = "auto";		
	}
	else
	{
		document.getElementsByClassName ("button_main_showroom")[0].style.opacity=0.4;
		document.getElementsByClassName ("button_main_showroom")[0].style.pointerEvents = "none";			
	}	
}






function cup_click(id)
{
	i=0;
	if(id<=7)
	{
		while(i<=7)
		{	
			document.getElementsByClassName ("circle_cup")[i].style.opacity=1.0;
			if(i==id)
			{
				document.getElementsByClassName ("circle_cup")[i].style.border="2px solid #CC3366";
				cup=document.getElementsByClassName ("cup")[i].innerHTML 
				document.getElementsByClassName ("cup")[8].style.color="";
				document.getElementsByClassName ("cup")[8].style.fontWeight="";
			}
			else
				document.getElementsByClassName ("circle_cup")[i].style.border="";
	
			i=i+1;
		}
	}
	else
	{
		
		cup="Keine Angabe"
		cup_onmouseleave();
		document.getElementsByClassName ("cup")[id].style.color="#CC3366";
		document.getElementsByClassName ("cup")[id].style.fontWeight="bold";
		
		i=0;
		while(i<=7)
		{			
			document.getElementsByClassName ("circle_cup")[i].style.opacity=0.4;
			i=i+1;
		}
		
		
		
	}
	check_cup_band_clicked()
	
}


function cup_onmouseenter(id)
{
	i=0;
	while(i<=7)
	{		
		if(i==id)
		{
			document.getElementsByClassName ("circle_cup")[i].style.border="2px solid #CC3366";
			document.getElementsByClassName ("circle_cup")[i].style.opacity=1.0
		}
		i=i+1;
	}
}


function cup_onmouseleave()
{

	i=0;
	while(i<=7)
	{	
		if(cup!="Keine Angabe")
		{
			
			document.getElementsByClassName ("circle_cup")[i].style.border="2px solid #e6e6e6";
			if(cup==document.getElementsByClassName ("cup")[i].innerHTML)
				document.getElementsByClassName ("circle_cup")[i].style.border="2px solid #CC3366";
				
			
		}
		else
		{
			document.getElementsByClassName ("circle_cup")[i].style.border="2px solid #e6e6e6";
			document.getElementsByClassName ("circle_cup")[i].style.opacity=0.4
		}
			
		i=i+1;
	}
}


function check_cup_band_clicked()
{
	

	zaehler=0;

		
		if(cup!="")
			zaehler=zaehler+1
		if(band!="")
			zaehler=zaehler+1


	if(zaehler==2)
	{
		document.getElementsByClassName ("button_main_showroom")[0].style.opacity=1.0;
		document.getElementsByClassName ("button_main_showroom")[0].style.pointerEvents = "auto";		
	}
	else
	{
		document.getElementsByClassName ("button_main_showroom")[0].style.opacity=0.4;
		document.getElementsByClassName ("button_main_showroom")[0].style.pointerEvents = "none";			
	}
	
}

function age_click(id)
{
	i=0;

	while(i<=5)
	{	
		if(i==id)
		{
			document.getElementsByClassName ("circle_age")[i].style.border="2px solid #CC3366";
			age=document.getElementsByClassName ("age")[i].innerHTML 
		}
		else
			document.getElementsByClassName ("circle_age")[i].style.border="";

		i=i+1;
	}
	
}

function select_colors()
{
	
	if(color_0=="1")
		document.getElementsByClassName ("color_selection")[0].checked=true
	if(color_1=="1")
		document.getElementsByClassName ("color_selection")[1].checked=true
	if(color_2=="1")
		document.getElementsByClassName ("color_selection")[2].checked=true
	if(color_3=="1")
		document.getElementsByClassName ("color_selection")[3].checked=true	

	document.getElementsByClassName ("button_main_showroom")[0].style.opacity=1.0
	document.getElementsByClassName ("button_main_showroom")[0].style.pointerEvents = "auto";	
	
}

function select_cup_band_age()
{


	i=0;
	zaehler=0;
	document.getElementsByClassName("brand_selection")[0].value=competitor_brand;
	while(i<=7)
	{

		if(cup==document.getElementsByClassName ("cup")[i].innerHTML)
		{
			document.getElementsByClassName ("circle_cup")[i].style.border="2px solid #CC3366";
			zaehler=zaehler+1;
		}
		
		if(band==document.getElementsByClassName ("band")[i].innerHTML)
		{
			document.getElementsByClassName ("circle_band")[i].style.border="2px solid #CC3366";
			zaehler=zaehler+1;
		}
		
		if(i<=5)
			if(age==document.getElementsByClassName ("age")[i].innerHTML)
				document.getElementsByClassName ("circle_age")[i].style.border="2px solid #CC3366";
		i=i+1;
	}
	if(zaehler==2)
	{
		document.getElementsByClassName ("button_main_showroom")[0].style.opacity=1.0
		document.getElementsByClassName ("button_main_showroom")[0].style.pointerEvents = "auto";
	}	
	
}


function quiz_page_laden_zurueck(seite)
{

	quiz_page_laden(seite);
	if(seite==1)
		pic_change_quiz(stil,3,0)
	if(seite==2)
		select_colors();
	if(seite==3)
		pic_change_quiz(form,1,2)
	if(seite==4)
		pic_change_quiz(position,2,3)		
	if(seite==5)
		pic_change_quiz(symmetrie,1,4)	
	if(seite==6)
		pic_change_quiz(sitz,3,5)		
	if(seite==7)
		insert_cup_band_information()
	if(seite==8)
		pic_change_quiz(band_problems,3,6)
	if(seite==9)
		pic_change_quiz(cup_problems,3,7)
		

}

function pic_change_quiz(id,max,question)
{
	i=0;
	if(question!=1)
		while(i<=max)
		{	
			if(i==id)
			{
				//document.getElementsByClassName ("small_pictures_huelle_showroom")[i].style.backgroundColor="#CC3366";
				document.getElementsByClassName ("photo_showroom")[i].style.border="2px solid #CC3366";
				document.getElementsByClassName ("button_main_showroom")[0].style.opacity=1.0
				document.getElementsByClassName ("button_main_showroom")[0].style.pointerEvents = "auto";
			}
			else
				document.getElementsByClassName ("photo_showroom")[i].style.border="";
	
			i=i+1;
		}
	
	if(question==0)
		stil=id 
	if(question==1)
	{

		if(document.getElementsByClassName ("color_selection")[0].checked==true)
			color_0=1
		else
			color_0=0
			
		if(document.getElementsByClassName ("color_selection")[1].checked==true)
			color_1=1
		else
			color_1=0
			
		if(document.getElementsByClassName ("color_selection")[2].checked==true)
			color_2=1
		else
			color_2=0
			
		if(document.getElementsByClassName ("color_selection")[3].checked==true)
			color_3=1
		else
			color_3=0
			


	}
		

	if(question==2)
		form=id

	if(question==3)
		position=id	
	if(question==4)
		symmetrie=id	
	if(question==5)
		sitz=id	

	if(question==6)
		band_problems=id	

	if(question==7)
		cup_problems=id		
		
	if(question==1)
		if(color_0==1 || color_1==1 || color_2==1 || color_3==1)
		{
			document.getElementsByClassName ("button_main_showroom")[0].style.opacity=1.0
			document.getElementsByClassName ("button_main_showroom")[0].style.pointerEvents = "auto";


		}
		else
		{
			document.getElementsByClassName ("button_main_showroom")[0].style.opacity=0.4
			document.getElementsByClassName ("button_main_showroom")[0].style.pointerEvents = "none";
		}
	else
	{

	}
	 
}

function quiz_beenden_vorlauf()
{
	quiztaken="yes";

	quiz_beenden();
	
}


function quiz_beenden()
{
	if(cup=="Keine Angabe")
		cup_=""
	else
		cup_=cup
		
		
	if(band=="Keine Angabe")
		band_=""
	else
		band_=band
		
		
			$.ajax({
			type: "POST",
			url: "/quiz_beenden/",
			dataType: "json",
			data: {'stil':stil,'color_0':color_0,'color_1':color_1,'color_2':color_2,'color_3':color_3,'form':form,'position':position,'symmetrie':symmetrie,'sitz':sitz,'quiztaken':quiztaken,'cup':cup_,'band':band_,'age':age,'band_problems':band_problems,'cup_problems':cup_problems},
			success: function(data) {
				window.location.href="/overview/Mein Showroom"	
			}
		});
}

function quiz_upload(seite)
{
	
	
	if(seite==8)
		competitor_brand=document.getElementsByClassName("brand_selection")[0].value
	
		
	
			$.ajax({
			type: "POST",
			url: "/quiz_beenden/",
			dataType: "json",
			data: {'stil':stil,'color_0':color_0,'color_1':color_1,'color_2':color_2,'color_3':color_3,'form':form,'position':position,'symmetrie':symmetrie,'sitz':sitz,'quiztaken':quiztaken,'cup':cup,'band':band,'age':age,'competitor_brand':competitor_brand,'band_problems':band_problems,'cup_problems':cup_problems },
			success: function(data) {
				if(seite==10)
				{

					$.ajax({
					type: "POST",
					url: "/band_cup_recommendation/",
					dataType: "json",
					data: {"":"" },
					success: function(data) {
						data=JSON.parse(data);
						
						cup_recommendation=data[0].cup_recommendation
						band_recommendation=data[0].band_recommendation
						empfehlungstext_sizing=data[0].empfehlungstext_sizing
						empfehlungstext_type=data[0].empfehlungstext_type
						quiz_page_laden(seite)
					}
					})
				}
				else
				{
				
									
					quiz_page_laden(seite)
					if(seite==1)
						pic_change_quiz(stil,3,0)
					if(seite==2)
						select_colors();
					if(seite==3)
						pic_change_quiz(form,1,2)
					if(seite==4)
						pic_change_quiz(position,2,3)		
					if(seite==5)
						pic_change_quiz(symmetrie,1,4)		
					if(seite==6)
						pic_change_quiz(sitz,3,5)	
					if(seite==7)
						select_cup_band_age();		
					if(seite==8)
						pic_change_quiz(band_problems,3,6)				
					if(seite==9)
						pic_change_quiz(cup_problems,3,7)
				}
				
			}
		});
}