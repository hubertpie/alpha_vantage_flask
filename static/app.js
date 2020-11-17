$(document).ready(function(){
	$('#live_currency_button').on('click', function(){
		console.log("klikniety")
		var from_symbol = $('#from_symbol').val();
		var to_symbol = $('#to_symbol').val();

		window.setInterval(function(){
			req = $.ajax({
			url: '/update',
			type: 'POST',
			data: {from_currency: from_symbol, to_currency: to_symbol}
	
		});

		req.done(function(data){
			var currentdate = new Date();
			console.log(currentdate.getTime())
			$("#current").text("Current exchange rate: " + data.current_exchange_rate);
		});
		}, 10000);

	});

});