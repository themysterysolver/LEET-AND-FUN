class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def BFS(src):
            visited=[False]*n
            visited[src]=True
            q=deque([src])
            while q:
                l=len(q)
                for i in range(l):
                    node=q.popleft()
                    if node==destination:
                        return True
                    for nn in adV[node]:
                        if not visited[nn]:
                            visited[nn]=True
                            q.append(nn)
            return False
        adV={i:[] for i in range(n)}
        #print(adV)
        for start,end in edges:
            adV[start].append(end)
            adV[end].append(start)
        #print(adV)
        return BFS(source)
        