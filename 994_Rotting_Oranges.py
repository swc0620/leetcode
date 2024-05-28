from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        def rot(x, y):
            if x in range(rows) and y in range(cols) and (x, y) not in visited and grid[x][y] == 1:
                nonlocal fresh
                visited.add((x, y))
                queue.append((x, y))
                fresh -= 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
            
        res = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                rot(r+1, c)
                rot(r-1, c)
                rot(r, c+1)
                rot(r, c-1)
            res += 1
        
        if fresh > 0:
            return -1
        return res
        