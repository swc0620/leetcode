class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, i = [], 0
        def backtracking(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            backtracking(i+1, subset)
            subset.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            backtracking(i+1, subset)
        
        backtracking(0, [])
        return res