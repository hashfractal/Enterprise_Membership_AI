# portfolio.py

import fileparse
import stock

class Portfolio:
		def __init__(self):
				self._holdings = []

		@classmethod
		def from_csv(cls, lines, **opts):
				self = cls()
				portdicts = fileparse.parse_csv(lines, 
																				select=['name','shares','price'], 
																				types=[str,int,float],
																				**opts)

		# your code here after making stock class using portdicts
				self._holdings = portdicts
				return self

		def append(self, holding: stock):
		# your code here
			self._holdings.append(holding)

		@property
		def total_cost(self):
			res = 0
			
		# your code here  
			
		def __iter__(self):
				return self._holdings.__iter__()

'''


		def __len__(self):
				return len(self._holdings)

		def __getitem__(self, index):
				return self._holdings[index]

		def __contains__(self, name):
				return any(s.name == name for s in self._holdings)

 

		def tabulate_shares(self):
				from collections import Counter
				total_shares = Counter()
				for s in self._holdings:
						total_shares[s.name] += s.shares
				return total_shares
'''


				
