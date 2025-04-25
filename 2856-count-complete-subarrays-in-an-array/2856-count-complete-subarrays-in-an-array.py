'''The idea behind solving this problme is that n-right is the no of more subarrays that we can include once we find the window of distinct'''
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l=len(set(nums))
        count=0
        left=0
        hash=dict()
        n=len(nums)
        #print(n,"DISTINCT:",l)
        for right in range(len(nums)):
            hash[nums[right]]=hash.get(nums[right],0)+1
            #print(right,hash)
            while len(hash)==l:
                count+=n-right
                hash[nums[left]]-=1
                if hash[nums[left]]==0:
                    del hash[nums[left]]
                left+=1
        return count
