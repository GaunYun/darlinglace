var button_click;
var gutscheincode;

 // This is called with the results from from FB.getLoginStatus().
  function statusChangeCallback(response) {
	  
    console.log('statusChangeCallback');
    console.log(response);
    // The response object is returned with a status field that lets the
    // app know the current login status of the person.
    // Full docs on the response object can be found in the documentation
    // for FB.getLoginStatus().
    if (response.status === 'connected') {
      // Logged into your app and Facebook.
	 // alert(response.status)
	  facebook_einloggen()


    } else if (response.status === 'not_authorized') {
      // The person is logged into Facebook, but not your app.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into this app.';
    } else {
      // The person is not logged into Facebook, so we're not sure if
      // they are logged into this app or not.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into Facebook.';
    }
  }

  // This function is called when someone finishes with the Login
  // Button.  See the onlogin handler attached to it in the sample
  // code below.
  function checkLoginState() {

    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
	  //alert(response)
    });
  }
  


  window.fbAsyncInit = function() {

	  button_click=0
  FB.init({
    appId      : '1796917517246883',
    cookie     : true,  // enable cookies to allow the server to access 
                        // the session
    xfbml      : true,  // parse social plugins on this page
    version    : 'v2.8' // use graph api version 2.5
  });
  

  // Now that we've initialized the JavaScript SDK, we call 
  // FB.getLoginStatus().  This function gets the state of the
  // person visiting this page and can return one of three states to
  // the callback you provide.  They can be:
  //
  // 1. Logged into your app ('connected')
  // 2. Logged into Facebook, but not your app ('not_authorized')
  // 3. Not logged into Facebook and can't tell if they are logged into
  //    your app or not.
  //
  // These three cases are handled in the callback function.

  FB.getLoginStatus(function(response) {
	
	
    statusChangeCallback(response);
  });
  
     FB.Event.subscribe('auth.login', function () {
		  facebook_einloggen()
        //  window.location = "http://example.com";
      });

  };

  // Load the SDK asynchronously
  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));

  // Here we run a very simple test of the Graph API after login is
  // successful.  See statusChangeCallback() for when this call is made.

	
	
	function gutscheincode_laden_fb(code)
	{
		gutscheincode=code;
		
	}
	
	function fb_login() {
		
		

    FB.login( function() {}, { scope: 'email,public_profile' } );
	    console.log('Welcome!  Fetching your information.... ');
	FB.api('/me?fields=first_name,last_name,email,age_range,gender,locale,link', function(response) {
		
  button_click=1;
  facebook_einloggen()
    });
}



function facebook_einloggen()
{
	if (button_click==1)
	{
		FB.api('/me?fields=first_name,last_name,email,age_range,gender,locale,link', function(response) {


		$.ajax({
				type: "POST",
				url: "/hello/facebook_login/",
				dataType: "json",
				data: { "id":response.id,"vorname":response.first_name,"nachname":  response.last_name,"email":  response.email,"min_alter":response.age_range.min,"max_alter":response.age_range.max,"geschlecht":response.gender,"gutscheincode":gutscheincode},
				success: function(data) {

					if(data=="ok")
                        location.reload();
				}
				});
			 });
	}
			

}
  