var url_lingerie;
var cart, wishlist,lingerie_sidebar,login,links;


function warenkorb_abrufen(anzahl)
{
	cart_gesamt=0;
	i=0;
	while(i<=cart.length-1)
	{
		cart_gesamt=cart_gesamt+parseInt(cart[i].anzahl)
		i=i+1;	
	}


	
	if (cart_gesamt!=0)
	{			
		document.getElementsByClassName("cart_text")[0].innerHTML=cart_gesamt;
		document.getElementsByClassName("cart")[0].style.backgroundImage="url('/static/Cart-open.PNG')";

	}
	else
	{

		document.getElementsByClassName("cart_text")[0].innerHTML=" ";
		document.getElementsByClassName("cart")[0].style.backgroundImage="url('/static/Cart.PNG')";

	}

}


function wishlist_abrufen_anzahl(anzahl)
{

	wishlist_gesamt=0;
	i=0;
	while(i<=wishlist.length-1)
	{
		wishlist_gesamt=wishlist_gesamt+1
		i=i+1;	
	}



	if (wishlist_gesamt!=0)
	{			
		document.getElementsByClassName("text_wishlist")[0].innerHTML=wishlist_gesamt;


	}
	else
	{

		document.getElementsByClassName("text_wishlist")[0].innerHTML=" ";


	}

}


function show_cart()
{
	cart=JSON.parse(document.getElementsByClassName("warenkorb_daten")[0].innerHTML)
}

function load_wishlist()
{
	wishlist=JSON.parse(document.getElementsByClassName("wishlist")[0].innerHTML)

}

function login_click_schliessen()
{
	enableScroll();
	el.style.visibility = "hidden"
	document.getElementsByClassName ("overlay")[0].style.visibility = "hidden"
	document.getElementById("x-mask").style.opacity="1.0";

}

 function alert_userdata_registration_successful(content1,content2)
 {	 


	document.getElementById("alert_box_reload_headline").innerHTML=content1;

	document.getElementById("alert_box_reload_body").innerHTML=content2;
	$('#alert_box_reload').modal('show');
	$('#login').modal('hide');




 }
 
 $('#alert_box_reload').on('hide.bs.modal', function () {

  location.reload();

});
 
  function alert_userdata(content1,content2)
 {	 
	
	document.getElementById("alert_box_headline").innerHTML=content1;
	document.getElementById("alert_box_body").innerHTML=content2;
	$('#alert_box').modal('show');
 }

function load_registration_login()
{
	
	$.ajax({
	type: "GET",
	url: "/hello/check_log_in/",
	dataType: "json",
	data: { "data":""},
	success: function(data) {	
		
	
		if(data!="yes")
		{
				closeNav();
				$('#login').modal('show');
		}
		else
			location.reload();
	}
	})
}

function reset_header()
{

	hide_dropdown(0);

	hide_dropdown(1);

}

function reset_sidebar()
{

	if(document.getElementsByClassName ("modal_mobile_sidebar")[0].style.visibility == "visible")
		closeNav();

}


