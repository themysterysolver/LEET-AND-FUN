class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def BFS(source,target):
            if len(blocked)==0:
                return True
            q=deque([(source[0],source[1])])
            visited=set()
            visited.add((source[0],source[1]))
            b=set()
            for x,y in blocked:
                b.add((x,y))
            directions=[(0,1),(1,0),(0,-1),(-1,0)]
            row=col=10**6
            limit=len(blocked)**2
            while q and len(visited)<=limit:
                x,y=q.popleft()
                if x==target[0] and y==target[1]:
                    return True
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if x<0 or ny<0 or nx>=row or ny>=col or (nx,ny) in visited or (nx,ny) in b:
                        continue
                    else:
                        q.append((nx,ny))
                        visited.add((nx,ny))
            return len(visited)>limit
        return BFS(source,target) and BFS(target,source)
                    

        