class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        def bfs():
            q = deque([x])
            count  = 0
            if y>x:
                return y-x
            visited = set()
            while q:
                l = len(q)
                for _ in range(l):
                    n = q.popleft()
                    if n in visited:
                        continue
                    visited.add(n)
                    if n == y:
                        return count
                    if n%5 == 0:
                        q.append(n//5) 
                    if n%11 == 0:
                        q.append(n//11)            
                    q.append(n+1)
                    q.append(n-1)
                #print(q)
                count += 1
        return bfs()
        # @cache
        # def dfs(x, count):
        #     if x == y:
        #         return count
        #     if x < y:
        #         return float('inf')
        #     c = float('inf')
            
        #     if x%5 == 0:
        #         c = min(c,dfs(x//5, count+1))
        #     if x%11 == 0:
        #         c = min(c,dfs(x//11, count+1))

        #     c = min(c,dfs(x+1,count+1),dfs(x-1,count+1))
        #     return c
            
        # return dfs(x,0)
        