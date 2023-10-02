class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        l = r = 0
        res = 0

        while r < len(s):
            if s[r] in substring:
                substring.remove(s[l])
                l += 1
            else:
                substring.add(s[r])
                r += 1
            
            res = max(res, len(substring))
    
        return res
