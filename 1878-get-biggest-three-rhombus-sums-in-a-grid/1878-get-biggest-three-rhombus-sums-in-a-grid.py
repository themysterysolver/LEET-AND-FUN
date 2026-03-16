class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        heap = []
        m,n = len(grid),len(grid[0])
        for size in range(m):
            #print('For the size!',size)
            for i in range(m):
                for j in range(n):
                    sumx = grid[i][j]
                    x,y = i,j
                    flag = True
                    #print('For:',i,j)
                    for _ in range(size):
                        x,y = x-1,y+1
                        #print('/',x,y)
                        if x<0 or y<0 or x>=m or y>=n:
                            flag = False
                            break
                        sumx+=grid[x][y]
                    for _ in range(size):
                        if not flag:
                            break
                        x,y = x+1,y+1
                        #print('\\',x,y)
                        if x<0 or y<0 or x>=m or y>=n:
                            flag = False
                            break
                        sumx+=grid[x][y]
                    for _ in range(size):
                        if not flag:
                            break
                        x,y = x+1,y-1
                        #print('/',x,y)
                        if x<0 or y<0 or x>=m or y>=n:
                            flag = False
                            break
                        sumx+=grid[x][y]
                    for _ in range(size-1):
                        if not flag:
                            break
                        x,y = x-1,y-1
                        #print('\\',x,y)
                        if x<0 or y<0 or x>=m or y>=n:
                            flag = False
                            break
                        sumx+=grid[x][y]
                    #print('Done-------')
                    if flag:
                        #print('added for',i,j,sumx)
                        heapq.heappush(heap,-sumx)
        ans = []
        s = set()
        count = 0
        while heap and count<3:
            b = -1*heapq.heappop(heap)
            if b not in s:
                ans.append(b)
                s.add(b)
                count+=1
        return ans
                    
                    
                     
