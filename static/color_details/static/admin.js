var links;
function admin_uebersicht()
{
	links=JSON.parse(document.getElementsByClassName("links_data")[0].innerHTML)		
	
	i=0;
	block=""
	
	while(i<=links.length-1)
	{
		block=block+"<div class='links' onclick='open_link("+i+")'>"+links[i].linkname+"</div>"
		
		
		i=i+1;	
	}
	
	document.getElementById("links").innerHTML=block;
}


function open_link(i)
{
	
	 		$.ajax({
		type: "GET",
		url: "/admin/uebersicht/"+links[i].link+"/",
		dataType: "json",
		data: { "":""},
		success: function(data) {

				alert("Successful")

 		}
 	})

	
	
}