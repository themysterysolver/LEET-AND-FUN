class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row,col=len(isWater),len(isWater[0])
        result=[[0]*col for _ in range(row)]
        visited=[[False]*col for _ in range(row)]
        q=deque([])
        for i in range(row):
            for j in range(col):
                if isWater[i][j]==1:
                    q.append((i,j))
                    visited[i][j]=True
        lvl=1
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        while q:
            l=len(q)
            for i in range(l):
                x,y=q.popleft()
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx>=row or ny>=col or visited[nx][ny]:
                        continue
                    else:
                        result[nx][ny]=lvl
                        q.append((nx,ny))
                        visited[nx][ny]=True
            lvl+=1
        return result
                    
