class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[l] <= nums[mid]: 
                if nums[mid] <= nums[r]:
                    return nums[l]
                else:
                    l = mid + 1
            else:
                r = mid
        return nums[r]