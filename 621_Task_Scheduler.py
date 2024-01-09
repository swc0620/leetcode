import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = []
        for count in counts.values():
            max_heap.append(-1 * count)
        heapq.heapify(max_heap)

        time = 0
        queue = deque()
        while max_heap or queue:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] <= time:
                task = queue.popleft()
                heapq.heappush(max_heap, task[0])
        
        return time