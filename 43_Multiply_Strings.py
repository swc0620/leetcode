class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1+i2] += digit
                res[i1+i2+1] += (res[i1+i2] // 10)
                res[i1+i2] = (res[i1+i2] % 10)
        
        res, begin_i = res[::-1], 0
        while begin_i < len(res) and res[begin_i] == 0:
            begin_i += 1
        
        res = map(str, res[begin_i:])
        return "".join(res)