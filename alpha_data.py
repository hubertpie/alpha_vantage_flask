from alpha_vantage.timeseries import TimeSeries
import csv
import secrets

ts = TimeSeries(key=secrets.API_KEY)

# Just for test Key
def get_data():
	return ts.get_intraday('GOOGL')

def currency_list():
	with open('physical_currency_list.csv') as csvfile:
		return [curr for curr in csv.reader(csvfile, delimiter=',')]
