class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        c  = Counter(str(n))
        mini = float('inf')
        #print(c)
        v = 0
        for key,val in c.items():
            if val<mini:
                mini = val
                v = key
            elif val == mini and key<v:
                v = key
        return int(v)