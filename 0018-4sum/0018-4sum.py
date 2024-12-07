class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k,l=j+1,len(nums)-1
                while k<l:
                    if nums[i]+nums[j]+nums[k]+nums[l]==target:
                        while k<l and nums[k]==nums[k+1]:
                            k+=1
                        while k<l and nums[l]==nums[l-1]:
                            l-=1
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                    elif nums[i]+nums[j]+nums[k]+nums[l]<target:
                        k+=1
                    else:
                        l-=1
        return result
                    