function load_header(login_)
{

	login=login_;

	show_cart();
	load_wishlist();


	
	var box="<div class='header_block_links'><div class='header_top_style_left' id='0' >Wie funktioniert Amoroso?</div><div class='header_top_style_left'>VIP Vorteile</div></div>\r";
	box=box+"<div class='mobile_menu' onclick='openNav()'>&nbsp;</div>"


	box=box+"<div class='header_block_rechts'>"
	box=box+"<div class='header_top_style_right'  onmouseenter='show_dropdown(0)' onmouseleave='hide_dropdown(0)'><div class='cart' onclick='warenkorb_aufrufen()'><div class='cart_text' ></div><div class='warenkorb_betitelung' style='text-align:center'>Warenkorb</div><div class='cart_overview_text_leer' >&nbsp;</div></div>"
	box=box+"<div class='dropdown_content' >"

	
	

	box=box+"</div>";
	
	box=box+"</div>";
	
	box=box+"<div class='header_top_style_right' onmouseenter='show_dropdown(1)' onmouseleave='hide_dropdown(1)'><div class='wishlist_overview' ><div class='text_wishlist' ></div><div class='wishlist_overview_text' onclick='wishlist_aufrufen()'>Wunschliste</div><div class='wishlist_overview_text_leer' onclick='wishlist_aufrufen()'>&nbsp;</div>"
	box=box+"<div class='dropdown_content'  style='margin-left:-10px'>"

	
	

	box=box+"</div>";
	
	box=box+"</div>";
	box=box+"</div>";
	if (login_=="true")
	{
		box=box+"<div class='header_top_style_right' onmouseenter='show_dropdown(2)' onmouseleave='hide_dropdown(2)'><div class='account_overview'> <div class='account_overview_text' onclick='account_aufrufen()'>Account</div><div class='account_overview_text_leer' onclick='account_aufrufen()'>&nbsp;</div>"
		box=box+"<div class='dropdown_content'>"
		box=box+"<div class='dropdown_content_account' onclick='account_aufrufen()'><div class='dropdown_content_account_overview' ><div class='dropdown_content_account_text' >Account Übersicht</div></div></div>"


		if(document.getElementsByClassName("bestellungen")[0].innerHTML!="[]")
		{
			
			box=box+"<div class='dropdown_content_account' onclick='bestellungen_bearbeiten()'><div class='dropdown_content_orders_overview' ><div class='dropdown_content_account_text' >Meine Bestellungen</div></div></div>"
			box=box+"<div class='dropdown_content_account' onclick='bestellung_zuruecksenden()'><div class='dropdown_content_exchanges_overview' ><div class='dropdown_content_account_text' >Rücksendungen</div></div></div>"
		}
		else
		{
			
			box=box+"<div class='dropdown_content_account' style='opacity:0.4;pointerEvents:none;cursor:initial;'><div class='dropdown_content_orders_overview' ><div class='dropdown_content_account_text' >Meine Bestellungen</div></div></div>"
			box=box+"<div class='dropdown_content_account' style='opacity:0.4;pointerEvents:none;cursor:initial;'><div class='dropdown_content_exchanges_overview' ><div class='dropdown_content_account_text' >Rücksendungen</div></div></div>"			
		}
		
		box=box+"<div class='dropdown_content_account' onclick='freunde_einladen()'><div class='dropdown_content_invite_friends_overview' ><div class='dropdown_content_account_text' >Freunde einladen</div></div></div>"			
		box=box+"<div class='dropdown_content_account' style='border-top:1px solid #e6e6e6' onclick='log_out()'><div class='dropdown_content_logout_overview' ><div class='dropdown_content_account_text' >Log-Out</div></div></div>"

		box=box+"</div></div></div>"
	}
	else
		box=box+"<div class='header_top_style_right' onclick='load_registration_login()'> <div class='dropdown_content_registrierung_overview' ><div class='registrierung_overview_text' >Registrierung/Login</div><div class='registrierung_overview_text_leer' >&nbsp;</div></div></div>"	
//<div class='header_top_style_right' onclick='log_out_aufrufen()'>Log-out</div>	

	
	box=box+"<div class='logo_huelle'><div class='header_logo'  onclick='logo_click()'/></div></div>\r"
	
	
	document.getElementsByClassName("header_top")[0].innerHTML=box;
	
	box=box+"<img class='header_logo' src='/static/logo_adore_me.png' /></img>\r"
	
	var box_bottom_1="<div class='box_links'><div><b>Sensuals</b></div><div id='ueber_uns' class='links_header' onclick='link_abrufen(this.id)'>Über uns</div><div>Presse</div><div id='impressum' class='links_header' onclick='link_abrufen(this.id)'>Impressum</div></div>";
	var box_bottom_2="<div class='box_links'><div><b>Produkt</b></div><div>Wie funktioniert VIP?</div><div>Freunde werben, erhalte 15€</div></div>";
	var box_bottom_3="<div class='box_links'><div><b>Hilfe & Support</b></div><div>FAQ</div><div>Konaktiere uns</div></div>";
	var box_bottom_4="<div class='box_links'><div><b>Join us</b></div><div>Jobs</div><div>Konaktiere uns</div><br><img class='logos' src='/static/facebook.png' /></img><img class='logos' src='/static/instagram.png' /></img><img class='logos' src='/static/twitter.png' /></img></div>";


	document.getElementsByClassName("header-bottom")[0].innerHTML="<div class='header_bottom_style'>"+box_bottom_1+box_bottom_2+box_bottom_3+box_bottom_4+"</div>";
	
	insert_cart_content_in_header()
	insert_wishlist_content_in_header()

}


