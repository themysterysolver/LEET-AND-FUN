class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h=sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=h[i]:
                count+=1
        return count