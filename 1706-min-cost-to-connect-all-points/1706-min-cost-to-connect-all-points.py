#prim's algorithm
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calManhattan(p1,p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        visited=[False]*len(points)
        heap=[(0,0)]#(cost,starting_point_idx)
        cost=0
        edgesUsed=0
        while edgesUsed<len(points):
            c,u=heapq.heappop(heap)
            if visited[u]:
                continue
            edgesUsed+=1
            cost+=c
            visited[u]=True
            for i in range(len(points)):
                if visited[i]:
                    continue
                d=calManhattan(points[i],points[u])
                heapq.heappush(heap,(d,i))
        return cost
