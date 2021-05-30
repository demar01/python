#https://www.educative.io/edpresso/finding-the-maximum-depth-of-a-binary-tree
#https://codeworkshop.dev/video-workshops/2020-05-07-how-to-traverse-a-binary-tree-in-python/

#     1
#   /   \
#  2     2
# /     
#3
class Node: 
  def __init__(self , value): 
      self.value = value 
      self.left = None
      self.right = None

def maxDepth(root):
  # Null node has 0 depth.
  if root == None:
    return 0
  # Get the depth of the left and right subtree 
  # using recursion.
  leftDepth = maxDepth(root.left)
  rightDepth = maxDepth(root.right)
  # Choose the larger one and add the root to it.
  if leftDepth > rightDepth:
    return leftDepth + 1
  else:
    return rightDepth + 1

# Driver code
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.right = Node(2)
print("The max depth is:", maxDepth(root))

# Preorder traversal returns [1,2,3,2]
def depth_first_traversal_pre(node):
    if node == None:
        return
    print(node.value) #printing the node before we call left and rigth
    depth_first_traversal_pre(node.left)
    depth_first_traversal_pre(node.right)

depth_first_traversal_pre(root)

#in order transversal returns [3,2,1,2]
def depth_first_traversal_io(node):
    if node == None:
        return
    depth_first_traversal_io(node.left)
    print(node.value) #visiting the left branch and go all the way down before we print out the value
    depth_first_traversal_io(node.right)

depth_first_traversal_io(root)

#post order transversal returns [3,2,2,1]

def depth_first_traversal_po(node):
    if node == None:
        return
    depth_first_traversal_po(node.left)
    depth_first_traversal_po(node.right)
    print(node.value) #operating on the value last

    
depth_first_traversal_po(root)