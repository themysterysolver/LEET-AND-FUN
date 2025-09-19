class Spreadsheet:

    def __init__(self, rows: int):
        self.hash = defaultdict(int)
        self.r = rows
    def setCell(self, cell: str, value: int) -> None:
        self.hash[cell] = value
    def resetCell(self, cell: str) -> None:
        self.hash [cell] = 0
    def getValue(self, formula: str) -> int:
        x = formula[1:]
        arr = x.split('+')
        a,b = arr[0],arr[1]
        ans = 0
        if a.isdigit():
            ans+=int(a)
        if b.isdigit():
            ans+=int(b)
        if a in self.hash:
            ans+=self.hash[a]
        if b in self.hash:
            ans+=self.hash[b]
        return ans


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)