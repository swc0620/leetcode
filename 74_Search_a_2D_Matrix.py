class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        def binary_search(l, r, target):
            nonlocal row, col
            if l > r:
                return False
            
            mid = (l+r) // 2
            m, n = divmod(mid, col)
            if matrix[m][n] > target:
                r = mid - 1
            elif matrix[m][n] < target:
                l = mid + 1
            else:
                return True
            
            return binary_search(l, r, target)
        
        return binary_search(0, row*col-1, target)