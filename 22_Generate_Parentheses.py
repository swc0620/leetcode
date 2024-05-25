class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtracking(op, cl, string, stack):
            if op < 0 or cl < 0:
                return
            if op == 0 and cl == 0:
                ans.append(string)
            
            backtracking(op-1, cl, string+"(", stack+"(")
            if stack:
                backtracking(op, cl-1, string+")", stack[:-1])
            
        backtracking(n, n, "", "")
        
        return ans