class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxi=0
        sumi=0
        hash=dict()
        left=0
        #print('l n l r s m h')
        for right in range(len(nums)):
            while nums[right] in hash:
                hash[nums[left]]-=1
                sumi-=nums[left]
                if hash[nums[left]]==0:
                    del hash[nums[left]]
                left+=1
            sumi+=nums[right]
            maxi=max(maxi,sumi)
            hash[nums[right]]=1
            #print(right,nums[right],left,right,sumi,maxi,hash)
        return maxi