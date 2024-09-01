class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        print(m,n,original)
        if len(original)!=m*n:
            return []
        a=[]
        for i in range(0,len(original),n):
            a.append(original[i:i+n])
        print(a)
        return a
        