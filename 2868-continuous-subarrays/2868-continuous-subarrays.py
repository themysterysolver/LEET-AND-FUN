class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        start,end=0,0
        count=0
        hash=dict()
        while end<len(nums):
            hash[nums[end]]=hash.get(nums[end],0)+1
            while max(hash)-min(hash)>2:
                hash[nums[start]]-=1
                if hash[nums[start]]==0:
                    del hash[nums[start]]
                start+=1
            count+=end-start+1
            end+=1
        return count