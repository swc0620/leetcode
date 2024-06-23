class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return False

            if rank[parent1] < rank[parent2]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            return True
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]