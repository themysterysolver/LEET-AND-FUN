class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        result=set()
        prefix=[0]*(len(nums)+1)
        curr=0
        for i in range(len(nums)):
            if nums[i]%p==0:
                curr+=1
            prefix[i]=curr
        print(prefix)
        for i in range(len(nums)+1):
            for j in range(i+1,len(nums)+1):
                if prefix[j-1]-prefix[i-1]<=k:
                    result.add(tuple(nums[i:j]))
        #print(result)
        return len(result)