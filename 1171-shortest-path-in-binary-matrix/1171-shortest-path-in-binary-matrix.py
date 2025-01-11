class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def display(matrix):
            for row in matrix:
                print(row)
            print('-----------')
        row=col=len(grid)
        #print(row,col)
        #display(grid)
        if grid[0][0]==1:
            return -1
        finish=(row-1,col-1)
        q=deque([(0,0)])
        directions=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        visited=set()
        visited.add((0,0))
        cell=0
        found=False
        while q:
            l=len(q)
            print(cell,list(q))
            for _ in range(l):
                x,y=q.popleft()
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx>=row or ny>=col or (nx,ny) in visited:
                        continue
                    else:
                        if grid[nx][ny]==0:
                            if (nx,ny)==finish:
                                found=True
                            q.append((nx,ny))
                            visited.add((nx,ny))
            cell+=1
            if found:
                return cell+1
        return -1 if row!=1 else 1
