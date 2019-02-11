$(document).ready(function() {



    // AJAX POST
    $('.add-todo').click(function(){

      console.log('am i called');
	alert("asd");
        $.ajax({
            type: "POST",
            url: "/polls/hello/add/",
            dataType: "json",
            data: { "item": $(".todo-item").val() },
            success: function(data) {
	
                alert(data.message);
            }
        });

    });





});
