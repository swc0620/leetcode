class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            courses[a].append(b)
        
        res = []
        visited, cycle = set(), set()
        def dfs(c):
            if c in visited:
                return True
            if c in cycle:
                return False
            
            cycle.add(c)
            for next_c in courses[c]:
                if not dfs(next_c):
                    return False
            cycle.remove(c)
            visited.add(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
        