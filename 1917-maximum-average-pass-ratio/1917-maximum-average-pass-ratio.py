class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calculate_Increase_In_Pass_Ratio(passes,total):
            return ((passes+1)/(total+1))-(passes/total)
        heap=[]
        for p,t in classes:
            heapq.heappush(heap,(-calculate_Increase_In_Pass_Ratio(p,t),p,t))
        print(list(heap))
        for i in range(extraStudents):
            _,p,t=heapq.heappop(heap)
            heapq.heappush(heap,(-calculate_Increase_In_Pass_Ratio(p+1,t+1),p+1,t+1))
        avg=0
        print(list(heap))
        while heap:
            _,p,t=heapq.heappop(heap)
            avg+=p/t
        return avg/len(classes)