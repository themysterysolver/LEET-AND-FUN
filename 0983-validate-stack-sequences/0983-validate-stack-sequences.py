class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        ptr=0
        for p in pushed:
            stack.append(p)
            while stack and stack[-1]==popped[ptr]:
                stack.pop()
                ptr+=1
        if ptr==len(popped):
            return True
        else:
            return False
