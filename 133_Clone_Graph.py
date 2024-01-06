from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        visited = {}
        queue = deque([node])
        visited[node.val] = Node(node.val, [])
        root = node

        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[node.val].neighbors.append(visited[neighbor.val])
        
        return visited[root.val]