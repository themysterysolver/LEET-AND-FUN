class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0:
            return []
        i,j = 1,1
        if x!=1:
            i = int(math.log(bound)/math.log(x))
        if y!=1:
            j = int(math.log(bound)/math.log(y))
        print(i,j)
        s = set()
        for X in range(i+1):
            for Y in range(j+1):
                el = x**X+y**Y
                if el<=bound:
                    s.add(el)
        return list(s)