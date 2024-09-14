class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d=dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        value_set=set(d.values())
        keys=[key for key,value in d.items() if value==1]
        return keys
        