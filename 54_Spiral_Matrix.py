class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t, l = 0, 0
        b, r = len(matrix), len(matrix[0])
        res = []

        while l < r and t < b:
            for i in range(r-l):
                res.append(matrix[t][l+i])
            t += 1

            for i in range(b-t):
                res.append(matrix[t+i][r-1])
            r -= 1

            if not (l < r and t < b):
                break
            
            for i in range(1, r-l+1):
                res.append(matrix[b-1][r-i])
            b -= 1

            for i in range(1, b-t+1):
                res.append(matrix[b-i][l])
            l += 1
        return res
