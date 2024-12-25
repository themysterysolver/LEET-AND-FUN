class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        coordinates=[]
        row,col=len(land),len(land[0])
        visited=[[False]*col for _ in range(row)]
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        def BFS(r,c):
            coord=[] #will be appended to final coordinates
            coord.extend([r,c])
            points=[]
            q=deque([(r,c)])
            visited[r][c]=True
            while q:
                x,y=q.popleft()
                points.append((x,y))
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx>=row or ny>=col:
                        continue
                    else:
                        if land[nx][ny]==1 and not visited[nx][ny]:
                            q.append((nx,ny))
                            visited[nx][ny]=True
            points.sort(key=lambda x:(-x[0],-x[1]))
            print(points)
            x,y=points[0]
            coord.extend([x,y])
            coordinates.append(coord)
        for i in range(row):
            for j in range(col):
                if land[i][j]==1 and not visited[i][j]:
                    BFS(i,j)
        return coordinates
