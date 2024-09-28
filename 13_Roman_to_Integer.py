class Solution:
    def romanToInt(self, s: str) -> int:
        r2i = {'O': 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s + 'O'
        res = 0
        for i in range(len(s)-1):
            curr = s[i]
            _next = s[i+1]
            if r2i[curr] < r2i[_next]:
                res -= r2i[curr]
            else:
                res += r2i[curr]
        return res

        