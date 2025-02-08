class NumberContainers:
    def __init__(self):
        self.hashheap=defaultdict(SortedSet)
        self.hash=dict()
    def change(self, index: int, number: int) -> None:
        if index in self.hash:
            p=self.hash[index]
            self.hashheap[p].remove(index)
            if not self.hashheap[p]:
                del self.hashheap[p]
        self.hash[index]=number
        self.hashheap[number].add(index)
    def find(self, number: int) -> int:
        if number in self.hashheap and self.hashheap[number]:
            return self.hashheap[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)