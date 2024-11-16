class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def checker(ans):
            flag=True
            for i in range(len(ans)-1):
                if ans[i+1]-ans[i]!=1:
                    flag=False
                    break
            return ans[-1] if flag else -1
        ans=[]
        for i in range(len(nums)-k+1):
            ans.append(nums[i:i+k])
        print(ans)
        result=[]
        for i in ans:
            result.append(checker(i))
        return result
