import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l+r) // 2
            count = 0
            for p in piles:
                count += math.ceil(p / mid)
            if count > h:
                l = mid + 1
            elif count <= h:
                r = mid
        return r

