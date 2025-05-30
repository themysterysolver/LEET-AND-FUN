#1 shotted the solution!
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        def backtrack(nums,curr):
            if k==len(nums):
                result.append(nums[:])
                return
            for i in range(curr+1,n+1):
                backtrack(nums+[i],i)
        for i in range(1,n+1):
            backtrack([i],i)
        return result