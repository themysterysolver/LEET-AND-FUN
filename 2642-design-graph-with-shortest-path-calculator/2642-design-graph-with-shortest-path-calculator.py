class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adL = {i:[] for i in range(n)}
        for u,v,c in edges:
            self.adL[u].append((v,c))
        self.n = n

    def addEdge(self, edge: List[int]) -> None:
        u,v,c = edge
        self.adL[u].append((v,c))

    def shortestPath(self, node1: int, node2: int) -> int:
        # q = d([node1])
        heap = []
        cost = [float('inf')]*self.n
        heapq.heappush(heap,(0,node1))
        cost[node1] = 0 
        while heap:
            c,n = heapq.heappop(heap)
            for nei,nc in self.adL[n]:
                if cost[nei]>nc+c:
                    cost[nei] = nc+c
                    heapq.heappush(heap,(cost[nei],nei))
        return cost[node2] if cost[node2]!=float('inf') else -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)