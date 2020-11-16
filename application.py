from flask import Flask, render_template, request
import alpha_data


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
	currency_list = alpha_data.currency_list()
	if request.method == 'POST':
		historical_exchange_rate = alpha_data.get_historical_exchange_rate(request.form['currency1'], request.form['currency2'])
		current_exchange_rate = alpha_data.get_current_exchange_rate(request.form['currency1'], request.form['currency2'])
		dates = [x[0] for x in historical_exchange_rate]
		ex_rate = [y[1] for y in historical_exchange_rate]
		return render_template('index.html', currency_list=currency_list, dates=dates, ex_rate=ex_rate, current_exchange_rate=current_exchange_rate)

	return render_template('index.html', currency_list=currency_list)