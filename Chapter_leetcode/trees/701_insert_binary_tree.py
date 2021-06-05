701. Insert into a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    elif root.val < val:
        root.right = root.insertIntoBST(root.right, val)
    else:
        root.left = root.insertIntoBST(root.left, val)
    return root

# https://www.youtube.com/watch?v=KfVj2MtiWFk
# root = [4,2,7,1,3], val = 5

# https://www.geeksforgeeks.org/insert-a-node-in-binary-search-tree-iteratively/