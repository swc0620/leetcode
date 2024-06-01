class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, old_mark, new_mark):
            if (r < 0 or r >= rows) or (c < 0 or c >= cols) or (r, c) in visited or board[r][c] != old_mark:
                return
            visited.add((r, c))
            board[r][c] = new_mark
            dfs(r+1, c, old_mark, new_mark)
            dfs(r-1, c, old_mark, new_mark)
            dfs(r, c+1, old_mark, new_mark)
            dfs(r, c-1, old_mark, new_mark)
        
        for r in [0, rows-1]:
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    dfs(r, c, "O", "T")
        for c in [0, cols-1]:
            for r in range(rows):
                if board[r][c] == "O" and (r, c) not in visited:
                    dfs(r, c, "O", "T")
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        