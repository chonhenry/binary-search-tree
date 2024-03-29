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
		if self.root == None:
			self.root = newnode
		else:
			current = self.root
			while (True):
				if value < current.value:
					if current.left == None:
						current.left = newnode
						break
					current = current.left
				elif value > current.value:
					if current.right == None:
						current.right = newnode
						break
					current = current.right
				else:
					break

	def lookup(self, value):
		current = self.root
		while(True):
			print(current)
			if current.value != value:
				if value < current.value:
					current = current.left
				else:
					current = current.right
			else:
				print('value ', value)
				if(current.left==None):
					print('None')
				else:
					print('left ', current.left.value)
				if(current.right==None):
					print('None')
				else:
					print('right ', current.right.value)
				break
			if current == None:
				print('Value not found')
				break

	def remove(self, value): #replace the delete node with the minimum node of the right subtree
		parent = None
		current = self.root
		while(True):
			if current==None:
				print("value not found")
				break
			elif value < current.value:
				parent = current
				current = current.left
			elif value > current.value:
				parent = current
				current = current.right
			elif current.value==value:
				if(current.left==None and current.right==None): #Case 1: delete node has no child
					if(parent.left==current):
						parent.left = None
					elif(parent.right==current):
						parent.right = None
					del current
					break
				elif (current.left!=None and current.right==None) or (current.left==None and current.right!=None): #Case 2: delete node has only one child
					parent.left = current.left
					del current
					break
				else: #case 3: delete node has two children
					smallest_p = current
					smallest = current.right
					while(smallest.left!=None):
						smallest_p = smallest
						smallest=smallest.left
					current.value = smallest.value
					smallest_p.left = smallest.right

					del smallest
					break

	def breadthFirstSearch(self):
		current = self.root
		arr = []
		queue = []
		queue.append(current)

		while len(queue)>0:
			current = queue.pop(0)
			arr.append(current.value)
			if current.left != None:
				queue.append(current.left)
			if current.right != None:
				queue.append(current.right)

		return arr

	def breadthFirstSearchRecursive(self, queue, arr):
		if len(queue)==0:
			return arr

		current = queue.pop(0)
		arr.append(current.value)
		if current.left != None:
			queue.append(current.left)
		if current.right != None:
			queue.append(current.right)

		return self.breadthFirstSearchRecursive(queue, arr)


	def height(self, r):
		if r==None:
			return 0
		else:
			return (1 + max(self.height(r.left), self.height(r.right)))

def inOrder(root):
	if root.left != None:
		inOrder(root.left)

	print(root.value)

	if root.right != None:
		inOrder(root.right)

def preOrder(root):
	print(root.value)

	if root.left != None:
		preOrder(root.left)

	if root.right != None:
		preOrder(root.right)

def postOrder(root):
	if root.left != None:
		postOrder(root.left)

	if root.right != None:
		postOrder(root.right)

	print(root.value)


tree = BinarySearchTree();
#50,28,78,12,40,66,90,9,18,37,43,57,69,81,93,3,10,15,21,30,38,42,46,54,60,67,72,80,84,92,96,13,29,55,56
tree.insert(50)
tree.insert(28)
tree.insert(78)
tree.insert(12)
tree.insert(40)
tree.insert(66)
tree.insert(90)
tree.insert(9)
tree.insert(18)
tree.insert(37)
tree.insert(43)
tree.insert(57)
tree.insert(69)
tree.insert(81)
tree.insert(93)
tree.insert(3)
tree.insert(10)
tree.insert(15)
tree.insert(21)
tree.insert(30)
tree.insert(38)
tree.insert(42)
tree.insert(46)
tree.insert(54)
tree.insert(60)
tree.insert(67)
tree.insert(72)
tree.insert(80)
tree.insert(84)
tree.insert(92)
tree.insert(96)
tree.insert(13)
tree.insert(29)
tree.insert(55)
tree.insert(56)

tree.remove(15)

print(tree.breadthFirstSearch())
print('height: ', tree.height(tree.root))
print(tree.breadthFirstSearchRecursive([tree.root], []))

print('inOrder')
inOrder(tree.root)

print('preOrder')
preOrder(tree.root)

print('postOrder')
postOrder(tree.root)


