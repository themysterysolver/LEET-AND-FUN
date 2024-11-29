#dijkstras algorithm
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        row,col=len(moveTime),len(moveTime[0])
        directions=[(0, 1),(1, 0),(0, -1),(-1, 0)]
        time=[[float('inf')]*col for _ in range(row)]
        time[0][0]=moveTime[0][0]
        heap=[(0,0,0)] #(time,x,y)
        while heap:
            t,x,y=heapq.heappop(heap)
            if (x,y)==(row-1,col-1):
                return t
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if nx<0 or ny<0 or nx>=row or ny>=col:
                    continue
                else:
                    waitTime=max(moveTime[nx][ny]-t,0)#if t>movieTime,then we can move next node
                    newT=t+1+waitTime
                    if time[nx][ny]==float('inf'):
                        if newT<time[nx][ny]:
                            time[nx][ny]=newT
                            heapq.heappush(heap,(newT,nx,ny))
        return -1
            