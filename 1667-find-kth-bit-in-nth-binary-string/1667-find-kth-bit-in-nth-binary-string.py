class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s_current="0"
        for i in range(1,n):
            s_prev=s_current
            s_rev=""
            for i in range(len(s_prev)-1,-1,-1):
                if s_prev[i]=='1':
                    s_rev+='0'
                else:
                    s_rev+='1'
            s_current=s_prev+"1"+s_rev
            #print(i,s_current)
        #print(s_current,s_current[k-1])
        return s_current[k-1]
        
        