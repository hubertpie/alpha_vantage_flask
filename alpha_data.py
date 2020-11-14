from alpha_vantage.foreignexchange import ForeignExchange
import csv
import secrets

ts = ForeignExchange(key=secrets.API_KEY)

def get_data(curr_from, curr_to):
	return ts.get_currency_exchange_daily(from_symbol=curr_from, to_symbol=curr_to, outputsize='full')

def currency_list():
	with open('physical_currency_list.csv') as csvfile:
		return [curr for curr in csv.reader(csvfile, delimiter=',')]
