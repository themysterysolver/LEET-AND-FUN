class Solution:
    def maxArea(self, height: List[int]) -> int:
        start,end=0,len(height)-1
        max_area=min(height[start],height[end])*(end-start)
        while start<end:
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
            max_area=max(min(height[start],height[end])*(end-start),max_area)
        return max_area
