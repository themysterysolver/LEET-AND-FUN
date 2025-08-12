class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque([])
        n = len(grid)
        flag = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i,j))
                if grid[i][j] == 0:
                    flag = True
        if not flag:
            return -1
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        count = 0
        while q:
            l = len(q)
            for _ in range(l):
                x,y = q.popleft()
                for dx,dy in directions:
                    nx,ny = x+dx,y+dy
                    if nx<0 or ny<0 or nx>=n or ny>=n or grid[nx][ny] == 1 or (nx,ny) in visited:
                        continue
                    else:
                        if grid[nx][ny] == 0:
                            q.append((nx,ny))
                            visited.add((nx,ny))
            count += 1
        return count-1

        