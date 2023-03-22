import csv
import Stock

def portfolio_cost(filename):
	#"Assignment\A2 Stock\portfolio.csv"
	res = 0
	for i in Stock.Get_PortPolio_List(filename):
		res += i.shares * i.price
	print(res)