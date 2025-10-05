class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        dp = [[0]*n for _ in range(m)]
        def display(mat):
            for row in mat:
                print(row)
            print('---------------')
        #display(dp)
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def bfs(nums):
            visited = set(nums)
            q = deque(nums)
            while q:
                x,y = q.popleft()
                dp[x][y]+=1
                for dx,dy in directions:
                    nx,ny = x+dx,y+dy
                    if nx<0 or ny<0 or nx>=m or ny>=n or (nx,ny) in visited:
                        continue
                    if heights[x][y]<=heights[nx][ny]:
                        q.append((nx,ny))
                        visited.add((nx,ny))
        pacific = [(0,i) for i in range(n)] + [(i,0) for i in range(m)]
        atlantic = [(m-1,i) for i in range(n)] + [(i,n-1) for i in range(m)]
        bfs(pacific)
        #display(dp)
        bfs(atlantic)
        #display(dp)
        dp[0][0]-=1
        dp[-1][-1]-=1
        res = []
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 2:
                    res.append([i,j])
        return res