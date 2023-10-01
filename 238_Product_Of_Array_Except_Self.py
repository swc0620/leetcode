class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        sol = [1] * length
        pre = post = 1
        for idx in range(length):
            sol[idx] *= pre
            pre *= nums[idx]
            sol[length-idx-1] *= post
            post *= nums[length-idx-1]
        
        return sol
        