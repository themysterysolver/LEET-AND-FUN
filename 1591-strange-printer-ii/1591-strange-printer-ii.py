#https://leetcode.com/problems/strange-printer-ii/solutions/6686781/topological-sort-kahns-algorithm-by-alex-2wce/
#https://www.youtube.com/watch?v=o2Myi-u_DLo
class Solution:
    def isPrintable(self, grid: List[List[int]]) -> bool:
        def display(grid):
            for row in grid:
                print(row)
            print('----------')
        display(grid)

        #store rec val
        border = defaultdict(lambda:[float('inf'),float('-inf'),float('inf'),float('-inf')]) #L,R,U,D
        m,n = len(grid),len(grid[0])

        for i in range(m):
            for j in range(n):
                color = grid[i][j]
                border[color][0] = min(border[color][0],j)
                border[color][1] = max(border[color][1],j)
                border[color][2] = min(border[color][2],i)
                border[color][3] = max(border[color][3],i)
        #cons map
        indegree = defaultdict(int)
        adL = defaultdict(list)

        for clr in border.keys():
            left,right,top,down = border[clr]
            for j in range(left,right+1):
                for i in range(top,down+1):
                    colour = grid[i][j]
                    if clr!=colour and colour not in adL[clr]:
                        adL[clr].append(colour)
                        indegree[colour]+=1
        
        #topo sort
        q = deque([])
        ans = []
        for k,v in border.items():
            if indegree[k] == 0:
                q.append(k)
                ans.append(k)        
        # ans = []
        while q:
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                for nei in adL[node]:
                    if indegree[nei]>0:
                        indegree[nei]-=1
                        if indegree[nei] == 0:
                            q.append(nei)
                            ans.append(nei)
        #rint(adL)
        #print(ans)
        return len(ans) == len(border)
