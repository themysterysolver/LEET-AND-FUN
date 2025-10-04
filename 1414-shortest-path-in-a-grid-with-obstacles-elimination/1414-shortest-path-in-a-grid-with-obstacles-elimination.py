class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = deque([(0,0,k)])
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        count = 0
        cost = {(0,0):k}
        m,n = len(grid),len(grid[0])
        while q:
            #print(q)
            l = len(q)
            for _ in range(l):
                x,y,c = q.popleft()
                if x == m-1 and y == n-1:
                    return count
                for dx,dy in dir:
                    nx,ny = x+dx,y+dy
                    if nx<0 or ny<0 or nx>=m or ny>=n:
                        continue
                    if grid[nx][ny] == 1:
                        if c-1<0:
                            continue
                        if (nx,ny) not in cost:
                            cost[(nx,ny)] = c-1
                            q.append((nx,ny,c-1))
                        else:
                            if cost[(nx,ny)]<c-1:
                                cost[(nx,ny)]=c-1
                                q.append((nx,ny,c-1))
                    else:
                        if (nx,ny) not in cost:
                            cost[(nx,ny)] = c
                            q.append((nx,ny,c))
                        else:
                            if cost[(nx,ny)]<c:
                                q.append((nx,ny,c))
                                cost[(nx,ny)]=c
            count+=1
        return -1