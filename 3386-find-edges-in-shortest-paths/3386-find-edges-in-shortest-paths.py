# HINT: we say and edges is and solution if the dist_from_start[u](weight before) + weight of node + dist_from_end[v]

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        adL = defaultdict(list)
        for idx,(u,v,w) in enumerate(edges):
            adL[u].append((v,w))
            adL[v].append((u,w))
        def dijkstras(src):
            vertices = [float('inf')]*n
            vertices[src] = 0
            heap = []
            heapq.heappush(heap,(0,src))
            while heap:
                cost,v = heapq.heappop(heap)
                if cost>vertices[v]: ## TLE
                    continue
                for nei,c in adL[v]:
                    if cost+c<vertices[nei]:
                        vertices[nei] = cost+c
                        heapq.heappush(heap,(vertices[nei],nei))
            return vertices
        forward = dijkstras(0)
        backward = dijkstras(n-1)
        #print(forward)
        #print(backward)

        ed = [False]*len(edges)
        if forward[-1] == float('inf') or backward[-1] == float('inf'):
            return ed
        for idx,(u,v,w) in enumerate(edges):
            if forward[u]+w+backward[v] == forward[n-1] or forward[v]+w+backward[u] == forward[n-1]:
                ed[idx] = True
        return ed

        