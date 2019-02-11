function VIP_nicht_kuendigen()
{


				alert_userdata_redirect_account_page("DANKE","Genieße Deine VIP Vorteile weiter! Wenn wir irgendetwas für Dich tun können, melde Dich gerne. <br><br>Du kannst Dich immer auf uns verlassen, wenn Du hochwertige Lingerie zu tollen Preisen suchst. <br>xoxo")

	
}


function show_page_VIP_kuendigung()
{
		window.location= "https://www.darlinglace.com/account_page/VIP_bearbeiten/VIP_kuendigung/";

	
}


function VIP_kuendigen()
{
		page_load(0);	
		$.ajax({
		type: "POST",
		url: "/account_page/cancel_VIP/",
		dataType: "json",
		data: { "data":"" },
		success: function(data) {
				page_load(1);	

				alert_userdata_redirect_account_page("VIP-MITGLIEDSCHAFT GEKÜNDIGT","Du hast Deine VIP-Mitgliedschaft gekündigt.")

			
		}
		})
		
	
}



 







function check_skip_button(skip,skip2)
{
	

	if(skip=="true")
	{
		document.getElementsByClassName("kauf_aussetzen_button")[0].style.opacity="0.3"
		document.getElementsByClassName("kauf_aussetzen_button")[0].style.pointerEvents = 'none';
	}
	else
	{
		document.getElementsByClassName("kauf_aussetzen_button")[0].style.opacity="1"
		document.getElementsByClassName("kauf_aussetzen_button")[0].style.pointerEvents = 'auto';
	}		
	if(skip2==0)
	{
		document.getElementsByClassName("guthaben_rueckerstattung_button")[0].style.opacity="0.3"
		document.getElementsByClassName("guthaben_rueckerstattung_button")[0].style.pointerEvents = 'none';
	}
	else
	{
		document.getElementsByClassName("guthaben_rueckerstattung_button")[0].style.opacity="1"
		document.getElementsByClassName("guthaben_rueckerstattung_button")[0].style.pointerEvents = 'auto';		
	}
}







function kauf_aussetzen()
{
	
		button_logo("0","kauf_aussetzen_text","kauf_aussetzen_logo","kauf_aussetzen")
		page_load(0);	
		$.ajax({
		type: "POST",
		url: "/skip_VIP/",
		dataType: "json",
		data: { "data":"" },
		success: function(data) {
			page_load(1);	
			button_logo("1","kauf_aussetzen_text","kauf_aussetzen_logo","kauf_aussetzen")	
			if(data=="not ok")
				alert_userdata("KEIN AUSSETZEN MEHR MÖGLICH","Leider ist die Frist zum Aufschieben des Kaufs abgelaufen. Versuche doch noch eine Rückerstattung zu erlangen.")
			else
			{
							
				get_data(data);
				alert_userdata("AUSSETZEN ERFOLGREICH","Du hast erfolgreich deine VIP Käufe für diesen Monat pausiert. Schau dir doch im nächsten Monat unsere neusten Lingerie Trends an.")

			}
			
		}
		})
	
}



function rueckerstattung_beantragen()
{
		page_load(0);	
		button_logo("0","guthaben_rueckerstattung_text","guthaben_rueckerstattung_logo","guthaben_rueckerstattung")	
		$.ajax({
		type: "POST",
		url: "/get_money_back_VIP/",
		dataType: "json",
		data: { "data":"" },
		success: function(data) {
			page_load(1);	
			button_logo("1","guthaben_rueckerstattung_text","guthaben_rueckerstattung_logo","guthaben_rueckerstattung")	
			if(data!="not ok")
			{
							
				get_data(data);
				alert_userdata("RÜCKERSTATTUNG ERFOLGREICH","Wir werden Dir in den nächsten Tagen Dein VIP Guthaben zurücküberweisen.")

			}
			
		}
		})
	
}



function get_data(data)
{
		feedback=JSON.parse(data)
		document.getElementsByClassName("vorhandenes_guthaben")[0].innerHTML="Vorhandenes Guthaben: "+feedback[0].guthaben+" €"
		check_skip_button(feedback[0].check_skip_button,feedback[0].check_rueckerstattung_button)
}





function check_free_bras (bra_ordered,bras_for_free)
{

	i=0
	while(i<= bra_ordered-1)
	{
		
		document.getElementsByClassName("bra_img")[i].src="/static/bra_filled.png"
		i=i+1;

	}
	
	if(bras_for_free>=1)
		document.getElementsByClassName("anzahl")[0].innerHTML="Sets umsonst: "+bras_for_free+"x <img class='bra_img' src='/static/bra_filled.png' width='25' height='25'/>"
}

function profil_hauptseite()
{
	
	window.location.href="/account_page/";
}

function VIP_mitgliedschaft_bearbeiten()
{
	
	window.location.href="/account_page/VIP_bearbeiten/";
}


