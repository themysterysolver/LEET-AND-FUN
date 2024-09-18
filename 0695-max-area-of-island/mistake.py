#here what I did is that,I checked on while entering the q,but there can be some cases I may be missing!!!
      '''MR.GPT:The issue is that in the BFS function, you're not checking the visited status before appending new cells to the queue.  
      This causes the same cell to be revisited in some cases. You should add a visited[nx][ny] = True right when you append a cell to the queue.'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        visited=[[False]*col for _ in range(row)]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        max_area=0
        def BFS(r,c):
            q=deque([(r,c)])
            area=0
            while q:
                area+=1
                x,y=q.popleft()
                visited[x][y]=True
                for dx,dy in direction:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx==row or ny==col or grid[nx][ny]==0:
                        continue
                    elif grid[nx][ny]==1 and not visited[nx][ny]:
                        q.append((nx,ny))
            return area

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and not visited[i][j]:
                    max_area=max(max_area,BFS(i,j))
        return max_area
