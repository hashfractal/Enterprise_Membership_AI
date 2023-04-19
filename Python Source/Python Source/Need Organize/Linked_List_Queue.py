import Single_Linked_List

class LinkedQueue:
	def __init__(self) -> None:
		self.Storage = Single_Linked_List.LinkedList()

	def enqueue(self, x):
		self.Storage.append(x)

	def dequeue(self):
		return self.Storage.pop(0)

	def front(self):
		return self.Storage.get(0)

	def isEmpty(self):
		return self.Storage.isEmpty()

	def dequeueAll(self):
		self.Storage.clear()

	def printQueue(self):
		self.Storage.printList()

q1 = LinkedQueue()
q1.enqueue("Mon")
q1.enqueue("Tue")
q1.enqueue(1234)
q1.enqueue("Wed")
q1.dequeue()
q1.enqueue('aaa')
q1.printQueue()