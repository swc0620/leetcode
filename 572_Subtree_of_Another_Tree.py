# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            left_res = sameTree(node1.left, node2.left)
            right_res = sameTree(node1.right, node2.right)

            return left_res and right_res
        
        def digTree(node, subRoot):
            if not node:
                return False
            
            res = sameTree(node, subRoot)
            if res:
                return True
            
            left_res = digTree(node.left, subRoot)
            right_res = digTree(node.right, subRoot)

            return left_res or right_res

        return digTree(root, subRoot)