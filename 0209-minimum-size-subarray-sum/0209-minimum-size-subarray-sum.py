class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start,end=0,0
        sumi=0
        mini=float('inf')
        while end<len(nums):
            sumi+=nums[end]
            while sumi>=target:
                if end-start+1<mini:
                    mini=end-start+1
                sumi-=nums[start]
                start+=1
            end+=1
        return mini if mini!=float('inf') else 0

