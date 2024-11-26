class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        topoSort=[]
        inDegree=[0]*numCourses
        adL={i:[] for i in range(numCourses)}
        for u,v in prerequisites:
            inDegree[u]+=1
            adL[v].append(u)
        print('INDEGREE:',inDegree)
        print('Adjacency list',adL)
        q=deque([])
        for i in range(len(inDegree)):
            if inDegree[i]==0:
                q.append(i)
        print('Q:',list(q))
        if not q:
            return False
        while q:
            n=q.popleft()
            topoSort.append(n)
            for neighbour in adL[n]:
                inDegree[neighbour]-=1
                if inDegree[neighbour]==0:
                    q.append(neighbour)
        print('INDEGREE->END:',inDegree)
        print('TOPO',topoSort)
        return len(topoSort)==numCourses