class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hash=dict()
        for i in nums:
            if i not in hash:
                hash[i]=1
            else:
                hash[i]+=1
        for key,val in hash.items():
            if val==1:
                return key
