from Single_Linked_List import *

class ChainedHashTable:
	def __init__(self, n):
		self.count = 0
		self.size = n
		self.storage = [LinkedList() for i in range(n)]

	def __hash(self, x:int):
		return x % self.size

	def insert(self, x:int):
		temp = self.storage[self.__hash(x)]
		temp.append(x)
		self.count += 1

	def search(self, x:int) -> ListNode:
		return self.storage[self.__hash(x)].select(x)

	def delete(self, x:int):
		if self.storage[self.__hash(x)].remove(x) != None:
			self.count -= 1

	def isEmpty(self):
		if self.count == 0:
			return True
		return False

	def clear(self):
		for i in self.storage:
			i.clear()

	def printall(self):
		for i in self.storage:
			i.printList()

if __name__ == "__main__":
	HT = ChainedHashTable(8)
	HT.insert(6)
	HT.insert(7)
	HT.insert(16)
	HT.insert(32)
	HT.insert(9)
	HT.delete(9)
	HT.printall()