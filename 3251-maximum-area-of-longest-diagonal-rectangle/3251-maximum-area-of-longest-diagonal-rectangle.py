class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxdiagonal,maxarea=0,0
        for l,h in dimensions:
            area=l*h
            d=l**2+h**2
            if d>maxdiagonal:
                maxdiagonal=d
                maxarea=area
            elif d==maxdiagonal:
                maxarea=max(maxarea,area)
        return maxarea