from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(r, c):
            queue = deque()
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            queue.append((r, c))
            while queue:
                r, c = queue.pop()
                for dx, dy in directions:
                    x, y = r + dx, c + dy
                    if x in range(rows) and y in range(cols) and grid[x][y] == "1" and (x, y) not in visited:
                        queue.append((x, y))
                        visited.add((x, y))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
        
        return res