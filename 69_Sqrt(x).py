class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 2, x // 2
        while l <= r:
            mid = (r + l) // 2
            target = mid * mid
            if x > target:
                l = mid + 1
            elif x < target:
                r = mid - 1
            else:
                return mid
        return r
            