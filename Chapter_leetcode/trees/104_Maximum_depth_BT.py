class Node:
    # Constructor to create a new node
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(node):
    return 1 + max(maxDepth(node.left), maxDepth(node.right)) if node else 0

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Height of tree is %d" %(maxDepth(root)))


#https://www.youtube.com/watch?v=gMhTUfQLr2E
#https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/