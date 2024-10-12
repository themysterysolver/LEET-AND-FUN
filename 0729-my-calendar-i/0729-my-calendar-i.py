#[s1,e1) [s2,e2)
#[s,e)  [start,end)
class MyCalendar:
    def __init__(self):
        self.slot=[]
    def book(self, start: int, end: int) -> bool:
        left,right=0,len(self.slot)-1
        while left<=right:
            mid=(left+right)//2
            if self.slot[mid][0]<start:
                left=mid+1
            else:
                right=mid-1
        if left>0 and self.slot[left-1][1]>start:
            return False
        if left<len(self.slot) and self.slot[left][0]<end:
            return False
        self.slot.insert(left,(start,end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)