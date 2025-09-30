class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        sumAreas = 0
        lx,ly,rx,ry = float('inf'),float('inf'),float('-inf'),float('-inf')
        for x1,y1,x2,y2 in rectangles:
            sumAreas+=(x2-x1)*(y2-y1)
            lx = min(lx,x1)
            ly = min(ly,y1)
            rx = max(rx,x2)
            ry = max(ry,y2)
            for corner in [(x1,y1),(x2,y2),(x1,y2),(x2,y1)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        return sumAreas == (rx-lx)*(ry-ly) and corners == {(lx,ly),(lx,ry),(rx,ry),(rx,ly)}
            