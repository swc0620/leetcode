class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)
        diff = (max_num - k) - (min_num + k)
        if diff > 0:
            return diff
        return 0