class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        
        tree = {i: [] for i in range(n)}
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        visited = set()
        def dfs(curr_node, prev_node):
            if curr_node in visited:
                return False

            visited.add(curr_node)
            for next_node in tree[curr_node]:
                if next_node == prev_node:
                    continue
                if not dfs(next_node, curr_node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
            
