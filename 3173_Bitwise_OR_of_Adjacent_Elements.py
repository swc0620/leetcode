class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums) - 1):
            nums[idx] = nums[idx] | nums[idx+1]
        return nums[0:len(nums) - 1]