class Solution:
    def addDigits(self, num: int) -> int:
        def add_digits(num):
            res = 0
            while True:
                num, r = divmod(num, 10)
                print(r)
                res += r
                if num == 0 and r == 0:
                    return res
        
        while len(str(num)) >= 2:
            num = add_digits(num)
        return num