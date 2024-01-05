# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx
        root_idx = 0

        def digTree(left, right):
            if left > right:
                return None
            
            nonlocal root_idx

            root_val = preorder[root_idx]
            root = TreeNode(root_val)
            root_idx += 1

            root.left = digTree(left, inorder_map[root_val] - 1)
            root.right = digTree(inorder_map[root_val] + 1, right)

            return root

        return digTree(0, len(preorder) - 1)
