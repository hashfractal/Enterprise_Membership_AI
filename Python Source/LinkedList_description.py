#Write a Python program to search a specific item in a given WSU linked list
#Then return true if the item is found otherwise return false.
#Class Node wich will generate Node for Linked List

class Node(object):
	# Singly linked node which make you to step forward and step backward
	# Thus you need to link of data
	def __init__(self, data=None, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev

#Class for
class WSU_linked_list(object):
		def __init__(self):
			self.head = None
			self.last = None
		#pre: Node object which has data
		#Method: add data in the linked List
		#Output: None
		def append_item(self, data):
				# Append an item
			if self.head == None:
				self.head = Node(data)
				self.last = self.head
			else:
				node = Node(data, None, self.last)
				self.last.next = node
				self.last = node
				#disconnect Link and setup new_item
				#check linked list if there are value that is looked by object

		def select_item(self, data):
			current = self.head
			while current:
				current = current.next
				if data == current.data:
					return current
			return None

		def remove_item(self, data):
			remove = self.select_item(data)
			if remove == self.head:
				self.head = self.head.next
				self.head.prev = None
			elif remove == self.last:
				self.last = self.last.prev
				self.last.next = None
			else:
				remove.prev.next = remove.next
				remove.next.prev = remove.prev
			del remove

		def iter(self):
				current = self.head
				while current:
						itemval = current.data
						current = current.next
						yield itemval

#print each elements
		def print_foward(self):
			for i in self.iter():
				print(i)
#search by end of linked list
		def search_item(self, val):
			for i in self.iter():
				if val == i:
					return True
			return False

#set Program Language Linked List for set Node
items = WSU_linked_list() #Instance linked List of Node Object
items.append_item('PHP')  #input program language
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
items.append_item('SQL')

print("Original list:")
items.print_foward()
items.remove_item("C#")
print("\n\nAfter Remove C#\n")
items.print_foward()
print("\n")

if items.search_item('SQL'):
	print("True")
else:
	print("False")

if items.search_item('C+'):
	print("True")
else:
	print("False")