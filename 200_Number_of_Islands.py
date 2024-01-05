from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(start, grid):
            deq = deque()
            deq.append(start)
            while deq:
                row, col = deq.popleft()
                grid[row][col] = "0"
                if row + 1 < len(grid) and grid[row+1][col] == "1" and (row+1, col) not in deq:
                    deq.append((row+1, col))
                if col + 1 < len(grid[0]) and grid[row][col+1] == "1" and (row, col+1) not in deq:
                    deq.append((row, col+1))
                if row - 1 >= 0 and grid[row-1][col] == "1" and (row-1, col) not in deq:
                    deq.append((row-1, col))
                if col - 1 >= 0 and grid[row][col-1] == "1" and (row, col-1) not in deq:
                    deq.append((row, col-1))
    
        cnt = 0
        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if col == "1":
                    cnt += 1
                    bfs((row_idx, col_idx), grid)
        
        return cnt