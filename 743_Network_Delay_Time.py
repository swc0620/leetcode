import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            adj[u].append((v, w))

        heap = [(0, k)]
        min_time = {}

        while heap:
            time, node = heapq.heappop(heap)

            if node in min_time:
                continue

            min_time[node] = time

            for neighbor, weight in adj[node]:
                if neighbor not in min_time:
                    heapq.heappush(heap, (time + weight, neighbor))

        if len(min_time) == n:
            return max(min_time.values())

        return -1