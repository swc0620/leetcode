class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev, prev_prev = 1, 1

        for k in range(2, n+1):
            curr = prev + prev_prev
            prev_prev = prev
            prev = curr
            
        return curr