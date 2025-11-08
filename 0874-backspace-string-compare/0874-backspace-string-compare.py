class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stackIt(el):
            stack = []
            for e in el:
                if stack and e == '#':
                    stack.pop()
                elif e!='#':
                    stack.append(e)
            #print(stack)
            return ''.join(stack)
        return stackIt(s) == stackIt(t)