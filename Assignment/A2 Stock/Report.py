import Stock

def portfolio_report(portfolio, price):
	#Assignment\A2 Stock\prices.csv
	#Assignment\A2 Stock\portfolio.csv
	stocklist = Stock.Get_PortPolio_List(portfolio)
	templist = Stock.Get_Price_List(price)
  
	for i in stocklist:
		for j in templist:
			if i.name == j.name:
				i.profit = j.price - i.price
				i.price = j.price
	Stock.printall(stocklist)