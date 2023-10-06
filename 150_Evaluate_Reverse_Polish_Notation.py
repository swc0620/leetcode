class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop()+stack.pop())
            elif c == '-':
                i1, i2 = stack.pop(), stack.pop()
                stack.append(i2-i1)
            elif c == '*':
                stack.append(stack.pop()*stack.pop())
            elif c == '/':
                i1, i2 = stack.pop(), stack.pop()
                stack.append(int(i2/i1))
            else:
                stack.append(int(c))
        
        return stack[0]