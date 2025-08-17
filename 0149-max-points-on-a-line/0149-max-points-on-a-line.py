class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        def slope(p1,p2):
            x1,y1 = p1
            x2,y2 = p2
            a = y2-y1
            b = x2-x1
            g = gcd(a,b)
            if g == 0:
                return (0,0)
            return (b//g,a//g)
        maxi = float('-inf')
        for p in points:
            hash = defaultdict(int)
            for q in points:
                hash[slope(p,q)]+=1
            maxi = max(max(hash.values())+1,maxi)
        return maxi
