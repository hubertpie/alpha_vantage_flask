from flask import Flask, render_template, request
import alpha_data


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
	currency_list = alpha_data.currency_list()
	if request.method == 'POST':
		data = alpha_data.get_data(request.form['currency1'], request.form['currency2'])
		dates = [x[0] for x in data]
		ex_rate = [y[1] for y in data]
		return render_template('index.html', currency_list=currency_list, dates=dates, ex_rate=ex_rate)

	return render_template('index.html', currency_list=currency_list)