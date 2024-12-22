class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adL={i:[] for i in range(len(graph))}
        print(adL)
        indegree=[0]*len(graph)
        for i,nodes in enumerate(graph):
            for j in nodes:
                adL[j].append(i)
                indegree[i]+=1
        print(adL,indegree)
        q=deque([])
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        print(q)
        if not q:
            return []
        topoSort=[]
        while q:
            n=q.popleft()
            topoSort.append(n)
            for i in adL[n]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        print(topoSort)
        topoSort.sort()
        return topoSort