function show_dropdown(id)
{

	if(window.innerWidth>=767)
		document.getElementsByClassName("dropdown_content")[id].style.display="block";

	
}

function hide_dropdown(id)
{
	if(window.innerWidth>=767)
		document.getElementsByClassName("dropdown_content")[id].style.display="none";
	
}


function link_abrufen(link_name)
{
	window.location.href="/hello/"+link_name
}

function wishlist_aufrufen()
{

	if(wishlist!="")
		window.location.href="/hello/overview/Wunschliste/"		
	
}


function insert_cart_content_in_header()
{
		i=0;
		box=""
	while(i<=cart.length-1)
	{

		box=box+"<div class='cart_dropdown'>"
	
		box=box+"<img src='"+cart[i].picture+"' class='cart_dropdown_picture' onclick='content_abrufen_cart("+i+")'/>"

		box=box+"<div style='margin-left:10px;float:left;	width:60px;font-size:12px;'><b>"+cart[i].style+"</b></div>"

		box=box+"<img class='schliessen_alert_cart' src='/static/x.png' width='7' onclick='cart_entfernen("+i+");' height='7'/></img>"

		
		box=box+"<br><div style='float:left;margin-left:10px;'>"+cart[i].bhgroesse+"</div> <br>"
		box=box+"<div style='float:left;margin-left:10px;'>"+cart[i].slipgroesse+"</div><br>"
		box=box+"<div style='float:left;margin-left:10px;'>Anz: "+cart[i].anzahl+"x</div><br><br>"
		


		box=box+"</div>";

		box=box+"<div class='linie_2'></div>"

		i=i+1;
	}
	
	if(cart.length-1>=0)
		box=box+"<div style='line-height:10px'><br><div class='get_to_cart' onclick='warenkorb_aufrufen()'>Zum Warenkorb</div><br></div>"

	
	document.getElementsByClassName("dropdown_content")[0].innerHTML=box;
	warenkorb_abrufen()
}


function insert_wishlist_content_in_header()
{
		i=0;
		box=""

	while(i<=wishlist.length-1)
	{

		
		box=box+"<div class='wishlist_dropdown'>"
	
		box=box+"<img src='"+wishlist[i].picture+"' class='wishlist_dropdown_picture' onclick='content_abrufen_wishlist("+i+")'/>"

		box=box+"<div style='margin-left:10px;float:left;	width:60px;font-size:12px;'><b>"+wishlist[i].name+"</b></div>"

		box=box+"<img class='schliessen_alert_cart' src='/static/x.png' width='7' onclick='wishlist_entfernen("+i+");' height='7'/></img>"

		box=box+"<br><br><br><br><br></div>";

		box=box+"<div class='linie_2'></div>"

		i=i+1;
	}
	
	if(wishlist.length-1>=0)
		box=box+"<div style='line-height:10px'><br><div class='get_to_cart' onclick='wishlist_aufrufen()'>Zur Wunschliste</div><br></div>"

	
	document.getElementsByClassName("dropdown_content")[1].innerHTML=box;
	wishlist_abrufen_anzahl()

}

