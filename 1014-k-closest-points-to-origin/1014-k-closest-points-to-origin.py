class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dis(x,y):
            return x**2+y**2
        hash=defaultdict(list)
        for x,y in points:
            hash[dis(x,y)].append([x,y])
        items=list(hash.items())
        heapq.heapify(items)
        ans=[]
        while k>0:
            if not items:
                break
            a=heapq.heappop(items)[1]
            ans+=a
            k-=len(a)
        return ans