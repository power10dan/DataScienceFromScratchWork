class Tree:
	def __init__(self, cargo, left=None, right=None):
		self.cargo = cargo
		self.left = left
		self.right = right
	
	def __str__(self):
		return str(self.cargo)

def preOrder(treeToPre):
	if treeToPre == None: 
		return
	print treeToPre.cargo
	preOrder(treeToPre.left)
	preOrder(treeToPre.right)

def postOrder(treeToPost):
	if treeToPost == None:
		return
	postOrder(treeToPost.left)
	postOrder(treeToPost.right)
	print treeToPost.cargo 

def inOrder(treeToIn):
	if treeToIn == None:
		return
	inOrder(treeToIn.left)
	print treeToIn.cargo
	inOrder(treeToIn.right)