function wishlist_entfernen(id)
{
	j=0;
	id2=-1
	while(j<=lingerie_selection.length-1)
	{

		if(wishlist[id].name==lingerie_selection[j].name)
			id2=j
		j=j+1;
	}
	
	if(id2>=0)
		wishlist_abrufen(id2)
		
}

function cart_entfernen(id)
{

		$.ajax({
			type: "GET",
			url: "/hello/add/",
			dataType: "json",
			data: { "add_or_erase":"change","anzahl":0,"gerichtname": cart[id].style,"stylecode": cart[id].stylecode,"colorcode": cart[id].colorcode,"bh_groesse": cart[id].bhgroesse,"slip_groesse": cart[id].slipgroesse  },
			success: function(data) {	

				cart=JSON.parse(data)

				insert_cart_content_in_header()
			
			}
			
		})
		
}



function cart_entfernen(id)
{

		$.ajax({
			type: "GET",
			url: "/hello/add/",
			dataType: "json",
			data: { "add_or_erase":"change","anzahl":0,"gerichtname": cart[id].style,"stylecode": cart[id].stylecode,"colorcode": cart[id].colorcode,"bh_groesse": cart[id].bhgroesse,"slip_groesse": cart[id].slipgroesse  },
			success: function(data) {	

				cart=JSON.parse(data)

				insert_cart_content_in_header()
			
			}
			
		})
		
}


 function links_laden(url)
 {



	if(document.getElementsByClassName("links")[0].innerHTML!="Dein Profil")
 		links=JSON.parse(document.getElementsByClassName("links")[0].innerHTML);
 	else
 		links=JSON.parse(document.getElementsByClassName("links")[1].innerHTML);

 	i=0;
 	box="<div style='margin-left:10px;float:left;'>"
 	url_lingerie="Wunschliste"
	while (i<=links.length-1)
	{
		if (i==url)
		{
			
 			box=box+"<div class='link_gruppen' onclick='content_abrufen("+i+")' onmouseenter='link_markieren("+i+")'>"+links[i].name+"</div>"
 			url_lingerie=links[i].name
 		}
 		else
 			box=box+"<div class='link_gruppen' onclick='content_abrufen("+i+")' onmouseenter='link_markieren("+i+")' onmouseleave='link_entmarkieren("+i+")'>"+links[i].name+"</div>"
 		i=i+1;
 	}
 	
 	box=box+"</div>"
 	

	if(url!=-1)
	{
	 	document.getElementsByClassName("sidebar_content")[0].innerHTML=box
	
		if(url!="None")
	 		link_markieren(url)
	 }

 }
 
 
 function bestellungen_bearbeiten()
{
	
	window.location.href="/hello/account_page/bestellungen_ansehen";
}

function bestellung_zuruecksenden()
{
	
	window.location.href="/hello/account_page/bestellung_zuruecksenden";
}

function freunde_einladen()
{
	
	window.location.href="/hello/account_page/freunde_einladen";
}


 
 function link_markieren(url)
 {


 		document.getElementsByClassName("link_gruppen")[url].style.color="#DB7093";
 		document.getElementsByClassName("link_gruppen")[url].style.borderBottom="2px solid #DB7093";
 		

 		
 	
 }
 
  function link_entmarkieren(url)
 {


	document.getElementsByClassName("link_gruppen")[url].style.color="#4E4E4E";
	document.getElementsByClassName("link_gruppen")[url].style.borderBottom="";

 		
 	
 }


  function content_abrufen_cart(i)
 {

		window.location.href="/hello/overview/"+url_lingerie+"/"+cart[i].style		
 }
 
  
 
  function content_abrufen_wishlist(i)
 {
		window.location.href="/hello/overview/"+url_lingerie+"/"+wishlist[i].name		
 }
 
 
 function content_abrufen(i)
 {

 	if(links[i].name=="Mein Showroom" && links[i].group1=="no")
 		quiz_laden();

	else
		window.location.href="/hello/overview/"+links[i].name		
 }




