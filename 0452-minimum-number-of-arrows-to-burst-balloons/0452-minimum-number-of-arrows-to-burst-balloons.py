class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        arrows=1
        end=points[0][1]
        print(points) 
        for x,y in points[1:]:
            if x>end:
                arrows+=1
                end=y
            else:
                end=min(end,y)
        return arrows


            