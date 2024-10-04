class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        l = min(m, n)
        res = ""
        for i in range(l):
            res += word1[i]
            res += word2[i]
        
        for i in range(l, m):
            res += word1[i]
        
        for i in range(l, n):
            res += word2[i]
        
        return res