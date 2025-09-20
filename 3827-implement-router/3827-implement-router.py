class Router:

    def __init__(self, memoryLimit: int):
        self.memory = memoryLimit
        self.q = deque([])
        self.s = set()
        self.destTime = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination,timestamp) in self.s:
            return False
        if self.memory == 0:
            (s,d,t) = self.q.popleft()
            #self.destTime[d].remove(t)
            self.s.remove((s,d,t))
            arr = self.destTime[d]
            idx = bisect.bisect_left(arr, t)
            if idx < len(arr) and arr[idx] == t:
                del arr[idx]
            self.memory+=1
        self.q.append((source,destination,timestamp))
        self.s.add((source,destination,timestamp))
        self.destTime[destination].append(timestamp)
        self.memory-=1

        #print(list(self.q))
        return True


    def forwardPacket(self) -> List[int]:
        if self.q:
            s,d,t = self.q.popleft()
            self.destTime[d].remove(t)
            self.memory+=1
            self.s.remove((s,d,t))
            return [s,d,t]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        def upper_bound(arr,target):
            left,right = 0,len(arr)-1
            ans = len(arr)
            while left<=right:
                mid = (left+right)//2
                if arr[mid]>target:
                    right = mid-1
                else:
                    ans = mid
                    left = mid+1
            return ans

        def lower_bound(arr,target):
            left,right = 0,len(arr)-1
            ans = -1
            while left<=right:
                mid = (left+right)//2
                
                if arr[mid]>=target:
                    ans = mid
                    right = mid-1
                else:
                    left = mid+1
            return ans

        arr = self.destTime[destination]
        #print(arr)
        #arr.sort()
        l = bisect.bisect_left(arr, startTime)
        r = bisect.bisect_right(arr, endTime)
        return r-l




# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)