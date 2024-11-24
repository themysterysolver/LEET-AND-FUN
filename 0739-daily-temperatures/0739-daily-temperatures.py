class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]#(val,idx)
        for i in range(len(temperatures)):
            while stack and stack[-1][0]<temperatures[i]:
                val,idx=stack.pop()
                result[idx]=i-idx
            stack.append((temperatures[i],i))
        print(result)
        return result