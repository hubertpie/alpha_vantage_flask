from flask import Flask, render_template, request
import alpha_data


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
	currency_list = alpha_data.currency_list()
	if request.method == 'POST':
		print(request.form['currency1'])
		print(request.form['currency2'])
		data = alpha_data.get_data(request.form['currency1'], request.form['currency2'])
		return render_template('index.html', data=data, currency_list=currency_list)

	return render_template('index.html', currency_list=currency_list)