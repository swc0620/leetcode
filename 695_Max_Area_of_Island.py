from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def bfs(grid, row_idx, col_idx):
            area = 0
            queue = deque([(row_idx, col_idx)])
            row_len, col_len = len(grid), len(grid[0])
            while queue:
                row_idx, col_idx = queue.popleft()
                grid[row_idx][col_idx] = 0
                area += 1
                
                if row_idx+1 < row_len and grid[row_idx+1][col_idx] == 1 and (row_idx+1, col_idx) not in queue:
                    queue.append((row_idx+1, col_idx))
                if row_idx-1 >= 0 and grid[row_idx-1][col_idx] == 1 and (row_idx-1, col_idx) not in queue:
                    queue.append((row_idx-1, col_idx))
                if col_idx+1 < col_len and grid[row_idx][col_idx+1] == 1 and (row_idx, col_idx+1) not in queue:
                    queue.append((row_idx, col_idx+1))
                if col_idx-1 >= 0 and grid[row_idx][col_idx-1] == 1 and (row_idx, col_idx-1) not in queue:
                    queue.append((row_idx, col_idx-1))
            return area

        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if grid[row_idx][col_idx] == 1:
                    area = bfs(grid, row_idx, col_idx)
                    max_area = max(max_area, area)

        return max_area
        