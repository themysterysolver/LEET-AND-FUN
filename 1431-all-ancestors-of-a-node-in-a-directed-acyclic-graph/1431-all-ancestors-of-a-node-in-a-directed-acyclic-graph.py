class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        #finding TOPO SORT using khans algorithm first
        adL={i:[] for i in range(n)}
        indegree=[0]*n
        #print(adL)
        for u,v in edges:
            adL[u].append(v)
            indegree[v]+=1
        #print(adL,indegree)
        q=deque([])
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        #print(q)
        topoOrder=[]
        while q:
            node=q.popleft()
            topoOrder.append(node)
            for neighbour in adL[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        #print(topoOrder)
        ancesstorSet=[set() for i in range(n)]
        for node in topoOrder:
            for neighbour in adL[node]:
                ancesstorSet[neighbour].add(node)
                ancesstorSet[neighbour].update(ancesstorSet[node])
        anc=[[] for i in range(n)]
        for i in range(n):
            for node in range(n):
                if i==node:
                    continue
                if node in ancesstorSet[i]:
                    anc[i].append(node)
        return anc
                
        