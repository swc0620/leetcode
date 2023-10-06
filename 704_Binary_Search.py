class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r, target):
            if l > r:
                return -1
            
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
            
            return binary_search(l, r, target)
        
        return binary_search(0, len(nums)-1, target)
