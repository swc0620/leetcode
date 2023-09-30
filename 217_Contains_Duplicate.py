class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numbers = set()
        for num in nums:
            if num in numbers:
                return True
            else:
                numbers.add(num)
        
        return False
        