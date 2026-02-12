class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        direction = {1:[(0,1),(0,-1)],2:[(1,0),(-1,0)],3:[(0,-1),(1,0)],4:[(0,1),(1,0)],5:[(-1,0),(0,-1)],6:[(0,1),(-1,0)]}
        q = deque([(0,0)])
        visited = set()
        visited.add((0,0))
        m,n = len(grid),len(grid[0])
        if grid == [[1]]:
            return True
        while q:
            x,y = q.popleft()
            curr = grid[x][y]
            for dx,dy in direction[curr]:
                nx,ny=x+dx,y+dy
                if nx<0 or ny<0 or nx>=m or ny>=n:
                    continue
                if (nx,ny) in visited:
                    continue
                c1 = grid[nx][ny]
                for dx1,dy1 in direction[c1]:
                    nx1,ny1 = nx+dx1,ny+dy1
                    #print("checking: From",(x,y),"to",(nx,ny),"revert cehck:",(nx1,ny1))
                    if (nx1,ny1) == (x,y):
                        if (nx,ny) == (m-1,n-1):
                            return True
                        q.append((nx,ny))
                        visited.add((nx,ny))
                        break
            print(q)
        return False

