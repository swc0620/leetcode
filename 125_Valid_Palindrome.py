class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalnum(c):
            c = ord(c)
            return (ord('a') <= c <= ord('z')) or (ord('A') <= c <= ord('Z')) or (ord('0') <= c <= ord('9'))

        pre, post = 0, len(s) - 1
        while True:
            while pre < len(s)-1 and not isalnum(s[pre]):
                pre += 1
            while post > 0 and not isalnum(s[post]):
                post -= 1
            if pre >= post:
                return True
        
            if s[pre].lower() != s[post].lower():
                return False
            
            pre += 1
            post -= 1