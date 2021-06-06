class Node:
    # Constructor to create a new node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isSameTree(p, q): 
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """    
    def dfs(p,q): #helper method 
    # 1. Both empty
        if not p and not q:
            return True
    # 2. Both non-empty -> Compare them
        if p is not None and q is not None:
            return ((p.val ==q.val) and dfs(p.left, b.left) and dfs(p.right, b.right))
    # 3. one empty, one not -- false
        return False

root1 = Node(1)
root2 = Node(1)

root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
  
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

if isSameTree(root1, root2):
    print ("Both trees are identical")
else:
    print ("Trees are not identical")

# https://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/

