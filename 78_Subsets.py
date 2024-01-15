class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(start, visited):
            res.append(visited)
            for idx in range(start, len(nums)):
                backtracking(idx+1, visited + [nums[idx]])
        backtracking(0, [])
        return res
