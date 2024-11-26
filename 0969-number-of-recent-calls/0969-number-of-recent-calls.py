class RecentCounter:
    def __init__(self):
        self.record=[]
    def ping(self, t: int) -> int:
        count=0
        self.record.append(t)
        end=len(self.record)-1
        #print('PING',t)
        while end>=0 and self.record[end]>=t-3000:
            #print(self.record[end])
            end-=1
            count+=1
        #print('---------------')
        return count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)