class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        head = slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        while True:
            head = nums[head]
            fast = nums[fast]
            if head == fast:
                break
        return fast
