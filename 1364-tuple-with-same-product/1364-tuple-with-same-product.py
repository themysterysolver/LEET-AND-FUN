class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hash=dict()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p=nums[i]*nums[j]
                hash[p]=hash.get(p,0)+1
        count=0
        for val in hash.values():
            count+=(val)*(val-1)*4
        return count