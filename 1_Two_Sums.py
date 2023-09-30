class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}
        for idx, num in enumerate(nums):
            rest = target - num
            if rest in hashmap:
                return [hashmap[rest], idx]
            hashmap[num] = idx
        
        return []