function kollektion_abrufen()
{
	i=0;
	while(i<=document.getElementsByClassName("link_gruppen").length-1)
	{
		if(document.getElementsByClassName("link_gruppen")[i].style.borderBottom!="")
			link=i
		
		i=i+1;
	}

		$.ajax({
		type: "GET",
		url: "/hello/kollektion_abrufen/",
		dataType: "json",
		data: {  "group":lingerie_selection[0].productgroup,"link":links[link].name },
		success: function(data) {			
			window.location= "/hello/overview/"+data+"/";


		}
	});

}


function account_aufrufen()
{
	window.location= "/hello/account_page/";
}

function logo_click()
{
	window.location= "/hello/start_page/";
}

function login_aufrufen()
{
	window.location= "/hello/start/";
}


function log_out()
{

	window.location= "/hello/log_out/";
}

function warenkorb_aufrufen()
{

	if(document.getElementsByClassName("cart_text")[0].innerHTML>0)
		window.location.href= "/hello/checkout/";
}


 
 function check_vollstaendigkeit()
 {
	 if(document.getElementById("username").value=="" || document.getElementById("passwort").value=="")
		  document.getElementById("eingabe_fehler").innerHTML="Bitte E-Mail Adresse und Passwort angeben";
	  else
		  return true		 
	 
 }
 
 
 function passwort_lang_genug()
 {

	 if(document.getElementById("passwort").value.length<6)
		  document.getElementById("eingabe_fehler").innerHTML="Das Passwort muss mindestens 6 Stellen haben";
	  else
		  return true
	 
	 
 }
 
 function eingabe_fehler_herausnehmen()
 {
	 document.getElementById("eingabe_fehler").innerHTML="";
 }
 

 
 
 function register()
 {
	 
	 if (check_vollstaendigkeit())
	 {
		if(passwort_lang_genug())
		{
			
			login_logo(0,"registrierung_text","registrierung_logo","registrierung")

			document.getElementsByClassName("login")[0].style.pointerEvents = 'none';
			document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'none';


			 $.ajax({
				type: "POST",
				url: "/hello/updater_user_registration/",
				dataType: "json",
				data: { "item": document.getElementById("username").value+","+document.getElementById("passwort").value},
				success: function(data) {

					if(data=="exists already")
					{
						document.getElementById("eingabe_fehler").innerHTML="Ein User mit dieser E-Mail Adresse existiert bereits"
						login_logo(1,"registrierung_text","registrierung_logo","registrierung")
						document.getElementsByClassName("login")[0].style.pointerEvents = 'auto';
						document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';

					}
					else	
					{
						if(data=="email falsch")
						{
							document.getElementById("eingabe_fehler").innerHTML="Bitte eine gültige E-Mail Adresse angeben";
							login_logo(1,"registrierung_text","registrierung_logo","registrierung")
							document.getElementsByClassName("login")[0].style.pointerEvents = 'auto';
							document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';

						}
						else
							if(data!="")
							{

								alert_userdata_registration_successful("ERFOLGREICH ANGEMELDET","Du hast dich erfolgreicht registriert.")

							}

				
						

							
					}
				}
			}); 
		}
	 }
 }
 
 
 function login_logo(index,text_area,logo_area,button_)
 {
	 
	 if (index==0)
	 {
		document.getElementsByClassName(""+text_area+"")[0].style.display="none";
		document.getElementsByClassName(""+logo_area+"")[0].style.display="block";

		document.getElementsByClassName(""+button_+"")[0].style.pointerEvents = 'none';
		

		
	 }
	 else
	 {
		document.getElementsByClassName(""+text_area+"")[0].style.display="block";
		document.getElementsByClassName(""+logo_area+"")[0].style.display="none";	
		document.getElementsByClassName(""+button_+"")[0].style.pointerEvents = 'auto';
		
		 
	 }
	 
 }
 
 
 
  function login_user()
 {	
 
	

	
	 if (check_vollstaendigkeit())
	 {

		 login_logo(0,"login_text","login_logo","login")
		document.getElementsByClassName("registrierung")[0].style.pointerEvents = 'none';
		document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'none';
		
		
		$.ajax({
			type: "GET",
			url: "/hello/check_log_in/",
			dataType: "json",
			data: { "data":""},
			success: function(data) {	
			
				if(data!="yes")
				{

						 $.ajax({
							type: "POST",
							url: "/hello/login_user/",
							dataType: "json",
							data: { "item": document.getElementById("username").value+","+document.getElementById("passwort").value },
							success: function(data) {
				
								
						
				
					
								if(data=="wrong data")
								{
				
									document.getElementById("eingabe_fehler").innerHTML="Bitte überprüfe noch einmal Deine E-Mail Adresse und Dein Passwort.";
									login_logo(1,"login_text","login_logo","login")
									document.getElementsByClassName("registrierung")[0].style.pointerEvents = 'auto';
									document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';
				
								}
								else			
								{
									location.reload();
								}
								
				
				
				
							},
							failure: function(data){
								login_logo(1,"login_text","login_logo","login")
								document.getElementsByClassName("registrierung")[0].style.pointerEvents = 'auto';
								document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';
				
								
							}
						});
			}
			else
				location.reload();
			}
		});
	 }
}
function openNav() {

		disableScroll();




	
	open_sidebar_main();
	


}

