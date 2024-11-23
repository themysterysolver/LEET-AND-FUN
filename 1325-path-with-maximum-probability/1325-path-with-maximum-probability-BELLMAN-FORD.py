#Belmann-ford algorithm
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        cost=[0]*n
        cost[start_node]=1
        for i in range(n-1):
            changes=False
            for j in range(len(edges)):
                u,v=edges[j]
                edgeCost=succProb[j]

                #u-->v
                if edgeCost*cost[u]>cost[v]:
                    cost[v]=edgeCost*cost[u]
                    changes=True
                #v-->u
                if edgeCost*cost[v]>cost[u]:
                    cost[u]=edgeCost*cost[v]
                    changes=True
            if not changes:
                break
        return cost[end_node]
                
