class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash=dict()
        for i in nums:
            if i not in hash:
                hash[i]=1
            else:
                hash[i]+=1
        maxi=max(hash.values())
        count=0
        for key,val in hash.items():
            if val==maxi:
                count+=val
        return count
