import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                adj[i][j] = abs(x1-x2) + abs(y1-y2)
        
        visited = set()
        heap = [(0, 0)]
        res = 0
        while len(visited) < len(points):
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for j in range(N):
                heapq.heappush(heap, (adj[i][j], j))
        return res
