class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        row,col = len(grid1),len(grid1[0])
        # def bfs(i,j):
        #     q = deque([(i,j)])
        #     visited.add((i,j))
        #     while q:
        #         x,y = q.popleft()
        #         for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        #             nx,ny = x+dx,y+dy
        #             if nx<0 or ny<0 or nx>=row or ny>=col or grid1[nx][ny] == 0 or (nx,ny) in visited:
        #                 continue
        #             q.append((nx,ny))
        #             visited.add((nx,ny))

        for i in range(row):
            for j in range(col):        
                if grid1[i][j] == 1:
                    visited.add((i,j))
        
        visited2 = set()
        def bfs2(i,j):
            q = deque([(i,j)])
            visited2.add((i,j))
            flag = True
            while q:
                x,y = q.popleft()
                if (x,y) not in visited:
                    flag = False
                for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nx,ny = x+dx,y+dy
                    if nx<0 or ny<0 or nx>=row or ny>=col or grid2[nx][ny] == 0 or (nx,ny) in visited2:
                        continue
                    q.append((nx,ny))
                    visited2.add((nx,ny))
                
                    
            return 1 if flag else 0
        count = 0
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1 and (i,j) not in visited2:
                    count+=bfs2(i,j)
                    #print(visited2)
        return count
        
