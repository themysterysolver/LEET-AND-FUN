# This is topo sort cycle detection question
# now they are asking topo sort order which is easy as course shedule - 1
# we start with 0 indegrees and find it.  
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        adL={i:[] for i in range(numCourses)}
        for v,u in prerequisites:
            adL[u].append(v)
            indegree[v]+=1
        #print("IN DEGREE:",indegree)
        #print("adL",list(adL.items()))
        q=deque([])
        topoOrder=[]
        for idx,i in enumerate(indegree):
            if i==0:
                q.append(idx)
        if not q:
            return []
        while q:
            node=q.popleft()
            topoOrder.append(node)
            for n in adL[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
        #print(topoOrder)
        return topoOrder if len(topoOrder)==numCourses else []