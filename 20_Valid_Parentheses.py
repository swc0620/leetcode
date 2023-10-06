class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        brackets = {'}':'{', ')':'(', ']':'['}
        stack = []
        for char in s:
            if char in brackets:
                if not stack or brackets[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        
        return not stack