#dijkstras algorithm
# passes 519/581 test cases,TLE
# with @cache 572/581 test cases passes
# pre-computation works!!
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adL = defaultdict(list)
        for i in range(len(original)):
            adL[original[i]].append((cost[i],changed[i]))
        mainCost = 0

        
        def dijkstras(src):
            vertices = [float('inf')]*26
            vertices[ord(src)-ord('a')] = 0
            heap = []
            heapq.heappush(heap,(0,src))
            while heap:
                cost,v = heapq.heappop(heap)
                for c,nei in adL[v]:
                    if cost+c<vertices[ord(nei)-ord('a')]:
                        vertices[ord(nei)-ord('a')] = cost+c
                        heapq.heappush(heap,(cost+c,nei))
            return vertices

        pre_compute = [dijkstras(chr(i+ord('a'))) for i in range(26)]
        for i in range(len(source)):
            if source[i]!=target[i]:
                ans = pre_compute[ord(source[i])-ord('a')][ord(target[i])-ord('a')]
                #print(i,ans)
                if ans == float('inf'):
                    return -1
                mainCost += ans
        return mainCost
        