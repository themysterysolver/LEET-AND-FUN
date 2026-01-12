class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x,y = points[0]
        ans = 0
        for a,b in points[1:]:
            ans+=max(abs(x-a),abs(y-b))
            x,y = a,b
        return ans