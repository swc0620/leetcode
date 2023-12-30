# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        res = []

        def digTree(node, level):
            nonlocal res
            if not node:
                return
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            
            digTree(node.left, level+1)
            digTree(node.right, level+1)

            return
    
        digTree(root, 0)
        return res

        