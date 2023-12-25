# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def digTree(node):
            if not node:    
                return True, -1
            
            left_balanced, left_height = digTree(node.left)
            right_balanced, right_height = digTree(node.right)
        
            if abs(left_height - right_height) > 1:
                return False, max(left_height, right_height) + 1
            
            return left_balanced and right_balanced, max(left_height, right_height) + 1

        balanced, height = digTree(root)

        return balanced