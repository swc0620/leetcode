class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return False

        row, col = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or r >= row) or (c < 0 or c >= col) or word[i] != board[r][c] or (r, c) in visited:
                return False

            visited.add((r, c))
            for dx, dy in directions:
                x, y = r + dx, c + dy
                if dfs(x, y, i+1):
                    return True
            visited.remove((r, c))
            return False

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False