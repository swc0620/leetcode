# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        has_p = (root.val == p.val)
        has_q = (root.val == q.val)

        def digTree(node, p, q, has_p, has_q):
            nonlocal ans

            if not node:
                return False, False
            
            left_has_p, left_has_q = digTree(node.left, p, q, has_p, has_q)
            right_has_p, right_has_q = digTree(node.right, p, q, has_p, has_q)

            has_p = ((node.val == p) or left_has_p or right_has_p)
            has_q = ((node.val == q) or left_has_q or right_has_q)

            if has_p and has_q and not ans:
                ans = node

            return has_p, has_q
                
        digTree(root, p.val, q.val, has_p, has_q)

        return ans