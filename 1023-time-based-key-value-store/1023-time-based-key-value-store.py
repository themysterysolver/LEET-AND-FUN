class TimeMap:
    def __init__(self):
        self.hash=dict()
    def set(self, key: str, value: str, timestamp: int) -> None:
        if not (key in self.hash):
            self.hash[key]=[]
        self.hash[key].append([timestamp,value])
    def get(self, key: str, timestamp: int) -> str:
        #print(self.hash)
        if key not in self.hash:
            return ""
        arr=self.hash[key]
        #print(arr)
        l,r=0,len(arr)-1
        res=""
        while l<=r:
            mid=(l+r)>>1
            t,v=arr[mid]
            if t<=timestamp:
                l=mid+1
                res=v
            else:
                r=mid-1
        return res




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)