from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        visited = set()
        queue = deque()

        def addRoom(r, c):
            if r in range(rows) and c in range(cols) and rooms[r][c] != -1 and (r, c) not in visited:
                visited.add((r, c))
                queue.append((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    addRoom(r, c)
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist += 1
                