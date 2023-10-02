class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        l, r = 0, 1
        substring = set(s[l])
        res = 1
        while r < len(s):
            if s[r] in substring:
                substring.remove(s[l])
                l += 1
            else:
                substring.add(s[r])
                r += 1
            res = max(res, len(substring))

        return res
