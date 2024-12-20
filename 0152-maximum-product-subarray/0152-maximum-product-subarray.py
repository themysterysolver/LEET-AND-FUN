class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=[0]*len(nums)
        suffix=[0]*len(nums)
        #print(prefix,suffix)
        pre=1
        for i in range(len(nums)):
            if nums[i]==0:
                prefix[i]=0
                pre=1
            else:
                #print(i,prefix[i],pre)
                pre*=nums[i]
                prefix[i]=pre
        print(prefix)
        suf=1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                suffix[i]=0
                suf=1
            else:
                #print(i,prefix[i],pre)
                suf*=nums[i]
                suffix[i]=suf
        print(suffix)
        return max(max(prefix),max(suffix))