class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        adL = {i+1:set() for i in range(n)}
        degree = {i+1:0 for i in range(n)}

        for u,v in edges:
            adL[u].add(v)
            adL[v].add(u)
            degree[u]+=1
            degree[v]+=1
        #print(adL,degree)

        mini = float('inf')
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for k in range(j+1,n+1):
                    if i in adL[j] and j in adL[k] and k in adL[i]:
                        mini = min(degree[i]+degree[j]+degree[k]-6,mini)
        return mini if mini!=float('inf') else -1

