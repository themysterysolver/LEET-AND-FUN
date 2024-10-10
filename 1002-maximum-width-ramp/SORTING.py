class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        index=[i for i in range(len(nums))]
        print(index)
        index.sort(key=lambda i:(nums[i],i))
        max_width=0
        min_index=len(nums)
        for i in index:
            max_width=max(i-min_index,max_width)
            min_index=min(min_index,i)
        return max_width
