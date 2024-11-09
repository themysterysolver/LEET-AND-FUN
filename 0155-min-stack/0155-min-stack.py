class MinStack:
    def __init__(self):
        self.stack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
    def pop(self) -> None:
        return self.stack.pop() if self.stack else null
    def top(self) -> int:
        return self.stack[-1] if self.stack else null
    def getMin(self) -> int:
        ans=self.stack[:]
        heapq.heapify(ans)
        return heapq.heappop(ans)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()