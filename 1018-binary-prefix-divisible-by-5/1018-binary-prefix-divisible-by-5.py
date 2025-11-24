class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = [False]*len(nums)
        l = len(nums)
        total = 0
        for i in range(l-1,-1,-1):
            total+=nums[i]*2**(l-i-1)
        #print(total) 
        for i in range(l-1,-1,-1):
            ans[i] = True if total%5 == 0 else False
            total-=nums[i]*2**(l-i-1)
        return ans