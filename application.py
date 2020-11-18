from flask import Flask, render_template, request, jsonify
import alpha_data


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
	currency_list = alpha_data.currency_list()
	if request.method == 'POST':
		from_symbol = request.form['from_symbol']
		to_symbol = request.form['to_symbol']
		historical_exchange_rate = alpha_data.get_historical_exchange_rate(from_symbol, to_symbol)
		dates = [x[0] for x in historical_exchange_rate]
		ex_rate = [y[1] for y in historical_exchange_rate]
		return render_template('index.html', currency_list=currency_list, dates=dates, ex_rate=ex_rate, from_symbol=from_symbol, to_symbol=to_symbol)

	return render_template('index.html', currency_list=currency_list)


@app.route("/update", methods=['POST'])
def update():
	from_symbol = request.form['from_currency_live']
	to_symbol = request.form['to_currency_live']	
	current_exchange_rate = alpha_data.get_current_exchange_rate(from_symbol, to_symbol)
	return jsonify({'result': 'success', 'current_exchange_rate': current_exchange_rate})