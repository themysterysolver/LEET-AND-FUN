class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        def display(matrix):
            for row in matrix:
                print(row)
            print('-----------')
        edger=[]
        for row in wall:
            d=[]
            for i in range(len(row)):
                if not d:
                    d.append(row[i])
                else:
                    d.append(row[i]+d[i-1])
            edger.append(d)
        display(edger)
        freq=dict()
        for row in edger:
            for i in row:
                freq[i]=freq.get(i,0)+1
        print(freq)
        heap=[]
        for key,val in freq.items():
            heapq.heappush(heap,(-val,key))
        print(heap)
        heapq.heappop(heap)
        print(heap)
        if heap:
            ans,k=heapq.heappop(heap)
        else:
            return len(wall)
        return len(wall)+ans