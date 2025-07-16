# lol than god constarint is greater than 2
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                el,freq = stack.pop()
                freq += 1
                if freq != k:
                    stack.append((el,freq))
            else:
                stack.append((c,1))
        #print(stack)
        result = ""
        for c,f in stack:
            result += c*f
        return result