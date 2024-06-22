class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1

        for num in nums:
            if num == 0:
                curr_min, curr_max = 1, 1
                continue
            temp = curr_min
            curr_min = min(curr_min * num, curr_max * num, num)
            curr_max = max(temp * num, curr_max * num, num)
            res = max(res, curr_max)
        
        return res