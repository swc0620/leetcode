# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def digTree(node, max_num):
            if not node:
                return 
            nonlocal res
            if node.val >= max_num:
                res += 1
                max_num = node.val
            
            digTree(node.left, max_num)
            digTree(node.right, max_num)

            return
            
        digTree(root, root.val)

        return res

