class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxd,maxa=0,0
        for l,h in dimensions:
            area=l*h
            d=l**2+h**2
            if d>maxd:
                maxd=d
                maxa=area
            elif d==maxd:
                maxa=max(maxa,area)
        return maxa