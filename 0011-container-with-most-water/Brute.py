#THIS IS BRUTE FORCE O(n^2)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        print(height)
        max_area=0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                area=min(height[i],height[j])*(j-i)
                max_area=max(area,max_area)
        return max_area
