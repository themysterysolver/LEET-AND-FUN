class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        adL={i:[] for i in range(len(vals))}
        heap={i:[] for i in range(len(vals))}
        for u,v in edges:
            adL[u].append(v)
            adL[v].append(u)
            heapq.heappush(heap[u],-vals[v])
            heapq.heappush(heap[v],-vals[u])
        maxi=float('-inf')
        #print("HEAP:",list(heap.items()))
        #print("ADL:",list(adL.items()))
        for i in range(len(vals)):
            sumi=vals[i]
            t=k
            while heap[i] and t!=0:
                x=heapq.heappop(heap[i])*(-1)
                if x<0:
                    break
                sumi+=x
                t-=1
            maxi=max(maxi,sumi)
            #print(i,vals[i],heap[i],adL[i],sumi,maxi)
        return maxi if maxi!=float('-inf') else 0