#[s1,e1) [s2,e2)
#[s,e)  [start,end)
class MyCalendar:
    def __init__(self):
        self.slot=[]
    def book(self, start: int, end: int) -> bool:
        print(self.slot)
        for s,e in self.slot:
            if s<end and start<e:#s<end and start<e ..............not(e<=start or end<=s)
                return False
        self.slot.append((start,end))
        return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
