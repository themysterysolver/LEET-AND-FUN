class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def BFS(sr,sc):
            chosen=image[sr][sc]
            q=deque([(sr,sc)])
            row,col=len(image),len(image[0])
            directions=[(0,1),(1,0),(0,-1),(-1,0)]
            visited=[[False]*col for _ in range(row)]
            visited[sr][sc]=True
            image[sr][sc]=color
            while q:
                l=len(q)
                for i in range(l):
                    x,y=q.popleft()
                    for dx,dy in directions:
                        nx,ny=x+dx,y+dy
                        if nx<0 or ny<0 or nx>=row or ny>=col:
                            continue
                        elif not visited[nx][ny] and image[nx][ny]==chosen:
                            q.append((nx,ny))
                            image[nx][ny]=color
                            visited[nx][ny]=True
        BFS(sr,sc)
        return image