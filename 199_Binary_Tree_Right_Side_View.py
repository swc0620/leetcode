# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def digTree(node, level):
            if not node:
                return
            
            if len(res) <= level:
                res.append(node.val)
            else:
                res[level] = node.val
            
            digTree(node.left, level+1)
            digTree(node.right, level+1)
        
        digTree(root, 0)
        return res