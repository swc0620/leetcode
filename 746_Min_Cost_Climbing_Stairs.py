class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            curr, prev, prev_prev = cost[i], cost[i-1], cost[i-2]
            temp = curr
            cost[i] = min(prev, prev_prev) + cost[i]
            prev_prev = prev
            prev = temp
        
        return min(cost[-1], cost[-2])