function closeNav() {

		enableScroll();
    document.getElementById("mySidenav").style.width = "0";
	document.getElementsByClassName ("overlay")[0].style.visibility = "hidden"
	
	document.getElementById("x-mask").style.opacity="1.0";

	document.getElementsByClassName ("modal_mobile_sidebar")[0].style.visibility = "hidden";

}


function open_sidebar_main(){

	block=""
	block=block+"<input class='search_field' name='search' placeholder='Suchen..' onfocus='search_field_sidebar()'>"
	block=block+"<div class='main_group_shopping' onlick='logo_click'>Shopping</div>"
	
	i=0;

	while (i<=links.length-1)
	{

		if (url_lingerie==links[i].name)
			block=block+"<div class='sub_group' onclick='content_abrufen("+i+")' ><b>"+links[i].name+"</b></div>"
 		else
 			block=block+"<div class='sub_group' onclick='content_abrufen("+i+")' >"+links[i].name+"</div>"
 		i=i+1;
 	}

	block=block+"<div class='main_group_wishlist' onclick='wishlist_aufrufen()'>Meine Wunschliste</div>"
	block=block+"<div class='linie_1'></div>"

	if(login=="true")
	{

		block=block+"<div class='main_group_account' onclick='account_aufrufen()'>Account</div>"
		block=block+"<div class='sub_group' onclick='account_aufrufen()'>Account Übersicht</div>"
		

		if(document.getElementsByClassName("bestellungen")[0].innerHTML!="[]")
		{
			block=block+"<div class='sub_group' onclick='bestellungen_bearbeiten()'>Meine Bestellungen</div>"
			block=block+"<div class='sub_group' onclick='bestellung_zuruecksenden()'>Rücksendungen</div>"
		}
		else
		{
			box=box+"<div class='dropdown_content_account' style='opacity:0.4;pointerEvents:none;cursor:initial;'><div class='dropdown_content_orders_overview' ><div class='dropdown_content_account_text' >Meine Bestellungen</div></div></div>"
			box=box+"<div class='dropdown_content_account' style='opacity:0.4;pointerEvents:none;cursor:initial;'><div class='dropdown_content_exchanges_overview' ><div class='dropdown_content_account_text' >Rücksendungen</div></div></div>"			
		}

		block=block+"<div class='linie_1'></div>"
		block=block+"<div class='main_group_log_out' onclick='log_out()'>Log-Out</div>"
	}
	else
	{
		block=block+"<div class='main_group_account' onclick='load_registration_login()'>Login/ Registrierung</div>"
	}
	block=block+"<div class='main_group_help'>Hilfe</div>"
	
	document.getElementById("mySidenav").innerHTML =block;
    document.getElementById("mySidenav").style.width = "250px";

	document.getElementsByClassName ("overlay")[0].style.visibility = "visible";


	
	document.getElementById("x-mask").style.opacity="0.4";


	document.getElementsByClassName ("modal_mobile_sidebar")[0].style.visibility = "visible";
}
	

	
	
	
function full_text_search()
{

			 $.ajax({
			type: "GET",
			url: "/hello/full_text_search/",
			dataType: "json",
			data: { "search_item": document.getElementById("searchbox").value  },
			success: function(data) {


					load_lingerie_sidebar(data)

				
			},
			error:function() {

					load_lingerie_sidebar("")

				
			}
			
			})
	
}


