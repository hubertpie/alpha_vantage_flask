from alpha_vantage.foreignexchange import ForeignExchange
import csv
import secrets

ts = ForeignExchange(key=secrets.API_KEY)

def get_historical_exchange_rate(curr_from, curr_to):
	data = ts.get_currency_exchange_daily(from_symbol=curr_from, to_symbol=curr_to, outputsize='compact')
	return [[x, data[0][x]['4. close']] for x in data[0]]
	
def currency_list():
	with open('physical_currency_list.csv') as csvfile:
		return [curr for curr in csv.reader(csvfile, delimiter=',')]

def get_current_exchange_rate(curr_from, curr_to):
	data = ts.get_currency_exchange_rate(from_currency=curr_from, to_currency=curr_to)
	return data[0]['5. Exchange Rate']