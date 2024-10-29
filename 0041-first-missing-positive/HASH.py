class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash={}
        maxi=0
        for i in nums:
            if i<=0:
                continue
            else:
                hash[i]=True
                maxi=max(maxi,i)
        for i in range(1,maxi+1):
            if i not in hash:
                return i
        return maxi+1
        
