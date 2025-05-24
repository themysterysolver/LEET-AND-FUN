class LUPrefix:
    def __init__(self, n: int):
        self.lup=set()
        self.long=0
    def upload(self, video: int) -> None:
        self.lup.add(video)
        while self.long+1 in self.lup:
            self.long+=1
        #print(self.lup,self.long)
    def longest(self) -> int:
        return self.long


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()