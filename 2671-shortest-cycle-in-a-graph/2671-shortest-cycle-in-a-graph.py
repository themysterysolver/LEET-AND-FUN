class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        mini = float('inf')
        adL = defaultdict(list)
        for u,v in edges:
            adL[u].append(v)
            adL[v].append(u)
        
        for i in range(n):
            q = deque([i])
            path = {i:0}
            parent = {i:-1}
            while q:
                l = len(q)
                for _ in range(l):
                    node = q.popleft()
                    for v in adL[node]:
                        if v not in path:
                            path[v] = path[node] + 1
                            q.append(v)
                            parent[v] = node
                        elif v in path and v!=parent[node]:
                            mini = min(mini,path[node]+path[v]+1)
        return mini if mini!=float('inf') else -1