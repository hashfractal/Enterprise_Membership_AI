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
		node = self.root # ���� ���� ����
		parent = None  # ���� ����� �θ� ���
		is_left_child = True # node�� parent�� ���� �ڽ� ������� ������ �ڽ� ������� Ȯ��

		# ������ ��� Ž��
		while True:
			if node is None:
				return False
			if key == node.key:
				break
			else:
				parent = node
				if key < node.key:
					node = node.left
					is_left_child = True # ���� �ڽ� ���� �������ϱ� �÷��׸� True�� ����
				else:
					node = node.right
					is_left_child = False # ������ �ڽ� ���� �������ϱ� �÷��׸� True�� ����
	
		# Ű�� ã�� �ڿ� �ڽ��� ���� ����̸� or �ڽ��� 1�� �ִ� ����̸�
		if node.left is None: # ���� �ڽ��� ������
			if node is self.root: #���� ���� ��尡 root�̸�, �ٷ� ������ �ڽ����� ��ü�Ѵ�.
				self.root = node.right
			# �Ʒ��� parent�� Ž�� �� ã�� ����� �ٷ� �� �θ� ��.(Ž�� �������� �׷��� ����)
			# parent - node - node�� �ڽ��� ������ ������ node��� �߰��� ������ ������ parent�� �ڽİ� node�� �ڽ��� ����
			# (node�� �ڽ��� ������ �ڿ����� None�� ��)
			elif is_left_child: #���� �ڽ� ��尡 �ִ� ���̴ϱ�
				parent.left = node.right # �θ��� ���� ������ ������ �ڽ��� ����Ŵ
			else: #������ �ڽ� ��尡 �ִ� ���̴ϱ�
				parent.right = node.right # �θ��� ������ ������ ������ �ڽ��� ����Ŵ
	
		elif node.right is None: # ������ �ڽ��� ������
			if node is self.root: 
				self.root = node.left #���� ���� ��尡 root�̸�, �ٷ� ���� �ڽ����� ��ü�Ѵ�.
			elif is_left_child:
				parent.left = node.left # �θ��� ���� ������ ���� �ڽ��� ����Ŵ
			else:
				parent.right = node.left # �θ��� ������ ������ ���� �ڽ��� ����Ŵ

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
