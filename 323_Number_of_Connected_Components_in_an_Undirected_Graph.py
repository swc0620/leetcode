class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):        
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 == root2:
                return 0
            if rank[root1] < rank[root2]:
                parent[root1] = root2
                rank[root2] += rank[root1]
            else:
                parent[root2] = root1
                rank[root1] += rank[root2]
            return 1
        
        res = n
        for node1, node2 in edges:
            res -= union(node1, node2)
        return res

        # visited = set()
        # ans = 0

        # tree = {i: [] for i in range(n)}
        # for a, b in edges:
        #     tree[a].append(b)
        #     tree[b].append(a)

        # def dfs(curr_node, prev_node):
        #     if curr_node in visited:
        #         return
            
        #     visited.add(curr_node)
        #     for next_node in tree[curr_node]:
        #         if next_node == prev_node:
        #             continue
        #         dfs(next_node, curr_node)
        #     return
        
        # for node in range(n):
        #     if node not in visited:
        #         ans += 1
        #         dfs(node, -1)
        
        # return ans