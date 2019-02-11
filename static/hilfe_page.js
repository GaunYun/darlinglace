function open_email()
{

	 document.getElementsByClassName("eingabefelder_headline")[0].value="";
	 document.getElementsByClassName("eingabefelder_textarea")[0].value="";

	$('#alert_box_email').modal('show');	
}


function send_email_support()
{
	button_logo("0","helpdesk_open_text","helpdesk_open_logo","helpdesk_open")	
		$.ajax({
				timeout:15000,
	 			error: function(){	
	 							button_logo("1","helpdesk_open_text","helpdesk_open_logo","helpdesk_open")	
						},
		type: "GET",
		url: "/send_email_support/",
		dataType: "json",
		data: { "von":  document.getElementsByClassName("input_eingabefelder_help")[0].value,"email":  document.getElementsByClassName("input_eingabefelder_help")[1].value,"betreff":  document.getElementsByClassName("input_eingabefelder_help")[2].value,"message":document.getElementsByClassName("eingabefelder_textarea")[0].value},
		success: function(data) {
			button_logo("1","helpdesk_open_text","helpdesk_open_logo","helpdesk_open")	
			document.getElementById("alert_box_headline").innerHTML="E-MAIL VERSANDT";
			document.getElementById("alert_box_body").innerHTML="Deine E-Mail an unser Support-Team wurde versandt. Wir melden uns schnellstmöglich bei Dir!";
				$('#alert_box_email').modal('hide');	

			$('#alert_box').modal('show');
		}
		
		})
}


function open_chat()
{

	$zopim.livechat.window.show();
}

function call_support()
{

	window.open('tel: 00493058849584');
}


function open_help_center()
{
	window.location=document.getElementsByClassName("help_center")[0].value
	
}