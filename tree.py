class Tree:
	def __init__(self):
		self.val = None
		self.left = None
		self.right = None


root = Tree()
root.val = 4
left, right = Tree(), Tree()
left.val, right.val = 2,5
root.left, root.right = left, right

left, right = Tree(), Tree()
left.val, right.val = 1, 3
root.left.left, root.left.right = left, right

# inorder traversal
def dfs(root):
	if not root: return
	dfs(root.left)
	print(root.val)
	dfs(root.right)

dfs(root)
