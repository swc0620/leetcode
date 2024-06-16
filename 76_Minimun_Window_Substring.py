class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count, window = {}, {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        
        res, res_len = [-1, -1], float('inf')
        l = 0
        have = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in count and window[c] == count[c]:
                have += 1
            
            while have == len(count):
                if (r - l + 1) < res_len:
                    res, res_len = [l, r], (r-l+1)

                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        if res_len != float('inf'):
            return s[l:r+1]
        else:
            return ""
