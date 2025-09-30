class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adL = defaultdict(list)
        for u,v in tickets:
            heapq.heappush(adL[u],v)
        
        #print(adL)
        
        path = []

        def dfs(node):
            while adL[node]:
                dfs(heapq.heappop(adL[node]))
            path.append(node)
        dfs("JFK")
        return path[::-1]    