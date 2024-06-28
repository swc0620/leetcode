class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def isPalindrome(substring, l, r):
            while l < r:
                if substring[l] != substring[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res