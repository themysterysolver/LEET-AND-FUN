class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        size=0
        start=0
        sumi,maxi=0,0
        hash=dict()
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]]=0
            hash[nums[i]]+=1
            size+=1
            sumi+=nums[i]
            while size>k:
                hash[nums[start]]-=1
                if hash[nums[start]]==0:
                    del hash[nums[start]]
                size-=1
                sumi-=nums[start]
                start+=1
            if k==size and len(hash)==k:
                maxi=max(maxi,sumi)  
        return maxi
                    
