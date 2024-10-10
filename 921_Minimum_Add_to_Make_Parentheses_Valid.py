class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op, add = 0, 0

        for c in s:
            if c == '(':
                op += 1
            else:
                if op > 0:
                    op -= 1
                else:
                    add += 1
        return op + add