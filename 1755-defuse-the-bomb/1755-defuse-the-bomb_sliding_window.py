class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result=[0]*len(code)
        if k==0:
            return result
        start,end,windowSum=1,k,0
        if k<0:
            start=len(code)-abs(k)
            end=len(code)-1
        for i in range(start,end+1):
            windowSum+=code[i]
        for i in range(len(code)):
            result[i]=windowSum
            windowSum-=code[start%len(code)]
            windowSum+=code[(end+1)%len(code)]
            start+=1
            end+=1
        return result
        
