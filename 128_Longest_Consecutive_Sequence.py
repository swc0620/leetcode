class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        while nums:
            length = 1
            num = nums.pop()

            nextNum = num + 1
            while nextNum in nums:
                nums.remove(nextNum)
                length += 1
                nextNum += 1
            
            beforeNum = num - 1
            while beforeNum in nums:
                nums.remove(beforeNum)
                length += 1
                beforeNum -= 1
            
            res = max(length, res)
        
        return res


