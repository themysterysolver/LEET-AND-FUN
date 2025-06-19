class MedianFinder:
    def __init__(self):
        self.arr=[]
        self.length=0

    def addNum(self, num: int) -> None:
        self.length+=1
        bisect.insort(self.arr,num)
        #print(self.arr,self.length)

    def findMedian(self) -> float:
        if self.length==1:
            return self.arr[0]
        mid=(self.length-1)//2
        #print(self.length,mid,mid+1)
        if self.length&1==1:
            #print("ODD")
            return self.arr[mid]
        else:
            #print("EVEN")
            return (self.arr[mid]+self.arr[mid+1])/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()