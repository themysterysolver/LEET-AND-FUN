class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adL={i:[] for i in range(n)}
        for u,v in connections:
            adL[u].append((v,1))
            adL[v].append((u,-1))
        print(adL)
        visited=set()
        visited.add(0)
        q=deque([(0,0)])
        count=0
        while q:
            l=len(q)
            for _ in range(l):
                n,s=q.popleft()
                if s==1:
                    count+=1
                for node,s1 in adL[n]:
                    if node not in visited:
                        q.append((node,s1))
                        visited.add(node)
        return count