class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        subSum = 0

        for num in nums:
            if subSum < 0:
                subSum = 0
            subSum += num
            maxSum = max(subSum, maxSum)

        return maxSum
        