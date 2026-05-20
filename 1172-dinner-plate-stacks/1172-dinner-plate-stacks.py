class DinnerPlates:

    def __init__(self, capacity: int):
        self.heap = []
        self.hash = defaultdict(list)
        self.c = capacity
        self.count = defaultdict(int)
        self.idx = 0
    
    def dis(self,msg):
        print(msg)
        for k,v in sorted(self.hash.items()):
            print(k,":",v)
        print('--')
        for k,v in sorted(self.count.items()):
            print(k,":",v)
        print('--')
        print(self.idx)
        print('HEAP:',self.heap)
        print('----------------------')

        

    def push(self, val: int) -> None:
        if not self.heap:
            if self.count[self.idx]<self.c:
                self.hash[self.idx].append(val)
                self.count[self.idx]+=1
            else:
                self.idx+=1
                self.hash[self.idx].append(val)
                self.count[self.idx]+=1
        else:
            print('pushy from heap!')
            idx = heapq.heappop(self.heap)
            if idx>self.idx:
                heap = []
                self.push(val)
                return 
            self.hash[idx].append(val)
            self.count[idx]+=1
        # self.dis(f"FROM PUSH the val {val}")

    def pop(self) -> int:
        if self.idx == 0 and self.count[self.idx]==0:
            # self.dis("FROM POP 0")
            return -1
        if self.count[self.idx]>0:
            self.count[self.idx]-=1
            idx = self.idx
            if self.count[self.idx] == 0:
                if self.idx>0:
                    self.idx-=1
            el = self.hash[idx].pop()
            # self.dis("FROM POP 1")
            return el
        else:
            self.idx-=1
            if self.idx == 0 and self.count[self.idx]==0:
                return -1
            # self.dis("FROM POP 2")
            return self.pop()

    def popAtStack(self, index: int) -> int:
        if self.count[index]>0:
            self.count[index]-=1
            heapq.heappush(self.heap,index)
            el = self.hash[index].pop()
            # self.dis(f"FROM POP at Sack {index} 0")
            return el
        # self.dis(f"FROM POP at Sack {index} 1")    
        return -1
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)