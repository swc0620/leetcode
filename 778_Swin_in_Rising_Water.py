import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        min_heap = [[grid[0][0], 0, 0]]
        heapq.heapify(min_heap)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited.add((0, 0))

        while min_heap:
            t, x, y = heapq.heappop(min_heap)
            if x == n-1 and y == n-1:
                return t
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= n or (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                heapq.heappush(min_heap, [max(t, grid[nx][ny]), nx, ny])