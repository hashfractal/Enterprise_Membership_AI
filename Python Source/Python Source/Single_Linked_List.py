class ListNode:
	def __init__(self, newItem, nextNode):
		self.item = newItem
		self.next = nextNode


class LinkedList:
	def __init__(self):
		self.dummy_head = ListNode(None, None)
		self.head = self.dummy_head
		self.__count = 0
	
	def insert(self, i:int, newItem):
		prev = self.__getNode(i - 1)
		prev.next = ListNode(newItem, prev.next)
		self.__count += 1
	def append(self, newItem):
		prev = self.__getNode(self.__count - 1)
		prev.next = ListNode(newItem, None)
		self.__count += 1
	def pop(self, i:int):   # i번 노드 삭제. 고정 파라미터
		if (i >= 0 and i <= self.__count-1):
			prev = self.__getNode(i - 1)
			curr = prev.next
			prev.next = curr.next
			self.__count -= 1
			return curr.item
		return None
	
	def remove(self, x):
		(prev, curr) = self.__findNode(x)
		if curr != None:
			prev.next = curr.next
			self.__count -= 1
			return x
		return None

	def get(self, i:int):
		curr = self.__getNode(i)
		return None if curr == None else curr.item

	def index(self, x) -> int:
		prev = self.head
		curr = prev.next
		idx = 0
		while curr != None:
			if curr.item == x:
				idx += 1
				return (idx)
			prev = curr
			curr = curr.next
		return None
	def isEmpty(self) -> bool:
		return self.head.next == None
	def size(self) -> int:
		return self.__count

	def clear(self):
		self.dummy_head.next = None
		self.__count = 0
	
	def count(self, x) -> int:
		res = 0
		prev = self.head
		curr = prev.next
		while curr != None:
			if curr.item == x:
				res += 1
			curr = curr.next
		return res

	def extend(self, a): # 여기서 a는 self와 같은 타입의 리스트
		for i in range(a.size()):
			self.append(a.get(i))
	 
	def copy(self):
		res = LinkedList()
		for i in range(self.size()):
			res.append(self.get(i))
		return res

	def reverse(self):
		temp = self.copy()
		self.clear()
		for i in range(temp.size()):
			self.insert(0, temp.get(i))
		
	
	def sort(self) -> None:
		temp = []
		for i in range(self.count):
			temp.append(self.get(i))
		temp.sort()
		for i in range(len(temp)):
			self.append(temp[i])

	def __findNode(self, x):
		prev = self.head
		curr = prev.next
		while curr != None:
			if curr.item == x:
				return (prev, curr)
			prev = curr
			curr = curr.next
		return (None, None)

	def __getNode(self, i:int) -> ListNode:
		curr = self.head
		for j in range(i + 1):
			curr = curr.next
		return curr
				
	def printList(self):
		for i in range(self.size()):
			print(self.get(i), end=" ")
		print()
	
	
if __name__ == "main":
	list = LinkedList()
	list.append(30)
	list.insert(0, 20)
	a = LinkedList()
	a.append(4) 
	a.append(3) 
	a.append(3) 
	a.append(2) 
	a.append(1)
	a.printList()
	list.extend(a)
	list.printList()
	list.reverse()
	list.printList()
	list.pop(0)
	list.printList()
	print("count(3):", list.count(3))
	print("get(2):", list.get(2))
	list.printList()