function load_lingerie_sidebar(data)
{
	lingerie_sidebar=data
	 var pics =[]
	 zaehler=0;
	 box=""

	i=0;
	 while(i<=lingerie_sidebar.length-1)
	 {
		var arr1 = lingerie_sidebar[i].pic.split(",");	
		for (j = 0; j < arr1.length; j++) {
			pics[j]=arr1[j].split(",");
		}  
		if(zaehler==0)
			box=box+"<div class='block'>\r";
		box=box+"<div class='box_1_small_image'><div><img class='image_box' src='"+pics[0]+"' onclick='detail_page_sidebar("+i+")'></img></div><div class='box_erste_ebene'><div class='gericht_auswahl_text' >"+lingerie_sidebar[i].name+"</div></div></div>\r";
		zaehler=zaehler+1;
			
		if(zaehler>=4)
		{
			box=box+"<span class='stretch'></span></div>\r"
			zaehler=0;
		}
		i=i+1;
	}

	document.getElementById("lingerie_sidebar").innerHTML =box;
}
	
	
	 function detail_page_sidebar(i)
 {

 	window.location.href=lingerie_sidebar[i].name;
 }
	
function search_field_sidebar(){
	enableScroll();
	    document.getElementById("mySidenav").style.width = "100%";
	block=""
	block=block+"<input type='text' id='searchbox' name='search' placeholder='Suchen..' autofocus='autofocus' style='width:80%;margin-left:10px;' oninput='full_text_search()'><img class='schliessen_searchbox' src='/static/x.png' width='15' onclick='close_searchbox_mobile()' height='15'/></img><br><br><div id='lingerie_sidebar'></div>"
	
	document.getElementById("mySidenav").innerHTML =block;	

}


function close_searchbox_mobile()
{
	
	
	openNav();	

}
	
	
	
	function password_check(passwort)
{
	

	if (passwort=="not ok")
	{


		box=""
		box=box+"<img class='schliessen_alert' src='/static/x.png' width='15' onclick='logo_click();' height='15'/></img><br><b><p style='text-align:center'>PASSWORT FESTLEGEN</b></p>";
		box=box+"<p style='margin-left:10px;margin-right:10px;font-size:14px;'>Bevor das Profil angepasst werden kann, muss zunächst ein Passwort für das Profil festgelegt werden.</p><br>";
		box=box+"<div class='button_alert_passwort'  onclick='passwort_bearbeiten()' >Passwort bearbeiten</button>";

		disableScroll();

		document.getElementsByClassName ("modal_medium")[0].innerHTML=box;
		document.getElementsByClassName("modal_medium")[0].style.visibility = "visible"
		document.getElementsByClassName ("overlay")[0].style.visibility = "visible"

		

		document.getElementById("x-mask").style.opacity="0.4";
		

	
	
	}
	

}


function passwort_bearbeiten()
{
	
		window.location.href="/hello/account_page/passwort_bearbeiten/";
}

function quiz_laden()
{


					$('#showroom').modal('show');
				
					 quiz_page_initialize()
					//quiz_page_laden(0)


	
}

 function alert_click_schliessen() {
	document.getElementsByClassName ("modal")[0].style.visibility = "hidden"
	document.getElementsByClassName ("overlay")[0].style.visibility = "hidden"
	document.getElementById("x-mask").style.opacity="1.0";
	enableScroll();
}




