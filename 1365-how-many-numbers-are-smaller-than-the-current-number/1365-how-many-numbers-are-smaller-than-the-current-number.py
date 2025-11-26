class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        hash = {i:float('inf') for i in s}
        #print(s)
        for idx,num in enumerate(s):
            hash[num] = min(hash[num],idx)
        #print(hash)
        return [hash[num] for num in nums]