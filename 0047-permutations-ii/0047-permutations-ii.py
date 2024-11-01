class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path,visited,result):
            if len(nums)==len(path):
                result.append(path[:])
                return
            for i,num in enumerate(nums):
                if visited[i]:
                    continue
                path.append(num)
                visited[i]=True
                backtrack(path,visited,result)
                path.pop()
                visited[i]=False
        result=[]
        visited=[False]*len(nums)
        path=[]
        backtrack(path,visited,result)
        ans=[]
        for r in result:
            if r not in ans:
                ans.append(r)
        return ans