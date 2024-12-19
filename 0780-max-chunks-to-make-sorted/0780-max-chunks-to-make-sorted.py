class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack=[]
        for i in arr:
            if not stack or i>stack[-1]:
                stack.append(i)
            else:
                top=stack.pop()
                while stack and stack[-1]>i:
                    stack.pop()
                stack.append(top)
            print(i,stack)
        return len(stack)