# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, n = 0, 0

        def digTree(node, k):
            nonlocal res, n
            if not node:
                return
            
            digTree(node.left, k)
            n += 1
            if n == k:
                res = node.val
            digTree(node.right, k)
        
        digTree(root, k)
        return res
        