class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items=[(-values[i],labels[i]) for i in range(len(values))]
        heapq.heapify(items)
        c={key:useLimit for key in set(labels)}
        sumx=0
        for _ in range(numWanted):
            if not items:
               break
            val,labe=heapq.heappop(items)
            if c[labe]>0:
                sumx+=val
                c[labe]-=1
            else:
                while True and items:
                    val,labe=heapq.heappop(items)
                    if c[labe]>0:
                        c[labe]-=1
                        sumx+=val
                        break
        return sumx*(-1)
            