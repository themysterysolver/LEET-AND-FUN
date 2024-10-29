class SmallestInfiniteSet:
    def __init__(self):
       self.curr_min=1
       self.heap=[] 

    def popSmallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        self.curr_min+=1
        return self.curr_min-1
        

    def addBack(self, num: int) -> None:
        if self.curr_min>num and num not in set(self.heap):
            heapq.heappush(self.heap,num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)