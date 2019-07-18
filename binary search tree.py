class node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self):
		self.root=None

	def insert(self, value):
		newnode = node(value)
		if self.root==None:
			self.root=newnode
		else:
			current = self.root
			while (True):
				if value<current.value:
					if current.left==None:
						current.left=newnode
						break
					current = current.left
				elif value>current.value:
					if current.right==None:
						current.right=newnode
						break
					current = current.right
				else:
					break

	def lookup(self, value):
		pass


tree = BinarySearchTree();
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)