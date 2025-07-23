class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x>y:
            score = 0
            stack = []
            for c in s:
                if c == 'b' and stack and stack[-1] == 'a':
                    stack.pop()
                    score += x
                else:
                    stack.append(c)
            stack1 = []
            for idx,c in enumerate(stack):
                if c == 'a' and stack1 and stack1[-1] == 'b':
                    stack1.pop()
                    score += y
                else:
                    stack1.append(c)
            return score
        else:
            score = 0
            stack = []
            for c in s:
                if c == 'a' and stack and stack[-1] == 'b':
                    stack.pop()
                    score += y
                else:
                    stack.append(c)
            stack1 = []
            for idx,c in enumerate(stack):
                if c == 'b' and stack1 and stack1[-1] == 'a':
                    stack1.pop()
                    score += x
                else:
                    stack1.append(c)
            return score
            #return score