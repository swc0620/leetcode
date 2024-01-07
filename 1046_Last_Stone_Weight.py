import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1
            if y-x > 0:
                heapq.heappush(stones, x-y)
        
        if stones:
            return stones[0] * -1
        return 0
        