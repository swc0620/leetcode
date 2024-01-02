# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        min_val = float('-inf')
        max_val = float('inf')
        
        def digTree(node, min_val, max_val):
            nonlocal res
            if not node:
                return True
            
            if node.val >= max_val or node.val <= min_val:
                res = False

            digTree(node.left, min_val, min(node.val, max_val))
            digTree(node.right, max(node.val, min_val), max_val)
        
        digTree(root, min_val, max_val)

        return res
