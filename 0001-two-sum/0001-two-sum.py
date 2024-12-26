class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash=dict()
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in hash:
                return [i,hash[complement]]
            hash[nums[i]]=i
        return []
            