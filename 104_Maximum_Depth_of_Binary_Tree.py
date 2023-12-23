# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_count = -1

        def digTree(node, count):
            nonlocal max_count
            if not node:
                max_count = max(max_count, count)
                return
            
            digTree(node.left, count+1)
            digTree(node.right, count+1)

        digTree(root, 0)
        return max_count
            
