from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        heap = [(-1 * value, key) for key, value in count.items()]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            _, key = heapq.heappop(heap)
            res.append(key)
        return res