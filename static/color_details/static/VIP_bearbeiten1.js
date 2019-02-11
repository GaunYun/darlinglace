function check_skip_button(skip,skip2)
{
	

	if(skip=="false")
	{
		document.getElementsByClassName("kauf_aussetzen_button")[0].style.opacity="0.3"
		document.getElementsByClassName("kauf_aussetzen_button")[0].style.pointerEvents = 'none';
	}
	if(skip2=="false")
	{
		document.getElementsByClassName("guthaben_rueckerstattung_button")[0].style.opacity="0.3"
		document.getElementsByClassName("guthaben_rueckerstattung_button")[0].style.pointerEvents = 'none';
	}
}




function kauf_aussetzen()
{
		$.ajax({
		type: "POST",
		url: "/hello/postpone_VIP/",
		dataType: "json",
		data: { "data":"" },
		success: function(data) {
			if(data=="not ok")
				alert_userdata("KEIN AUSSETZEN MEHR MÖGLICH","Leider ist die Frist zum Aufschieben des Kaufs abgelaufen. Versuche doch noch eine Rückerstattung zu erlangen.")
			else
			{
							
				get_data();

			}
			
		}
		})
	
}



function rueckerstattung_beantragen()
{
		$.ajax({
		type: "POST",
		url: "/hello/get_money_back_VIP/",
		dataType: "json",
		data: { "data":"" },
		success: function(data) {
			if(data=="not ok")
				alert_userdata("RÜCKERSTATTUNG NICHT MEHR MÖGLICH","Leider ist die Frist für die Rückerstattung des VIP Budgets vom letzten Monat abgelaufen. Schau dir doch unsere neusten Trends einmal an.")
			else
			{
							
				get_data();

			}
			
		}
		})
	
}



function get_data()
{
		$.ajax({
	type: "POST",
	url: "/hello/guthaben_abrufen/",
	dataType: "json",
	data: { "data":"" },
	success: function(data) {
		document.getElementsByClassName("vorhandenes_guthaben")[0].innerHTML="Vorhandenes Guthaben: "+data+" €"
		
				$.ajax({
				type: "POST",
				url: "/hello/check_skip_button/",
				dataType: "json",
				data: { "data":"" },
				success: function(data) {

							$.ajax({
							type: "POST",
							url: "/hello/check_rueckerstattung_button/",
							dataType: "json",
							data: { "data":"" },
							success: function(data_2) {
								check_skip_button(data,data_2)
							}
							
						})
				}
				
			})
			
	}
})
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
	
	window.location.href="/hello/account_page/";
}