class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = 1
        n = len(digits)
        while i < n:
            if digits[-1 * i] != 10:
                break
            digits[-1 * i] = 0
            digits[-1 * (i+1)] += 1
            i += 1
        else:
            if digits[-1 * n] == 10:
                digits[-1 * n] = 0
                return [1] + digits
        
        return digits