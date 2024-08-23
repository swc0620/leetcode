# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1

        def digTree(node, parent):
            nonlocal res
            if not node:
                return
            if node.val >= parent:
                res += 1
                parent = node.val
            digTree(node.left, parent)
            digTree(node.right, parent)
        
        if root.right:
            digTree(root.right, root.val)
        if root.left:
            digTree(root.left, root.val)
        
        return res