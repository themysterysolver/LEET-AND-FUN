#dijkstras
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adL=defaultdict(list)
        for u,v,w in times:
            adL[u].append((w,v))
        spt=[float('inf')]*(n+1) #shortest path
        spt[k]=0
        heap=[(0,k)]
        while heap:
            currWeight,u=heapq.heappop(heap)
            for weight,v in adL[u]:
                if spt[v]>currWeight+weight:
                    spt[v]=currWeight+weight
                    heapq.heappush(heap,(spt[v],v))
        #print(spt)
        shortest_path=spt[1:]
        return max(shortest_path) if float('inf') not in shortest_path else -1

# THOUGHT PROCESS
# - We use shortest path algo using dijkstras to choose the most optimal time to reach any node
# - then we choose the longest time to reach any node from the optimal time choosen 