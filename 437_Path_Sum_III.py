from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def traverse(node, total_sum):
            nonlocal cnt
            if not node:
                return
            
            total_sum += node.val
            cnt += sum_cnt[total_sum - targetSum]
            sum_cnt[total_sum] += 1

            traverse(node.left, total_sum)
            traverse(node.right, total_sum)
            sum_cnt[total_sum] -= 1
        
        cnt = 0
        sum_cnt = defaultdict(int)
        sum_cnt[0] = 1
        traverse(root, 0)
        return cnt
