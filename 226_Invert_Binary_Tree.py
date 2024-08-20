# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def digTree(node):
            if not node:
                return
            digTree(node.left)
            digTree(node.right)
            
            temp = node.left
            node.left = node.right
            node.right = temp
        
        digTree(root)
        return root
        