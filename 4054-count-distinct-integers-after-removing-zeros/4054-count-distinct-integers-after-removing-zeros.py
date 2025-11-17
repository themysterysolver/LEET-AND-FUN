class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        l = len(s)
        powers = [1]
        for i in range(l-1):
            powers.append(powers[-1]*9)
        #print(powers)
        sumx = 0
        if l == 1:
            return n
        ''' last number logic handling'''
        for i in range(l):
            d = int(s[i])
            if d == 0:
                break
            #print(n,d,sumx)
            sumx+=(d-1)*powers[-i-1]
            #print(sumx)
        else:
            sumx+=1
        return sum(powers)+sumx-1


        