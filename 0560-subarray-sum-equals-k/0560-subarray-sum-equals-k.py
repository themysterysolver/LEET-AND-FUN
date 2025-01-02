#BF
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        hash={0:1}# 0 as a sum in prefix exist by default in nums. 
        prefixsum=0
        for num in nums:
            prefixsum+=num
            if prefixsum-k in hash:
                count+=hash[prefixsum-k]
            hash[prefixsum]=hash.get(prefixsum,0)+1
        return count
        