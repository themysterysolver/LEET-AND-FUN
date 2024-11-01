class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path,visited,result):
            if len(path)==len(nums):
                result.append(path[:])
                return 
            for i,num in enumerate(nums):
                if visited[i]==True:
                    continue
                path.append(num)
                visited[i]=True
                backtrack(path,visited,result)
                path.pop()
                visited[i]=False
        result=[]
        path=[]
        visited=[False]*len(nums)
        backtrack(path,visited,result)
        return result