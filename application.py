from flask import Flask, render_template, request
import alpha_data


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
	#data = alpha_data.get_data()
	return render_template('index.html', data=data)