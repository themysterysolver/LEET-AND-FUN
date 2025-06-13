class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        maxi=0
        for i in s:
            if i>0:
                maxi=max(maxi,i)
        for i in range(1,maxi+1):
            if i not in s:
                return i
        return maxi+1
        