import Sinlge_Linked_List

class LinkedStack:
	def __init__(self) -> None:
		self.Storage = Sinlge_Linked_List.LinkedList()
	
	def push(self, x):
		self.Storage.insert(0, x)
		
	def pop(self):
		return self.Storage.pop(0)

	def top(self):
		return self.Storage.get(0)

	def isEmpty(self):
		return self.Storage.isEmpty()

	def popAll(self):
		for i in range(self.Storage.count()):
			yield self.Storage.get(i)
	def PrintStack(self):
		print("Stack from top: ", end="")
		self.Storage.printList()

if __name__ == "__main__":
	st1 = LinkedStack()
	st1.push(100)
	st1.push(200)
	print("Top is", st1.top())
	st1.pop()
	st1.push("monday")
	st1.PrintStack()
	print('isEmpty?', st1.isEmpty())