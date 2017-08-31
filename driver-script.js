$(document).ready(function(){	
	$(".hamburger").click(function(){
		displaySide();
	});

	$(".cancel").click(function(){
		cancel();
	});







	function displaySide(){
		$("#wrapper").css({"display": "block"});
	}

	function cancel(){
		$("#wrapper").hide()
	}

});