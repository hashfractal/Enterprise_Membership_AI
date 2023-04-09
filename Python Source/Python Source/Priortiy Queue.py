from typing import Self
from heap import *

class PriorityQueue:

	def __init__ (self):
		self.storage = Heap()

	def push(self, args):
		self.storage.insert(args)

	def pop(self):
		return self.storage.deleteMax()

	def prt(self):
		self.storage.heapPrint()


if __name__ == "__main__":
	pq = PriorityQueue()
	pq.push(7)
	pq.push(5)
	pq.push(9)
	pq.push(1)
	pq.push(3)
	pq.prt()
	print("pop: ", pq.pop())
	pq.prt()
