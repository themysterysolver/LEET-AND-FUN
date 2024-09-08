class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d=dict()
        a=[0,0]
        n=len(nums)
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
                continue
            a[0]=nums[i]
            break
        s=sum(list(set(nums)))
        a[1]=(n*(n+1)//2)-s
        return a
            