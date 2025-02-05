class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        exist=set()
        for i,(u,v) in enumerate(equations):
            exist.add(u)
            exist.add(v)
        graph={i:dict() for i in exist}
        for i,(u,v) in enumerate(equations):#similar to json
            graph[u][v]=values[i]
            graph[v][u]=1.0/values[i]
        print(graph)
        result=[]
        def BFS(x,y):
            if x==y and x in exist:
                return 1
            if x not in exist or y not in exist:
                return -1
            sumi=0
            q=deque([(x,1)])
            visited=set()
            visited.add(x)
            while q:
                l=len(q)
                for i in range(l):
                    s,val=q.popleft()
                    d=graph[s]
                    for v,val1 in d.items():
                        if v not in visited:
                            q.append((v,val*val1))
                            visited.add(v)
                            if v==y:
                                return val*val1
            return -1
        for x,y in queries:
            result.append(BFS(x,y))
        return result
