class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res =  helper(x * x, n // 2)
            if n % 2 == 1:
                return x * res 
            else:
                return res
        
        res = helper(x, abs(n))
        if n >= 0:
            return res
        else:
            return 1 / res