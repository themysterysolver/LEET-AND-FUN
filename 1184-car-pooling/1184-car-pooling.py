#classic diff array concept
#sanjeev goat!
#just setting prefix diff array and making intervals count by processing 'em
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxi = max(t for n,f,t in trips)
        #print(maxi)
        prefix = [0]*(maxi+2)
        #print(prefix)
        for w,f,t in trips:
            prefix[f]+=w
            prefix[t]-=w
        pre = 0
        #print(prefix)
        mod = [0]*(maxi+2)
        for i in range(len(prefix)):
            pre += prefix[i]
            mod[i] = pre
        #print(mod)
        return max(mod)<=capacity

