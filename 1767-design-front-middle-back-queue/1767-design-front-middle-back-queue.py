class FrontMiddleBackQueue:
    
    def __init__(self):
        self.nums=[]

    def pushFront(self, val: int) -> None:
        self.nums=[val]+self.nums
        #print(self.nums)

    def pushMiddle(self, val: int) -> None:
        l=len(self.nums)
        self.nums.insert(l//2,val)
        #print(self.nums)

    def pushBack(self, val: int) -> None:
        self.nums.append(val)
        #print(self.nums)

    def popFront(self) -> int:
        return self.nums.pop(0) if self.nums else -1

    def popMiddle(self) -> int:
        l=len(self.nums)
        if l%2==0:
            return self.nums.pop(l//2-1) if self.nums else -1
        else:
            return self.nums.pop(l//2) if self.nums else -1
        
    def popBack(self) -> int:
        return self.nums.pop() if self.nums else -1