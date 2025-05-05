class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for num in operations:
            if num.lstrip('-').isdigit():
                stack.append(num)
            elif num=="D": 
                stack.append(str(int(stack[-1])*2))
            elif num=="C":
                stack.pop()
            elif num=="+":
                if len(stack) >= 2:
                    stack.append(str(int(stack[-1])+int(stack[-2])))
            #print(num,stack)
        return sum(map(int,stack))