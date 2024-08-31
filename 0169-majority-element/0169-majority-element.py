class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxi=0
        mn=0
        b=list(set(nums))
        for i in b:
            if nums.count(i)>maxi:
                maxi=nums.count(i)
                mn=i
        return mn