class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def calcSquareSum(n):
            res = 0
            while n:
                q, r = divmod(n, 10)
                res += (r ** 2)
                n = q

            return res

        while n not in visited:
            visited.add(n)
            n = calcSquareSum(n)

            if n == 1:
                return True
        
        return False