$(document).ready(function(){
	$('#live_currency_button').on('click', function(){
		var from_symbol = $('#from_currency_live').val();
		var to_currency = $('#to_currency_live').val();

		window.setInterval(function(){
		req = $.ajax({
			url: '/update',
			type: 'POST',
			data: {
					from_currency_live: from_symbol, 
					to_currency_live: to_currency
				}
		});

		req.done(function(data){
			$("#current").text("Current exchange rate: " + data.current_exchange_rate);
		});

		},30000);

	});

});