class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        closest = []
        for i in range(len(nums)):
            if i == 0:
                closest.append(1)
            elif i == len(nums)-1:
                closest.append(len(nums)-2)
            else:
                if abs(nums[i]-nums[i+1])>=abs(nums[i]-nums[i-1]):
                    closest.append(i-1)
                else:
                    closest.append(i+1)
        #print(closest)
        n = len(nums)
        prefix = [0]*n
        pre = 0
        for i in range(1,n):
            if closest[i-1]==i:
                pre+=1
            else:
                pre+=abs(nums[i]-nums[i-1]) 
            prefix[i] = pre 
        #print(prefix)
        suffix = [0]*n
        suff = 0
        for i in range(n-2,-1,-1):
            if closest[i+1]==i:
                suff+=1
            else:
                suff+=abs(nums[i]-nums[i+1]) 
            suffix[i] = suff 
        #print(suffix)
        ans = []
        for a,b in queries:
            if a<b:
                ans.append(prefix[b]-prefix[a])
            else:
                ans.append(suffix[b]-suffix[a])
        #print(ans)
        return ans