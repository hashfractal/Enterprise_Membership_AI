from platform import node
from tkinter import INSERT
from tkinter.messagebox import NO


class TreeNode:
	def __init__(self, key, value, left, right) -> None:
		self.key = key
		self.value = value
		self.left = left
		self.right = right

class BinarySearchTree:
	def __init__(self) -> None:
		self.root = None

	def search(self, key) -> TreeNode:
		node = self.root
		while True:
			if node is None:
				return None
			if key == node.key:
				return node
			elif key < node.key:
				node = node.left
			else:
				node = node.right

	def insert(self, key, value = ""):
		def add_node(node, key, value):
			if key == node.key:
				return False
			elif key < node.key:
				if node.left is None:
					node.left = TreeNode(key, value, None, None)
				else:
					add_node(node.left, key, value)
			else:
				if node.right is None:
					node.right = TreeNode(key, value, None, None)
				else:
					add_node(node.right, key, value)
			return True
		if self.root is None:
			self.root = TreeNode(key, value, None, None)
			return True

		else:
			return add_node(self.root, key, value)

	def delete(self, key):
		node = self.root # 현재 노드로 지정
		parent = None  # 현재 노드의 부모 노드
		is_left_child = True # node는 parent의 왼쪽 자식 노드인지 오른쪽 자식 노드인지 확인

		# 삭제할 노드 탐색
		while True:
			if node is None:
				return False
			if key == node.key:
				break
			else:
				parent = node
				if key < node.key:
					node = node.left
					is_left_child = True # 왼쪽 자식 노드로 내려가니까 플래그를 True로 설정
				else:
					node = node.right
					is_left_child = False # 오른쪽 자식 노드로 내려가니까 플래그를 True로 설정
	
		# 키를 찾은 뒤에 자식이 없는 노드이면 or 자식이 1개 있는 노드이면
		if node.left is None: # 왼쪽 자식이 없으면
			if node is self.root: #만약 삭제 노드가 root이면, 바로 오른쪽 자식으로 대체한다.
				self.root = node.right
			# 아래의 parent는 탐색 시 찾은 노드의 바로 위 부모가 됨.(탐색 로직에서 그렇게 적용)
			# parent - node - node의 자식의 구도가 있으면 node라는 중간이 빠지기 때문에 parent의 자식과 node의 자식을 연결
			# (node의 자식이 없으면 자연스레 None이 들어감)
			elif is_left_child: #왼쪽 자식 노드가 있는 것이니까
				parent.left = node.right # 부모의 왼쪽 참조가 오른쪽 자식을 가리킴
			else: #오른쪽 자식 노드가 있는 것이니까
				parent.right = node.right # 부모의 오른쪽 참조가 오른쪽 자식을 가리킴
	
		elif node.right is None: # 오른쪽 자식이 없으면
			if node is self.root: 
				self.root = node.left #만약 삭제 노드가 root이면, 바로 왼쪽 자식으로 대체한다.
			elif is_left_child:
				parent.left = node.left # 부모의 왼쪽 참조가 왼쪽 자식을 가리킴
			else:
				parent.right = node.left # 부모의 오른쪽 참조가 왼쪽 자식을 가리킴

	def printall(self):
		def print_subtree(node):
			if node is not None:
				print(f"{node.key}: {node.value}", end="")
				print_subtree(node.left)
				print_subtree(node.right)
		root = self.root
		print_subtree(root)

if __name__ == "__main__":
	BST = BinarySearchTree()
	BST.insert(1)
	BST.insert(10)
	BST.insert(9)
	BST.insert(15)
	BST.insert(11)
	BST.insert(5)
	BST.insert(8)
	BST.insert(7)
	BST.printall()
