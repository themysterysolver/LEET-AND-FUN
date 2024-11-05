class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def distanceCal(x1,y1,x2,y2):
            return math.sqrt((x2-x1)**2+(y2-y1)**2)
        def display(mat):
            for row in mat:
                print(row)
            print('-------------------')
        #BFS
        def BFS(r,i):
            l=len(bombs)
            visited=[False]*l
            visited[i]=True
            q=deque([(r,i)])
            while q:
                l=len(q)
                r,idx=q.popleft()
                for i in range(len(bombs)):
                    if not visited[i] and r-distance[idx][i]>=0:
                        q.append((bombs[i][-1],i))
                        visited[i]=True
            return visited.count(True)
        #distance calculation!
        l=len(bombs)
        distance=[[0]*l for _ in range(l)]
        display(distance)
        for i in range(l):
            for j in range(l):
                distance[i][j]=distanceCal(bombs[i][0],bombs[i][1],bombs[j][0],bombs[j][1])
        display(distance)
        #logic
        countMax=1
        for i in range(len(bombs)):
            countMax=max(countMax,BFS(bombs[i][-1],i))
        return countMax
