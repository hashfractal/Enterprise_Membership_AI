import csv

class Stock:
	
	def __init__(self, name, shares, price):
		self.name = name
		self.shares = int(shares)
		self.price = float(price)
		self.profit = 0
	
	def sell():
		return None
	def cost():
		return None
	
def printall(stocklist):
	print("%5s| %10s| %10s| %10s| %10s|" % ("Name", "Shares", "Price", "Profit", "Total"))
	for i in stocklist:
		print("%5s| %10d| %10.2f| %10.2f| %10.2f|" % (i.name, i.shares, i.price, i.profit, i.shares * i.price))
  
def updatestock(stocklist):
	templist = []
	temp = csv.reader(open("Assignment\A2 Stock\prices.csv"))
	for i in temp:
		if len(i) != 0:
			tempstock = Stock(i[0], 0, float(i[1]))
			templist.append(tempstock)
		
	for i in stocklist:
		for j in templist:
			if i.name == j.name:
				i.profit = j.price - i.price
				i.price = j.price
			
def Get_PortPolio_List(portfolio):
	stocklist = []
	temp = csv.reader(open(portfolio))
	for i in temp:
		if i == ["name", "shares", "price"]:
			continue
		stock = Stock(i[0], i[1], i[2])
		stocklist.append(stock)
	return stocklist
  
def Get_Price_List(price):
	templist = []
	temp = csv.reader(open(price))
	for i in temp:
		if len(i) != 0:
			tempstock = Stock(i[0], 0, float(i[1]))
			templist.append(tempstock)
	return templist