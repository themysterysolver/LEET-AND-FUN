class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        if k ==0:
            return nums
        ws = k+k+1
        ans = [-1]*len(nums)
        if len(nums)<ws:
            return ans

        sumx = sum(nums[:ws])
        ans[k] = sumx//ws
        for i in range(k+1,len(nums)-k):
            #print(i,sumx,nums[i+k],nums[i-k])
            sumx+=nums[i+k]
            sumx-=nums[i-k-1]
            #print(i,sumx)
            ans[i]=sumx//ws
            #print('-----------')
        return ans