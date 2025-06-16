class MyCircularQueue:
    def __init__(self, k: int):
        self.arr=[0]*k
        self.cap=k
        self.size=0
        self.front=0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        rear=(self.front+self.size)%self.cap
        self.arr[rear]=value
        self.size+=1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front=(self.front+1)%self.cap
        self.size-=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        rear=(self.front+self.size-1)%self.cap
        return self.arr[rear]
        

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.cap
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()