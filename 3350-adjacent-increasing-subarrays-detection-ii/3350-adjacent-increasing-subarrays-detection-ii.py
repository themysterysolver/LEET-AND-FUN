class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        count = 0
        nums.insert(0,float('-inf'))
        nums.append(float('-inf'))
        ans = []
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                count+=1
            else:
                ans.append(count)
                count = 1
            #print(i,ans)
        #print(ans)
        maxi = 0
        for i in range(1,len(ans)):
            maxi = max(maxi,min(ans[i],ans[i-1]))
        for i in range(len(ans)):
            maxi = max(maxi,ans[i]//2)
        return maxi if maxi!=0 else 1
