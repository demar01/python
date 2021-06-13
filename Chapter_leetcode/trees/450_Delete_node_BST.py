# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key:
            # 4 posibilities
            #not children. We want whatever direction we came from return to a none, since we are getting rid of that node
            #1
            if not root.left and not root.right: return None
            #2
            if not root.left and root.right: return root.right
            #3
            if  root.left and not root.right: return root.left
            #4 if both have children
            # we move first to the right 
            pnt = root.right
            while pnt.left: pnt= pnt.left #keep making left traversals to the left to get greatest numbers
            root.val= pnt.val
            root.right= self.deleteNode(root.right, root.val)
        elif root.val >key:
            root.left= self.deleteNode(root.left, key)
        else:
            root.right= self.deleteNode(root.right, key)
        return root
    
#time complexity is the high of the tree O(n)