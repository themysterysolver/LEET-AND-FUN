#dijkstras algorithm
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        row,col=len(moveTime),len(moveTime[0])
        count=0
        heap=[(0,0,0,1)]
        time=[[float('inf')]*col for _ in range(row)]
        while heap:
            t,x,y,move=heapq.heappop(heap)
            if (x,y)==(row-1,col-1):
                return t
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if nx<0 or ny<0 or nx>=row or ny>=col:
                    continue
                else:
                    waitTime=max(moveTime[nx][ny]-t,0)
                    newT=t+waitTime+move
                    if newT<time[nx][ny]:
                        time[nx][ny]=newT
                        newMove=2 if move==1 else 1 
                        heapq.heappush(heap,(newT,nx,ny,newMove))
        return -1